import re


def search_engine():
    # Define the variables used to store data
    occurrences = []
    line_num = 0
    # Remember rstrip, lstrip and strip
    # If you'd prefer, enter the direct path in the code instead of using the input function
    file_path = input(r'Please provide the exact path for the file you want to access: ').lower().strip('\"')
    search = input("Type the word you would like to search for: ").lower()
    pattern = re.compile(search, re.IGNORECASE)

    # Open the chosen txt file, reading it
    with open(file_path, "rt") as my_file:

        # Each line it reads, line_num adds to keep track of where it is
        for line in my_file:
            line_num += 1

            # If a match is found, line_num and the line itself (striping the \n at the end) will be appended to the
            # occurrences list
            if pattern.search(line) is not None:
                occurrences.append((line_num, line.rstrip("\n")))

    # Open the recipient txt file, writing it
    with open(r"C:\Users\lucia\PycharmProjects\pythonProject\results.txt", "w") as results:
        # For each item (line) in the occurrences list, write the item as a string in the txt, adding \n for new line
        for item in occurrences:
            results.write(str(item))
            results.write("\n")

        # At the end of the file, \n and write how many matches have been found counting the length of the list
        # Print it for the IDE as well
        results.write("\n")
        results.write(f"Query found {len(occurrences)} matches")
        print(f"Query found {len(occurrences)} matches")


search_engine()
