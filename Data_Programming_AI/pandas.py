import pandas

commute_df = pandas.read_csv("commute_data.csv")
print(commute_df.head())

commute_df.columns = ['county_name', 'total_commuters', 'super_commuters', 'state_code', 'county_code']

print(commute_df.head())

