##
# rm_white.py
# removes the whitespace at the end of a line


def rm_whitespace(string):
    """
    Removes the whitespace at the end of a string
    """
    # Convert string to list for easier manipulation
    string_ls = list(string)

    # Reverse because we want to remove the spaces at the
    # end of the line
    string_ls.reverse()

    # This for loop will get the index of the first character that
    # isnt a space
    char = 0
    for char in range(len(string_ls)):
        if string_ls[char] != " ":
            break

    # Get from the list only the chars that arent spaces
    new_string_ls = string_ls[char:]

    # Put it back into the order it's supposed to have
    new_string_ls.reverse()

    # Convert to string
    new_string = ''.join(new_string_ls)

    # When the string is just spaces new_string will equal
    # a single space, we do not want this! This if checks for that
    return "" if new_string == " " else new_string


def main(filename):
    """
    Removes the whitespace at the end of each line
    """
    lines = list()

    # Read the given file
    with open(filename, 'r') as file:
        # Get the lines without the trailing newline
        # while (line := file.readline()):
        line = file.readline()
        while line:
            lines.append(line.strip('\n'))
            line = file.readline()

    # Store into a new file
    with open("nows_" + filename, 'w') as new_file:
        for line in lines:
            new_file.write(rm_whitespace(line) + '\n')

if __name__ == "__main__":
    main(input("File name: "))
