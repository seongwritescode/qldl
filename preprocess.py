import pandas as pd


# df= pd.read_csv('/home/thinhnd/study/naru/datasets/Vehicle__Snowmobile__and_Boat_Registrations.csv')
# print(df.head)
# columns = [col for col, dt in df.dtypes.items() if dt == object]
# df[columns] = df[columns].fillna('')

# df.to_csv('/home/thinhnd/study/naru/datasets/Vehicle__Snowmobile__and_Boat_Registrations_1.csv', index=False)


df = pd.read_csv('/home/thinhnd/study/naru/datasets/Vehicle__Snowmobile__and_Boat_Registrations_1.csv')
columns = [col for col, dt in df.dtypes.items() if dt == object]
print(columns)
df[columns] = df[columns].fillna('None')   
df.to_csv('/home/thinhnd/study/naru/datasets/Vehicle__Snowmobile__and_Boat_Registrations.csv', index=False)
