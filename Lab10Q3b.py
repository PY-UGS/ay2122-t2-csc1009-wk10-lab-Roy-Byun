def switch_module(module):
    switcher = {
        "CSC1006": "Mathematics II",
        "CSC1007": "Operating System",
        "CSC1008": "Data Structures and Algorithms",
        "CSC1009": "Object-Oriented Programming",
        "CSC1010": "Computer Networks"
    }
    return switcher.get(module, "Not found")


def main():

    module = input("Enter module code in CAPITAL: ")
    print(switch_module(module))


if __name__ == "__main__":
    main()