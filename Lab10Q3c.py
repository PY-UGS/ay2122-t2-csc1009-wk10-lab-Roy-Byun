def descend_odd(start, end):
    for i in range(start, end, -1):
        if i % 2 == 1:
            print("Value of odd number in between ", start, "and ", end, " are: ", i)


def main():

    start = int(input("Enter starting Number: "))
    end = int(input("Enter last Number: "))

    descend_odd(start, end)


if __name__ == "__main__":
    main()

