def write_result_file(file_to_write, result):
    with open(file_to_write, "w") as result_file:
        result_file.write(str(result))
