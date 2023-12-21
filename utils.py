"""utils"""
def read_lines_from_file(file_path)-> list:
    """get list of input lines"""
    with open(file_path, 'r', encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
