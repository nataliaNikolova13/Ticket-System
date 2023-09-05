from datetime import date
from enum import Enum

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
    def __init__(self, title, description, location, date, organizer, numAvailableSeats, category, status):
        self.title = title
        self.description = description
        self.location = location
        self.date = date
        self.organizer = organizer
        self.numAvailableSeats = numAvailableSeats
        self.seatsTaken = 0
        self.category = category
        self.subcategories = []
        self.status = status
        # self.photo = photo

    def addSubcategories(self, subcategory):
        self.subcategories.append(subcategory)

    def IsSoldOut(self):
        if self.numAvailableSeats == self.seatsTaken:
            return True
        return False    
