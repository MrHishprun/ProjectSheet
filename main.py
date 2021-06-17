import pandas as pd


# If pandas is not installed: pip install pandas

class Program:
    def __init__(self):
         file = input("Insert file name (without extension): ")
        self.namexlsx = "D:\\xlsx\\" + file + ".xlsx"
        self.namecsv = "D:\\csv\\" + file + ".csv"
        Program.export(self.namexlsx, self.namecsv)

    def export(namexlsx, namecsv):
        try:
            read_file = pd.read_excel(namexlsx, sheet_name='Sheet1', index_col=0)
            read_file.to_csv(namecsv, index=True, sep=',')
            print("Conversion to .csv file has been successful.")

        except FileNotFoundError:
            print("File not found, check file name again.")
            print("Conversion to .csv file has failed.")


Program()
