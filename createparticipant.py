import csv


class CreateParticipant:
    def __init__(self, Name, College, Contact, Mail):
        self.name = Name
        self.college = College
        self.contact = Contact
        self.mail = Mail

    def details(self):
        return {
            "Name": self.name,
            "College": self.college,
            "Contact": self.contact,
            "Mail": self.mail
        }


with open("participant_details.csv", "a", newline="\n") as file:
    fieldnames = ["Name", "College", "Contact", "Mail"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    while True:
        name = input("\tYour Name? ")
        college = input("\tCollege name? ")
        contact = input("\tContact number? ")
        mail = input("\tYour mail id? ")

        partDetails = CreateParticipant(name, college, contact, mail)
        writer.writerow(partDetails.details())

        more_participant = input(
            "Do you want to add more participant? (yes/no): ")
        if more_participant.lower() != 'yes':
            break
