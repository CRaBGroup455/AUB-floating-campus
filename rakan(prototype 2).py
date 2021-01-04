import pandas as pd
import webbrowser as wb

df = pd.DataFrame({"links": [0, 0, 0, 0, 0]})


class Professor:
    def __init__(self, name, age, ID, email):
        self.name = name
        self.age = age
        self.ID = ID
        self.email = email

    def upload(self):
        link = input("upload your link here: ")  # Professors upload the meeting link to students
        df.links[0] = link  # add link to database
        print(" the link:" + link + " has been uploaded successfully!")

    def research(self):
        print("Click here to access AUB libraries")  # Professors conduct research using AUB libraries
        wb.open_new_tab('www.aub.edu.lb/libraries/Pages/default.aspx')

    def __str__(self):
        return 'name: ' + str(self.name) + "\nage: " + str(self.age) + "\nID: " + str(self.ID)

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def GetID(self):
        return self.ID

    def GetEmail(self):
        return self.email


class student:
    def __init__(self, name, age, ID, email):
        self.name = name
        self.age = age
        self.ID = ID
        self.email = email

    def Accessmap(self):
        print('map intialized')  # Webserver initializes the view campus map

    def Accessroom(self):
        if df.links[0] == 0:
            print('no link available')  # in case no link is available
        else:
            wb.open_new_tab(str(df.links[0]))  # initialize the link uploaded by the professor

    def Discounts(self):
        WebServer.RequestLocation()  # Webserver sends a location request to the user

        if SearchEngine.RequestLocation() == False:
            print("No location found")  # if user rejects the location request, the function stops
        else:
            SearchEngine.AccessDiscounts()  # Search engine searches the database and lists the restaurants
            # close to the user with their respective info

    def Book(self):
        BookingEngine.RequestBooking()
        if timeslot == True:
            BookingEngine.AcceptBooking()  # sends request to student affairs for approval
            if StudentAffairs.approve():
                BookingEngine.Bookslot()  # if the request is approved, book the time
            else:
                print("no approval given")
        if timeslot == False:
            print("no slot available at this time")

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def GetID(self):
        return self.ID

    def GetEmail(self):
        return self.email
