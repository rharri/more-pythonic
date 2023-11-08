COLS = 33


def print_columns():
    for col in range(COLS):
        print('|', end="")

    print("", end="\n")


def print_tabstop(tabsize=8):
    for col in range(COLS):
        if col % tabsize == 0:
            print('T', end="")
            continue
        print('-', end="")

    print("", end="\n")


if __name__ == "__main__":
    print_columns()
    print_tabstop()

    s = "01\t012\t0123\t01234"
    print(s)

    print(s.expandtabs(tabsize=8))

    print_tabstop(4)
    print(s.expandtabs(tabsize=4))

    print("", end="\n")
    print("length =", len(s))
    print("length =", len(s.expandtabs(8)))
    print("length =", len(s.expandtabs(4)))

    """
    Python Docs:
    Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current 
    column and the given tab size.
    """

    print("", end="\n")

    def print_employee_table():
        header = "Name\tTitle\tSalary\tHire Date".expandtabs(16)
        print(header)
        print("=" * len(header))

        emp1 = "Foo Bar\tProgrammer\t100000.00\t11/8/2023".expandtabs(16)
        emp2 = "Foo Bar\tProgrammer\t100000.00\t11/8/2023".expandtabs(16)
        emp3 = "Foo Bar\tProgrammer\t100000.00\t11/8/2023".expandtabs(16)
        for emp in (emp1, emp2, emp3):
            print(emp)

    print_employee_table()
