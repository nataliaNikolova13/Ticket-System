from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image, ImageTk, ImageFilter, ImageEnhance 
import os
from tkinter import filedialog
from event import Event, Status, Category
from users import User, NormalUser, Organizer, Role
from pageLayout import Layout

root = Tk()
ticketSystem = Layout(root)
root.mainloop()