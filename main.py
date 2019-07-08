import pandas
import csv

# with open('slcsp/slcsp.csv') as slcsp_reader:
#     slcsp_reader = csv.reader(slcsp_reader)
#     line_count = 0
#     for row in slcsp_reader:
#         if line_count == 1:
#             zip_codes.append(row)
#         else:
#             line_count += 1

# ihtiyacım olan şey plan_id'deki (row[0]) son 5 eleman ve karşılığı olan rate değeri
# with open('deneme.csv') as deneme_file:
#     deneme_reader = csv.reader(deneme_file, delimiter=',')
#     line_count = 0
#     for row in deneme_reader:
#         if line_count == 1:
#             plans.append(row[0])
#         else:
#             line_count += 1

plan = pandas.read_csv('deneme.csv')
zips = pandas.read_csv('deneme2.csv')

for i in range(len(plan)):
    temp = plan.plan_id[i]
    for j in range(len(zips)):
        if int(temp[-5:]) == int(zips.zipcode[j]):
            print(str(plan.rate[i]))
