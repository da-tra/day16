from prettytable import PrettyTable

table = PrettyTable() 
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"]), table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
table.vrules = True
table.vertical_char = "$"
table.horizontal_char = "$"
junction_char = "$"
print(table.align)
print(table.vrules)
print(table)