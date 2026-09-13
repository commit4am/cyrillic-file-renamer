# Cyrillic File Renamer

A small utility that transliterates Cyrillic MP3 filenames to Latin, in place.

Music files acquired from Russian-language sources arrive with Cyrillic names,
and a lot of things downstream handle them badly — DJ software that indexes by
filename, USB sticks formatted FAT32, CDJ hardware, car stereos, older media
servers. What you usually get is not a clean error but a track list of
unreadable boxes, or a file that silently fails to load mid-set.

This fixes the names before that happens.

## How it works

Transliteration comes from [`cyrtranslit`](https://pypi.org/project/cyrtranslit/),
which uses per-language mappings rather than one universal Cyrillic-to-Latin
table. That distinction is real: several characters map differently between
Russian, Serbian, Bulgarian and Ukrainian, so a single substitution table gets
at least one of them wrong. The script sets `LANGUAGE = "ru"`.

Two details beyond the transliteration itself:

- **The extension is split off first**, transliterated separately from the
  name, and reattached — so the `.mp3` survives untouched.
- **Collisions get a numeric suffix.** Two different Cyrillic titles can
  transliterate to the same Latin string, and `os.rename` overwrites silently
  when they do. The script probes for an unused `name_1.mp3`, `name_2.mp3`
  before renaming, which turns a silent deletion into a duplicate.

Files whose transliterated name matches the original are left alone, so
re-running over a folder is harmless.

## Run it

```bash
pip install -r requirements.txt
cd /path/to/your/music
python /path/to/rename.py
```

It takes no arguments and operates on the **current working directory only** —
no recursion into subfolders. Each rename is printed as it happens.

Renames are not reversible once the original name is gone. Run it on a copy
first if the folder matters.

## Scope

Deliberately narrow: `.mp3` files, Russian Cyrillic, one directory. Widening it
to other extensions, other languages or a recursive walk means changing the
three constants at the top of the file.

## Stack

Python, `cyrtranslit`.
