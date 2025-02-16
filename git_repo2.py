print("Welcome to place the rabbit")
field = [ ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"] ]
print(f"{field[0]} \n{field[1]} \n{field[2]} ")
print("\nWere should the rabbit go? 🐇")
position = input("Please choose a row and a column:")
row = int(position[0])
column = int(position[1])
field[row-1][column-1] = "🐇"
print("\nSuccess...\n")
print(f"{field[0]} \n{field[1]} \n{field[2]} ")


# We have a simple project in Python. The project is a game about a rabbit that wants to go to the food. We have three rows and three columns. The first row has three columns and the second row has three columns. It also asks you to affect the row number and the column number.
