
import pandas as pd
import re
import csv
print("Greetings Folks, If you are a students of our campus you don't need to pay anything, Rest all of the guest participants have to pay accordingly!!!")

print('''\n Charges For the Registraions are as follows: 
      
          1) If you are our campus student then everything is free for you\n
          2) If You are outside student then you have to pay accordingly: \n
                    a) 50% Off on totals for Campus Ambassadors.add()
                    b) 10,000 INR for each Stand Alone Event.
                    c) 500 INR for 3 events. 
                    d) 100 INR more per event if you want to participate in more than 3 events.
                    e) 500 INR for stay at Campus hostels. 
                    f) 1500 INR extra charges for the Pro-Nites.''')


class Participate:
    def __init__(self):
        self.stand_alone_events = []
        self.tech_events = []
        self.pro_nite_tickets = 0
        self.Stay = 0
        self.total = 0

    def participate_in_stand_alone_events(self):
        num_events = int(
            input("How many Stand Alone Events do you want to participate in? "))
        if num_events > 4:
            print("Limit exceeded, You can not register more than 4 SA Events!!")
        for _ in range(num_events):
            event_name = input("Enter the name of the Stand Alone Event: ")
            self.stand_alone_events.append(event_name)
        print(
            f'The Stand Alone Events you registered are : {self.stand_alone_events}')

    def participate_in_tech_events(self):
        num_events = int(
            input("How many Tech Events do you want to participate in (at least 3)? "))
        for _ in range(num_events):
            event_name = input(f"Enter the name of Tech Event {_ + 1}: ")
            self.tech_events.append(event_name)
        print(f'The Tech Events you registered are : {self.tech_events}')

    def attend_pro_nites(self):
        choice = input("Do you want to attend the Pro Nites? (yes/no): ")
        if choice.lower() == "yes":
            self.pro_nite_tickets = 3

    def NeedStay(self):
        Stay = input(
            "Do you want to stay at our campus hostel during fest? (yes/no): ")
        if Stay.lower() == 'yes':
            self.Stay = 1

    def calculate_total_payment(self):
        stand_alone_cost = len(self.stand_alone_events) * 10000
        tech_cost = len(self.tech_events) * 150
        pro_nite_cost = self.pro_nite_tickets * 1500
        Stay_cost = self.Stay*500
        total_cost = stand_alone_cost + tech_cost + pro_nite_cost + Stay_cost
        self.total = total_cost
        return total_cost

class Totals:
    def __init__(self, Stand_Alone_Events, Tech_Events, Pro_Nite, Stay, Total):
        self.stand_alone_events = Stand_Alone_Events
        self.tech_events = Tech_Events
        self.pro_nite_tickets = Pro_Nite
        self.Stay = Stay
        self.total = Total

    def details(self):
        return {
            "Stand_Alone_Events": self.stand_alone_events,
            "Tech_Events": self.tech_events,
            "Pro_Nite": self.pro_nite_tickets,
            "Stay": self.Stay,
            "Total": self.total
        }

obj = Totals("Stand_Alone_Events", "Tech_Events", "Pro_Nite", "Stay", "Total")

with open("participant_details.csv", "a", newline="\n") as file:
    fieldnames = ["Stand_Alone_Events", "Tech_Events", "Pro_Nite", "Stay", "Total"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow(obj.details())


# with open("participant_details.csv", "a", newline="\n") as file:
#     fieldnames = ["Stand_Alone_Events",
#                   "Tech_Events", "Pro_Nite", "Stay", "Total"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writerow(obj.details())


# class Campus_Student:
#     def __init__(self, rollnumber):
#         self.rollnumber = rollnumber

#     def check_roll_number(self, campstudent):
#         self.campStudent = input('Are you our campus student? (yes/no)')
#         if self.campStudent == 'yes':
#             roll_number = ('Please enter your university Roll Number: ')
#         roll_Pattern = r"^19EUC\d{5}$"
#         if re.match(roll_Pattern, roll_number):
#             print("University roll number verified!!")
#         else:
#             print("No such roll number exist")


# campusstudent = Campus_Student()
# campusstudent.check_roll_number()


participant = Participate()
participant.participate_in_stand_alone_events()
participant.participate_in_tech_events()
participant.attend_pro_nites()
total_payment = participant.calculate_total_payment()
print(f"Total Payment: {total_payment} INR")
