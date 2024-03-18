rows = 5


# Name inside star pattern
name = input("Enter the name:")
name_length = len(name)
center_spaces = (rows * 2 - 1 - name_length) // 2

# Upper half
for i in range(1, rows + 1):
    if i == rows // 2 + 1:
        print("*" * (center_spaces) + name + " " * (center_spaces))
    else:
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
