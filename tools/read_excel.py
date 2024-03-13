import pandas as pd

file_path = r'./excel/Data_temp.xlsx'
df = pd.read_excel(file_path, sheet_name='高斯噪声')  
df = df.iloc[66:72] # [start : end] ,好像是不包含end的
print(df)
# print(df.columns.values)
# cluster,icp,a,b,c,d = df.loc[:,['ET','ET.1','ET.2','ET.3','ET.4']].values
# print(d)