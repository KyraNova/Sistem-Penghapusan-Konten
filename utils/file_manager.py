def read_list(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

def remove_content(file_path, new_content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(new_content)