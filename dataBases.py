import sqlite3

connUsers = sqlite3.connect('users.db')
cursUsers = connUsers.cursor()

tableUsers = """ CREATE TABLE IF NOT EXISTS USERS(
                    UserName CHAR(100) NOT NULL PRIMARY KEY,
                    Email CHAR(100) NOT NULL,
                    Password CHAR(25) NOT NULL,
                    Role CHAR(25)
        
        )"""



connGenres = sqlite3.connect('genres.db')
cursGenres = connGenres.cursor()

tableGenres = """ CREATE TABLE IF NOT EXISTS GENRES(
            UserName CHAR(100) NOT NULL,
            Genre CHAR(59) NOT NULL,
            visited INT,
            PRIMARY KEY (UserName, Genre),
            FOREIGN KEY (UserName) REFERENCES USE (UserName) 
            ON DELETE CASCADE ON UPDATE NO ACTION

)
"""

cursGenres.execute(tableGenres)
cursGenres.close()


connEvent = sqlite3.connect('events.db')
cursEvent = connEvent.cursor()

tableEvents = """CREATE TABLE IF NOT EXISTS EVENTS(
                Title CHAR(100) NOT NULL  PRIMARY KEY,
                Description CHAR(1000) NOT NULL,
                Location CHAR(100) NOT NULL,
                Date INT, 
                Month INT,
                Year INT,
                Organizer CHAR(100) NOT NULL,
                NumAvailableSeats INT, 
                SeatsTaken INT, 
                Category CHAR(50) NOT NULL,
                Subcategory CHAR(100) NOT NULL,
                Status CHAR(50) NOT NULL,
                FOREIGN KEY (Organizer) REFERENCES USERS (UserName) 
            ON DELETE CASCADE ON UPDATE NO ACTION
)
"""



connTicketsBought = sqlite3.connect('tickets.db')
cursTickets = connTicketsBought.cursor()

tableTickets = """ CREATE TABLE IF NOT EXISTS TICKETS(
            UserName CHAR(100) NOT NULL,
            Title CHAR(100) NOT NULL,
            numTickets INT,
            PRIMARY KEY (UserName, Title),
            FOREIGN KEY (UserName) REFERENCES USERS (UserName) 
            ON DELETE CASCADE ON UPDATE NO ACTION,
            FOREIGN KEY (Title) REFERENCES EVENTS (Title) 
            ON DELETE CASCADE ON UPDATE NO ACTION
)
"""

cursUsers.execute(tableUsers)
connUsers.close()

cursEvent.execute(tableEvents)
connEvent.close()

cursTickets.execute(tableTickets)
connTicketsBought.close()