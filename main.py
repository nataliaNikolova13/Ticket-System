from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image, ImageTk, ImageFilter, ImageEnhance 
import os
from tkinter import filedialog
from event import Event, Status, Category
from users import User, NormalUser, Organizer, Role
from pageLayout import Layout
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = Tk()
ticketSystem = Layout(root)
style = tb.Style("flatly")
# style = tb.Style("litera")
root.mainloop()