import pandas as pd
import webbrowser as wb
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from student import Student
from Professor import Professor

df = pd.DataFrame({"links": [None, None]})
rakan = Student('rakan', 20, 201907075, 'rab42@mail.aub.edu', df)
Zaraket = Professor('Fadi', 35, 20100000, 'fz11@mail.aub.edu', df)

window1 = Tk()                         # creation of the first window seen by user
window1.title("Registration")           # setting the title of the first window
window1.geometry('600x600')             # setting the width and the length of the first window
lbl = Label(window1, text='Hello and Welcome to our user interface :) ')
lbl.grid(column=0, row=0)
lbl1 = Label(window1, text='Please specify whether \n you are a professor, \n student, or employee')
lbl1.grid(column=1, row=1)   # creation of two labels

selected = IntVar()    # Extremely crutial variable that doesn't allow the user to pick 2 choices at a time!

rad1 = Radiobutton(window1, text='Student', value=1, variable=selected)
rad2 = Radiobutton(window1, text='Professor', value=2, variable=selected)
rad3 = Radiobutton(window1, text='Employee', value=3, variable=selected)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)      # creation of the three radio buttons


def AccessRoom():               # command function for the button "Enter Lecture"
    b = rakan.accessRoom()
    if not b:
        messagebox.showwarning('Warning!', ' The link is not uploaded yet! ')


def Research():             # command function for the button "Access AUB libraries"
    d = Zaraket.research()


def firstFrame():
    result = selected.get()     # we identify which radio button the user picked and check it.
    if result == 1:    # if the user picked "student", then the interface of the student is initialized
        window1.destroy()
        window2 = Tk()
        window2.title("Student")
        window2.geometry('600x600')

        lbl2 = Label(window2, text='Hello student :)')
        lbl2.grid(column=0, row=0)
        btn1 = Button(window2, text="Enter Lecture", command=AccessRoom)
        btn1.grid(column=0, row=1)                          # creation of a button
        btn2 = Button(window2, text="Check for Discounts")
        btn2.grid(column=1, row=1)
        btn3 = Button(window2, text="Book")
        btn3.grid(column=2, row=1)

    elif result == 2:    # if the user picked "Professor", then the interface of the Professor is initialized
        window1.destroy()
        window3 = Tk()
        window3.title("Professor")
        window3.geometry('600x600')
        lbl3 = Label(window3, text='Hello Professor :)')
        lbl3.grid(column=0, row=0)
        lbl4 = Label(window3, text='Enter the link here:')
        lbl4.grid(column=0, row=1)
        txt = Entry(window3, width=10)      # An entry where the user can type whatever he/she wants
        txt.grid(column=1, row=1)
        txt.focus()         # for the user to be able to write the text directly instead of clicking on the entry

        def Upload():           # command function for the button "Upload link to students"
            link = str(txt.get())
            if link == '':
                messagebox.showwarning('Warning!', 'You did not type your link!')
                # if nothing is typed, a warning message is shown
            else:
                Zaraket.upload(link)
                messagebox.showinfo('Notification', 'Your link has been uploaded!')

        btn4 = Button(window3, text="Upload link to students", command=Upload)
        btn4.grid(column=0, row=2)
        btn5 = Button(window3, text="Access AUB libraries", command=Research)
        btn5.grid(column=1, row=2)

    elif result == 3:            # if the user picked "Employee", then the interface of the employee is initialized
        window1.destroy()
        window4 = Tk()
        window4.title("Employee")
        window4.geometry('600x600')
        lbl5 = Label(window4, text='Hello Employee :)')
        lbl5.grid(column=0, row=0)
        btn6 = Button(window4, text="Student Affairs")
        btn6.grid(column=0, row=1)
        btn7 = Button(window4, text="Check Parking lot")
        btn7.grid(column=1, row=1)

    else:
        messagebox.showwarning('Warning!', ' You have not picked yet! ')
        # if the user doesn't pick anything, he'll get a warning notification


btn = Button(window1, text=" Next ", command=firstFrame)
btn.grid(column=1, row=3)
window1.mainloop()      # initialize window1 as main window



