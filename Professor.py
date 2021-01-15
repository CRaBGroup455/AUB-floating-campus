import webbrowser as wb


class Professor:
    def __init__(self, name, age, ID, email, df): # where df is the small database
        self.name = name
        self.age = age
        self.ID = ID
        self.email = email
        self.df = df

    def upload(self, link):
        self.df.links[0] = link  # store link in the database

    def research(self):
        wb.open_new_tab('www.aub.edu.lb/libraries/Pages/default.aspx') #Initialize the link of "AUB libraries"

    def __str__(self):
        return 'name: ' + str(self.name) + "\nage: " + str(self.age) \
               + "\nID: " + str(self.ID) + "\nemail: " + str(self.email)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getID(self):
        return self.ID

    def getEmail(self):
        return self.email