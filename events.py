import csv
class Events:
    def __init__(self):
        self.stand_alone_events = ["Go-Karting", "Robo War", "RC Nitro", "MUN"]
        self.tech_events = []

    def Tech_Events(self, csv_file):
        with open(r'/home/narayanj/Practice/THAR/events.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tech_events.append(row["EVENT NAME"])
                
    # def pro_nites():
    #     stars = {
    #         'day1': 'Shreya Ghosal', 
    #         'day2': 'Vishal Shekhar',
    #         'dya3': 'Sanam Band'
    #             }
    #     print(stars)

    def DisplayEvents(self):
        print('\n')
        for i in range(1, 103):
            print('-', end='')
# ANSI escape codes for bold text
        bold_text = "\n\033[1mCome, Participate, Win exciting cash prizes and test your Tech Skills, Team THAR'23 invites you all !!\033[0m"
# Print the text in bold
        print(bold_text)

        for i in range(1, 103):
            print('-', end='')
        print("\n\n >>> STAND ALONE EVENTS:\n")
        for i, event in enumerate(self.stand_alone_events, start=1):
            print(f"\t {i}. {event}")

        print("\n>>> TECHNICAL EVENTS:\n")
        for i, event in enumerate(self.tech_events, start=1):
            print(f"\t {i}. {event}")

obj = Events()
obj.Tech_Events("/home/narayanj/Practice/THAR/events.csv")
obj.DisplayEvents()


# import pandas as pd
# df = pd.read_csv(r'/home/narayanj/Practice/THAR/EventsData/events.csv')
# GroupEvents = df['EVENT NAME'].tolist()
# StandAlone = ['Go-Kart', 'Robo War', 'RC Nitro', 'MUN']
# class Events:
#     def __init__(self):
#         self.StandEveList = []
#         self.Groupevelist = []
#         self.row_index = 0
#         print("Greetings Buddy, We are organizing both Stand-Alone and Group events\n")

#     def getevents(self):
#             print('Our Stand Alone events are: \n')
#             for i, j in enumerate(StandAlone, 1):
#                 print(i, j)
#             print('\n')
#             print('Our Group events are: \n')
#             for i, j in enumerate(GroupEvents, 1):
#                 print('\t')
#                 print(i, j)

#     def TakeGroupEve(self):
#         NumGroup = int(input("Number of events (Group Events) you are interested in? "))
#         for i in range(0, NumGroup):
#             event = input("Which event do you want to participate in? ")
#             self.Groupevelist.append(event)
#         print('\n')
#         print(f'So you have registered in {NumGroup} events and these are: \n')
#         count = 1
#         for i in self.Groupevelist:
#             print(count, i)
#             count += 1

#     def TakestandEve(self):
#         self.StandEveList = []
#         NumStand = int(input('Number of Stand Alone events you are interested in? '))
#         for i in range(0, NumStand):
#             event = input('Which event do you want to participate in? ')
#             self.StandEveList.append(event)
#         print('\n')
#         print(f'So you have registered in {NumStand} events and these are: \n')
#         Count = 1
#         for i in self.StandEveList:
#             print(Count, i)
#             Count += 1

#     def appEventscsv(self):
#         data_file = '/home/narayanj/Practice/THAR/StudentsData/DATA1.csv'
#         df = pd.read_csv(data_file)

#         # Set the 'STAND ALONE EVENTS' and 'GROUP EVENTS' columns for the current row index
#         df.at[self.row_index, 'STAND ALONE EVENTS'] = ', '.join(self.StandEveList)
#         df.at[self.row_index, 'GROUP EVENTS'] = ', '.join(self.Groupevelist)

#         # Save the modified DataFrame back to the CSV file
#         df.to_csv(data_file, index=False)

#     def increment_row_index(self):
#         self.row_index += 1

# participant = Events()
# participant.getevents()

# for i in range(2):
#     participant.TakeGroupEve()
#     participant.TakestandEve()
#     participant.appEventscsv()
#     participant.increment_row_index()