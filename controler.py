from event import Category
from event import Event as EventCreator
from users import Role, NormalUser, Organizer
import sqlite3
from tkinter import *
import datetime
# from tkinter import ttk


class Controler():
    def __init__(self):
        self.currentUserLogged = False
        self.currentUser = False
        # self.currentUser = True
        self.currentCategory = Category.UNKNOWN
        self.currentRole = Role.Unknown
        
        self.currentDate = datetime.datetime.now()
        self.updateEventStatus()


    def passLogInInfo(self, username, password, role):

        connUsers = sqlite3.connect('users.db')
        cursUsers = connUsers.cursor()
        
        cursUsers.execute('SELECT * FROM USERS WHERE (UserName = ? AND Password = ? AND Role = ?)', (username, password, Role(int(role)).name))

        entry = cursUsers.fetchone()
       
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
          
         
    def logOut(self):
        self.currentUser = False
        self.currentUserLogged = False
        self.currentCategory = Category.UNKNOWN
        self.currentRole = Role.Unknown


    def passCreateEventInfo(self, title, description, location, date, capacity, category, subCategories, status):
        organizer = self.currentUser.userName
        list = date.split('/')
        
        event = EventCreator(title, description, location, int(list[0]), int(list[1]), int(list[2]), organizer, int(capacity), category, status, subCategories)
        
        event.addToDataBase()
        self.updateEventStatus()
        # list = date.split('/')

    def passEditEventInfo(self, title, description, location, date, capacity, category, subCategories, status):
        organizer = self.currentUser.userName
        list = date.split('/')
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('UPDATE EVENTS SET Description = ?, Location = ?, Date = ?, Month = ?, Year = ?, NumAvailableSeats = ?, Category = ?, Subcategory = ?, Status = ? WHERE (Title = ?)', (description, location, int(list[0]), int(list[1]), int(list[2]), capacity, category, subCategories, status, title))
        
        result = cursEvent.fetchone()
        connEvent.commit()
        connEvent.close()
        self.updateEventStatus()

    def passDeleteInfo(self, title):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        connTicketsBought = sqlite3.connect('tickets.db')
        cursTickets = connTicketsBought.cursor()

        cursEvent.execute('DELETE FROM EVENTS WHERE(Title = ?)', (title,))
        cursTickets.execute('DELETE FROM TICKETS WHERE(Title = ?)', (title, ))

        connEvent.commit()
        connEvent.close()
        connTicketsBought.close()



    def printAllEventsGetData(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Status = ? OR Status = ?)', ("Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllConcerts(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Concert","Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllFestivals(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Festivals","Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllByOrganizer(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Organizer = ?)', (self.currentUser.userName,))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def getAllByOrgSorted(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Organizer = ?) ORDER BY SeatsTaken DESC', (self.currentUser.userName,))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def getAllTicketsByUser(self):
        username = self.currentUser.userName
        connTicket = sqlite3.connect('tickets.db')
        cursTicket = connTicket.cursor()
        cursTicket.execute('SELECT * FROM TICKETS WHERE(Username = ?)', (username, ))
        result = cursTicket.fetchall()
        connTicket.close()
        return result
    
    def boolUserHasBookedTicket(self, title):
        username = self.currentUser.userName
        connTicket = sqlite3.connect('tickets.db')
        cursTicket = connTicket.cursor()
        cursTicket.execute('SELECT * FROM TICKETS WHERE(Username = ? AND Title = ?)', (username, title))
        result = cursTicket.fetchone()
        connTicket.close()
        if result is None:
            return False
        else:
            return True
        
    def unbookOneTicket(self, title):
        username = self.currentUser.userName
        connTicket = sqlite3.connect('tickets.db')
        cursTicket = connTicket.cursor()
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursTicket.execute('UPDATE TICKETS SET numTickets=numTickets-1 WHERE (Username = ? AND Title = ?)', (username, title))
        cursEvent.execute("UPDATE EVENTS SET SeatsTaken=SeatsTaken-1 WHERE (Title = ?)", (title,))
        connTicket.commit()
        connEvent.commit()
        connTicket.close()
        connEvent.close()

    def unbookAllTicket(self, title):   
        username = self.currentUser.userName
        connTicket = sqlite3.connect('tickets.db')
        cursTicket = connTicket.cursor()
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursTicket.execute('SELECT * FROM TICKETS WHERE (Username = ? AND Title = ?)', (username, title))
        result = cursTicket.fetchone()
        numTickets = int(result[2])
        cursTicket.execute('DELETE FROM TICKETS WHERE (Username = ? AND Title = ?)', (username, title))

        cursEvent.execute('SELECT SeatsTaken FROM EVENTS WHERE (Title = ?)', (title, ))
        numSeats = cursEvent.fetchone()
        # print(numSeats[0])
        numSeats = numSeats[0]
        cursEvent.execute("UPDATE EVENTS SET SeatsTaken=? WHERE (Title = ?)", (numSeats - numTickets, title))
        connTicket.commit()
        connEvent.commit()
        connTicket.close()
        connEvent.close() 

    
    def searchByKeyword(self, keyword):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Organizer LIKE ? OR Title LIKE ? OR Location LIKE ? OR Description LIKE ? OR Category LIKE ? OR Subcategory LIKE ?)', ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def searchByInterval(self, start, end):
        start = start.split('/')
        end = end.split('/')
        startDate = datetime.datetime(int(start[2]), int(start[1]), int(start[0]))
        endDate = datetime.datetime(int(end[2]), int(end[1]), int(end[0]))
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        # cursEvent.execute('')
        eventsInInterval = []

        cursEvent.execute('SELECT * FROM EVENTS')
        allEvent = cursEvent.fetchall()

        for event in allEvent:
            dateEvent = datetime.datetime(int(event[5]), int(event[4]), int(event[3]))
            if dateEvent >= startDate and dateEvent <= endDate:
                eventsInInterval.append(event)

        connEvent.close()
        return eventsInInterval
    
    def getMostVisitedFestival(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Festivals","Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getMostVisitedConcert(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Concert","Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getMostVisitedSeminar(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Seminars","Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getMostVisitedExhibitions(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Exhibitions", "Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getMostVisitedCharity(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Charity", "Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getMostVisitedTheater(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Theater", "Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getMostVisitedSport(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ("Sport", "Ongoing", "Upcoming"))
        result = cursEvent.fetchone()
        connEvent.close()
        return result
    
    def getEventByTitle(self, title):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Title = ?)', (title,))
        result = cursEvent.fetchone()
        connEvent.close()
        return result

    
    def getTopGenres(self):
        if self.currentUser == False:
            return False 
        # user not logged
        else:
            userName = self.currentUser.userName

            connGenres = sqlite3.connect('genres.db')
            cursGenres = connGenres.cursor()

            cursGenres.execute('SELECT * FROM GENRES WHERE (UserName = ?) ORDER BY visited DESC', (userName, ))
            entry = cursGenres.fetchall()

            prefGenres = []
            for e in entry:
                prefGenres.append(e[1])

            connGenres.close
            self.getrecEvents(prefGenres)

        return self.getrecEvents(prefGenres)

    def getrecEvents(self, prefGenres):
        userName = self.currentUser.userName
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        connTicketsBought = sqlite3.connect('tickets.db')
        cursTickets = connTicketsBought.cursor()
        allEventWithGivenGenres = []
        for genre in prefGenres:
            cursEvent.execute('SELECT * FROM EVENTS WHERE (Subcategory LIKE ? AND (Status = ? OR Status = ?)) ORDER BY SeatsTaken DESC', ('%' + genre + '%', "Ongoing", "Upcoming"))
            events = cursEvent.fetchall()
            for event in events:
                if event not in allEventWithGivenGenres:
                    allEventWithGivenGenres.append(event)
        

        cursTickets.execute('SELECT Title FROM Tickets WHERE(UserName = ?)', (userName, ))
        entry = cursTickets.fetchall()
        allVisitedEvents = []
        for i in entry:
            allVisitedEvents.append(i[0])

        
        recEvents = []

        for i in range(0, len(allEventWithGivenGenres)):
            
            if allEventWithGivenGenres[i][0] not in allVisitedEvents:
                recEvents.append(allEventWithGivenGenres[i])

       
        connEvent.close()
        connTicketsBought.close()
        return recEvents
        
    
    def printAllSeminars(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Seminars", "Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllExhibitions(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Exhibitions", "Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllCharity(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Charity", "Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllSport(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Sport", "Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result
    
    def printAllTheater(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Category = ? AND (Status = ? OR Status = ?))', ("Theater", "Ongoing", "Upcoming"))
        result = cursEvent.fetchall()
        connEvent.close()
        return result

    def getAllInfoAboutEvent(self, title, organizator):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Title = ? AND Organizer = ?)', (title, organizator))
        result = cursEvent.fetchone()
        connEvent.close()
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
        
        
    
    def bookTicket(self, title, subCategories):
        if self.currentUser == False:
            return False
        buyer = self.currentUser.userName

        if self.checkIfSeatsSoldOut(title) == True:
            return False

        connUsers = sqlite3.connect('users.db')
        cursUsers = connUsers.cursor()

        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()

        connTickets = sqlite3.connect('tickets.db')
        cursTickets = connTickets.cursor()

        cursTickets.execute('SELECT * FROM TICKETS WHERE (UserName = ? AND Title = ?)', (buyer, title))
        entry = cursTickets.fetchone()
        boolFirst = True
        if entry is None:
            cursTickets.execute("insert into TICKETS VALUES(?, ?, ?)", (buyer, title, 1))
        else:
            boolFirst = False
            cursTickets.execute('UPDATE TICKETS SET numTickets=numTickets+1 WHERE (UserName = ? AND Title = ?)', (buyer, title)) 
        
        
        connTickets.commit()
        
        connUsers.close()
        cursEvent.close()
        connTickets.close()
        self.updateEventInfo(title)
        self.insertLikedGenres(buyer, subCategories, boolFirst)
        return True
    
    def insertLikedGenres(self, buyer, subCategories, boolFirst):
        connUsers = sqlite3.connect('users.db')
        cursUsers = connUsers.cursor()
        connGenres = sqlite3.connect('genres.db')
        cursGenres = connGenres.cursor()
        

        genres = subCategories.split(', ')

        if boolFirst == True:
            for i in genres:
                cursGenres.execute('SELECT * FROM GENRES WHERE (UserName = ? AND Genre = ?)', (buyer, i))
                entry = cursGenres.fetchone()
                if entry is None:
                    cursGenres.execute('insert into GENRES VALUES (?, ?, ?)', (buyer, i, 1))
                else:
                    cursGenres.execute('UPDATE GENRES SET visited=visited+1 WHERE (UserName = ? AND Genre = ?)', (buyer, i))    
                # cursGenres.execute("insert into GENRES VALUES(?, ?)", (buyer, i, 1))

        connGenres.commit()
        connGenres.close()
        connUsers.close()
    
    def updateEventInfo(self, title):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        
        cursEvent.execute("UPDATE EVENTS SET SeatsTaken=SeatsTaken+1 WHERE (Title = ?)", (title,))

        connEvent.commit()
        connEvent.close()


    def updateEventStatus(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()

        cursEvent.execute('SELECT * FROM EVENTS')
        allEvent = cursEvent.fetchall()

        for event in allEvent:
            dateEvent = datetime.datetime(int(event[5]), int(event[4]), int(event[3]))
            if dateEvent < self.currentDate:
                cursEvent.execute("UPDATE EVENTS SET Status=? WHERE (Title = ?)", ("Past", event[0]))
            else:     
                cursEvent.execute("UPDATE EVENTS SET Status=? WHERE (Title = ?)", ("Ongoing", event[0]))


        connEvent.commit()
        connEvent.close()   



   


    



