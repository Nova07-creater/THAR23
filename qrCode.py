import pandas as pd
import qrcode


class studentsData:
    def __init__(self, datafile):
        self.df = pd.read_csv(datafile)
        self.dataList1 = self.df["Name"].tolist()
        self.dataList2 = self.df["College"].tolist()
        self.dataList3 = self.df["Contact"].tolist()
        self.dataList4 = self.df["Mail"].tolist()
        # self.dataList3 = self.df["CITY"].tolist()
        # self.dataList7 = self.df["STAND ALONE EVENTS"].tolist()
        # self.dataList8 = self.df["GROUP EVENTS"].tolist()
        # self.dataList9 = self.df["CONTACT NO."].tolist()

    def genQRcode(self):
        data_list = list(zip(self.dataList1, self.dataList2, self.dataList3, self.dataList4))
                             
        for data in data_list:
            img = qrcode.make(data)
            name = data[0]
            img.save(f"{name}")

if __name__ == "__main__":
    data_file_path = '/home/narayanj/Practice/participant_details.csv'
    student_data = studentsData(data_file_path)
    student_data.genQRcode()