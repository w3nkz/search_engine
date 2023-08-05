import re


def search_engine():
    occurrences = []
    line_num = 0
    print("Welcome. This is a search engine developed by w3nkz\n")
    file_path = input("Please enter the path of the file you want to access: ").lower().strip('\"')

    while len(occurrences) == 0:
        with open(file_path, "rt") as to_be_read:
            search = input("Enter the word you would like to search: ")
            pattern = re.compile(search, re.IGNORECASE)
            for line in to_be_read:
                line_num += 1
                if pattern.search(line) is not None:
                    occurrences.append((line_num, line.rstrip("\n")))
            print(f"Query found {len(occurrences)} matches\n")
            if len(occurrences) == 0:
                answer = ""
                while answer == "":
                    answer = input("Would you like to continue searching in the same file? "
                                   "Type either yes of no: \n").lower().strip()
                    if answer == "yes":
                        continue
                    if answer == "no":
                        print("Quitting the program")
                        quit()
                    else:
                        print("Only yes or no answer accepted.")
                        answer = ""
    with open(r"C:\Users\lucia\PycharmProjects\pythonProject\results.txt", "w") as results:
        results.write(f"You searched for [{search.upper()}]")
        results.write("\n")
        results.write("\n")

        for item in occurrences:
            results.write(str(item))
            results.write("\n")

        results.write("\n")
        results.write(f"Query found {len(occurrences)} matches")


search_engine()
