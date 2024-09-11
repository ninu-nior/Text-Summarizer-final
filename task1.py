# Creating a UTF-8 encoded file in Python
file_path = "requirements.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("This is a UTF-8 encoded file.")
