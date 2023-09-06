import sqlite3

connUsers = sqlite3.connect('users.db')
cursUsers = connUsers.cursor()

tableUsers = """ CREATE TABLE IF NOT EXISTS USERS(
                    UserName CHAR(100) NOT NULL,
                    Email CHAR(100) NOT NULL,
                    Password CHAR(25) NOT NULL,
                    Role CHAR(25)
        
        )"""
cursUsers.execute(tableUsers)
connUsers.close()


connGenres = sqlite3.connect('genres.db')
cursGenres = connGenres.cursor()

tableGenres = """ CREATE TABLE IF NOT EXISTS GENRES(
            UserName CHAR(100) NOT NULL,
            GENRES CHAR(59) NOT NULL
)
"""

cursGenres.execute(tableGenres)
cursGenres.close()


connEvent = sqlite3.connect('events.db')
cursEvent = connEvent.cursor()

tableEvents = """CREATE TABLE IF NOT EXISTS EVENTS(
                Title CHAR(100) NOT NULL,
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
                Status CHAR(50) NOT NULL
)
"""
cursEvent.execute(tableEvents)
cursEvent.close()