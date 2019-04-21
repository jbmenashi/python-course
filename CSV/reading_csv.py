from csv import reader, DictReader

# with open("mookie.csv") as file:
#    csv_reader = reader(file)
#    next(csv_reader)
#    for season in csv_reader:
#       print(f"{season[0]} - AVG: {season[17]}, HR: {season[11]}, RBI: {season[12]}")


with open("mookie.csv") as file:
   csv_reader = DictReader(file)
   for row in csv_reader:
      print(f"{row['Year']} - AVG: {row['BA']}, HR: {row['HR']}, RBI: {row['RBI']}")