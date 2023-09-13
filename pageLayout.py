from tkinter import *
from tkinter import ttk
from controler import Controler
import textwrap
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Layout():
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket System")
        self.root.geometry("600x650")

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
        self.editEventFrame = Frame(self.root)
        self.editEventFrame.pack()
        self.moreInfoPage = Frame(self.root)
        self.moreInfoPage.pack()
        self.mostPopularFrame = Frame(self.root)
        self.mostPopularFrame.pack()
        self.recFrame = Frame(self.root)
        self.recFrame.pack()
        self.orgFrame = Frame(self.root)
        self.orgFrame.pack()
        self.userFrame = Frame(self.root)
        self.userFrame.pack()
        self.searchFrame = Frame(self.root)
        self.searchFrame.pack()
        # self.statFrame = Frame(self.root)
        # self.statFrame.pack()
        self.secondFrame = Frame(self.root)
        # self.scrollBar()
        self.homePage()

    def createMenu(self):

        menubar = Menu(self.root, relief=FLAT)
        self.root.config(menu=menubar)

        eventsMenu = Menu(menubar, tearoff=0)

        eventsMenu.add_command(label="All events", command=self.homePage)
        eventsMenu.add_command(label="Concerts", command=self.concertPage)
        eventsMenu.add_command(label="Festivals", command=self.festivalPage)
        eventsMenu.add_command(label="Seminars", command=self.seminarsPage)
        eventsMenu.add_command(label="Exhibitions", command=self.exhibitionsPage)
        eventsMenu.add_command(label="Charities", command=self.charityPage)
        eventsMenu.add_command(label="Sport events", command=self.sportPage)
        eventsMenu.add_command(label="Theater", command=self.theaterPage)

        menubar.add_cascade(label="Events", menu=eventsMenu)
        menubar.add_cascade(label="Most Popular",command=self.mostPopular)
        menubar.add_cascade(label="Recommendation",command=self.recPage)
        menubar.add_cascade(label="Search",command=self.searchPage)

        if self.controler.currentUserLogged == False:
            menubar.add_cascade(label="Log In",command=self.logIn)
        else:
            profileMenu = Menu(menubar, tearoff=0)
            # profileMenu.add_command(label="View Profile", command="")
            profileMenu.add_command(label="Log Out", command=self.logOut)
            if self.controler.currentRole.name == "Organizer":
                
                menubar.add_cascade(label="Profile", menu=profileMenu,command="")
                profileMenu.add_command(label="View Profile", command=self.organizerProfileView)
                profileMenu.add_command(label="Create event", command=self.createEvent)
                # profileMenu.add_command(label="View statistics", command=self.viewStatPage)
            else:
                menubar.add_cascade(label="Profile", menu=profileMenu,command="")    
                profileMenu.add_command(label="View Profile", command=self.userProfileView)


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
        self.logInFrame.pack()
        
        self.titleLogIn = Label(self.logInFrame, text="Log In", justify=CENTER, font=('Arial', 13))
        self.titleLogIn.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=(25, 10))
        radio_var = StringVar(value=1)
        userName = StringVar()
        password = StringVar()
        self.entryUsernameLable = Label(self.logInFrame, text="Enter Username", justify=CENTER, font=('Arial', 10))
        self.entryUsernameLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryPasswordLable = Label(self.logInFrame, text="Enter Password", justify=CENTER, font=('Arial', 10))
        self.entryPasswordLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryUsername = Entry(self.logInFrame, bg="white")
        self.entryUsername.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)
        self.entryPassword = Entry(self.logInFrame, bg="white", show="*")
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
        if userName == "" or email == "" or password == "":
            errorLable = Label(self.registrtionFrame, text="You have to enter valid information", font=('Arial', 10))
            errorLable.grid(row=18, column=0, columnspan=2, sticky="nswe")  
        else:
            self.controler.passRegistrationInfo(userName, email, password, radio)
            self.homePage()
            self.createMenu()


    def registration(self):
        self.destroyFrames()
        self.registrtionFrame = Frame(self.root)
        self.registrtionFrame.pack()
        
        self.titleRegistrtion = Label(self.registrtionFrame, text="Registration", justify=CENTER, font=('Arial', 13))
        self.titleRegistrtion.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=(25,10))

        self.entryUsernameLable = Label(self.registrtionFrame, text="Enter Username", justify=CENTER, font=('Arial', 10))
        self.entryUsernameLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryPasswordLable = Label(self.registrtionFrame, text="Enter Password", justify=CENTER, font=('Arial', 10))
        self.entryPasswordLable.grid(row=3, column=0, sticky="nswe", pady=5, padx=5)
        self.entryEmailLable = Label(self.registrtionFrame, text="Enter Email", justify=CENTER, font=('Arial', 10))
        self.entryEmailLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryUsername = Entry(self.registrtionFrame, bg="white")
        self.entryUsername.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)
        self.entryPassword = Entry(self.registrtionFrame, bg="white", show="*")
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

        self.titleAllEvents = Label(self.secondFrame, text="All events", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllEvent(self.secondFrame)

    def concertPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All concerts", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllConcerts(self.secondFrame)    

    def festivalPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All Festivals", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllFestivals(self.secondFrame)   

    def seminarsPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All Seminars", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllSeminars(self.secondFrame)   

    def exhibitionsPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All Exhibitions", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllExhibitions(self.secondFrame)      

    def charityPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All Charities", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllCharities(self.secondFrame)   

    def sportPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All Sport Events", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllSports(self.secondFrame) 

    def theaterPage(self):
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

        self.titleAllEvents = Label(self.secondFrame, text="All Theater & Art Events", justify=LEFT, font=('Arial', 14))
        self.titleAllEvents.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0), padx=20)   
        self.printAllTheater(self.secondFrame) 

    def printAllTheater(self, frame):
        result = self.controler.printAllTheater()
        self.printEvent(frame, result)  

    def printAllSports(self, frame):
        result = self.controler.printAllSport()
        self.printEvent(frame, result)               

    def printAllCharities(self, frame):
        result = self.controler.printAllCharity()
        self.printEvent(frame, result)       

    def printAllExhibitions(self, frame):
        result = self.controler.printAllExhibitions()
        self.printEvent(frame, result)
    
    def printAllSeminars(self, frame):
        result = self.controler.printAllSeminars()
        self.printEvent(frame, result)
    
    def printAllFestivals(self, frame):
        result = self.controler.printAllFestivals()
        self.printEvent(frame, result)

    def printAllConcerts(self, frame):
        result = self.controler.printAllConcerts()  
        self.printEvent(frame, result)

    def printEvent(self, frame, result):
        count = 6
        for i in range(0, len(result)):
            myFrame = tb.Frame(frame, bootstyle="flatly")
            myFrame.grid(row=count, pady=20)
            titleLable = Label(frame, text=result[i][0], font=('Arial', 12), justify=LEFT)
            titleLable.grid(row=count, sticky="w", padx=15)
            t = "Date: " + str(result[i][3]) + '.' + str(result[i][4]) + '.' + str(result[i][5])
            dateLable = Label(frame, text=t)
            dateLable.grid(row=count+1, sticky="w", padx=20)
            t = "Location: " + result[i][2]
            locationLable = Label(frame, text=t)
            locationLable.grid(row =count+2, sticky="w", padx=20)
            t = "Organizer: " + result[i][6]
            orgLabel = Label(frame, text=t)
            orgLabel.grid(row=count+3, sticky="w", padx=20)
            t = "Category: " + str(result[i][9]) 
            categoryLabel = Label(frame, text=t)
            categoryLabel.grid(row=count+4, sticky="w", padx=20)
            moreInfoBtn = Button(frame, text="More Information", font=('Arial', 10), width=20, command=lambda i = i:self.passMoreInfoBtn(result[i][0], result[i][6]))
            moreInfoBtn.grid(row=count+5, sticky="w", pady=10, padx=10)
            count = count + 10    


    def mostPopular(self):
        self.destroyFrames()
        self.mostPopularFrame = Frame(self.root)
        self.mostPopularFrame.pack(fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.mostPopularFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.mostPopularFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="w")
        

        lableTitle = Label(self.secondFrame, text="Check out the most visited event of each category", font=('Arial', 14))
        lableTitle.grid(row=0, pady=(10, 10), padx=10)


        result = []
        bestConcerts = self.controler.getMostVisitedConcert()
        bestFestival = self.controler.getMostVisitedFestival()
        bestSeminar = self.controler.getMostVisitedSeminar()
        bestExhibition = self.controler.getMostVisitedExhibitions()
        bestCharity = self.controler.getMostVisitedCharity()
        bestSport = self.controler.getMostVisitedSport()
        bestTheater = self.controler.getMostVisitedTheater()

        lst = []

        if bestConcerts is not None:
            lst.append("Concert")
            result.append(bestConcerts)
        if bestFestival is not None:
            lst.append("Festival")
            result.append(bestFestival) 
        if bestSeminar is not None:
            lst.append("Seminar")
            result.append(bestSeminar)
        if bestExhibition is not None:
            lst.append("Exhibition")
            result.append(bestExhibition)
        if bestCharity is not None:
            lst.append("Charity")
            result.append(bestCharity)
        if bestSport is not None:
            lst.append("Sport event")
            result.append(bestSport)   
        if bestTheater is not None:
            lst.append("Theater & Art")
            result.append(bestTheater)     

        self.printEventWithAddLable(self.secondFrame, result, lst)  

    def printEventWithAddLable(self, frame, result, lst):
        count = 2
        for i in range(0, len(result)):
            myFrame = tb.Frame(frame, bootstyle="flatly")
            myFrame.grid(row=count, pady=10, padx=30)
            cat = "The most visited event in Category: " + lst[i]
            lf = tb.LabelFrame(frame, text=cat, width=60, relief="groove", padding=10, style='primary.TLabelframe')
            lf.grid(column=0, row=count-1, padx=15, pady=10, sticky="w")
            # categoryLable = Label(frame, text=cat, font=('Arial', 12), justify=LEFT)
            # categoryLable.grid(row=count-1, sticky="w", pady=5, padx=10)
            titleLable = Label(lf, text=result[i][0], font=('Arial', 12), justify=LEFT)
            titleLable.grid(row=count, sticky="w", padx=15)
            t = "Date: " + str(result[i][3]) + '.' + str(result[i][4]) + '.' + str(result[i][5])
            dateLable = Label(lf, text=t)
            dateLable.grid(row=count+1, sticky="w", padx=20)
            t = "Location: " + result[i][2]
            locationLable = Label(lf, text=t)
            locationLable.grid(row =count+2, sticky="w", padx=20)
            t = "Organizer: " + result[i][6]
            orgLabel = Label(lf, text=t)
            orgLabel.grid(row=count+3, sticky="w", padx=20)
            t = "Category: " + str(result[i][9]) 
            categoryLabel = Label(lf, text=t)
            categoryLabel.grid(row=count+4, sticky="w", padx=20)
            tl = tb.Separator(lf, orient='horizontal', style='primary.Horizontal.TSeparator')
            tl.grid(row= count+5, pady=(6,0), padx=(20, 400))
            moreInfoBtn = Button(lf, text="More Information", font=('Arial', 10), width=20, command=lambda i = i:self.passMoreInfoBtn(result[i][0], result[i][6]))
            moreInfoBtn.grid(row=count+6, sticky="w", pady=10, padx=10)
            count = count + 10         

    def printAllEvent(self, frame):
        result = self.controler.printAllEventsGetData()
        self.printEvent(frame, result)
            

    def passMoreInfoBtn(self, title, organizator):
        self.destroyFrames()    
        self.moreInfoPage = Frame(self.root)
        self.moreInfoPage.pack(fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.moreInfoPage)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.moreInfoPage, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")

        titleLable = Label(self.secondFrame, text=title, font=('Arial', 15), justify=LEFT)
        titleLable.grid(row=0, sticky="nw", pady=10, columnspan=2, padx=10)
        result = self.controler.getAllInfoAboutEvent(title, organizator)
        descr = "Description: " + result[1]
        splitDescr = textwrap.wrap(descr, 80)
        descr = '\n'.join(splitDescr)
        labDescr = Label(self.secondFrame, text=descr, justify=LEFT, font=('Arial', 11), padx=10)
        location = "Location: " + result[2]
        labLocation = Label(self.secondFrame, text=location, font=('Arial', 11), justify=LEFT, padx=10)
        date = "Date: " + str(result[3]) + '.' + str(result[4]) + '.' + str(result[5])
        labDate = Label(self.secondFrame, text=date, font=('Arial', 11), justify=LEFT, padx=10)
        org = "Organizer: " + result[6]
        labOrg = Label(self.secondFrame, text = org, font=('Arial', 11), justify=LEFT, padx=10)
        capacity = "Capacity: " + str(result[7])
        labCapacity = Label(self.secondFrame, text = capacity, font=('Arial', 11), justify=LEFT, padx=10)
        takenSeats = "Seats sold: " + str(result[8])
        boolSpaceLeft = True
        if result[8] >= result[7]:
            boolSpaceLeft = False
        labSeats = Label(self.secondFrame, text = takenSeats, font=('Arial', 11), justify=LEFT, padx=10)
        category = "Category: " + result[9]
        labCat = Label(self.secondFrame, text = category, font=('Arial', 11), justify=LEFT, padx=10)
        subCat = "Subcategories: " + result[10]
        splitCat = textwrap.wrap(subCat, 60)
        subCat = '\n'.join(splitCat)
        
        sub = result[10]
        labSubCat = Label(self.secondFrame, text = subCat, font=('Arial', 11), justify=LEFT, padx=10)
        status = "Status: " + result[11]
        labStatus = Label(self.secondFrame, text = status, font=('Arial', 11), justify=LEFT, padx=10)
        
        labDate.grid(row=1, sticky="w", columnspan=2, padx=2)
        labDescr.grid(row=9, sticky="w", pady=10, columnspan=2, padx=2)
        labLocation.grid(row=2, sticky="w", columnspan=2, padx=2)
        labOrg.grid(row=3, sticky="w", columnspan=2, padx=2)
        labCapacity.grid(row=7, sticky="w", columnspan=2, padx=2)
        labSeats.grid(row=8, sticky="w", columnspan=2, padx=2)
        labCat.grid(row=4, sticky="w", columnspan=2, padx=2)
        labSubCat.grid(row=5, sticky="w", columnspan=2, padx=2)
        labStatus.grid(row=6, sticky="w", columnspan=2, padx=2)

        bookTicketsBtn = Button(self.secondFrame, text="Book Ticket", font=('Arial', 11), command=lambda:self.bookTicket(title, organizator, boolSpaceLeft, sub, result[11]), width=40)
        bookTicketsBtn.grid(row = 12, sticky="nswe", pady=5, columnspan=2, padx=(10, 0))
        if self.controler.currentRole.name == "Organizer" and result[6] == self.controler.currentUser.userName:
            editEventBtn = Button(self.secondFrame, text="Edit Event", font=('Arial', 11), command=lambda:self.editEventView(title), width=40)
            editEventBtn.grid(row = 14, sticky="nswe", pady=5, columnspan=2, padx=(10, 0))
            deleteEventBtn = Button(self.secondFrame, text="Delete Event", font=('Arial', 11), command=lambda:self.deleteEventView(title), width=40)
            deleteEventBtn.grid(row = 15, sticky="nswe", pady=(5, 20), columnspan=2, padx=(10, 0))
        if self.controler.currentUser != False and self.controler.boolUserHasBookedTicket(title) == True:
            unbookTicketBtn = Button(self.secondFrame, text="Unbook One Ticket", font=('Arial', 11), command=lambda:self.unbookOneTicketView(title), width=16)
            unbookTicketBtn.grid(row = 13, column=0, sticky="nswe", pady=5, padx=(10, 2))
            unbookAllTicketsBtn = Button(self.secondFrame, text="Unbook All Tickets", font=('Arial', 11), command=lambda:self.unbookAllTicketView(title), width=16)
            unbookAllTicketsBtn.grid(row = 13, column=1, sticky="nswe", pady=5, padx=(2, 0))


    def unbookOneTicketView(self, title):
        self.controler.unbookOneTicket(title) 
        self.userProfileView()
        confWindow = Toplevel(self.root)
        confWindow.title("Confirmation")
        confWindow.geometry("250x150")
        text = Label(confWindow, text="You have successfully \n unbooked One Ticket", font=('Arial',12))
        text2 = Label(confWindow, text="We are sorry you couldn't make it!", font=('Arial',10))
        text.pack(pady=(20, 0))
        text2.pack(pady=10)
        

    def unbookAllTicketView(self, title):
        self.controler.unbookAllTicket(title) 
        self.userProfileView()
        confWindow = Toplevel(self.root)
        confWindow.title("Confirmation")
        confWindow.geometry("250x150")
        text = Label(confWindow, text="You have successfully \n unbooked All your Tickets", font=('Arial',12))
        text2 = Label(confWindow, text="We are sorry you couldn't make it!", font=('Arial',10))
        text.pack(pady=(20, 0))
        text2.pack(pady=10)

    def editEventView(self, title):
        result = self.controler.getEventByTitle(title)
        self.destroyFrames()
        self.editEventFrame = Frame(self.root)
        self.editEventFrame.pack()
        
        self.titleCreateEvent = Label(self.editEventFrame, text="Edit Event", justify=CENTER, font=('Arial', 13))
        self.titleCreateEvent.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=5)

        self.entryTitleEventLable = Label(self.editEventFrame, text="Enter Title", justify=CENTER, font=('Arial', 10))
        self.entryTitleEventLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryTitleEvent = Entry(self.editEventFrame, bg="white")
        self.entryTitleEvent.insert(0, result[0])
        self.entryTitleEvent.config(state= "disabled")
        self.entryTitleEvent.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)

        self.entryDescriptionEventLable = Label(self.editEventFrame, text="Enter Description", justify=CENTER, font=('Arial', 10))
        self.entryDescriptionEventLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryDescriptionEvent = Text(self.editEventFrame, bg="white", height=6, width=25)
        self.entryDescriptionEvent.insert(END, result[1])
        self.entryDescriptionEvent.grid(row=2, column=1, sticky="nswe", pady=5, padx=5)

        self.entryLocationEventLable = Label(self.editEventFrame, text="Enter Location", justify=CENTER, font=('Arial', 10))
        self.entryLocationEventLable.grid(row=3, column=0, sticky="nswe", pady=5, padx=5)
        self.entryLocationEvent = Entry(self.editEventFrame, bg="white")
        self.entryLocationEvent.insert(0, result[2])
        self.entryLocationEvent.grid(row=3, column=1, sticky="nswe", pady=5, padx=5)

        self.entryDateEventLable = Label(self.editEventFrame, text="Enter Date", justify=CENTER, font=('Arial', 10))
        self.entryDateEventLable.grid(row=4, column=0, sticky="nswe", pady=5, padx=5)
        date = str(result[3]) + '.' + str(result[4]) + '.' + str(result[5])
        self.entryDateEvent = Entry(self.editEventFrame, bg="white")
        self.entryDateEvent.insert(0, date)
        self.entryDateEvent.grid(row=4, column=1, sticky="nswe", pady=5, padx=5)

        self.entryCapacityEventLable = Label(self.editEventFrame, text="Enter Capacity", justify=CENTER, font=('Arial', 10))
        self.entryCapacityEventLable.grid(row=5, column=0, sticky="nswe", pady=5, padx=5)
        self.entryCapacityEvent = Entry(self.editEventFrame, bg="white")
        self.entryCapacityEvent.insert(0, result[7])
        self.entryCapacityEvent.grid(row=5, column=1, sticky="nswe", pady=5, padx=5)

        self.entryMainCategoryEventLable = Label(self.editEventFrame, text="Choose Main Category", justify=CENTER, font=('Arial', 10))
        self.entryMainCategoryEventLable.grid(row=6, column=0, sticky="nswe", pady=5, padx=5)
        options = ["Concert", "Festivals", "Seminars", "Exhibitions", "Charity", "Sport", "Theater"]
        clicked = StringVar()
        # print(result)
        for option in options:
            # print(option, result[8])
            if option == result[9]:
                clicked.set(option)
        drop = OptionMenu(self.editEventFrame, clicked , *options )
        drop.grid(row=6, column=1, sticky="nswe", pady=5, padx=5)
        # print(clicked.get())
    
        self.entrySubCategoriesLable = Label(self.editEventFrame, text="Enter Subcategories", justify=CENTER, font=('Arial', 10))
        self.entrySubCategoriesLable.grid(row=7, column=0, sticky="nswe", pady=5, padx=5)
        self.entrySubCategories = Entry(self.editEventFrame, bg="white")
        self.entrySubCategories.insert(0, result[10])
        self.entrySubCategories.grid(row=7, column=1, sticky="nswe", pady=5, padx=5)

        self.entryStatusEventLable = Label(self.editEventFrame, text="Choose status", justify=CENTER, font=('Arial', 10))
        self.entryStatusEventLable.grid(row=8, column=0, sticky="nswe", pady=5, padx=5)
        optionsStatus = ["Ongoing", "Upcoming"]
        clickedStatus = StringVar()
        # print(result[11])
        for status in optionsStatus:
            # print()
            if status == result[11]:
                clickedStatus.set(status)
        # clickedStatus.set("Ongoing")
        dropStatus = OptionMenu(self.editEventFrame, clickedStatus , *optionsStatus )
        dropStatus.grid(row=8, column=1, sticky="nswe", pady=5, padx=5)

        self.createEventBtn = Button(self.editEventFrame, width=20, text="Edit Event", font=('Arial', 10), command=lambda :self.clickedEditEventBtn(self.entryTitleEvent, self.entryDescriptionEvent, self.entryLocationEvent, self.entryDateEvent, self.entryCapacityEvent, clicked, self.entrySubCategories, clickedStatus))
        self.createEventBtn.grid(row=9, column=0, columnspan=2, pady=5)

    def deleteEventView(self, title):
        self.controler.passDeleteInfo(title)
        self.organizerProfileView()


    def clickedEditEventBtn(self, entryTitleEvent, entryDescriptionEvent, entryLocationEvent, entryDateEvent, entryCapacityEvent, clicked, entrySubCategories, clickedStatus):
        title = entryTitleEvent.get()
        description = entryDescriptionEvent.get("1.0",END)
        location = entryLocationEvent.get()
        date = entryDateEvent.get()
        capacity = entryCapacityEvent.get()
        category = clicked.get()
        subCategories = entrySubCategories.get()
        status = clickedStatus.get()
        # print

        # self.controler.passRegistrationInfo(userName, email, password, radio)
        self.controler.passEditEventInfo(title, description, location, date, capacity, category, subCategories, status)
        self.organizerProfileView()


    def organizerProfileView(self):
        self.destroyFrames()
        self.orgFrame = Frame(self.root)
        self.orgFrame.pack(fill=BOTH, expand=1)
        self.myCanvas = Canvas(self.orgFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.orgFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")   

        orgLabel = Label(self.secondFrame, text = "User: " + self.controler.currentUser.userName, font=('Arial', 14), justify=LEFT)
        orgLabel.grid(row=0, sticky="nw", pady=(10, 0), padx=15) 

        orgEventLabel = Label(self.secondFrame, text = "Your Events:", font=('Arial', 13), justify=LEFT)
        orgEventLabel.grid(row=1, sticky="nw", pady=10, padx=15) 

        result = self.controler.printAllByOrganizer()
        self.printEvent(self.secondFrame, result)

        

    def userProfileView(self):
        self.destroyFrames()
        self.userFrame = Frame(self.root)
        self.userFrame.pack(fill=BOTH, expand=1)
        self.myCanvas = Canvas(self.userFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.userFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")   

        # lblFrame = tb.LabelFrame(self.secondFrame, text="Ticket")

        orgLabel = Label(self.secondFrame, text = "User: " + self.controler.currentUser.userName, font=('Arial', 14), justify=LEFT)
        orgLabel.grid(row=0, sticky="nw", pady=15, padx=10)  

        tLabel = Label(self.secondFrame, text = "You have booked tickets for: ", font=('Arial', 13), justify=LEFT)
        tLabel.grid(row=1, sticky="nw", pady=(0, 10), padx=10)  

        # lf = ttk.LabelFrame(self.secondFrame, text='Ticket')
        # lf.grid(column=0, row=0, padx=20, pady=20)

        # lblFrame = ttk.LabelFrame(self.secondFrame, text="Ticket", style='primary.TLabelframe') #, style='info.TLabelframe'
        # lblFrame.grid(column=0, row=2, padx=20, pady=20)

        result = self.controler.getAllTicketsByUser()
        count = 2
        for i in range(0, len(result)):
            lf = tb.LabelFrame(self.secondFrame, text='Ticket', width=60, relief="groove", padding=10, style='primary.TLabelframe')
            lf.grid(column=0, row=count, padx=15, pady=10, sticky="w")
            titleLable = Label(lf, text="Event: " + result[i][1], font=('Arial', 12), justify=LEFT, width=40)
            titleLable.grid(row=count+1, sticky="w")
            seatsLable = Label(lf, text="Number of seats: " + str(result[i][2]), font=('Arial', 12), justify=LEFT, width=40)
            seatsLable.grid(row=count+2, sticky="w", pady=(5, 10))
            count = count + 5



    def bookTicket(self, title, org, boolSpaceLeft, sub, status):
        res = self.controler.bookTicket(title, sub)
        if res == False:
            errorLable = Label(self.secondFrame, text="You have to be logged in to book tickets")
            errorLable.grid(row=16, columnspan=2)    
        else:
            if boolSpaceLeft == False:
                errorLable = Label(self.secondFrame, text="There are no more tickets left")
                errorLable.grid(row=16, columnspan=2)
            elif status == "Past":
                errorLable = Label(self.secondFrame, text="You can't book a ticket, the event has already past")
                errorLable.grid(row=16, columnspan=2) 
            elif status == "Upcoming":
                errorLable = Label(self.secondFrame, text="The tickets haven't been released yet")
                errorLable.grid(row=16, columnspan=2)       
            else:
                self.passMoreInfoBtn(title, org)    
                self.confirmationWindow()

    def confirmationWindow(self):
        confWindow = Toplevel(self.moreInfoPage)
        confWindow.title("Confirmation")
        confWindow.geometry("250x150")
        text = Label(confWindow, text="You have booked \n your ticket!", font=('Arial',12))
        text2 = Label(confWindow, text="Have fun!", font=('Arial',12))
        text.pack(pady=(20, 0))
        text2.pack(pady=10)



    def logOut(self):
        self.controler.logOut()
        self.homePage()
        self.createMenu() 

    def createEvent(self):
        self.destroyFrames()
        self.createEventFrame = Frame(self.root)
        self.createEventFrame.pack()
        
        self.titleCreateEvent = Label(self.createEventFrame, text="Create Event", justify=CENTER, font=('Arial', 13))
        self.titleCreateEvent.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=(5, 10))

        self.entryTitleEventLable = Label(self.createEventFrame, text="Enter Title", justify=CENTER, font=('Arial', 10))
        self.entryTitleEventLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)
        self.entryTitleEvent = Entry(self.createEventFrame, bg="white")
        self.entryTitleEvent.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)

        self.entryDescriptionEventLable = Label(self.createEventFrame, text="Enter Description", justify=CENTER, font=('Arial', 10))
        self.entryDescriptionEventLable.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)
        self.entryDescriptionEvent = Text(self.createEventFrame, bg="white", height=6, width=25)
        self.entryDescriptionEvent.grid(row=2, column=1, sticky="nswe", pady=5, padx=5)

        self.entryLocationEventLable = Label(self.createEventFrame, text="Enter Location", justify=CENTER, font=('Arial', 10))
        self.entryLocationEventLable.grid(row=3, column=0, sticky="nswe", pady=5, padx=5)
        self.entryLocationEvent = Entry(self.createEventFrame, bg="white")
        self.entryLocationEvent.grid(row=3, column=1, sticky="nswe", pady=5, padx=5)

        self.entryDateEventLable = Label(self.createEventFrame, text="Enter Date", justify=CENTER, font=('Arial', 10))
        self.entryDateEventLable.grid(row=4, column=0, sticky="nswe", pady=5, padx=5)
        self.entryDateEvent = tb.DateEntry(self.createEventFrame, style='secondary.TCalendar')
        self.entryDateEvent.grid(row=4, column=1, sticky="nswe", pady=5, padx=5)

        self.entryCapacityEventLable = Label(self.createEventFrame, text="Enter Capacity", justify=CENTER, font=('Arial', 10))
        self.entryCapacityEventLable.grid(row=5, column=0, sticky="nswe", pady=5, padx=5)
        self.entryCapacityEvent = Entry(self.createEventFrame, bg="white")
        self.entryCapacityEvent.grid(row=5, column=1, sticky="nswe", pady=5, padx=5)

        self.entryMainCategoryEventLable = Label(self.createEventFrame, text="Choose Main Category", justify=CENTER, font=('Arial', 10))
        self.entryMainCategoryEventLable.grid(row=6, column=0, sticky="nswe", pady=5, padx=5)
        options = ["Concert", "Festivals", "Seminars", "Exhibitions", "Charity", "Sport", "Theater"]
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
        optionsStatus = ["Ongoing", "Upcoming"]
        clickedStatus = StringVar()
        clickedStatus.set("Ongoing")
        dropStatus = OptionMenu(self.createEventFrame, clickedStatus , *optionsStatus )
        dropStatus.grid(row=8, column=1, sticky="nswe", pady=5, padx=5)

        self.createEventBtn = Button(self.createEventFrame, width=20, text="Create Event", font=('Arial', 10), command=lambda :self.clickedCreateEventBtn(self.entryTitleEvent, self.entryDescriptionEvent, self.entryLocationEvent, self.entryDateEvent, self.entryCapacityEvent, clicked, self.entrySubCategories, clickedStatus))
        self.createEventBtn.grid(row=9, column=0, columnspan=2, pady=5)

    def clickedCreateEventBtn(self, entryTitleEvent, entryDescriptionEvent, entryLocationEvent, entryDateEvent, entryCapacityEvent, clicked, entrySubCategories, clickedStatus):
        title = entryTitleEvent.get()
        if title == "":
            title = "Unknown"
        description = entryDescriptionEvent.get("1.0",END)
        location = entryLocationEvent.get()
        if location == "":
            location = "Unknown"
        date = self.entryDateEvent.entry.get()
        capacity = entryCapacityEvent.get()
        if capacity == "":
            capacity = 0
        category = clicked.get()
        subCategories = entrySubCategories.get()
        status = clickedStatus.get()
        # print

        # self.controler.passRegistrationInfo(userName, email, password, radio)
        self.controler.passCreateEventInfo(title, description, location, date, capacity, category, subCategories, status)
        self.homePage()

    def recPage(self):
        self.destroyFrames()
        self.recFrame = Frame(self.root)
        self.recFrame.pack(fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.recFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.recFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")

        lableTitle = Label(self.secondFrame, text="Check out what we have for you, based on you previous bookings", font=('Arial', 14))
        lableTitle.grid(row=0, pady=(10, 10), padx=10)
        if self.controler.getTopGenres() == False:
            errorLable = Label(self.secondFrame, justify=LEFT, text="Make your first booking, so that we can give you a recommendation", font=('Arial', 12))
            errorLable.grid(row=1, sticky="nw", pady=10, padx=15)
        else: 
            result = self.controler.getTopGenres()
            self.printEvent(self.secondFrame, result)
    
    def searchPage(self):
        self.destroyFrames()
        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.searchFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.searchFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")

        lableTitle = Label(self.secondFrame, text="Search by keyword", font=('Arial', 13), justify=LEFT)
        lableTitle.grid(row=0, pady=(10, 10), sticky="w", padx=20)

        self.keywordLable = Label(self.secondFrame, text="Enter Keyword", justify=CENTER, font=('Arial', 10))
        self.keywordLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=25)
        self.entryKeyword = Entry(self.secondFrame, bg="white")
        self.entryKeyword.grid(row=1, column=1, sticky="nswe", pady=5, padx=25)

        self.intervalDateLable = Label(self.secondFrame, text="Search by time Interval", font=('Arial', 13), justify=LEFT)
        self.intervalDateLable.grid(row=2, columnspan=4, pady=(10, 10), sticky="w", padx=20)

        self.startDateLabel = Label(self.secondFrame, text="Start date", justify=CENTER, font=('Arial', 10))
        self.startDateLabel.grid(row=3, column=0, sticky="nswe", pady=5, padx=25)
        
        self.startDateEntry = tb.DateEntry(self.secondFrame, style='secondary.TCalendar')
        self.startDateEntry.grid(row=3, column=1, sticky="nswe", pady=5, padx=25)
        # print(self.startDateEntry.get())
        self.endDateLabel = Label(self.secondFrame, text="End date", justify=CENTER, font=('Arial', 10))
        self.endDateLabel.grid(row=4, column=0, sticky="nswe", pady=5, padx=25)
        self.endDateEntry = tb.DateEntry(self.secondFrame, style='secondary.TCalendar')
        self.endDateEntry.grid(row=4, column=1, sticky="nswe", pady=5, padx=25)

        self.SearchBtn = Button(self.secondFrame, width=40, text="Search", font=('Arial', 10), command=lambda :self.clickedSearchBtn(self.entryKeyword, self.secondFrame, self.startDateEntry.entry.get(), self.endDateEntry.entry.get()))
        self.SearchBtn.grid(row=5, column=0, columnspan=2, sticky="nswe",pady=10, ipadx=20, padx=20)

        
    def clickedSearchBtn(self, entryKeyword, frame, startDateEntry, endDateEntry):
        print(startDateEntry)
        result = []
        if entryKeyword.get() != '':
            result = self.controler.searchByKeyword(entryKeyword.get())
        elif startDateEntry != '' and endDateEntry != '':
            result = self.controler.searchByInterval(startDateEntry, endDateEntry) 
        elif entryKeyword.get() != '' and startDateEntry != '' and endDateEntry != '':
            keywordSearch = self.controler.searchByKeyword(entryKeyword.get())     
            dateSearch = self.controler.searchByInterval(startDateEntry, endDateEntry) 

            for event in keywordSearch: 
                if event in dateSearch:
                    result.append(event)   


        self.destroyFrames()
        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(fill=BOTH, expand=1)

        self.myCanvas = Canvas(self.searchFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.myScrollbar = ttk.Scrollbar(self.searchFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.configure(yscrollcommand=self.myScrollbar)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        self.secondFrame = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0), window=self.secondFrame, anchor="nw")

        lableTitle = Label(self.secondFrame, text="Search by keyword", font=('Arial', 13), justify=LEFT)
        lableTitle.grid(row=0, pady=(10, 10), sticky="w", padx=20)

        self.keywordLable = Label(self.secondFrame, text="Enter Keyword", justify=CENTER, font=('Arial', 10))
        self.keywordLable.grid(row=1, column=0, sticky="nswe", pady=5, padx=25)
        self.entryKeyword = Entry(self.secondFrame, bg="white")
        self.entryKeyword.grid(row=1, column=1, sticky="nswe", pady=5, padx=25)

        self.intervalDateLable = Label(self.secondFrame, text="Search by time Interval", font=('Arial', 13), justify=LEFT)
        self.intervalDateLable.grid(row=2, columnspan=4, pady=(10, 10), sticky="w", padx=20)

        self.startDateLabel = Label(self.secondFrame, text="Start date", justify=CENTER, font=('Arial', 10))
        self.startDateLabel.grid(row=3, column=0, sticky="nswe", pady=5, padx=25)
        self.startDateEntry = tb.DateEntry(self.secondFrame, style='secondary.TCalendar')
        self.startDateEntry.grid(row=3, column=1, sticky="nswe", pady=5, padx=25)
        # print(self.startDateEntry.get())
        self.endDateLabel = Label(self.secondFrame, text="End date", justify=CENTER, font=('Arial', 10))
        self.endDateLabel.grid(row=4, column=0, sticky="nswe", pady=5, padx=25)
        self.endDateEntry = tb.DateEntry(self.secondFrame, style='secondary.TCalendar')
        self.endDateEntry.grid(row=4, column=1, sticky="nswe", pady=5, padx=25)

        self.SearchBtn = Button(self.secondFrame, width=40, text="Search", font=('Arial', 10), command=lambda :self.clickedSearchBtn(self.entryKeyword, self.secondFrame, self.startDateEntry.entry.get(), self.endDateEntry.entry.get()))
        self.SearchBtn.grid(row=5, column=0, columnspan=2, sticky="nswe",pady=10, ipadx=20, padx=20)

        if len(result) == 0:
            errorLable = Label(self.secondFrame, text="There are no search results found")
            errorLable.grid(row=6, columnspan=2)

        self.printEvent(self.secondFrame, result)
        


        
    
    def destroyFrames(self):
        self.logInFrame.destroy()
        self.registrtionFrame.destroy()
        self.homeFrame.destroy()
        self.createEventFrame.destroy()
        self.moreInfoPage.destroy()
        self.secondFrame.destroy()
        self.mostPopularFrame.destroy()
        self.recFrame.destroy()
        self.editEventFrame.destroy()
        self.orgFrame.destroy()
        self.userFrame.destroy()
        self.searchFrame.destroy()
        # self.statFrame.destroy()
        
          
        





