def ijones(height, width, plate):
    path_to = [[0 for _ in range(width)] for _ in range(height)]
    paths_to_letter = {}

    for row in range(height):
        current_letter = plate[row][0]
        path_to[row][0] = 1
        paths_to_letter[current_letter] = paths_to_letter.setdefault(current_letter, 0) + 1

    for column in range(1, width):
        new_paths_to_letter = {}
        for row in range(height):
            current_letter = plate[row][column]
            path_to[row][column] = paths_to_letter.get(current_letter, 0)
            if plate[row][column-1] != current_letter:
                path_to[row][column] += path_to[row][column-1]
            new_paths_to_letter[current_letter] = new_paths_to_letter.setdefault(current_letter, 0) + path_to[row][column]

        for letter in new_paths_to_letter:
            paths_to_letter[letter] = paths_to_letter.setdefault(letter, 0) + new_paths_to_letter[letter]

    if height == 1:
        return path_to[0][width-1]

    return path_to[0][width-1] + path_to[height-1][width-1]
