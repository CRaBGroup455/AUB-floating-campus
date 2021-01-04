import pandas as pd
import webbrowser as wb

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
        return 'name: ' + str(self.name) + "\nage: " + str(self.age) \
               + "\nID: " + str(self.ID) + "\nemail: " + str(self.email)

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def GetID(self):
        return self.ID

    def GetEmail(self):
        return self.email