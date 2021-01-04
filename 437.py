import pandas as pd
import urllib
import webbrowser as wb


class Professor:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def upload(self):
        link = input("upload your link here: ")  # Professors upload the meeting link to students
        print(" the link: " + link + " has been uploaded successfully!")

    def research(self):
        print("Click here to access AUB libraries")  # Professors conduct research using AUB libraries
        wb.open_new_tab('www.aub.edu.lb/libraries/Pages/default.aspx')

class student:
    def __init__(self,name,age,ID):
        self.name = name
        self.age = age
        self.ID = ID

    def Accessmap(self):
        WebServer.accessmap() # Webserver initializes the view campus map

    def Accessroom(self):
        WebServer.accessroom() # Webserver initializes the link of the lecture

    def Discounts(self):
        WebServer.RequestLocation() # Webserver sends a location request to the user

        if SearchEngine.RequestLocation() == False:
            print("No location found") # if user rejects the location request, the function stops
        else:
            SearchEngine.AccessDiscounts() # Search engine searches the database and lists the restaurants
                                           # close to the user with their respective info

    def Booking(self):
        BookingEngine.RequestBooking()
        if timeslot == True:
            BookingEngine.AcceptBooking() # sends request to student affairs for approval
            if StudentAffairs.approve():
                BookingEngine.Bookslot() # if the request is approved, book the time
            else:
                print("no approval given")
        if timeslot == False:
            print("no slot available at this time")
