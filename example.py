from ijones import ijones, ijones_reader, ijones_writer

if __name__ == "__main__":
    received_data = ijones_reader.read_plate_file("test/ijones.in3.txt")
    results = ijones.ijones(*received_data)
    print(results)
    ijones_writer.write_result_file("ijones.out.txt", results)
