import pandas as pd
import webbrowser as wb

df = pd.DataFrame({"links": [None]})

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import Menu
from tkinter import ttk
import student

window1 = Tk()
window1.title("Registration")
window1.geometry('600x600')
lbl = Label(window1, text='Hello and Welcome to our user interface :)')
lbl1 = Label(window1, text='Please specify whether \n you are a professor, \n student, or employee')
lbl1.grid(column=1, row=1)
lbl.grid(column=0, row=0)

selected = IntVar()

rad1 = Radiobutton(window1, text='Student', value=1, variable=selected)  # set different values to every radiobutton
rad2 = Radiobutton(window1, text='Professor', value=2, variable=selected)
rad3 = Radiobutton(window1, text='Employee', value=3, variable=selected)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)


def firstFrame():
    result = selected.get()
    if result == 1:
        window1.destroy()
        window2 = Tk()
        window2.title("Student")
        window2.geometry('600x600')

        lbl2 = Label(window2, text='Hello student :)')
        lbl2.grid(column=1, row=1)

    elif result == 2:
        window1.destroy()
        window3 = Tk()
        window3.title("Professor")
        window3.geometry('600x600')
    elif result == 3:
        window1.destroy()
        window4 = Tk()
        window4.title("Employee")
        window4.geometry('600x600')
    else:
        messagebox.showwarning('Warning!', ' You have not picked yet :) ')


btn = Button(window1, text=" Next ", command=firstFrame)
btn.grid(column=1, row=3)

"""def Mclicked():
    messagebox.showinfo('Message title', 'Message content')
    #messagebox.showewarning('Message title', 'Message content')
    #messagebox.showeerror('Message title', 'Message content')


def clicked():
    print(selected.get())


btn = Button(window, text="Click Me", command=Mclicked)
btn.grid(column=1, row=0)

txt = Entry(window, width=10)  # to disable, add state = 'disabled'
txt.grid(column=2, row=0)
txt.focus()  # focus to write text write away

combo = Combobox(window)
combo['values'] = ('Please Select', 1, 2, 3, 4, 5)
combo.current(0)
combo.grid(column=4, row=0)
combo.get()

chk_state = IntVar()
chk_state.set(0)  # uncheck
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=5, row=0)

rad1 = Radiobutton(window, text='Student', value=1, variable=selected)  # set different values to every radiobutton
rad2 = Radiobutton(window, text='Professor', value=2, variable=selected)
rad3 = Radiobutton(window, text='Employee', value=3, variable=selected)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

txtsc = scrolledtext.ScrolledText(window, width=10, height=10)
txtsc.grid(column=0, row=2)

#res = messagebox.askquestion('Message title','Message content')       #if you click OK or yes or retry, it will return True value,
                                                                        #but if you choose no or cancel, it will return False.
                                                                        #The only function that returns one of three values
                                                                        #is askyesnocancel function, it returns True or False
                                                                        #or None.
#res = messagebox.askyesno('Message title','Message content')
#res = messagebox.askyesnocancel('Message title','Message content')
#res = messagebox.askokcancel('Message title','Message content')
#res = messagebox.askretrycancel('Message title','Message content')

var =IntVar()
var.set(0)
spin = Spinbox(window, from_=0, to=150, width = 10, textvariable = var)
spin.grid(column = 0, row = 4)

bar = Progressbar(window, length=200)
bar['value'] = 10
bar.grid(column = 0, row = 5)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
window.config(menu=menu)
menu.add_cascade(label='File', menu=new_item)
"""
window1.mainloop()


class Restaurant(object):  # Restaurants interested in being on the discount list
    def __init__(self, name, location, offer, telno, website):  # Initializing offers info
        self.name = name
        self.location = location
        self.offer = offer
        self.telno = telno
        self.website = website

    def __str__(self):
        return ('name: ' + str(self.name) + "\nLocation: " + str(self.location) + "\nOffer: " + str(
            self.offer) + "\nTelephone number: " + str(self.telno))

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getOffer(self):
        return self.offer

    def getNumber(self):
        return self.telno

    def getWebsite(self):
        return self.website


class Procurement(object):
    def __init__(self):
        self.offers = pd.DataFrame()

    def Load(self, File):
        self.offers = pd.read_csv(File)

    def Save(self, File):
        self.offers.to_csv(File + ".csv")

    def addRestaurant(self, restaurant):
        new_data = {'Name': restaurant.getName(),
                    'Location': restaurant.getLocation(),
                    'Offer': restaurant.getOffer(),
                    'Telephone #': restaurant.getNumber(),
                    'Website': restaurant.getWebsite()
                    }
        self.offers = self.offers.append(new_data, ignore_index=True)

    def getByLocation(self, location):
        return self.offers[self.offers['Location'] == location]  # returns the offers of restaurants by location


# components for project
""" Rayane Saade, 26/12/2020
Student Affairs and CenterForTeachingAndLearning
Naming conventions suggestions: strict CamelCasing

In this class, we have decided to use the singleton design pattern
"""
import numpy as np

"""
Ensure a class only has one instance, and provide a global point of
access to it.
Source:https://sourcemaking.com/design_patterns/singleton/python/1
"""


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class StudentAffairs(metaclass=Singleton):
    def __init__(self, pathBookingFile):
        self.pathBookingFile = pathBookingFile

    def CreateListLocations(self, ):


    def bookingRooms(self):
        pass

    def GetListLocations(self):
        pass

    def SetListLocations(self):
        pass

    def AppendListLocations(self):
        pass

    def ShrinkListLocations(self):
        pass

    def GetListRequests(self):
        pass

    def SetListRequests(self):
        pass

    def AppendListRequests(self, RequestNumber):
        pass

    def ShrinkListRequests(self, RequestNumber):
        pass

    def ApproveRequest(self, RequestNumber):
        pass

    def DenyRequest(self, RequestNumber):
        pass


class Singleton2(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class CenterForTeachingAndLearning(metaclass=Singleton2):
    def __init__(self):
        pass

    def collectInfo(self):
        pass

    def displayInfo(self):
        pass

    def RequestFromStudents(self):
        pass

    # imagine some type of data collection from students
    def RunASurvey(self):
        # selects  number of students to give out information
        # selects those students in a pseudorandom fashion
        pass


def main():
    m1 = StudentAffairs()
    m2 = StudentAffairs()
    assert m1 is m2


"""
if __name__ == "__main__":
    main()

a = Restaurant(1, 2, 3, 4, 5)
c = Restaurant(2, 1, 3, 2, 4)
b = Procurement()
print(b.addRestaurant(a))
print(b.addRestaurant(c))
print(b.addRestaurant(a))
print(b.offers)
print(b.getByLocation(2))
print(b.getByLocation(1))
b.Save("Cool restaurant directory")
"""
