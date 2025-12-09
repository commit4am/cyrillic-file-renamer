import os
import cyrtranslit

LANGUAGE = "ru"  # for Russian Cyrillic

for filename in os.listdir():
    if os.path.isfile(filename) and filename.lower().endswith(".mp3"):
        name_part, ext = os.path.splitext(filename)
        new_name = cyrtranslit.to_latin(name_part, LANGUAGE) + ext

        if new_name != filename:
            # avoid overwriting existing files
            counter = 1
            base_name = os.path.splitext(new_name)[0]
            while os.path.exists(new_name):
                new_name = f"{base_name}_{counter}{ext}"
                counter += 1

            os.rename(filename, new_name)
            print(f"{filename} → {new_name}")
