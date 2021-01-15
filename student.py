import webbrowser as wb
from Webserver import WebServer
from BookingEngine import BookingEngine


class Student:
    def __init__(self, name, age, ID, email, df):  # where df is the small database
        self.name = name
        self.age = age
        self.ID = ID
        self.email = email
        self.df = df

    def accessMap(self):
        WebServer.mapInitialize()
        print('map intialized')  # Webserver initializes the view of the campus map

    def accessRoom(self):
        if self.df.links[0] is None:
            return False  # in case no link is available
        else:
            wb.open_new_tab(str(self.df.links[0]))  # initialize the link uploaded by the professor
            return True             # return True for the GUI to know the operation was successful

    def getDiscounts(self):
        WebServer.requestLocation()  # Webserver sends a location request to the user

        if not WebServer.requestLocation():
            print("No location found")  # if user rejects the location request, the function stops
        else:
            Location = ''
            Procurement.getByLocation(Location)  # The procurement class searches the database and lists the restaurants
            # close to the user with their respective information

    def Book(self, timeslot):
        if timeslot:
            BookingEngine.sendBooking()  # if there's a timeslot available, send request to student affairs for approval
            if StudentAffairs.ApproveRequest():
                BookingEngine.bookSlot()  # if the request is approved, book the time
            else:
                print("no approval given")
        if not timeslot:
            print("no slot available at this time")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getID(self):
        return self.ID

    def getEmail(self):
        return self.email
