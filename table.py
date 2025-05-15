from prettytable import PrettyTable

table = PrettyTable()
Name = ("Aniket","Meghma","Soha","Aditya","Ujjawal")
Age = (20,19,19,22,20)
Place = ("Noida","Kolkata","Asansol","Noida","Madhubani")
table.add_column("Name",Name)
table.add_column("Age",Age)
table.add_column("Place",Place)
table.align = "l"
print(table)