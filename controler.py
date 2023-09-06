from event import Category
from event import Event as EventCreator
from users import Role, NormalUser, Organizer
import sqlite3
from tkinter import *
# from tkinter import ttk


class Controler():
    def __init__(self):
        self.currentUserLogged = False
        self.currentUser = False
        # self.currentUser = True
        self.currentCategory = Category.UNKNOWN
        self.currentRole = Role.Unknown
        # self.currentRole = Role.Organizer


    def passLogInInfo(self, username, password, role):
        # print(role)
        # print(Role(int(role)).name)
        # print(Role(role).name)

        # print(role.name)
        
        # print("Username %s Password %s Role %s"%(username, password, Role(int(role)).name))  

        connUsers = sqlite3.connect('users.db')
        cursUsers = connUsers.cursor()
        # cursUsers.execute('SELECT count(*) FROM USERS')
        cursUsers.execute('SELECT * FROM USERS WHERE (UserName = ? AND Password = ? AND Role = ?)', (username, password, Role(int(role)).name))

        entry = cursUsers.fetchone()
        # print(entry)
        if entry is None:
            return False
        else:
            if Role(int(role)).name == "NormalUser":
                self.currentUser = NormalUser(entry[0], entry[1], entry[2])
            elif Role(int(role)).name == "Organizer":
                self.currentUser = Organizer(entry[0], entry[1], entry[2])  
            else:
                print("Problem with log in")      
            self.currentRole = Role(int(role))  
            self.currentUserLogged = True 
            return True
          

    def passRegistrationInfo(self, username, email, password, role):
        # print(role)
        if Role(int(role)).name == "NormalUser":
            user = NormalUser(username, email, password)
            user.addUserToDataBase()
        elif Role(int(role)).name == "Organizer":
            user = Organizer(username, email, password)
            user.addUserToDataBase()
        else:
            print("Problem with passRegistrationInfo")  

        self.currentUser = user
        self.currentRole = Role(int(role))  
        self.currentUserLogged = True 
        # print("ok")  
        # 
    def logOut(self):
        self.currentUser = False
        self.currentUserLogged = False
        self.currentCategory = Category.UNKNOWN
        self.currentRole = Role.Unknown


    def passCreateEventInfo(self, title, description, location, date, capacity, category, subCategories, status):
        organizer = self.currentUser.userName
        list = date.split('/')
        # print(*list)
        # event = Event(title, description, location, int(list[0]), int(list[1]), int(list[2]), organizer, int(capacity), category, status, subCategories) 
        print(category)
        event = EventCreator(title, description, location, int(list[0]), int(list[1]), int(list[2]), organizer, int(capacity), category, status, subCategories)
        # print(category)title, description, location, date, month, year, organizer, numAvailableSeats, category, status, subcategories
        event.addToDataBase()

    def printAllEvents(self, frame):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS')
        result = cursEvent.fetchall()
        count = 1
        for i in range(0, len(result)):
            # print(result[i])
            titleLable = Label(frame, text=result[i][0], font=('Arial', 12), justify=LEFT)
            titleLable.grid(row=count, sticky="w")
            t = "Date: " + str(result[i][3]) + '.' + str(result[i][4]) + '.' + str(result[i][5])
            dateLable = Label(frame, text=t)
            dateLable.grid(row=count+1, sticky="w")
            t = "Location: " + result[i][2]
            locationLable = Label(frame, text=t)
            locationLable.grid(row =count+2, sticky="w")
            t = "Organizer: " + result[i][6]
            orgLabel = Label(frame, text=t)
            orgLabel.grid(row=count+3, sticky="w")
            t = "Category: " + str(result[i][9]) 
            categoryLabel = Label(frame, text=t)
            categoryLabel.grid(row=count+4, sticky="w")
            moreInfoBtn = Button(frame, text="More Information", font=('Arial', 10), width=20, command=lambda:self.passMoreInfoBtn(result[i][0], result[i][6], frame))
            moreInfoBtn.grid(row=count+5, sticky="n", pady=10)
            count = count + 10

        connEvent.close()


    # def passMoreInfoBtn(self, title, organizer, frame):
    #     frame.destroy()
    #     titleLable = Label(frame, text=title, font=('Arial', 12), justify=LEFT)
    #     titleLable.grid(row=0, sticky="nswe")

   


    



