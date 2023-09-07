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
    
    def printAllConcerts(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?)', ("Concert",))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllFestivals(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?)', ("Festivals",))
        result = cursEvent.fetchall()
        connEvent.close()
        # self.getMostVisitedFEstival()
        return result
    
    def getMostVisitedFestival(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?) ORDER BY SeatsTaken DESC', ("Festivals",))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result
    
    def getMostVisitedConcert(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?) ORDER BY SeatsTaken DESC', ("Concert",))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result
    
    def getMostVisitedSeminar(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?) ORDER BY SeatsTaken DESC', ("Seminars",))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result
    
    def getMostVisitedExhibitions(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?) ORDER BY SeatsTaken DESC', ("Exhibitions",))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result
    
    def getMostVisitedCharity(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?) ORDER BY SeatsTaken DESC', ("Charity",))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result
    
    def getMostVisitedSport(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?) ORDER BY SeatsTaken DESC', ("Sport",))
        result = cursEvent.fetchone()
        connEvent.close()
        # print(result)
        return result
    
    
    def printAllSeminars(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?)', ("Seminars",))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllExhibitions(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?)', ("Exhibitions",))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllCharity(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?)', ("Charity",))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllSport(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ?)', ("Sport",))
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
    
    def checkIfSeatsSoldOut(self, title):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Title = ?)', (title,))
        result = cursEvent.fetchone()
        connEvent.close()
        if result[7] == result[8]:
            return True
        else:
            return False
        # print(len(result))
        
    
    def bookTicket(self, title, subCategories):
        if self.currentUser == False:
            return False
        buyer = self.currentUser.userName

        if self.checkIfSeatsSoldOut(title) == True:
            return False

        connTickets = sqlite3.connect('tickets.db')
        cursTickets = connTickets.cursor()

        cursTickets.execute("insert into TICKETS VALUES(?, ?)", (buyer, title))
        connTickets.commit()
        connTickets.close()
        self.updateEventInfo(title)
        self.insertLikedGenres(buyer, subCategories)
        return True
    
    def insertLikedGenres(self, buyer, subCategories):
        connGenres = sqlite3.connect('genres.db')
        cursGenres = connGenres.cursor()

        genres = subCategories.split(', ')

        for i in genres:
            cursGenres.execute("insert into GENRES VALUES(?, ?)", (buyer, i))

        connGenres.commit()
        connGenres.close()
    
    def updateEventInfo(self, title):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        
        cursEvent.execute("UPDATE EVENTS SET SeatsTaken=SeatsTaken+1 WHERE (Title = ?)", (title,))

        connEvent.commit()
        connEvent.close()



   


    



