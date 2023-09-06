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
        self.homeFrame = Frame(self.root)
        self.homeFrame.pack()
        self.createEventFrame = Frame(self.root)
        self.createEventFrame.pack()
        # self.scrollBar()

    def createMenu(self):

        menubar = Menu(self.root, relief=FLAT)
        self.root.config(menu=menubar)

        eventsMenu = Menu(menubar, tearoff=0)

        eventsMenu.add_command(label="All events", command=self.homePage)
        eventsMenu.add_command(label="Concerts", command="")
        eventsMenu.add_command(label="Festivals", command="")
        eventsMenu.add_command(label="Seminars", command="")
        eventsMenu.add_command(label="Exhibitions", command="")
        eventsMenu.add_command(label="Charities", command="")
        eventsMenu.add_command(label="Sport events", command="")

        menubar.add_cascade(label="Events", menu=eventsMenu)
        menubar.add_cascade(label="Most Popular",command="")
        menubar.add_cascade(label="Recommendation",command="")

        if self.controler.currentUserLogged == False:
            menubar.add_cascade(label="Log In",command=self.logIn)
        else:
            profileMenu = Menu(menubar, tearoff=0)
            profileMenu.add_command(label="View Profile", command="")
            profileMenu.add_command(label="Log Out", command=self.logOut)
            menubar.add_cascade(label="Profile", menu=profileMenu,command="")
            if self.controler.currentRole.name == "Organizer":
                profileMenu.add_command(label="Create event", command=self.createEvent)
                profileMenu.add_command(label="View statistics", command="")


    def scrollBar(self):
        self.mainFrame = Frame(self.ho)
        self.mainFrame.pack(fill=BOTH, expand=1)
        self.myCanvas = Canvas(self.mainFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.mainFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")
        # return self.secondFrame

    def searchBar(self):
        pass

    def logIn(self):
        self.destroyFrames()
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

        # self.logInBtn = Button(self.logInFrame, width=20, text="Log In", font=('Arial', 10), command=lambda y = "":self.controler.passLogInInfo(self.entryUsername.get(), self.entryPassword.get(), radio_var.get()))
        self.logInBtn = Button(self.logInFrame, width=20, text="Log In", font=('Arial', 10), command=lambda y = "":self.clickLogInBtn(self.entryUsername, self.entryPassword, radio_var))
        self.logInBtn.grid(row=6, column=0, columnspan=2, pady=5)
        
        self.RegisterBtn = Button(self.logInFrame, width=20, text="Register", font=('Arial', 10), command=self.registration)
        self.RegisterBtn.grid(row=7, column=0, columnspan=2, pady=5)

    def clickLogInBtn(self, entryUsername, entryPassword, radio_var):
        userName = entryUsername.get()
        password = entryPassword.get()
        radio = radio_var.get()
        if self.controler.passLogInInfo(userName, password, radio) == True:
            self.homePage()
            self.createMenu()
        else:
            errorLable = Label(self.logInFrame, text="User not found", font=('Arial', 10))
            errorLable.grid(row=8, column=0, columnspan=2, sticky="nswe")    

    
    def clickRegisterBtn(self, entryUsername, entryEmail, entryPassword, radio_var):
        # print("ok")
        userName = entryUsername.get()
        email = entryEmail.get()
        password = entryPassword.get()
        radio = radio_var.get()
        self.controler.passRegistrationInfo(userName, email, password, radio)
        self.homePage()
        self.createMenu()


    def registration(self):
        self.destroyFrames()
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

        # self.RegisterBtn = Button(self.registrtionFrame, width=20, text="Register", font=('Arial', 10), command=lambda :[self.controler.passRegistrationInfo(self.entryUsername.get(), self.entryEmail.get(), self.entryPassword.get(), radio_var.get()), self.homePage, self.createMenu])
        self.RegisterBtn = Button(self.registrtionFrame, width=20, text="Register", font=('Arial', 10), command=lambda :self.clickRegisterBtn(self.entryUsername, self.entryEmail, self.entryPassword, radio_var))
        self.RegisterBtn.grid(row=9, column=0, columnspan=2, pady=5)


    def homePage(self):
        self.destroyFrames()
        self.homeFrame = Frame(self.root)
        self.homeFrame.pack(fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.homeFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.homeFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")

        self.titleAllEvents = Label(self.secondFrame, text="All events", justify=CENTER, font=('Arial', 13))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=5)   
        self.controler.printAllEvents(self.secondFrame)

    def logOut(self):
        self.controler.logOut()
        self.homePage()
        self.createMenu() 

    def createEvent(self):
        self.destroyFrames()
        self.createEventFrame = Frame(self.root)
        self.createEventFrame.pack(fill=BOTH, expand=1)
        
        self.titleCreateEvent = Label(self.createEventFrame, text="Create Event", justify=CENTER, font=('Arial', 13))
        self.titleCreateEvent.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=5)

        self.entryTitleEventLable = Label(self.createEventFrame, text="Enter Title", justify=CENTER, font=('Arial', 10))
        self.entryTitleEventLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryTitleEvent = Entry(self.createEventFrame, bg="white")
        self.entryTitleEvent.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)

        self.entryDescriptionEventLable = Label(self.createEventFrame, text="Enter Description", justify=CENTER, font=('Arial', 10))
        self.entryDescriptionEventLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryDescriptionEvent = Entry(self.createEventFrame, bg="white")
        self.entryDescriptionEvent.grid(row=2, column=1, sticky="nswe", pady=5, padx=5)

        self.entryLocationEventLable = Label(self.createEventFrame, text="Enter Location", justify=CENTER, font=('Arial', 10))
        self.entryLocationEventLable.grid(row=3, column=0, sticky="nswe", pady=5, padx=5)
        self.entryLocationEvent = Entry(self.createEventFrame, bg="white")
        self.entryLocationEvent.grid(row=3, column=1, sticky="nswe", pady=5, padx=5)

        self.entryDateEventLable = Label(self.createEventFrame, text="Enter Date (dd/mm/yyyy)", justify=CENTER, font=('Arial', 10))
        self.entryDateEventLable.grid(row=4, column=0, sticky="nswe", pady=5, padx=5)
        self.entryDateEvent = Entry(self.createEventFrame, bg="white")
        self.entryDateEvent.grid(row=4, column=1, sticky="nswe", pady=5, padx=5)

        self.entryCapacityEventLable = Label(self.createEventFrame, text="Enter Capacity", justify=CENTER, font=('Arial', 10))
        self.entryCapacityEventLable.grid(row=5, column=0, sticky="nswe", pady=5, padx=5)
        self.entryCapacityEvent = Entry(self.createEventFrame, bg="white")
        self.entryCapacityEvent.grid(row=5, column=1, sticky="nswe", pady=5, padx=5)

        self.entryMainCategoryEventLable = Label(self.createEventFrame, text="Choose Main Category", justify=CENTER, font=('Arial', 10))
        self.entryMainCategoryEventLable.grid(row=6, column=0, sticky="nswe", pady=5, padx=5)
        options = ["Concert", "Festivals", "Seminars", "Exhibitions", "Charity", "Sport"]
        clicked = StringVar()
        clicked.set("Concert")
        drop = OptionMenu(self.createEventFrame, clicked , *options )
        drop.grid(row=6, column=1, sticky="nswe", pady=5, padx=5)
        # print(clicked.get())
    
        self.entrySubCategoriesLable = Label(self.createEventFrame, text="Enter Subcategories", justify=CENTER, font=('Arial', 10))
        self.entrySubCategoriesLable.grid(row=7, column=0, sticky="nswe", pady=5, padx=5)
        self.entrySubCategories = Entry(self.createEventFrame, bg="white")
        self.entrySubCategories.grid(row=7, column=1, sticky="nswe", pady=5, padx=5)

        self.entryStatusEventLable = Label(self.createEventFrame, text="Choose status", justify=CENTER, font=('Arial', 10))
        self.entryStatusEventLable.grid(row=8, column=0, sticky="nswe", pady=5, padx=5)
        optionsStatus = ["Past", "Upcoming"]
        clickedStatus = StringVar()
        clickedStatus.set("Upcoming")
        dropStatus = OptionMenu(self.createEventFrame, clickedStatus , *optionsStatus )
        dropStatus.grid(row=8, column=1, sticky="nswe", pady=5, padx=5)

        self.createEventBtn = Button(self.createEventFrame, width=20, text="Create Event", font=('Arial', 10), command=lambda :self.clickedCreateEventBtn(self.entryTitleEvent, self.entryDescriptionEvent, self.entryLocationEvent, self.entryDateEvent, self.entryCapacityEvent, clicked, self.entrySubCategories, clickedStatus))
        self.createEventBtn.grid(row=9, column=0, columnspan=2, pady=5)

    def clickedCreateEventBtn(self, entryTitleEvent, entryDescriptionEvent, entryLocationEvent, entryDateEvent, entryCapacityEvent, clicked, entrySubCategories, clickedStatus):
        title = entryTitleEvent.get()
        description = entryDescriptionEvent.get()
        location = entryLocationEvent.get()
        date = entryDateEvent.get()
        capacity = entryCapacityEvent.get()
        category = clicked.get()
        subCategories = entrySubCategories.get()
        status = clickedStatus.get()
        # print

        # self.controler.passRegistrationInfo(userName, email, password, radio)
        self.controler.passCreateEventInfo(title, description, location, date, capacity, category, subCategories, status)
        self.homePage()


    def destroyFrames(self):
        self.logInFrame.destroy()
        self.registrtionFrame.destroy()
        self.homeFrame.destroy()
        self.createEventFrame.destroy()
        
          
        





