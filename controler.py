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

    def printAllEventsGetData(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS')
        result = cursEvent.fetchall()
        connEvent.close()
        return result


    def getAllInfoAboutEvent(self, title, organizator):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Title = ? AND Organizer = ?)', (title, organizator))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result


   


    



