def ijones(height, width, plate):
    def _extend_occurrences(extended_dict, extended_letter, new_occurrences):
        if extended_dict.get(extended_letter):
            extended_dict[extended_letter].extend(new_occurrences)
        else:
            extended_dict[extended_letter] = new_occurrences

    def _append_occurrences(appended_dict, appended_letter, new_occurrence):
        if appended_dict.get(appended_letter):
            appended_dict[appended_letter].append(new_occurrence)
        else:
            appended_dict[appended_letter] = [new_occurrence]

    path_to = [[0 for i in range(width)] for j in range(height)]
    letter_occurrences = {}

    for row in range(height):
        current_letter = plate[row][0]
        path_to[row][0] = 1
        _append_occurrences(letter_occurrences, current_letter, (row, 0))

    for column in range(1, width):
        new_letter_occurrences = {}
        for row in range(height):
            current_letter = plate[row][column]
            for occurrence in letter_occurrences.get(current_letter, []):
                path_to[row][column] += path_to[occurrence[0]][occurrence[1]]
            if plate[row][column-1] != current_letter:
                path_to[row][column] += path_to[row][column-1]
            _append_occurrences(new_letter_occurrences, current_letter, (row, column))

        for letter in new_letter_occurrences:
            _extend_occurrences(letter_occurrences, letter, new_letter_occurrences[letter])

    if height == 1:
        return path_to[0][width-1]

    return path_to[0][width-1] + path_to[height-1][width-1]
