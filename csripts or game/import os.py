import os

search_filename = "reaction_cover"  # без расширения, если не знаешь точное
search_folder = "C:\\"  # начни с C:\ или укажи конкретную папку

for root, dirs, files in os.walk(search_folder):
    for file in files:
        if search_filename.lower() in file.lower():
            full_path = os.path.join(root, file)
            print("Файл найден:", full_path)
