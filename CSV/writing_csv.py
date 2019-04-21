from csv import reader, writer, DictWriter

# with open("mookie.csv", "w") as file:
#    csv_writer = writer(file)
#    csv_writer.writerow(['Year', '2020'])

# with open("mookie.csv") as file:
#    csv_reader = reader(file)
#    with open("the_best.csv", "w") as file:
#       csv_writer = writer(file)
#       for row in csv_reader:
#          csv_writer.writerow(["THE BEST" for stat in row])

with open("mookie.csv", "w") as file:
   headers = ["Year", "AVG", "HR", "RBI"]
   csv_writer = DictWriter(file, fieldnames=headers)
   csv_writer.writeheader()
   csv_writer.writerow({
      "Year": 2020,
      "AVG": .375,
      "HR": 47,
      "RBI": 133
   })
   