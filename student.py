import pandas as pd
import webbrowser as wb


class student:
    def __init__(self, name, age, ID, email):
        self.name = name
        self.age = age
        self.ID = ID
        self.email = email

    def Accessmap(self):
        WebServer.MapInitialize()
        print('map intialized')  # Webserver initializes the view campus map

    def Accessroom(self):
        if df.links[0] is None:
            print('no link available')  # in case no link is available
        else:
            wb.open_new_tab(str(df.links[0]))  # initialize the link uploaded by the professor

    def GetDiscounts(self):
        WebServer.RequestLocation()  # Webserver sends a location request to the user

        if not WebServer.RequestLocation():
            print("No location found")  # if user rejects the location request, the function stops
        else:
            SearchEngine.AccessDiscounts()  # Search engine searches the database and lists the restaurants
            # close to the user with their respective info

    def Book(self, timeslot):
        if timeslot:
            BookingEngine.SendBooking() # sends request to student affairs for approval
            if StudentAffairs.ApproveRequest():
                BookingEngine.BookSlot()  # if the request is approved, book the time
            else:
                print("no approval given")
        if not timeslot:
            print("no slot available at this time")

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def GetID(self):
        return self.ID

    def GetEmail(self):
        return self.email