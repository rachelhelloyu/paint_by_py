import pandas as pd

file_path = r'./excel/Data_temp.xlsx'
df = pd.read_excel(file_path, sheet_name='无噪声')  
print(df.columns.values)
print(df.iloc[0:6])
# cluster,icp,a,b,c,d = df.loc[:,['ET','ET.1','ET.2','ET.3','ET.4']].values
# print(d)