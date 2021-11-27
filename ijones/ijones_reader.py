def read_plate_file(file_to_read):

    with open(file_to_read, "r") as plate_file:
        plate_params = list(plate_file.readline().split(" "))
        plate_width = int(plate_params[0])
        plate_height = int(plate_params[1])
        plate = []

        for line in plate_file:
            plate.append(line)

    return plate_height, plate_width, plate
