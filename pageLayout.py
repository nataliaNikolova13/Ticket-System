from tkinter import *
from tkinter import ttk
from controler import Controler

class Layout():
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket System")
        self.root.geometry("800x800")

        self.controler = Controler()

        self.createMenu(self.root)

    def createMenu(self,root):

        menubar = Menu(self.root, relief=FLAT)
        self.root.config(menu=menubar)

        eventsMenu = Menu(menubar, tearoff=0)

        eventsMenu.add_command(label="Concerts", command="")
        eventsMenu.add_command(label="Festivals", command="")
        eventsMenu.add_command(label="Seminars", command="")
        eventsMenu.add_command(label="Exhibitions", command="")
        eventsMenu.add_command(label="Charities", command="")
        eventsMenu.add_command(label="Sport events", command="")

        menubar.add_cascade(label="Events", menu=eventsMenu, command="")

        menubar.add_cascade(label="Recommendation",command="")

        if self.controler.currentUser == False:
            menubar.add_cascade(label="Log In",command="")
        else:
            profileMenu = Menu(menubar, tearoff=0)
            profileMenu.add_command(label="View Profile", command="")
            profileMenu.add_command(label="Log Out", command="")
            menubar.add_cascade(label="Profile", menu=profileMenu,command="")

    def searchBar(self):
        pass








# menubar.add_cascade(
#     label="Books",
#     menu=book_menu
# )
