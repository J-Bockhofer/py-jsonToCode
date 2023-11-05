def generate_file(filepath, file_name, text):
    temp_path = filepath + file_name
    with open(file_name, 'w') as f:
        f.write(text)