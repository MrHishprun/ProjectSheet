import pandas as pd
# If pandas is not installed: pip install pandas

class Program:
    def __init__(self):
        file = input("Insert file name (without extension): ")
        self.namexlsx = "D:\\" + file + ".xlsx"
        self.nametxt = "D:\\" + file + ".txt"
        Program.export(self.namexlsx, self.namexlsx)

    def export(namexlsx, nametxt):
        try:
            df = pd.read_excel(namexlsx, sheet_name='Sheet1', index_col=0)
            with open(nametxt, 'w') as filetxt:
                df.to_string(filetxt, index=True)
            print("Conversion to .txt file has been successful.")

        except FileNotFoundError:
            print("File not found, check file name again.")
            print("Conversion to .txt file has failed.")


Program()
