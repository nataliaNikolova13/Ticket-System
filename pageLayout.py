from tkinter import *
from tkinter import ttk
from controler import Controler

class Layout():
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket System")
        self.root.geometry("600x600")

        self.controler = Controler()

        self.createMenu()
        self.logInFrame = Frame(self.root)
        self.logInFrame.pack() #fill=BOTH, expand=1
        self.registrtionFrame = Frame(self.root)
        self.registrtionFrame.pack() #fill=BOTH, expand=1
        # self.scrollBar()

    def createMenu(self):

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
            menubar.add_cascade(label="Log In",command=self.logIn)
        else:
            profileMenu = Menu(menubar, tearoff=0)
            profileMenu.add_command(label="View Profile", command="")
            profileMenu.add_command(label="Log Out", command="")
            menubar.add_cascade(label="Profile", menu=profileMenu,command="")

    def scrollBar(self):
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack(fill=BOTH, expand=1)
        self.myCanvas = Canvas(self.mainFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.mainFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")

    def searchBar(self):
        pass

    def logIn(self):
        self.registrtionFrame.destroy()
        self.logInFrame = Frame(self.root)
        self.logInFrame.pack(fill=BOTH, expand=1)
        
        self.titleLogIn = Label(self.logInFrame, text="Log In", justify=CENTER, font=('Arial', 13))
        self.titleLogIn.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=5)
        radio_var = StringVar(value=1)
        userName = StringVar()
        password = StringVar()
        self.entryUsernameLable = Label(self.logInFrame, text="Enter Username", justify=CENTER, font=('Arial', 10))
        self.entryUsernameLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryPasswordLable = Label(self.logInFrame, text="Enter Password", justify=CENTER, font=('Arial', 10))
        self.entryPasswordLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryUsername = Entry(self.logInFrame, bg="white")
        self.entryUsername.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)
        self.entryPassword = Entry(self.logInFrame, bg="white")
        self.entryPassword.grid(row=2, column=1, sticky="nswe", pady=5, padx=5)
        self.UsrRadionBtn = Radiobutton(self.logInFrame, text="Log In as a User", variable=radio_var, value=1, font=('Arial', 10))
        self.UsrRadionBtn.grid(row=4, column=0, columnspan=2, sticky="nswe")
        self.OrgRadionBtn = Radiobutton(self.logInFrame, text="Log In as an Organizer", variable=radio_var, value=2, font=('Arial', 10))
        self.OrgRadionBtn.grid(row=5, column=0, columnspan=2, sticky="nswe")

        self.logInBtn = Button(self.logInFrame, width=20, text="Log In", font=('Arial', 10), command=lambda y = "":self.controler.passLogInInfo(self.entryUsername.get(), self.entryPassword.get(), radio_var.get()))
        self.logInBtn.grid(row=6, column=0, columnspan=2, pady=5)
        
        self.RegisterBtn = Button(self.logInFrame, width=20, text="Register", font=('Arial', 10), command=self.registration)
        self.RegisterBtn.grid(row=7, column=0, columnspan=2, pady=5)

    def registration(self):
        self.logInFrame.destroy()
        self.registrtionFrame = Frame(self.root)
        self.registrtionFrame.pack(fill=BOTH, expand=1)
        
        self.titleRegistrtion = Label(self.registrtionFrame, text="Registration", justify=CENTER, font=('Arial', 13))
        self.titleRegistrtion.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=5)

        self.entryUsernameLable = Label(self.registrtionFrame, text="Enter Username", justify=CENTER, font=('Arial', 10))
        self.entryUsernameLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryPasswordLable = Label(self.registrtionFrame, text="Enter Password", justify=CENTER, font=('Arial', 10))
        self.entryPasswordLable.grid(row=3, column=0, sticky="nswe", pady=5, padx=5)
        self.entryEmailLable = Label(self.registrtionFrame, text="Enter Email", justify=CENTER, font=('Arial', 10))
        self.entryEmailLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryUsername = Entry(self.registrtionFrame, bg="white")
        self.entryUsername.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)
        self.entryPassword = Entry(self.registrtionFrame, bg="white")
        self.entryPassword.grid(row=3, column=1, sticky="nswe", pady=5, padx=5)   
        self.entryEmail = Entry(self.registrtionFrame, bg="white")
        self.entryEmail.grid(row=2, column=1, sticky="nswe", pady=5, padx=5)  

        radio_var = StringVar(value=1)
        self.UsrRadionBtn = Radiobutton(self.registrtionFrame, text="Register as a User", variable=radio_var, value=1, font=('Arial', 10))
        self.UsrRadionBtn.grid(row=7, column=0, columnspan=2, sticky="nswe")
        self.OrgRadionBtn = Radiobutton(self.registrtionFrame, text="Register as an Organizer", variable=radio_var, value=2, font=('Arial', 10))
        self.OrgRadionBtn.grid(row=8, column=0, columnspan=2, sticky="nswe")

        self.RegisterBtn = Button(self.registrtionFrame, width=20, text="Register", font=('Arial', 10), command=lambda y = "":self.controler.passRegistrationInfo(self.entryUsername.get(), self.entryEmail.get(), self.entryPassword.get(), radio_var.get()))
        self.RegisterBtn.grid(row=9, column=0, columnspan=2, pady=5)
        





