from datetime import date
from enum import Enum
import sqlite3
import dataBases


class Status(Enum):
    PAST = 0
    ONGOING = 1
    UPCOMING = 2

class Category(Enum):
    CONCERT = 0
    FESTIVALS = 1
    SEMINARS = 2
    EXHIBITIONS = 3
    CHARITY = 4   
    SPORT = 5
    UNKNOWN = 6

class Event():
    def __init__(self, title, description, location, date, month, year, organizer, numAvailableSeats, category, status, subcategories):
        # print("constr")
        self.title = title
        self.description = description
        self.location = location
        self.date = date
        self.month = month
        self.year = year
        self.organizer = organizer
        self.numAvailableSeats = numAvailableSeats
        self.seatsTaken = 0
        self.category = category
        self.subcategories = subcategories
        self.status = status
        # self.photo = photo

    # def addSubcategories(self, subcategory):
    #     self.subcategories.append(subcategory)

    def IsSoldOut(self):
        if self.numAvailableSeats == self.seatsTaken:
            return True
        return False    
    
    def addToDataBase(self):
        connEvent = sqlite3.connect('events.db')
        cursEvent = connEvent.cursor()
        cursEvent.execute('SELECT * FROM EVENTS WHERE (Title = ? AND Description = ? AND Location = ? AND Date = ? AND Month = ? AND Year = ? AND Organizer = ? AND NumAvailableSeats = ? AND SeatsTaken = ? AND Category = ? AND Subcategory = ? AND Status = ?)',
                          (self.title, self.description, self.location, self.date, self.month, self.year, self.organizer, self.numAvailableSeats, self.seatsTaken, self.category, self.subcategories, self.status))
        
        entry = cursEvent.fetchone()
        if entry is None:
            cursEvent.execute("insert into EVENTS VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.title, self.description, self.location, self.date, self.month, self.year, self.organizer, self.numAvailableSeats, self.seatsTaken, self.category, self.subcategories, self.status))

        connEvent.commit()
        connEvent.close()

    # def print(self, frame):
    #     titleLable = Label(frame, text=self.title)
    #     titleLable.pack()

