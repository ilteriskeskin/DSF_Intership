import pandas as pd

plan = pd.read_csv('slcsp/plans.csv')
zips = pd.read_csv('slcsp/slcsp.csv')

rates = []

for i in range(len(plan)):
    temp = plan.plan_id[i]
    for j in range(len(zips)):
        if int(temp[-5:]) == int(zips.zipcode[j]):
            rates.append(plan.rate[i])


zips['rate'] = pd.Series(rates)
zips.to_csv('slcsp/slcsp.csv')