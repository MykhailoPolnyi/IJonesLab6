def ijones(height, width, plate):
    path_to = [[0 for i in range(width)] for j in range(height)]
    letter_occurrences = {}

    for row in range(height):
        current_letter = plate[row][0]
        path_to[row][0] = 1
        letter_occurrences[current_letter] = letter_occurrences.get(current_letter, 0) + 1

    for column in range(1, width):
        new_letter_occurrences = {}
        for row in range(height):
            current_letter = plate[row][column]
            path_to[row][column] = path_to[row][column-1] + letter_occurrences.get(current_letter, 0)
            new_letter_occurrences[current_letter] = new_letter_occurrences.get(current_letter, 0) + 1
        for letter in new_letter_occurrences:
            letter_occurrences[letter] = letter_occurrences.get(letter, 0) + new_letter_occurrences[letter]

    for word in plate:
        print(word)

    print("-"*width)
    for row in path_to:
        print(row)
    print(letter_occurrences)

    return path_to[0][width-1] + path_to[height-1][width-1]


if __name__ == "__main__":
    print(ijones(3, 4, ("aaaa", "aaaa", "aaaa")))
