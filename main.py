import events
import createparticipant
import charges
import qrCode
class WelcomeMessage:
    def display(self):

        x= "\033[1mWelcome to the Tech Dunes of Rajathan, Team THAR'23 Welcomes you all\033[0m\n"
        y = x.center(180)
        print(y)
        # print(x.center(50))
ob1=  WelcomeMessage()
ob1.display()