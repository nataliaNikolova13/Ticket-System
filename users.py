from enum import Enum
import sqlite3
import dataBases

class Role(Enum):
    Unknown = 0
    NormalUser = 1
    Organizer = 2

class User():
    def __init__(self, userName, email, password):
        self.userName = userName
        self.email = email
        self.password = password
        self.role = Role.Unknown
        # self.photo = photo


class NormalUser(User):
    def __init__(self, userName, email, password):
        super().__init__(userName, email, password)
        # self.eventsVisited = []
        # self.genresPrefered = []
        # self.eventsLiked = []
        self.role = Role.NormalUser

    # def addVisitedEvents(self, event):
    #     self.eventsVisited.append(event)  

    # def addPreferedGenre(self, genre):
    #     self.genresPrefered.append(genre)

    # def addLikedEvents(self, liked):
    #     self.eventsLiked.append(liked)  

    # def unlikeEvent(self, event):
    #     pass
    #     # to add

    def addUserToDataBase(self):
        connUsers = sqlite3.connect('users.db')
        cursUsers = connUsers.cursor()

        cursUsers.execute('SELECT * FROM USERS WHERE (UserName = ? AND Email = ? AND Password = ? AND Role = ?)',
                     (self.userName, self.email, self.password, self.role.name))
        entry = cursUsers.fetchone()
        # print(entry)
        if entry is None:
            # print("yes")
            cursUsers.execute("insert into USERS VALUES(?, ?, ?, ?)", (self.userName, self.email, self.password, "NormalUser")) 
        connUsers.commit()
        connUsers.close()




class Organizer(User):
    def __init__(self, userName, email, password):
        super().__init__(userName, email, password)
        # self.eventsOrganized = [] 
        self.role = Role.Organizer

    # def addEventOrganized(self, event):
    #     self.eventsOrganized.append(event)         

    def addUserToDataBase(self):
        connUsers = sqlite3.connect('users.db')
        cursUsers = connUsers.cursor()

        cursUsers.execute('SELECT * FROM USERS WHERE (UserName = ? AND Email = ? AND Password = ? AND Role = ?)',
                     (self.userName, self.email, self.password, self.role.name))
        entry = cursUsers.fetchone()
        if entry is None:
            cursUsers.execute("insert into USERS VALUES(?, ?, ?, ?)", (self.userName, self.email, self.password, "Organizer"))  

        connUsers.commit()
        connUsers.close()             


