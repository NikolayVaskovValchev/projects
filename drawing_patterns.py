# 🖼️ Python Pattern Drawing Project

# ---- MENU ----
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# User's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Taking the dimensions by the choice of the user
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5, 8]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# ---- PATTERNS ----

#CHOICE 1 --> RIGHT-ANGLED TRIANGLE
if choice == 1:

    for x in range(rows + 1):
        print(x * "*")

#CHOICE 2 -->  SQUARE WITH A HOLLOW CENTER
elif choice == 2:

    for x in range(size + 1):
        if x == 0 or x == size:
            print("*" * size)
        else:
            print("*" + (" " * (size - 2)) + "*")

#CHOICE 3 --> DIAMOND
elif choice == 3:

    for x in range(rows):
        spaces = rows - x - 1
        stars = 2 * x + 1
        print(" " * spaces + stars * "*")
    for x in range(rows - 2, -1, -1):
        spaces = rows - x - 1
        stars = 2 * x + 1
        print(" " * spaces + stars * "*")

#CHOICE 4 --> LEFT-ANGLED TRIANGLE
elif choice == 4:

    for x in range(rows, 0, -1):  # Start from rows and decrease to 1
        print(x * "*")

    ##CHOICE 5 --> HOLLOW SQUARE
elif choice == 5:

    for x in range(size + 1):
        if x == 0 or x == size:
            print("*" * size)
        else:
            print("*" + (" " * (size - 2)) + "*")

#CHOICE 6 --> PYRAMID
elif choice == 6:

    for x in range(rows):
        spaces = rows - x - 1
        stars = 2 * x + 1
        print(" " * spaces + stars * "*")

#CHOICE 7 --> REVERSED PYRAMID
elif choice == 7:

    for x in range(rows -1, -1, -1):
        spaces = rows - x - 1
        stars = 2 * x + 1
        print(" " * spaces + stars * "*")

#CHOICE 8 --> RECTANGLE WITH A HOLLOW CENTER
elif choice == 8:
    # TODO: Handle separate width and height inputs for rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    pass

else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit