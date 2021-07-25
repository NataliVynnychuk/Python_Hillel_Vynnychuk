# import csv
#
# def read_from_csv(filename):
#     with open(filename, 'r') as csv_file:
#         reader = csv.DictReader(csv_file, delimiter=",")
#         data = []
#         for row in reader:
#             data.append(row)
#         return data
#
#
# filename = "new_data.csv"
# new_data = read_from_csv(filename)
# for row in new_data:
#     row["Percentage"] = int(row["Sum"] * 0.2)
# print(new_data)

