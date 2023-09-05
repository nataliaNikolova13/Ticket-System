from enum import Enum

class Role(Enum):
    Unknown = 0
    NormalUser = 1
    Organizer = 2

class User():
    def __init__(self, userName, email, password, logedIn):
        self.userName = userName
        self.email = email
        self.password = password
        self.role = Role.Unknown
        # self.logIn = logIn
        # self.photo = photo


class NormalUser(User):
    def __init__(self):
        self.eventsVisited = []
        self.genresPrefered = []
        self.eventsLiked = []
        self.role = Role.NormalUser

    def addVisitedEvents(self, event):
        self.eventsVisited.append(event)  

    def addPreferedGenre(self, genre):
        self.genresPrefered.append(genre)

    def addLikedEvents(self, liked):
        self.eventsLiked.append(liked)  

    def unlikeEvent(self, event):
        pass
        # to add

    def login(self, name, password):
        pass    


class Organizer(User):
    def __init__(self):
        self.eventsOrganized = [] 
        self.role = Role.Organizer

    def addEventOrganized(self, event):
        self.eventsOrganized.append(event)                  


