import pandas as pd

df = pd.read_csv("Chess_Registrations.csv", header=None)

to_list = df.values.tolist()
for name, number in to_list:
    print(name, "+91"+str(number))
# print(to_list)

