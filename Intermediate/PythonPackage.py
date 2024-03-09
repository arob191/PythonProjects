from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Company Name", ["SpaceX", "Tesla", "X", "Neuralink"])
my_table.add_column("Industry", ["Rocketry", "Automotive", "Social Media", "NeuroScience"])

my_table.align = "l"

print(my_table)