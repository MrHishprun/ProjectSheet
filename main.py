import pandas as pd
plik = input("Podaj nazwe pliku źródłowego (bez rozszerzenia): ")
nazwaxlsx = "D:\\" + plik + ".xlsx"
nazwatxt =  "D:\\" + plik + ".txt"
df = pd.read_excel(nazwaxlsx, sheet_name='Sheet1', index_col=0)
with open(nazwatxt, 'w') as pliktxt:
    df.to_string(pliktxt, index=True)