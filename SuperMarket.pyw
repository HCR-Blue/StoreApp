import sqlite3
from tkinter import *
import tkinter.ttk as ttk
# from tkinter.ttk import Progressbar
import random
import tkinter.messagebox as messagebox
# from PIL import ImageTk, Image
from tkinter.ttk import Notebook, Style
from time import sleep
import datetime
import os
import customtkinter as ctk

# from tabulate import tabulate #  This library is for Printing Documents with lines table creations
# from prettytable import PrettyTable
# import prettytable
from tkinter import filedialog
# from PIL import Image
from persiantools.jdatetime import JalaliDate
import persiantools
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageGrab, ImageFilter, ImageTk
import requests
# from cmbox import CMInfo
# # msg = CMInfo("This is my title", "This is the text of me and\n i am custom messagebox.")


try:
    path = os.mkdir("C://My_Store")
except:
    ""

#======== Create Dir for config file through db file ========
# try:
#     path = os.mkdir("SysConfig")
# except:
#     ""

# with sqlite3.connect("SysConfig/db_config.db") as db:
#     cur = db.cursor()
#     # =---------- App Configuration --------------
#     cur.execute(
#         """
#         CREATE TABLE IF NOT EXISTS ConfigTable(
#         APPID INTEGER PRIMARY KEY AUTOINCREMENT,
#         APPTITLE TEXT NOT NULL,
#         APPNAME TEXT NOT NULL,
#         APPUSER TEXT NOT NULL,
#         APPPASSWORD TEXT NOT NULL,
#         APPTHEME TEXT NOT NULL,
#         APPLANG TEXT NOT NULL,
#         APPTIME DATE NOT NULL);
#         """
#     )






DEFAULTHCRBG = "#4B4B4B"  # 72959F
CTKLIGHT = "#EBEBEB"
CTKDARK = "#242424"
TKDARK = "#4B4B4B"
mygreen = "#d2ffd2"
myred = "#dd0505"
mylightblue = "light blue"
DEFAULTHCRBG = "#4B4B4B"  # 72959F
BGCOL1 = "#003A45"
BGCOL2 = "#2f2f2f"
FGCOL1 = "#FFFFFF"
FGCOL2 = "#6f7f3f"
FGCOL3 = "#ffffff"
FGCOL4 = "dark red"
BGCOL4 = "white"
BGGRAY = "#6f8f9f"
BGLIGHTBLUE = "light blue"
BGBLUE = "blue"
BGBLACK = "black"
BGYELLOW = "yellow"
BGGREEN = "green"
BGRED = "red"
BGLIGHTYELLOW = "light yellow"
BGDEFAULT = "DFDFDF"
BGORANGE = "orange"
BGLIGHTGREEN = "light green"
BGWHITE = "white"
BGLIGHTGRAY = "light gray"
BGDARKSKY = "#0F1F3F"
MODERNBACK = "#420052"
MODERNFORGROUND = "#8F49A6"
MODERNBACKBLUE = "#5D96A1"
MODERNFORGROUNDBLUE = "#454D9C"
MODERNLIGHTBLUE = "#5D96A1"
MODERNPINK = "#410070"
CTKDARK_ENT = "#2B2B2B"
DarkBlue = "#39003D"
MikroTik = "#7A949A"
DARKENTRY = "#343638"
GRAY_NEW = "#ADADAD"
S4DARK = "#1F1F1F"
S4LIGHT = "#2B2B2B"
S4TEAL = "#0099ff"
S4ORANGE = "#FFC800"
S4BLUE = "#226699"
TEXT_COL_1 = S4BLUE
BTN_HOVER = "light green"#"#FFA500"
BTN_VENDOR = "#A9A900"
CTKDARK_FRM = "#333333"

Override = [1]
root = ctk.CTk()
root.title("Space4 (Management System)")
root.iconbitmap("Space4.ico")
root.attributes("-fullscreen", True)
# root.state("zoomed")
# root.wm_attributes("-topmost", True)
# root.call('tk', 'scaling', -1)
# root.overrideredirect(Override)
# root.wm_state("iconic")
# root.configure(borderwidth=5)
root.call("set", "encoding", "utf-8")
# root.wm_attributes('-transparentcolor', 'black')
# root.wm_attributes('-transparentcolor', root['bg']) # choose for transparent on any widget
default_font_bold1 = ("Tahoma", 10, "bold")
default_font_bold = ("Tahoma", 12, "bold")
default_font = ("Tahoma", 12, "normal")
default_font_bold2 = ("Tahoma", 8, "bold")
ctk.set_appearance_mode("Dark")


# def force_resize(root):
#     for widget in root.winfo_children():
#         if isinstance(widget, ctk.CTkFrame) or isinstance(widget, ctk.CTkLabel):
#             widget.grid_propagate(False)
#         if isinstance(widget, ctk.CTkToplevel):
#             force_resize(widget)



# def ConfigSubmitFunc():
#     DateNow = datetime.date.today()
#     conn = sqlite3.connect("SysConfig/db_config.db")
#     # cur = conn.cursor()
#     # cur.execute(
#     #     f"""
#     #     insert into ConfigTable(
#     #     APPTITLE,
#     #     APPNAME,
#     #     APPUSER,
#     #     APPPASSWORD,
#     #     APPTHEME,
#     #     APPLANG,
#     #     APPTIME
#     #     )
#     #     values(
#     #     'Space4 software engineering team',
#     #     'Fardin Supermarket',
#     #     'Ahmad',
#     #     '1312',
#     #     'Dark',
#     #     'Dari',
#     #     '{DateNow}'
#     #     )
#     #     """
#     # )
#     # conn.commit()
#     # conn.close()

#     cur = conn.execute(
#         """
#         SELECT *
#         FROM ConfigTable
#         """
#     )
#     fetch = cur.fetchall()
#     for data in fetch:
#         AppTitle = data[0]
#         AppName = data[1]
#         root.title(AppT)
#     cur.close()
#     conn.close()

# ConfigSubmitFunc()

# from ttkthemes import ThemedStyle
# style5 = ThemedStyle(root)
# style5.set_theme("plastik")

# entry = ttk.Entry(root, style="Shadow.TEntry")
# entry.grid()




DateNow = datetime.date.today()



#===================== Images ===================
# ========== Images ===========

Img00 = Image.open("PsysDataDir/StoreImg1.png")
Img0_0 = Img00.resize((50, 50))
StoreImg1 = ImageTk.PhotoImage(Img0_0)

Img0_1 = Image.open("PsysDataDir/GraphImg1.png")
Img0_2 = Img0_1.resize((50, 50))
GraphImg1 = ImageTk.PhotoImage(Img0_2)

Img0_3 = Image.open("PsysDataDir/DebtsImg.png")
Img0_4 = Img0_3.resize((50, 50))
DebtsImg = ImageTk.PhotoImage(Img0_4)

Img0_5 = Image.open("PsysDataDir/ExpenseImg.png")
Img0_5 = Img0_5.resize((50, 50))
ExpenseImg = ImageTk.PhotoImage(Img0_5)




Img1_0 = Image.open("PsysDataDir/SellImg.png")
Img1_1 = Img1_0.resize((20, 20))
SellImg_1 = ImageTk.PhotoImage(Img1_1)

Img1_2 = Image.open("PsysDataDir/EditImg.png")
Img1_3 = Img1_2.resize((20, 20))
EditImg_1 = ImageTk.PhotoImage(Img1_3)

Img1_4 = Image.open("PsysDataDir/DeleteImg.png")
Img1_5 = Img1_4.resize((20, 20))
DeleteImg_1 = ImageTk.PhotoImage(Img1_5)

Img1_6 = Image.open("PsysDataDir/RefreshImg.png")
Img1_7 = Img1_6.resize((20, 20))
RefreshImg_1 = ImageTk.PhotoImage(Img1_7)

Img1_8 = Image.open("PsysDataDir/UpdateImg.png")
Img1_9 = Img1_8.resize((20, 20))
UpdateImg_1 = ImageTk.PhotoImage(Img1_9)

Img1_10 = Image.open("PsysDataDir/ShowImg.png")
Img1_11 = Img1_10.resize((20, 20))
ShowImg_1 = ImageTk.PhotoImage(Img1_11)

Img1_12 = Image.open("PsysDataDir/ReceiveImg.png")
Img1_13 = Img1_12.resize((20, 20))
PriceImg1 = ImageTk.PhotoImage(Img1_13)

Img1_14 = Image.open("PsysDataDir/graphImg.png")
Img1_15 = Img1_14.resize((150, 150))
GraphImg = ImageTk.PhotoImage(Img1_15)

Img1_16 = Image.open("PsysDataDir/Space4Img.png")
Img1_17 = Img1_16.resize((90, 90))
Space4Img1 = ImageTk.PhotoImage(Img1_17)

Img1_18 = Image.open("PsysDataDir/MotivLogoImg.png")
Img1_19 = Img1_18.resize((85, 50))
MotiveLogoImg = ImageTk.PhotoImage(Img1_19)

"""
TabImg5 = Image.open('PsysDataDir/Space4Img.png')
TabImg1_5 = TabImg5.resize((50,50),Image.ANTIALIAS)
Space4TitleLogo = ImageTk.PhotoImage(TabImg1_5)
"""


Space4TitleLogo = ctk.CTkImage(dark_image=Image.open("PsysDataDir/Space4Img.png"))
SaveImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/SaveImg.png"))
EditImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/EditImg.png"))
DeleteImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/DeleteImg.png"))
ClearImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/ClearImg.png"))
RefreshImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/RefreshImg.png"))
PrintImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/PrintImg.png"))
ReceiveImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/ReceiveImg.png"))
RefundImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/RefundImg.png"))
UpdateImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/UpdateImg.png"))
VendorImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/VendorImg.png"))
MinimizeImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/MinimizeImg.png"))
ExitImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/ExitImg.png"))
DepositImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/DepositImg.png"))
WithdrawImg = ctk.CTkImage(dark_image=Image.open("PsysDataDir/WithdrawImg.png"))


#---------------------------------------------------------
#========== Date, Time, Exit Button ==========
root_header = ctk.CTkFrame(root, fg_color=MODERNPINK)
root_header.place(x=0, y=0)

def Quit_1():
    AskYsNoMsg = messagebox.askyesno("Space4","مطمعن هستی که میخوای خارج شوی")
    if AskYsNoMsg > 0:
        root.destroy()


# current_date = JalaliDate.today()
# formatted_date = current_date.strftime('%Y-%m-%d')
from time import strftime
formatted_date = strftime("%Y-%m-%d - %a")
DateLabel_1 = ctk.CTkLabel(
    root_header,
    text=formatted_date,
    font=("Nexa Light",15),
    text_color=BGWHITE)
DateLabel_1.grid(row=0,column=0, padx=20, pady=2)

#------ Time -------
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.configure(text=current_time)
    time_label.after(1000, update_time)

time_label = ctk.CTkLabel(root_header, font=("Nexa Light",15),text_color=BGWHITE)
time_label.grid(row=0,column=1, padx=20, pady=2)
update_time()

#------ Enabel Tabs ----
def EnableTabs():
    Eroot = ctk.CTkToplevel(root)
    Eroot.title("دسترسی به مدیریت")
    Eroot.iconbitmap('Space41.ico')
    Eroot.resizable(0, 0)
    Eroot.grab_set()
    Eroot.geometry("220x250+500+200")

    password1 = "1312"
    admin = "Admin"

    #--------- Creating BankTable with secret word -------------
    def EnableFunc(*args):
        if EnableEntry.get() == password1:
            tabControl.add(tab1, state=NORMAL)
            tabControl.add(tab2, state=NORMAL)
            tabControl.add(tab3, state=NORMAL)
            safeMoodRoot0()
            Eroot.destroy()
            messagebox.showinfo("Space4", "کلمه عبور درست \n\
                همه گزینه ها فعال شد")
            tabControl.select(tab1)

        elif EnableEntry.get() == admin:
            ConnHide = sqlite3.connect("C:/My_Store/StoreDb.db")
            BnkCur = ConnHide.cursor()
            BnkCur.execute(
                f"""
                insert into BankTable (
                BALANCE,
                BNKDATE
                )
                values(
                0,
                '{DateNow}'
                )
                """
            )
            ConnHide.commit()
            ConnHide.close()
            messagebox.showinfo("Administrator", "Banking is enabled...")
        elif EnableEntry.get() == "":
            messagebox.showerror("Space4", "ورودی نمیتواند خالی باشد")
        else:
            messagebox.showerror("Space4", "کلمه عبور اشتباه است")
    def safeMoodRoot0():
        def RemoveSafeLbls1():
            SafeMoodLbl0.destroy()
        SafeMoodLbl0 = ctk.CTkLabel(
            master=root,
            text="Safe mood is\nDisabled by admin.",
            font=("Nexa Heavy",50,"bold"),
            text_color="#11FF00",
            justify=CENTER,
        )
        SafeMoodLbl0.place(x=380,y=200)
        root.after(5000, RemoveSafeLbls1)

    def safeMoodRoot():
        def RemoveSafeLbls():
            SafeMoodLbl1.destroy()
            SafeMoodLbl2.destroy()
            SafeMoodLbl3.destroy()
        SafeMoodLbl1 = ctk.CTkLabel(
            master=root,
            text="Safe mood is\nEnabled by admin.",
            font=("Nexa Heavy",50,"bold"),
            text_color=BGRED,
            justify=CENTER,
        )
        SafeMoodLbl1.place(x=380,y=200)
        SafeMoodLbl2 = ctk.CTkLabel(
            master=root,
            text="دسترسی به اطلاعات موقتاً مسدود شد",
            font=("Tahoma",20,"bold"),
            text_color=BGLIGHTBLUE,
        )
        SafeMoodLbl2.place(x=440,y=320)
        SafeMoodLbl3 = ctk.CTkLabel(
            master=root,
            text="Secured by: Space4 software engineering team.",
            font=("Gilroy Light",15),
            text_color=BGYELLOW,
        )
        SafeMoodLbl3.place(x=460,y=380)
        root.after(5000, RemoveSafeLbls)

    def DisableFunc():
        safeMoodRoot()
        tabControl.add(tab1, state=DISABLED)
        tabControl.add(tab2, state=DISABLED)
        tabControl.add(tab3, state=DISABLED)
        Eroot.destroy()
        messagebox.showinfo("Space4", "حالت امن فعال شد")
        tabControl.select(tab4)
    # ---------- Widgets -------------
    EnableTabLogoLbl = Label(
        master=Eroot,
        image=Space4Img1,
        bg="#333333",
        bd=0
        )
    EnableTabLogoLbl.pack(fill=BOTH, expand=True)
    EnableTabFrm = ctk.CTkFrame(
        Eroot,
        corner_radius=5,
        fg_color=CTKDARK_FRM
        )
    EnableTabFrm.pack(fill=BOTH, expand=True)
    EnableTabFrm1 = ctk.CTkFrame(
        Eroot,
        corner_radius=5,
        fg_color=CTKDARK_FRM
        )
    EnableTabFrm1.pack(fill=BOTH, expand=True)
    EnableTabFrm2 = ctk.CTkFrame(
        Eroot,
        corner_radius=5,
        fg_color=CTKDARK_FRM
        )
    EnableTabFrm2.pack(fill=BOTH, expand=True)
    #--------------------------------------

    EnableTtlLbl = ctk.CTkLabel(
        EnableTabFrm,
        text="چک پاینت شناسایی هویت کاربر",
        justify=RIGHT,
        font=default_font_bold
    )
    EnableTtlLbl.pack(padx=10,pady=10)
    EnableEntry = ctk.CTkEntry(
        master=EnableTabFrm1,
        placeholder_text="کلمه عبور خود را وارد کنید",
        justify=LEFT,
        font=default_font_bold,
        width=170,
        show="*"
    )
    EnableEntry.pack(padx=10,pady=10)
    EnableEntry.bind("<Return>", EnableFunc)
    EnableBtn = ctk.CTkButton(
        master=EnableTabFrm2,
        text="حالت کار",
        font=default_font_bold,
        width=70,
        fg_color=TEXT_COL_1,
        command=EnableFunc
    )
    EnableBtn.grid(row=0,column=1,padx=10,pady=10)
    DisableBtn = ctk.CTkButton(
        master=EnableTabFrm2,
        text="حالت امن",
        font=default_font_bold,
        width=70,
        fg_color=TEXT_COL_1,
        command=DisableFunc
    )
    DisableBtn.grid(row=0,column=0,padx=23,pady=10)

    Eroot.mainloop()

def MinimizeFunc():
    root.iconify()

#----- Exit ------
ExitBtn1 = ctk.CTkButton(
    root_header,
    command=Quit_1,
    width=70,
    compound=RIGHT,
    text="خروج",
    image=ExitImg,
    font=default_font_bold,
    hover_color=BGLIGHTGREEN,
    fg_color=MODERNPINK,
    text_color=BGRED
    )
ExitBtn1.grid(row=0,column=5, padx=5, pady=2)

MinimizeButton1 = ctk.CTkButton(
    root_header,
    command=MinimizeFunc,
    width=70,
    compound=RIGHT,
    image=MinimizeImg,
    text="راندن",
    font=default_font_bold,
    hover_color=BGLIGHTGREEN,
    fg_color=MODERNPINK,
    text_color=S4TEAL
    )
MinimizeButton1.grid(row=0,column=4, padx=5, pady=2)

EnableTabButton1 = ctk.CTkButton(
    root_header,
    command=EnableTabs,
    width=70,
    compound=RIGHT,
    image=VendorImg,
    text="ادمین",
    font=default_font_bold,
    hover_color=BGLIGHTGREEN,
    fg_color=MODERNPINK,
    text_color=S4TEAL
    )
EnableTabButton1.grid(row=0,column=3, padx=5, pady=2)
#=--------------------
TitleApp1 = ctk.CTkLabel(
    root_header,
    compound=RIGHT,
    text="         Fardin Supermarket",
    font=("Arial Black", 15),
    text_color=BGLIGHTYELLOW
    )
TitleApp1.grid(row=0,column=2, padx=250, pady=2)

Ads_label = ctk.CTkLabel(root_header, text="Space4 Software engineering team.", fg_color=MODERNPINK)
Ads_label.place(x=270, y=0)
#------------ Happy New year message -------------

NewYearDate = strftime("%m-%d")
current_date = JalaliDate.today()
NewYear = current_date.strftime('%Y')
if NewYearDate == "02-19":
    Ads_label.configure(
        text=f" {NewYear}    سال نو مبارک",
        font=("B Titr", 17),
        text_color="#11FF00"
    )
elif NewYearDate == "02-20":
    Ads_label.configure(
        text=f" {NewYear}    انیش سال نو را برایت تبریک میگوید",
        font=("B Titr", 17),
        text_color="#11FF00"
    )
elif NewYearDate == "02-21":
    Ads_label.configure(
        text=f" {NewYear}    سال نو مبارک جناب فردین",
        font=("B Titr", 17),
        text_color="#11FF00"
    )
elif NewYearDate == "02-22":
    Ads_label.configure(
        text=f" {NewYear}    سال نو مبارک جناب فردین",
        font=("B Titr", 17),
        text_color="#11FF00"
    )

#============== Motivational quotes json file read ==============
import random
import json


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        messagebox.showerror(file_path)


def display_random_quote():
    random_quote = random.choice(data)['text']
    quoteLbl1.configure(text=random_quote)


file_path = "jsonfile/quotes.json"
data = read_json_file(file_path)


# def move_text(): # Animation
#     x = quoteLbl1.winfo_x()
#     if x < root.winfo_width():
#         quoteLbl1.place(x=x+1)
#         quoteLbl1.after(10, move_text)

quoteLbl1 = ctk.CTkLabel(
    master=root,
    text="Space4 Software engineering team.",
    font=("B Nazanin", 14, "bold"),
    text_color=BGLIGHTYELLOW
)
quoteLbl1.place(x=200, y=700)
display_random_quote()
# move_text()
quoteLogo1 = Label(
    master=root,
    image=MotiveLogoImg,
    text="",
    bg=S4DARK
)
quoteLogo1.place(x=50, y=700)
# ========================= Style ==========================


style = Style(root)
style.theme_use(
    "default"
)  # >>>>>>> TNotebook.Tab anchor is for placing the tab title and image
style.configure(
    "TNotebook.Tab",
    background=S4DARK,
    anchor="nsew",
    borderwidth=0,
    foreground="#ffffff",
    width=11,
    padding=[10, 10],
    tabmargins=[0, 0, 0, 0],
    font=default_font_bold1,
    bd=0,
)
style.configure("TNotebook", background=CTKDARK, borderwidth=0, padding=[10, 10])
style.map(
    "TNotebook.Tab",
    background=[("selected", S4LIGHT)],
    foreground=[("selected", S4TEAL)],
)
style.layout("cb.TNotebook.Tab", [("TNotebook.Tab", {"side": "right", "sticky": "ne"})])
style.configure("TCombobox", font=default_font_bold)
style.configure("righttab.TNotebook", tabposition="en", sticky="ne")
# style.configure(
#     "Custom.DateEntry",
#     fieldbackground=S4DARK,
#     foreground=CTKLIGHT,
#     borderwidth=0,
#     relief=SOLID,
# )
# TreeView Part
style.configure(
    "Treeview.Heading",
    background=CTKDARK,
    borderwidth=0,
    anchor=E,
    foreground=BGLIGHTBLUE,
    padding=[3, 4],
    tabmargins=[2, 5, 2, 0],
    font=default_font_bold2,
)
style.configure(
    "Treeview",
    background="#333333",
    anchor=E,
    foreground="#ffffff",
    font=default_font_bold2,
    rowheight=27,
    fieldbackground="#33333",
)
style.map(
    "Treeview",
    background=[("selected", TEXT_COL_1)],
    foreground=[("selected", "#000000")],
)
style.layout(
    "cb.Treeview.Row",
    [
        ("Treeitme.row", {"sticky": "e"}),
        ("Treeitme.image", {"side": "right", "sticky": "e"}),
    ],
)

#=========================
tabControl = ttk.Notebook(root, style="righttab.TNotebook")
tab1 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab2 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab3 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)
tab4 = ctk.CTkFrame(tabControl, border_width=0, corner_radius=7)

tabControl.add(tab1, text="خرید و فروش", image=StoreImg1, compound=TOP, sticky=NE, state=DISABLED)
tabControl.add(tab2, text="تفصیلات", image=ExpenseImg, compound=TOP, sticky=NE, state=DISABLED)
tabControl.add(tab3, text="باقیات", image=DebtsImg, compound=TOP, sticky=NE, state=DISABLED)
tabControl.add(tab4, text="عملکردها", image=GraphImg1, compound=TOP, sticky=NE)

tabControl.select(tab1)
tabControl.grid(row=0, column=1, padx=30, pady=50, sticky=E)

# ============== Mini Tab2_1 =========================
tabControlMini = ttk.Notebook(tab1, style="RTL.TNotebook")
tab1_1 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)
tab1_2 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)
tab1_3 = ctk.CTkFrame(tabControlMini, border_width=0, corner_radius=0)

tabControlMini.add(tab1_3, text="اصلاح ریکارد", compound=TOP, sticky=NE)
tabControlMini.add(tab1_2, text="لیست باقیات از دوکان", compound=TOP, sticky=NE)
tabControlMini.add(tab1_1, text="خرید و فروش", compound=TOP, sticky=NE)
tabControlMini.select(tab1_1)
tabControlMini.pack(side="right")

style1 = Style(tabControlMini)
style1.configure("RTL.TNotebook", tabposition="ne")





#------------ Table creatings =======================
with sqlite3.connect("C:/My_Store/StoreDb.db") as db:
    cur = db.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS StorageTable(
        SRID INTEGER PRIMARY KEY AUTOINCREMENT,
        SRMODEL TEXT NOT NULL,
        SRTYPE TEXT NOT NULL,
        SRGROUP TEXT NOT NULL,
        SRPRICE REAL NOT NULL,
        SRQTT INTEGER NOT NULL,
        SRDATE DATE,
        SRNOTE TEXT NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS StorageSoldTable(
        SOLDID INTEGER PRIMARY KEY AUTOINCREMENT,
        SOLDMODEL TEXT NOT NULL,
        SOLDTYPE TEXT NOT NULL,
        SOLDGROUP TEXT NOT NULL,
        SOLDPRICE REAL NOT NULL,
        SOLDQTT INTEGER NOT NULL,
        SOLDDATE DATE,
        SOLDNOTE TEXT NOT NULL,
        SOLDREALPRICE REAL NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS FCostTable(
        FTID INTEGER PRIMARY KEY AUTOINCREMENT,
        FTYPE REAL NOT NULL,
        FCOSTTYPE REAL NOT NULL,
        FAMOUNT REAL NOT NULL,
        FDATE DATE,
        FNOTE TEXT NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LenderTable(
        LDRID INTEGER PRIMARY KEY AUTOINCREMENT,
        LDRLENDER TEXT NOT NULL,
        LDRBEHALF TEXT NOT NULL,
        LDRAMOUNT REAL NOT NULL,
        LDRDATE DATE,
        LDRNOTE TEXT NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS DebtorTable(
        DBTID INTEGER PRIMARY KEY AUTOINCREMENT,
        DBTDEBTOR TEXT NOT NULL,
        DBTBEHALF TEXT NOT NULL,
        DBTAMOUNT REAL NOT NULL,
        DBDATE DATE,
        DBTNOTE TEXT NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS SellingDebtTable(
        SLID INTEGER PRIMARY KEY AUTOINCREMENT,
        SLNAME TEXT NOT NULL,
        SLFNAME TEXT NOT NULL,
        SLADDR TEXT NOT NULL,
        SLMTYPE TEXT NOT NULL,
        SLQTTY INTEGER NOT NULL,
        SLPRICE REAL NOT NULL,
        SLDAMOUNT REAL NOT NULL,
        SLDATE DATE,
        SLNOTE TEXT NOT NULL);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS CashTable(
        CSHID INTEGER PRIMARY KEY AUTOINCREMENT,
        CSHAMOUNT REAL NOT NULL,
        CSHREALPRICE REAL NOT NULL,
        CSHQTTY INTEGER NOT NULL,
        CSHDATE DATE);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS HalfPayTable(
        HFID INTEGER PRIMARY KEY AUTOINCREMENT,
        HFAMOUNT REAL NOT NULL,
        HFDATE DATE);
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS BankTable(
            BNKID INTEGER PRIMARY KEY AUTOINCREMENT,
            BALANCE REAL NOT NULL,
            BNKDATE DATE);
        """
    )

# ========================= tab1 Store ==========================
# ========================= tab1 Store ==========================
# ========================= tab1 Store ==========================
# ========================= tab1 Store ==========================
# ========================= tab1 Store ==========================
# ========================= tab1 Store ==========================
# ========================= tab1 Store ==========================



#========================= Tab1_1 ============================
#========================= Tab1_1 ============================
#========================= Tab1_1 ============================
#========================= Tab1_1 ============================
SRMODEL = StringVar()
SRTYPE = StringVar()
SRGROUP = StringVar()
SRPRICE = StringVar()
SRQTT = StringVar()
SRDATE = StringVar()
SRNOTE = StringVar()
SEARCHVAR0 = StringVar()
SEARCHVAR1 = StringVar()


def SRSubmit():
    SRConn1 = sqlite3.connect("C:/My_Store/StoreDb.db")
    SRCur1 = SRConn1.cursor()
    if strEnty2.get() == "":
        messagebox.showwarning(
            "ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود."
        )
    else:
        if SRPRICE.get() == "" or SRQTT.get() == "":
            SRCur1.execute(
                f"""
                insert into StorageTable(
                SRMODEL,
                SRTYPE,
                SRGROUP,
                SRPRICE,
                SRQTT,
                SRDATE,
                SRNOTE
                )
                values(
                '{SRMODEL.get()}',
                '{SRTYPE.get()}',
                '{SRGROUP.get()}',
                0,
                0,
                '{SRDATE.get()}',
                '{SRNOTE.get()}'
                )
                """
            )

        else:
            SRCur1.execute(
                f"""
                insert into StorageTable(
                SRMODEL,
                SRTYPE,
                SRGROUP,
                SRPRICE,
                SRQTT,
                SRDATE,
                SRNOTE
                )
                values(
                '{SRMODEL.get()}',
                '{SRTYPE.get()}',
                '{SRGROUP.get()}',
                '{SRPRICE.get()}',
                '{SRQTT.get()}',
                '{SRDATE.get()}',
                '{SRNOTE.get()}'
                )
                """
            )

    SRConn1.commit()
    SRConn1.close()
    strEnty2.delete(0, END)
    strEnty3.delete(0, END)
    strEnty4.delete(0, END)
    strEnty5.delete(0, END)
    strEnty7.delete(0, END)
    strEnty1.focus()
    SRRef()


def SRRef():
    # AutoUpdateBankFunc()
    ReRef()
    TreeStg.delete(*TreeStg.get_children())
    TreeStgConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeStgCor = TreeStgConn.execute(
        """
        SELECT
        SRNOTE,
        SRDATE,
        SRQTT,
        SRPRICE,
        SRGROUP,
        SRTYPE,
        SRMODEL,
        SRID
        FROM StorageTable
        ORDER BY SRID DESC
        """
    )
    fetchTreeStg = TreeStgCor.fetchall()
    for indexSR in fetchTreeStg:
        TreeStg.insert("", "end", values=indexSR)
    TreeStgCor.close()
    TreeStgConn.close()

    # Sooooold ----------------------------------------
    TreeStgSold.delete(*TreeStgSold.get_children())
    TreeStgSoldConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeStgSoldCor = TreeStgSoldConn.execute(
        """
        SELECT
        SOLDNOTE,
        SOLDDATE,
        SOLDQTT,
        SOLDPRICE,
        SOLDGROUP,
        SOLDTYPE,
        SOLDMODEL,
        SOLDID
        FROM StorageSoldTable
        ORDER BY SOLDID DESC
        """
    )
    fetchTreeStgSold = TreeStgSoldCor.fetchall()
    for indexSRSold in fetchTreeStgSold:
        TreeStgSold.insert("", "end", values=indexSRSold)
    TreeStgSoldCor.close()
    TreeStgSoldConn.close()


    #----------------------------------------
    TreeStgSum.delete(*TreeStgSum.get_children())
    TreeStgSumConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    queryStgSum1 = """
    SELECT
    SUM(SRPRICE * SRQTT) AS SMG0
    FROM StorageTable
    """
    TreeStgSumCor = TreeStgSumConn.execute(queryStgSum1)
    fetchTreeStgSum = TreeStgSumCor.fetchall()
    for dataTreeStgSum in fetchTreeStgSum:
        SMG0 = dataTreeStgSum[0]
        try:
            SMGS = SMG0
            TreeStgSum.insert("", "end", values=(SMGS))
        except:
            SMGS = "هیچ"
            TreeStgSum.insert("", "end", values=(SMGS))
    TreeStgSumCor.close()
    TreeStgSumConn.close()


    #----------------- balance -------------------
    TreeStgSum2.delete(*TreeStgSum2.get_children())
    TreeStgSum2Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    queryStgSum2 = """SELECT BALANCE FROM BankTable WHERE BNKID=1"""
    TreeStgSum2Cor = TreeStgSum2Conn.execute(queryStgSum2)
    fetchTreeStgSum2 = TreeStgSum2Cor.fetchall()
    for dataTreeStgSum in fetchTreeStgSum2:
        dataSTGSUM = dataTreeStgSum[0]
        try:
            SMGS = int(dataSTGSUM)
            TreeStgSum2.insert("", "end", values=(SMGS))
        except:
            SMGS = "هیچ"
            TreeStgSum2.insert("", "end", values=(SMGS))
    TreeStgSum2Cor.close()
    TreeStgSum2Conn.close()

    #----------------------------------------------------
    TreeStgSum2.delete(*TreeStgSum2.get_children())
    TreeStgSum2Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    queryStgSum2 = """
        SELECT
        (SELECT IFNULL(SUM(HFAMOUNT), 0) FROM HalfPayTable) AS HalfPaySum,
        (SELECT IFNULL(SUM(CSHAMOUNT * CSHQTTY), 0) FROM CashTable) AS CashTableSum,
        (SELECT IFNULL(SUM(HFAMOUNT), 0) FROM HalfPayTable) + (SELECT IFNULL(SUM(CSHAMOUNT * CSHQTTY), 0) FROM CashTable) AS TotalResult
    """
    TreeStgSum2Cor = TreeStgSum2Conn.execute(queryStgSum2)
    fetchTreeStgSum2 = TreeStgSum2Cor.fetchall()
    for dataTreeStgSum2 in fetchTreeStgSum2:
        HalfPaySum = dataTreeStgSum2[0]
        CashTableSum = dataTreeStgSum2[1]
        TotalResult = dataTreeStgSum2[2]

        try:
            SMGS = int(TotalResult)
            TreeStgSum2.insert("", "end", values=(SMGS))
        except:
            SMGS = "هیچ"
            TreeStgSum2.insert("", "end", values=(SMGS))
    TreeStgSum2Cor.close()
    TreeStgSum2Conn.close()


    #----------------------------------------
    TSS3.delete(*TSS3.get_children())
    TSS3Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    queryStgSum3 = """
        SELECT
        SUM(CSHAMOUNT * CSHQTTY),
        SUM(CSHREALPRICE * CSHQTTY)
        FROM CashTable
        """
    TSS3Cor = TSS3Conn.execute(queryStgSum3)
    fetchTSS3 = TSS3Cor.fetchall()
    for dataTSS3 in fetchTSS3:
        SMG3_0 = dataTSS3[0]
        SMG3_1 = dataTSS3[1]
        try:
            SMGS3 = int(SMG3_0) - int(SMG3_1)
            TSS3.insert("", "end", values=(SMGS3))
        except:
            SMGS3 = "هیچ"
            TSS3.insert("", "end", values=(SMGS3))
    TSS3Cor.close()
    TSS3Conn.close()


    #----------------------------------------
    TSS4.delete(*TSS4.get_children())
    TSS4Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    queryStgSum4 = """
    SELECT
    SUM(SOLDPRICE * SOLDQTT) AS SMG4
    FROM StorageSoldTable
    """
    TSS4Cor = TSS4Conn.execute(queryStgSum4)
    fetchTSS4 = TSS4Cor.fetchall()
    for dataTSS4 in fetchTSS4:
        SMG4 = dataTSS4[0]
        try:
            SMGS4 = SMG4
            TSS4.insert("", "end", values=(SMGS4))
        except:
            SMGS4 = "هیچ"
            TSS4.insert("", "end", values=(SMGS4))
    TSS4Cor.close()
    TSS4Conn.close()


def SRClear():
    strEnty6.delete(0, END)
    strEnty1.set("انتخاب نوع جنس")
    strEnty2.delete(0, END)
    strEnty3.delete(0, END)
    strEnty4.delete(0, END)
    strEnty5.delete(0, END)
    strEnty6.insert(0, DateNow)
    strEnty7.delete(0, END)
    strEnty1.focus()


def StrDeletFunc():
    StrSelected_item = TreeStg.selection()
    if StrSelected_item:
        for StrSelected_item in TreeStg.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM StorageTable WHERE SRID=?",
                    (TreeStg.set(StrSelected_item, "#8"),),
                )
                conn.commit()
                TreeStg.delete(StrSelected_item)
                conn.close()
                SRRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")


def TreeSoldDeleteFunc():
    SoldSelected_item = TreeStgSold.selection()
    if SoldSelected_item:
        for SoldSelected_item in TreeStgSold.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM StorageSoldTable WHERE SOLDID=?",
                    (TreeStgSold.set(SoldSelected_item, "#8"),),
                )
                conn.commit()
                TreeStgSold.delete(SoldSelected_item)
                conn.close()
                SRRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")




def EditingFuncStr():
    try:
        conn = sqlite3.connect("C:/My_Store/StoreDb.db")
        cur1 = conn.cursor()
        selected_item = TreeStg.selection()[0]
        for selected_item in TreeStg.selection():
            LrQueryEdit = """
            SELECT
            SRMODEL,
            SRTYPE,
            SRGROUP,
            SRPRICE,
            SRQTT,
            SRDATE,
            SRNOTE
            FROM StorageTable
            WHERE SRID=?
            """
            cur1.execute(
                LrQueryEdit,
                (TreeStg.set(selected_item, "#8"),),
            )
            fetch1 = cur1.fetchall()
            for Row in fetch1:
                data1 = Row[0]
                data2 = Row[1]
                data3 = Row[2]
                data4 = Row[3]
                data5 = Row[4]
                data6 = Row[5]
                data7 = Row[6]
                SRClear()
                strEnty6.delete(0, END)

                strEnty1.set(data1)
                strEnty2.insert(0, data2)
                strEnty3.insert(0, data3)
                strEnty4.insert(0, data4)
                strEnty5.insert(0, data5)
                strEnty6.insert(0, data6)
                strEnty7.insert(0, data7)

        cur1.close()
        conn.close()
        strEnty1.focus()
    except:
        messagebox.showerror("Space4", "عدم  شناسایی  ریکارد منتخب")


def SaveUpdateFuncStr():
    if strEnty2.get() == "":
        messagebox.showerror("Space4", "نوعیت نا مشخص")
    else:
        if strEnty2.get() != "":
            dt1 = strEnty1.get()
            dt2 = strEnty2.get()
            dt3 = strEnty3.get()
            dt4 = strEnty4.get()
            dt5 = strEnty5.get()
            dt6 = strEnty6.get()
            dt7 = strEnty7.get()
            for selected_item in TreeStg.selection():
                conn = sqlite3.connect("C:/My_Store/StoreDb.db")
                cur = conn.cursor()
                UpdQueryL = """
                UPDATE StorageTable
                SET
                SRMODEL=?,
                SRTYPE=?,
                SRGROUP=?,
                SRPRICE=?,
                SRQTT=?,
                SRDATE=?,
                SRNOTE=?
                WHERE SRID=?
                """
                cur.execute(
                    UpdQueryL,
                    (
                        dt1,
                        dt2,
                        dt3,
                        dt4,
                        dt5,
                        dt6,
                        dt7,
                        TreeStg.set(selected_item, "#8"),
                    ),
                )

                SRClear()
                messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                conn.commit()
                conn.close()
                SRRef()
        else:
            messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")




# ============ Storage Frames =============

StoreEnt_FrameTop_right = ctk.CTkFrame(master=tab1_1)
StoreEnt_FrameTop_right.grid(row=0, column=1, padx=5, pady=10, sticky=NE)

StoreTreeFrameTop_left = ctk.CTkFrame(master=tab1_1)
StoreTreeFrameTop_left.grid(row=0, column=0, padx=5, pady=10, rowspan=3, sticky=NE)


StoreBtnFrameBot_left = ctk.CTkFrame(master=tab1_1)
StoreBtnFrameBot_left.grid(row=1, column=1, padx=5, pady=10, sticky=NE)

StoreSumTreeFrameBot_right = ctk.CTkFrame(master=tab1_1)
StoreSumTreeFrameBot_right.grid(row=2, column=1, padx=5, pady=10, sticky=NE)


# ============ Labels and entries ===============

strLabel0 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="درج اقلام",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
)
strLabel0.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

strLabel1 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="نوع جنس",
    font=default_font_bold,
)
strLabel1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

strLabel2 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="نام جنس",
    font=default_font_bold,
)
strLabel2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

strLabel3 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="طبقه",
    font=default_font_bold,
)
strLabel3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)

strLabel4 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="قیمت فی",
    font=default_font_bold,
)
strLabel4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)

strLabel5 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="تعداد",
    font=default_font_bold,
)
strLabel5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)

strLabel6 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="تاریخ",
    font=default_font_bold,
)
strLabel6.grid(row=6, column=1, padx=5, pady=5, sticky=NE)

strLabel7 = ctk.CTkLabel(
    master=StoreEnt_FrameTop_right,
    text="نوت",
    font=default_font_bold,
)
strLabel7.grid(row=7, column=1, padx=5, pady=5, sticky=NE)

# ================ Entry Part ===============
TValues_1 = [
    "نوشیدنی",
    "روغنیات",
    "غله جات",
    "خوراکی",
    "دیگر",
]
SRMODEL.set("انتخاب نوع جنس")
strEnty1 = ctk.CTkComboBox(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    values=TValues_1,
    justify=RIGHT,
    variable=SRMODEL,
)
strEnty1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

strEnty2 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRTYPE,
)
strEnty2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

strEnty3 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRGROUP,
)
strEnty3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

strEnty4 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRPRICE,
)
strEnty4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)

strEnty5 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRQTT,
)
strEnty5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)

strEnty6 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRDATE
)
strEnty6.grid(row=6, column=0, padx=5, pady=5, sticky=NE)
strEnty6.insert(0, DateNow)

strEnty7 = ctk.CTkEntry(
    master=StoreEnt_FrameTop_right,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=SRNOTE,
)
strEnty7.grid(row=7, column=0, padx=5, pady=5, sticky=NE)

# -------------------- Buttons tab1 -------------------
# -------------------- Buttons tab1 -------------------
StrSaveBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=SaveImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color=TEXT_COL_1,
    text="ذخیره",
    width=40,
    font=default_font_bold2,
    command=SRSubmit,
)
StrSaveBtn1.grid(row=0, column=5, padx=2, pady=2)
StrUpdateBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=UpdateImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color=TEXT_COL_1,
    text="آپدیت",
    width=40,
    font=default_font_bold2,
    command=SaveUpdateFuncStr
)
StrUpdateBtn1.grid(row=0, column=4, padx=2, pady=2)
StrClearBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=ClearImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color=TEXT_COL_1,
    text="پاک کردن",
    width=40,
    font=default_font_bold2,
    command=SRClear,
)
StrClearBtn1.grid(row=0, column=3, padx=2, pady=2)
StrEditBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=EditImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color=TEXT_COL_1,
    text="ویرایش",
    width=40,
    font=default_font_bold2,
    command=EditingFuncStr
)
StrEditBtn1.grid(row=0, column=2, padx=2, pady=2)
StrRefreshBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=RefreshImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color=TEXT_COL_1,
    text="تجدید ",
    width=40,
    font=default_font_bold2,
    command=SRRef,
)
StrRefreshBtn1.grid(row=0, column=1, padx=2, pady=2)
StrDeleteBtn1 = ctk.CTkButton(
    StoreBtnFrameBot_left,
    image=DeleteImg,
    compound=TOP,
    hover_color=BTN_HOVER,
    fg_color=TEXT_COL_1,
    text="حذف",
    width=40,
    font=default_font_bold2,
    command=StrDeletFunc,
)
StrDeleteBtn1.grid(row=0, column=0, padx=2, pady=2)


# ============ Mini Treeview for Summing ============


# ============= Tree Storage and Selling options ============
# ============= Tree Storage and Selling options ============


def sell_item():
    selected_item = TreeStg.selection()
    item_values = TreeStg.item(selected_item)["values"]
    bill_text = "Space4 auto billing system.\n\n\
    Note: {}\n\
    Date: {}\n\
    Quantity: {}\n\
    Price: {}\n\
    Group: {}\n\
    Material Type: {}\n\
    Model: {}\n\n\n\
    Do you want to print out?".format(
        item_values[0],
        item_values[1],
        item_values[2],
        item_values[3],
        item_values[4],
        item_values[5],
        item_values[6],
    )

    askme1 = messagebox.askyesno("Space4 factor generator", bill_text)
    if askme1 > 0:
        messagebox.showinfo("Space4", "Your bill just printed out")


def BillingFunc():
    SellRoot = ctk.CTkToplevel(root)
    SellRoot.title("Space4 software")
    SellRoot.iconbitmap('Space4.ico')
    SellRoot.geometry("+300+220")
    SellRoot.resizable(0, 0)
    SellRoot.grab_set()

    SLNAME = StringVar()
    SLFNAME = StringVar()
    SLADDR = StringVar()
    SLMTYPE = StringVar()
    SLQTTY = StringVar()
    SLPRICE = StringVar()
    SLDAMOUNT = StringVar()
    SLDATE = StringVar()
    SLNOTE = StringVar()


    def SellSubmit():
        DateNow = datetime.date.today()
        if SellCheck3.get() > 0:
            for selected_item0 in TreeStg.selection():
                conn0 = sqlite3.connect("C:/My_Store/StoreDb.db")
                cur0 = conn0.cursor()
                cur01 = conn0.cursor()
                conn1 = cur0.execute(
                    """
                    SELECT
                    SRMODEL,
                    SRTYPE,
                    SRGROUP,
                    SRPRICE,
                    SRQTT,
                    SRDATE,
                    SRNOTE
                    FROM StorageTable
                    WHERE SRID=?
                    """,
                    (TreeStg.set(selected_item0, "#8"),),
                )
                fetch = cur0.fetchall()
                for data in fetch:
                    data0 = data[0]
                    data1 = data[1]
                    data2 = data[2]
                    data3 = data[3]
                    data4 = data[4]
                    data5 = data[5]
                    data6 = data[6]
                    dtget1 = SellEnty1.get()
                    dtget2 = SellEnty2.get()
                    dtget3 = SellEnty3.get()
                    dtget4 = SellEnty4.get()
                    dtget5 = SellEnty5.get()
                    dtget6 = SellEnty6.get()
                    dtget7 = halfPayEnt7.get()
                    dataSum12 = int(dtget1)*int(dtget2)
                    dataSum7 = int(dataSum12) - int(dtget7)
                    if int(data4) > 0:
                        cur0.execute(
                            f"""
                            insert into StorageSoldTable (
                            SOLDMODEL,
                            SOLDTYPE,
                            SOLDGROUP,
                            SOLDPRICE,
                            SOLDQTT,
                            SOLDDATE,
                            SOLDNOTE,
                            SOLDREALPRICE
                            )
                            values(
                            '{data0}',
                            '{data1}',
                            '{data2}',
                            '{dtget1}',
                            '{dtget2}',
                            '{DateNow}',
                            '{data6}',
                            '{data3}'
                            )
                            """
                        )
                        try:
                            dtget_123 = int(dtget1) * int(dtget2)
                            dt3_4 = int(data3) * int(data4)
                            bill_text1 = "Space4 auto billing system.\n\n\
                            Model: {}\n\
                            Material Type: {}\n\
                            Group: {}\n\
                            Price: {}\n\
                            Quantity: {}\n\
                            Date: {}\n\
                            Note: {}\n\
                            Name: {}\n\
                            Debt Amount: {}".format(
                                data0,
                                data1,
                                data2,
                                dtget_123,
                                dtget2,
                                DateNow,
                                data6,
                                dtget3,
                                dataSum7
                            )
                            SoldCounter = int(data4) - int(dtget2)
                            cur01.execute(
                                "UPDATE StorageTable SET SRQTT=? WHERE SRID=?",
                                (SoldCounter, TreeStg.set(selected_item0, "#8")),
                            )
                            messagebox.showinfo("Space4", bill_text1)
                        except:
                            messagebox.showerror(
                                "Space4", "ذخیره اطلاعات \
                                روش انجام نشد"
                            )
                    else:
                        messagebox.showwarning(
                            "Space4",
                            "مدیر عزیز\nهیچ مواد در گدام موجود نیست\n\
                            اگر مواد موجود دارید لطف نموده\n\
                            اول به لیست گدام اضافه کنید \n\
                            و بعداً اقدام به فروش آن کنید",
                        )
                    cur2 = conn0.cursor()
                    cur2.execute(
                        f"""
                        insert into SellingDebtTable (
                        SLNAME,
                        SLFNAME,
                        SLADDR,
                        SLMTYPE,
                        SLQTTY,
                        SLPRICE,
                        SLDAMOUNT,
                        SLDATE,
                        SLNOTE
                        )
                        values(
                        '{dtget3}',
                        '{dtget4}',
                        '{dtget5}',
                        '{data1}',
                        '{dtget2}',
                        '{dataSum12}',
                        '{dataSum7}',
                        '{DateNow}',
                        '{dtget6}'
                        )
                        """
                    )
                    cur3 = conn0.cursor()
                    cur3.execute(
                        f"""
                        insert into HalfPayTable (
                        HFAMOUNT,
                        HFDATE
                        )
                        values(
                        '{halfPayEnt7.get()}',
                        '{DateNow}'
                        )
                        """
                    )
                    conn0.commit()
                    conn1.close()
                    conn0.close()
                    SellRoot.destroy()
                    SRRef()

        elif SellCheck3.get() < 1:
            for selected_item in TreeStg.selection():
                conn = sqlite3.connect("C:/My_Store/StoreDb.db")
                cur = conn.cursor()
                conn1 = cur.execute(
                    """
                    SELECT
                    SRMODEL,
                    SRTYPE,
                    SRGROUP,
                    SRPRICE,
                    SRQTT,
                    SRDATE,
                    SRNOTE
                    FROM StorageTable
                    WHERE SRID=?
                    """,
                    (TreeStg.set(selected_item, "#8"),),
                )
                fetch = cur.fetchall()
                for data in fetch:
                    data0 = data[0]
                    data1 = data[1]
                    data2 = data[2]
                    data3 = data[3]
                    data4 = data[4]
                    data5 = data[5]
                    data6 = data[6]
                    dtget1 = SellEnty1.get()
                    dtget2 = SellEnty2.get()
                    if int(data4) > 0:
                        cur.execute(
                            f"""
                            insert into StorageSoldTable (
                            SOLDMODEL,
                            SOLDTYPE,
                            SOLDGROUP,
                            SOLDPRICE,
                            SOLDQTT,
                            SOLDDATE,
                            SOLDNOTE,
                            SOLDREALPRICE
                            )
                            values(
                            '{data0}',
                            '{data1}',
                            '{data2}',
                            '{dtget1}',
                            '{dtget2}',
                            '{DateNow}',
                            '{data6}',
                            '{data3}'
                            )
                            """
                        )
                        cur4 = conn.cursor()
                        ent1 = SellEnty1.get()
                        ent2 = SellEnty2.get()
                        cur4.execute(
                            f"""
                            insert into CashTable (
                            CSHAMOUNT,
                            CSHREALPRICE,
                            CSHQTTY,
                            CSHDATE
                            )
                            values(
                            '{ent1}',
                            '{data3}',
                            '{ent2}',
                            '{DateNow}'
                            )
                            """
                        )
                        try:
                            dtget_123 = int(dtget1) * int(dtget2)
                            dt3_4 = int(data3) * int(data4)
                            bill_text1 = "Space4 auto billing system.\n\n\
                            Model: {}\n\
                            Material Type: {}\n\
                            Group: {}\n\
                            Price: {}\n\
                            Quantity: {}\n\
                            Date: {}\n\
                            Note: {}\n".format(
                                data0,
                                data1,
                                data2,
                                dtget_123,
                                dtget2,
                                DateNow,
                                data6
                            )
                            SoldCounter = int(data4) - int(dtget2)
                            cur.execute(
                                "UPDATE StorageTable SET SRQTT=? WHERE SRID=?",
                                (SoldCounter, TreeStg.set(selected_item, "#8")),
                            )
                            messagebox.showinfo("Space4", bill_text1)
                        except:
                            messagebox.showerror(
                                "Space4", "ذخیره اطلاعات \
                                روش انجام نشد"
                            )
                    else:
                        messagebox.showwarning(
                            "Space4",
                            "مدیر عزیز\nهیچ مواد در گدام موجود نیست\n\
                            اگر مواد موجود دارید لطف نموده\n\
                            اول به لیست گدام اضافه کنید \n\
                            و بعداً اقدام به فروش آن کنید",
                        )
                    conn.commit()
                    conn1.close()
                    conn.close()
                    SellRoot.destroy()
                    SRRef()
    def CheckBoxDebFunc():
        if SellCheck3.get() > 0:
            # SellEnty1.configure(state=NORMAL, font=default_font_bold)
            # SellEnty2.configure(state=NORMAL, font=default_font_bold)
            SellEnty3.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty4.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty5.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty6.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            halfPayEnt7.configure(
                state=NORMAL,
                font=default_font_bold,
                border_width=2
                )
            SellEnty3.focus()
        elif SellCheck3.get() < 1:
            # SellEnty1.configure(state=DISABLED, font=default_font_bold)
            # SellEnty2.configure(state=DISABLED, font=default_font_bold)
            SellEnty3.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty4.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty5.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty6.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            halfPayEnt7.configure(
                state=DISABLED,
                font=default_font_bold,
                border_width=0
                )
            SellEnty1.focus()

    SellTitleLbl = ctk.CTkLabel(
        SellRoot,
        text="فروش جنس",
        justify=RIGHT,
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
    )
    SellTitleLbl.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

    SellLabel2 = ctk.CTkLabel(
        master=SellRoot,
        text="تعداد",
        font=default_font_bold,
    )
    SellLabel2.grid(row=1, column=1, padx=5, pady=5, sticky=NE)
    SellLabel1 = ctk.CTkLabel(
        master=SellRoot,
        text="قیمت فی",
        font=default_font_bold,
    )
    SellLabel1.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

    SellCheck3 = ctk.CTkCheckBox(
        SellRoot,
        onvalue=1,
        offvalue=0,
        text="قرضه",
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
        fg_color=TEXT_COL_1,
        hover_color=BGLIGHTGREEN,
        command=CheckBoxDebFunc
    )
    SellCheck3.grid(row=3, column=1, padx=5, pady=5, sticky=E)
    SellLabel4 = ctk.CTkLabel(
        master=SellRoot,
        text="نام مشتری",
        font=default_font_bold,
    )
    SellLabel4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)
    SellLabel5 = ctk.CTkLabel(
        master=SellRoot,
        text="نام پدر",
        font=default_font_bold,
    )
    SellLabel5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)
    SellLabel6 = ctk.CTkLabel(
        master=SellRoot,
        text="آدرس",
        font=default_font_bold,
    )
    SellLabel6.grid(row=6, column=1, padx=5, pady=5, sticky=NE)
    SellLabel7 = ctk.CTkLabel(
        master=SellRoot,
        text="نوت",
        font=default_font_bold,
    )
    SellLabel7.grid(row=7, column=1, padx=5, pady=5, sticky=NE)
    SellLabel8 = ctk.CTkLabel(
        master=SellRoot,
        text="مقدار نقده",
        font=default_font_bold,
    )
    SellLabel8.grid(row=8, column=1, padx=5, pady=5, sticky=NE)

    #--------- Entry ------------
    SellEnty2 = ctk.CTkEntry(
        master=SellRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
        placeholder_text="تعداد را وارد کنید",
    )
    SellEnty2.grid(row=1, column=0, padx=5, pady=5, sticky=NE)
    SellEnty2.focus()
    SellEnty1 = ctk.CTkEntry(
        master=SellRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
        placeholder_text="قیمت را وارد کنید",
    )
    SellEnty1.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

    SellEnty3 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty3.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
    SellEnty4 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty4.grid(row=5, column=0, padx=5, pady=5, sticky=NE)
    SellEnty5 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty5.grid(row=6, column=0, padx=5, pady=5, sticky=NE)
    SellEnty6 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SellEnty6.grid(row=7, column=0, padx=5, pady=5, sticky=NE)
    halfPayEnt7 = ctk.CTkEntry(
        master=SellRoot,
        state=DISABLED,
        border_width=0,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
        placeholder_text="مقدار نقده را وارد کنید"
    )
    halfPayEnt7.grid(row=8, column=0, padx=5, pady=10, sticky=NE)

    SellSaveBtn = ctk.CTkButton(
        SellRoot,
        text="فروش",
        font=default_font_bold,
        fg_color=TEXT_COL_1,
        hover_color=BGLIGHTGREEN,
        command=SellSubmit
    )
    SellSaveBtn.grid(row=9, column=0, padx=5, pady=10, sticky=NE)

    SellRoot.mainloop()
    # ===================================================
    # ===================== Sell Root Ended =============
def ViewPriceFunc():
    for selected_item in TreeStg.selection():
        conn = sqlite3.connect("C:/My_Store/StoreDb.db")
        cur = conn.cursor()
        conn1 = cur.execute(
            """
            SELECT
            SUM(SRPRICE*SRQTT) AS SUM0,
            SRTYPE,
            SRQTT
            FROM StorageTable
            WHERE SRID=?
            """,
            (TreeStg.set(selected_item, "#8"),),
        )
        fetch = cur.fetchall()
        for data in fetch:
            dataSum1 = data[0]
            dataSum2 = data[1]
            dataSum3 = data[2]
            try:
                messagebox.showinfo(
                    "Space4",
                    f"\tTotal: {dataSum1}\n\
                    Name: {dataSum2}\n\
                    Qtty: {dataSum3}"
                )
            except:
                messagebox.showerror("Space4 Error", "جنس شناسای نشد\n\
                    مشکل احتمالاً از طریقه وارد کردن داده  خود شما است")
        conn1.close()
        conn.close()






def SearchFunc1():
    if SEARCHVAR0.get() == "01":
        if searchEnt1.get() != "":
            TreeStg.delete(*TreeStg.get_children())
            Sconn = sqlite3.connect("C:/My_Store/StoreDb.db")
            Scur = Sconn.execute(
                """
                SELECT
                SRNOTE,
                SRDATE,
                SRQTT,
                SRPRICE,
                SRGROUP,
                SRTYPE,
                SRMODEL,
                SRID
                FROM StorageTable
                WHERE SRMODEL LIKE?
                """,
                ("%" + str(searchEnt1.get()) + "%",),
            )
            Sfetch = Scur.fetchall()
            for Sdata in Sfetch:
                TreeStg.insert("", "end", values=(Sdata))
        else:
            messagebox.showinfo("Space4", "لطفاً نوع جنس را وارد کنید")

    elif SEARCHVAR0.get() == "02":
        if searchEnt1.get() != "":
            TreeStg.delete(*TreeStg.get_children())
            Sconn = sqlite3.connect("C:/My_Store/StoreDb.db")
            Scur = Sconn.execute(
                """
                SELECT
                SRNOTE,
                SRDATE,
                SRQTT,
                SRPRICE,
                SRGROUP,
                SRTYPE,
                SRMODEL,
                SRID
                FROM StorageTable
                WHERE SRTYPE LIKE?
                """,
                ("%" + str(searchEnt1.get()) + "%",),
            )
            Sfetch = Scur.fetchall()
            for Sdata in Sfetch:
                TreeStg.insert("", "end", values=(Sdata))
        else:
            messagebox.showinfo("Space4", "لطفاً نوع جنس را وارد کنید")

    elif SEARCHVAR0.get() == "03":
        if searchEnt1.get() != "":
            TreeStg.delete(*TreeStg.get_children())
            Sconn = sqlite3.connect("C:/My_Store/StoreDb.db")
            Scur = Sconn.execute(
                """
                SELECT
                SRNOTE,
                SRDATE,
                SRQTT,
                SRPRICE,
                SRGROUP,
                SRTYPE,
                SRMODEL,
                SRID
                FROM StorageTable
                WHERE SRGROUP LIKE?
                """,
                ("%" + str(searchEnt1.get()) + "%",),
            )
            Sfetch = Scur.fetchall()
            for Sdata in Sfetch:
                TreeStg.insert("", "end", values=(Sdata))
        else:
            messagebox.showinfo("Space4", "لطفاً نوع جنس را وارد کنید")
    else:
        messagebox.showerror("Space4", "لطفاً  یکی از گزینه های زیر را در سمت راست \n\
            .ورودی جستجو انتخاب کنید و دوباره جستجو کنید\n\
            نوع جنس\n\
            نام جنس\n\
            طبقه جنس")

# def O_RadioFunc1():
#     TreeStg.delete(*TreeStg.get_children())
#     TreeStgConn = sqlite3.connect("C:/My_Store/StoreDb.db")
#     TreeStgCor = TreeStgConn.execute(
#         """
#         SELECT
#         SRNOTE,
#         SRDATE,
#         SRQTT,
#         SRPRICE,
#         SRGROUP,
#         SRTYPE,
#         SRMODEL,
#         SRID
#         FROM StorageTable
#         WHERE SRMODEL LIKE?
#         """,
#         ("%" + "روغنیات" + "%",),
#         )
#     fetchTreeStg = TreeStgCor.fetchall()
#     for indexSR in fetchTreeStg:
#         TreeStg.insert("", "end", values=indexSR)
#     TreeStgCor.close()
#     TreeStgConn.close()



# def O_RadioFunc2():
#     TreeStg.delete(*TreeStg.get_children())
#     TreeStgConn = sqlite3.connect("C:/My_Store/StoreDb.db")
#     TreeStgCor = TreeStgConn.execute(
#         """
#         SELECT
#         SRNOTE,
#         SRDATE,
#         SRQTT,
#         SRPRICE,
#         SRGROUP,
#         SRTYPE,
#         SRMODEL,
#         SRID
#         FROM StorageTable
#         WHERE SRMODEL LIKE?
#         """,
#         ("%" + "نوشیدنی" + "%",),
#         )
#     fetchTreeStg = TreeStgCor.fetchall()
#     for indexSR in fetchTreeStg:
#         TreeStg.insert("", "end", values=indexSR)
#     TreeStgCor.close()
#     TreeStgConn.close()


# def O_RadioFunc3():
#     TreeStg.delete(*TreeStg.get_children())
#     TreeStgConn = sqlite3.connect("C:/My_Store/StoreDb.db")
#     TreeStgCor = TreeStgConn.execute(
#         """
#         SELECT
#         SRNOTE,
#         SRDATE,
#         SRQTT,
#         SRPRICE,
#         SRGROUP,
#         SRTYPE,
#         SRMODEL,
#         SRID
#         FROM StorageTable
#         WHERE SRMODEL LIKE?
#         """,
#         ("%" + "غله جات" + "%",),
#         )
#     fetchTreeStg = TreeStgCor.fetchall()
#     for indexSR in fetchTreeStg:
#         TreeStg.insert("", "end", values=indexSR)
#     TreeStgCor.close()
#     TreeStgConn.close()





# #--------- ----------------------- ---------------------------- ---

# """
# styleStr = ttk.Style()# this is another style for tree views
# styleStr.configure('MyStyle.Treeview', highlightthickness=5, bd=0, font=default_font_bold1)
# styleStr.configure('MyStyle.Treeview.heading',font=default_font_bold)
# styleStr.layout('MyStyle.Treeview',[('MyStyle.Treeview.treearea', {'sticky': 'nsew'})])
# """
#-------------------------
#------ O Laser Radiobuttons -----------

ORadioTypeFrame = ctk.CTkFrame(
    StoreTreeFrameTop_left,
    corner_radius=5,
    fg_color=TKDARK
)
ORadioTypeFrame.place(x=5, y=5)
#Radio Main Frame
ORadio1_1 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=SEARCHVAR0,
    font=default_font_bold1,
    text="طبقه جنس",
    width=20,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    value="03",
)
ORadio1_1.grid(row=0, column=0, sticky=E, padx=5, pady=3)
ORadio1_2 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=SEARCHVAR0,
    font=default_font_bold1,
    text="نام جنس",
    width=20,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    value="02",
)
ORadio1_2.grid(row=0, column=1, sticky=E, padx=5, pady=3)
ORadio1_3 = ctk.CTkRadioButton(
    ORadioTypeFrame,
    variable=SEARCHVAR0,
    font=default_font_bold1,
    text="نوع جنس",
    width=20,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    value="01",
)
ORadio1_3.grid(row=0, column=2, sticky=E, padx=5,pady=3)

# -----------------------
searchFrm1 = ctk.CTkFrame(
    StoreTreeFrameTop_left,
    corner_radius=5,
    fg_color=TKDARK
    )
searchFrm1.place(x=340,y=5)

searchBtn1 = ctk.CTkButton(
    master=searchFrm1,
    text="جستجو",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=SearchFunc1
    )
searchBtn1.grid(row=0,column=0,sticky=NE,padx=10)

searchEnt1 = ctk.CTkEntry(
    master=searchFrm1,
    placeholder_text="جستجوی جنس",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
searchEnt1.grid(row=0,column=1,sticky=NE,padx=2)



# =======================================================

TreeStorageLbl = ctk.CTkLabel(
    master=StoreTreeFrameTop_left,
    text="لیست اجناس موجوده",
    font=default_font_bold,
    text_color=("teal", BGLIGHTGREEN),
    justify=RIGHT,
)
TreeStorageLbl.grid(row=0, column=0, padx=20, pady=5, sticky=NE)

TreeStrFrame = ctk.CTkFrame(StoreTreeFrameTop_left)
TreeStrFrame.grid(row=1, column=0, padx=5, sticky=NE)
TreeStg = ttk.Treeview(
    TreeStrFrame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"),
    selectmode="extended",
    height=8,
    style='MyStyle.Treeview'
)
TreeStg.heading("L1", text="نوت", anchor=E)
TreeStg.heading("L2", text="تاریخ", anchor=E)
TreeStg.heading("L3", text="تعداد", anchor=E)
TreeStg.heading("L4", text="قیمت فی", anchor=E)
TreeStg.heading("L5", text="طبقه", anchor=E)
TreeStg.heading("L6", text="نام جنس", anchor=E)
TreeStg.heading("L7", text="نوع جنس", anchor=E)
TreeStg.heading("L8", text="ID", anchor=E)

TreeStg.column("#0", stretch=NO, minwidth=0, width=0)
TreeStg.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#2", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#3", stretch=NO, minwidth=0, width=70, anchor=E)
TreeStg.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#6", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#7", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStg.column("#8", stretch=NO, minwidth=0, width=60, anchor=E)
TreeStg.grid(padx=0, pady=0)


TreeStg.delete(*TreeStg.get_children())
TreeStgConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeStgCor = TreeStgConn.execute(
    """
    SELECT
    SRNOTE,
    SRDATE,
    SRQTT,
    SRPRICE,
    SRGROUP,
    SRTYPE,
    SRMODEL,
    SRID
    FROM StorageTable
    ORDER BY SRID DESC
    """
)
fetchTreeStg = TreeStgCor.fetchall()
for indexSR in fetchTreeStg:
    TreeStg.insert("", "end", values=indexSR)
TreeStgCor.close()
TreeStgConn.close()


def SellPopup(event):
    try:
        selectedRow = TreeStg.selection()[0]
        SellMenu = Menu(
            TreeStg,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        SellMenu.add_command(
            compound=LEFT,
            image=SellImg_1,
            label="فروش",
            command=BillingFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=PriceImg1,
            label="مشاهده قیمت",
            command=ViewPriceFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=StrDeletFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=RefreshImg_1,
            label="تجدید",
            command=SRRef
        )
        SellMenu.add_command(
            compound=LEFT,
            image=EditImg_1,
            label="ویرایش",
            command=EditingFuncStr
        )
        SellMenu.add_command(
            compound=LEFT,
            image=UpdateImg_1,
            label="ذخیره تغییرات",
            command=SaveUpdateFuncStr
            )
        try:
            SellMenu.tk_popup(event.x_root, event.y_root)
        finally:
            SellMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeStg.bind("<Button-3>", SellPopup)


# ============== Sold Tree view =====================
# ============== Sold Tree view =====================

TreeStorageLblSold = ctk.CTkLabel(
    master=StoreTreeFrameTop_left,
    text="لیست اجناس فروخته شده",
    font=default_font_bold,
    text_color=("teal", BGLIGHTGREEN),
    justify=RIGHT,
)
TreeStorageLblSold.grid(row=2, column=0, padx=20, pady=5, sticky=NE)


TreeStrFrameSold = ctk.CTkFrame(StoreTreeFrameTop_left)
TreeStrFrameSold.grid(row=3, column=0, padx=5, sticky=NE)
TreeStgSold = ttk.Treeview(
    TreeStrFrameSold,
    columns=("L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"),
    selectmode="extended",
    height=8,
)
TreeStgSold.heading("L1", text="نوت", anchor=E)
TreeStgSold.heading("L2", text="تاریخ", anchor=E)
TreeStgSold.heading("L3", text="تعداد", anchor=E)
TreeStgSold.heading("L4", text="قیمت فی", anchor=E)
TreeStgSold.heading("L5", text="طبقه", anchor=E)
TreeStgSold.heading("L6", text="نام جنس", anchor=E)
TreeStgSold.heading("L7", text="نوع جنس", anchor=E)
TreeStgSold.heading("L8", text="ID", anchor=E)

TreeStgSold.column("#0", stretch=NO, minwidth=0, width=0)
TreeStgSold.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#2", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#3", stretch=NO, minwidth=0, width=70, anchor=E)
TreeStgSold.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#6", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#7", stretch=NO, minwidth=0, width=100, anchor=E)
TreeStgSold.column("#8", stretch=NO, minwidth=0, width=60, anchor=E)
TreeStgSold.grid(padx=0, pady=0)


TreeStgSold.delete(*TreeStgSold.get_children())
TreeStgSoldConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeStgSoldCor = TreeStgSoldConn.execute(
    """
    SELECT
    SOLDNOTE,
    SOLDDATE,
    SOLDQTT,
    SOLDPRICE,
    SOLDGROUP,
    SOLDTYPE,
    SOLDMODEL,
    SOLDID
    FROM StorageSoldTable
    ORDER BY SOLDID DESC
    """
)
fetchTreeStgSold = TreeStgSoldCor.fetchall()
for indexSRSold in fetchTreeStgSold:
    TreeStgSold.insert("", "end", values=indexSRSold)
TreeStgSoldCor.close()
TreeStgSoldConn.close()



# ======= This is a test of CashTable Display data======
# connCSH = sqlite3.connect("C:/My_Store/StoreDb.db")
# CurCSH = connCSH.execute(
#     """
#     SELECT
#     CSHID,
#     CSHAMOUNT,
#     CSHREALPRICE,
#     CSHDATE
#     FROM CashTable
#     """
# )
# fetchCSH = CurCSH.fetchall()
# for indexCSH in fetchCSH:
#     print(indexCSH)
# CurCSH.close()
# connCSH.close()
#--------------------------------
def SellPopup1(event):
    try:
        selectedRow = TreeStgSold.selection()[0]
        SellMenu = Menu(
            TreeStgSold,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        SellMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=TreeSoldDeleteFunc
        )
        try:
            SellMenu.tk_popup(event.x_root, event.y_root)
        finally:
            SellMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeStgSold.bind("<Button-3>", SellPopup1)

#=----------- Popup end---------------
# ------- Costs ------------

TreeStgSumFrame1 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TreeStgSumFrame1.grid(row=0, column=1, padx=10, pady=10, sticky=W)
TreeStgSum = ttk.Treeview(
    TreeStgSumFrame1,
    columns=("S1"),
    selectmode="none",
    height=1
)
TreeStgSum.heading("S1", text="ارزش اجناس موجود", anchor=E)
TreeStgSum.column("#0", stretch=NO, minwidth=0, width=0)
TreeStgSum.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TreeStgSum.grid()


TreeStgSum.delete(*TreeStgSum.get_children())
TreeStgSumConn = sqlite3.connect("C:/My_Store/StoreDb.db")
queryStgSum1 = """
SELECT
SUM(SRPRICE * SRQTT) AS SMG0
FROM StorageTable
"""
TreeStgSumCor = TreeStgSumConn.execute(queryStgSum1)
fetchTreeStgSum = TreeStgSumCor.fetchall()
for dataTreeStgSum in fetchTreeStgSum:
    SMG0 = dataTreeStgSum[0]
    try:
        SMGS = SMG0
        TreeStgSum.insert("", "end", values=(SMGS))
    except:
        SMGS = "هیچ"
        TreeStgSum.insert("", "end", values=(SMGS))
TreeStgSumCor.close()
TreeStgSumConn.close()


# ----------------------------------------------
TreeStgSumFrame2 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TreeStgSumFrame2.grid(row=0, column=0, padx=10, pady=10, sticky=W)
TreeStgSum2 = ttk.Treeview(
    TreeStgSumFrame2, columns=("S1"), selectmode="none", height=1
)
TreeStgSum2.heading("S1", text="عاید نقده", anchor=E)
TreeStgSum2.column("#0", stretch=NO, minwidth=0, width=0)
TreeStgSum2.column("#1", stretch=NO, minwidth=0, width=130, anchor=E)
TreeStgSum2.grid()


TreeStgSum2.delete(*TreeStgSum2.get_children())
TreeStgSum2Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
queryStgSum2 = """
    SELECT
    (SELECT IFNULL(SUM(HFAMOUNT), 0) FROM HalfPayTable) AS HalfPaySum,
    (SELECT IFNULL(SUM(CSHAMOUNT * CSHQTTY), 0) FROM CashTable) AS CashTableSum,
    (SELECT IFNULL(SUM(HFAMOUNT), 0) FROM HalfPayTable)
    + (SELECT IFNULL(SUM(CSHAMOUNT * CSHQTTY), 0) FROM CashTable) AS TotalResult
"""
TreeStgSum2Cor = TreeStgSum2Conn.execute(queryStgSum2)
fetchTreeStgSum2 = TreeStgSum2Cor.fetchall()
for dataTreeStgSum2 in fetchTreeStgSum2:
    HalfPaySum = dataTreeStgSum2[0]
    CashTableSum = dataTreeStgSum2[1]
    TotalResult = dataTreeStgSum2[2]

    try:
        SMGS = int(TotalResult)
        TreeStgSum2.insert("", "end", values=(SMGS))
    except:
        SMGS = "هیچ"
        TreeStgSum2.insert("", "end", values=(SMGS))
TreeStgSum2Cor.close()
TreeStgSum2Conn.close()
# ==========================================
# ==========================================

TSSF3 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TSSF3.grid(row=1, column=1, padx=10, pady=10, sticky=W)
TSS3 = ttk.Treeview(TSSF3, columns=("S1"), selectmode="none", height=1)
TSS3.heading("S1", text="مفاد از فروشات نقده", anchor=E)
TSS3.column("#0", stretch=NO, minwidth=0, width=0)
TSS3.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TSS3.grid()


TSS3.delete(*TSS3.get_children())
TSS3Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
queryStgSum3 = """
    SELECT
    SUM(CSHAMOUNT * CSHQTTY),
    SUM(CSHREALPRICE * CSHQTTY)
    FROM CashTable
    """
TSS3Cor = TSS3Conn.execute(queryStgSum3)
fetchTSS3 = TSS3Cor.fetchall()
for dataTSS3 in fetchTSS3:
    SMG3_0 = dataTSS3[0]
    SMG3_1 = dataTSS3[1]
    try:
        SMGS3 = int(SMG3_0) - int(SMG3_1)
        TSS3.insert("", "end", values=(SMGS3))
    except:
        SMGS3 = "هیچ"
        TSS3.insert("", "end", values=(SMGS3))
TSS3Cor.close()
TSS3Conn.close()



# ----------------------------------------------
TSSF4 = ctk.CTkFrame(StoreSumTreeFrameBot_right)
TSSF4.grid(row=1, column=0, padx=10, pady=10, sticky=W)
TSS4 = ttk.Treeview(TSSF4, columns=("S1"), selectmode="none", height=1)
TSS4.heading("S1", text="مجموعه فروشات", anchor=E)
TSS4.column("#0", stretch=NO, minwidth=0, width=0)
TSS4.column("#1", stretch=NO, minwidth=0, width=130, anchor=E)
TSS4.grid()


TSS4.delete(*TSS4.get_children())
TSS4Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
queryStgSum4 = """
SELECT
SUM(SOLDPRICE * SOLDQTT) AS SMG4
FROM StorageSoldTable
"""
TSS4Cor = TSS4Conn.execute(queryStgSum4)
fetchTSS4 = TSS4Cor.fetchall()
for dataTSS4 in fetchTSS4:
    SMG4 = dataTSS4[0]
    try:
        SMGS4 = SMG4
        TSS4.insert("", "end", values=(SMGS4))
    except:
        SMGS4 = "هیچ"
        TSS4.insert("", "end", values=(SMGS4))
TSS4Cor.close()
TSS4Conn.close()

#========================= Tab1_2 ============================
#========================= Tab1_2 ============================
#========================= Tab1_2 ============================
#========================= Tab1_2 ============================

def TreeSellDebtDeleteFunc():
    SellS_item = TreeSellDebt.selection()
    if SellS_item:
        for SellS_item in TreeSellDebt.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM SellingDebtTable WHERE SLID=?",
                    (TreeSellDebt.set(SellS_item, "#10"),),
                )
                conn.commit()
                TreeSellDebt.delete(SellS_item)
                conn.close()
                ReRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")


def SRepayFunc():
    if RepayEnt1.get() != "":
        dt1 = RepayEnt1.get()
        for SL_item1 in TreeSellDebt.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            conn1 = cur.execute(
                "SELECT SLDAMOUNT FROM SellingDebtTable WHERE SLID=?",
                (TreeSellDebt.set(SL_item1, "#10"),),
            )
            fetch = cur.fetchall()
            for data in fetch:
                data0 = data[0]
                addm = int(data0) - int(dt1)
                cur.execute(
                    "UPDATE SellingDebtTable SET SLDAMOUNT=? WHERE SLID=?",
                    (addm, TreeSellDebt.set(SL_item1, "#10")),
                )

                curHF = conn.cursor()
                curHF.execute(
                    f"""
                    insert into HalfPayTable (
                    HFAMOUNT,
                    HFDATE
                    )
                    values(
                    '{dt1}',
                    '{DateNow}'
                    )
                    """
                )
                RepayEnt1.delete(0, END)
                messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                conn.commit()
                conn1.close()
                conn.close()
                ReRef()
    else:
        messagebox.showinfo("اوووه", "رسید درج نگردید")

def ReRef():
    TreeSellDebt.delete(*TreeSellDebt.get_children())
    TreeSellDebtConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeSellDebtCor = TreeSellDebtConn.execute(
        """
        SELECT
        SLNOTE,
        SLDATE,
        SLPRICE,
        SLDAMOUNT,
        SLQTTY,
        SLMTYPE,
        SLADDR,
        SLFNAME,
        SLNAME,
        SLID
        FROM SellingDebtTable
        ORDER BY SLID DESC
        """
    )
    fetchTreeSellDebt = TreeSellDebtCor.fetchall()
    for indexSellD in fetchTreeSellDebt:
        TreeSellDebt.insert("", "end", values=indexSellD)
    TreeSellDebtCor.close()
    TreeSellDebtConn.close()
    showTotalDebtsFunc()

    #----------------- tOTAL ------------------------------------

def showTotalDebtsFunc():
    conn_Count = sqlite3.connect("C:/My_Store/StoreDb.db")
    Cur_Count = conn_Count.execute(
        """
        SELECT SUM(SLDAMOUNT)
        FROM SellingDebtTable
        """
    )
    fetch_Count = Cur_Count.fetchall()
    for index_count in fetch_Count:
        TotalDebtsBtn.configure(text=index_count)
    Cur_Count.close()
    conn_Count.close()


def PersonSearchFunc():
    if searchEntSell1.get() != "":
        TreeSellDebt.delete(*TreeSellDebt.get_children())
        Sconn = sqlite3.connect("C:/My_Store/StoreDb.db")
        Scur = Sconn.execute(
            """
            SELECT
            SLNOTE,
            SLDATE,
            SLPRICE,
            SLDAMOUNT,
            SLQTTY,
            SLMTYPE,
            SLADDR,
            SLFNAME,
            SLNAME,
            SLID
            FROM SellingDebtTable
            WHERE SLNAME LIKE?
            """,
            ("%" + str(searchEntSell1.get()) + "%",),
        )
        Sfetch = Scur.fetchall()
        for Sdata in Sfetch:
            TreeSellDebt.insert("", "end", values=(Sdata))
    else:
        messagebox.showinfo("Space4", "لطفاً نام شخص مرود نظر را وارد کنید")


def InsertNewDebtFunc():
    if NewDebtEnt1.get() != "":
        dt1 = NewDebtEnt1.get()
        for SL_item1 in TreeSellDebt.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            conn1 = cur.execute(
                "SELECT SLDAMOUNT FROM SellingDebtTable WHERE SLID=?",
                (TreeSellDebt.set(SL_item1, "#10"),),
            )
            fetch = cur.fetchall()
            for data in fetch:
                data0 = data[0]
                addm1 = int(data0) + int(dt1)
                cur.execute(
                    "UPDATE SellingDebtTable SET SLDAMOUNT=?, SLPRICE=? WHERE SLID=?",
                    (addm1,addm1, TreeSellDebt.set(SL_item1, "#10")),
                )
                NewDebtEnt1.delete(0, END)
                messagebox.showinfo("Space4 Software", "!رسید موفقانه  درج گردید")
                conn.commit()
                conn1.close()
                conn.close()
                ReRef()


# def EditDebtFunc():
#     try:
#         conn = sqlite3.connect("C:/My_Store/StoreDb.db")
#         cur1 = conn.cursor()
#         selected_item = TreeStg.selection()[0]
#         for selected_item in TreeStg.selection():
#             DebQuery = """
#             SELECT
#             SLNAME,
#             SLFNAME,
#             SLADDR,
#             SLMTYPE,
#             SLQTTY,
#             SLPRICE,
#             SLDAMOUNT,
#             SLDATE,
#             SLNOTE
#             FROM SellingDebtTable
#             WHERE SLID=?
#             """
#             cur1.execute(
#                 DebQuery,
#                 (TreeStg.set(selected_item, "#10"),),
#             )
#             fetch1 = cur1.fetchall()
#             for Row in fetch1:
#                 data1 = Row[0]
#                 data2 = Row[1]
#                 data3 = Row[2]
#                 data4 = Row[3]
#                 data5 = Row[4]
#                 data6 = Row[5]
#                 data7 = Row[6]
#                 SRClear()
#                 strEnty6.delete(0, END)
#                 strEnty1.set(data1)
#                 strEnty2.insert(0, data2)
#                 strEnty3.insert(0, data3)
#                 strEnty4.insert(0, data4)
#                 strEnty5.insert(0, data5)
#                 strEnty6.insert(0, data6)
#                 strEnty7.insert(0, data7)
#         cur1.close()
#         conn.close()
#         strEnty1.focus()
#     except:
#         messagebox.showerror("Space4", "عدم  شناسایی  ریکارد منتخب")

#============== Main Tab mini Frame ===========
SellDebtFrame1 = ctk.CTkFrame(master=tab1_2)
SellDebtFrame1.grid(
    row=0,
    column=0,
    padx=5,
    pady=10,
    rowspan=3,
    sticky=NE
)


# -------- Search Debtors ---------------
# -------- Search Debtors ---------------
searchFrmSell = ctk.CTkFrame(
    SellDebtFrame1,
    corner_radius=5,
    fg_color=TKDARK
    )
searchFrmSell.place(x=5, y=2)

TotalDebtsBtn = ctk.CTkButton(
    master=searchFrmSell,
    text="مجموع قرض",
    font=default_font_bold,
    text_color=BGYELLOW,
    fg_color=CTKDARK,
    hover_color=CTKDARK_FRM,
    width=120,
    command=showTotalDebtsFunc
    )
TotalDebtsBtn.grid(row=0, column=0, sticky=NE, padx=10, pady=5)
RefreshRepay1 = ctk.CTkButton(
    master=searchFrmSell,
    text="تجدید",
    font=default_font_bold,
    width=50,
    fg_color=TEXT_COL_1,
    command=ReRef
    )
RefreshRepay1.grid(row=0, column=1, sticky=NE, padx=10, pady=5)
searchBtnSell1 = ctk.CTkButton(
    master=searchFrmSell,
    text="جستجو",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=PersonSearchFunc
    )
searchBtnSell1.grid(row=0, column=2, sticky=NE, padx=10, pady=5)

searchEntSell1 = ctk.CTkEntry(
    master=searchFrmSell,
    placeholder_text="جستجوی شخص",
    justify=RIGHT,
    font=default_font_bold,
    width=120
    )
searchEntSell1.grid(row=0,column=3,sticky=NE,padx=5, pady=5)

#---------------------
RepayBtn1 = ctk.CTkButton(
    master=searchFrmSell,
    text="رسید",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=SRepayFunc
    )
RepayBtn1.grid(row=0,column=4,sticky=NE,padx=10, pady=5)

RepayEnt1 = ctk.CTkEntry(
    master=searchFrmSell,
    placeholder_text="درج کردن رسید",
    justify=RIGHT,
    font=default_font_bold,
    width=120
    )
RepayEnt1.grid(row=0,column=5,sticky=NE,padx=5, pady=5)

NewDebtBtn1 = ctk.CTkButton(
    master=searchFrmSell,
    text="دفعه کردن",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=InsertNewDebtFunc
    )
NewDebtBtn1.grid(row=0,column=6,sticky=NE,padx=10, pady=5)
NewDebtEnt1 = ctk.CTkEntry(
    master=searchFrmSell,
    placeholder_text="درج قرض جدید",
    justify=RIGHT,
    font=default_font_bold,
    width=120
    )
NewDebtEnt1.grid(row=0,column=7,sticky=NE,padx=2, pady=5)



def TreeSellEditFunc():
    SellEditRoot = ctk.CTkToplevel(root)
    SellEditRoot.title("سیستم مدیریت فروشگاه")
    SellEditRoot.iconbitmap("Space4.ico")
    SellEditRoot.resizable(0, 0)
    SellEditRoot.grab_set()

    def SlClear():
        SlEditEnt8.delete(0, END)
        SlEditEnt1.delete(0, END)
        SlEditEnt2.delete(0, END)
        SlEditEnt3.delete(0, END)
        SlEditEnt4.delete(0, END)
        SlEditEnt5.delete(0, END)
        SlEditEnt6.delete(0, END)
        SlEditEnt7.delete(0, END)
        SlEditEnt8.insert(0, DateNow)
        SlEditEnt9.delete(0, END)
        SlEditEnt1.focus()

    def InsertAfterFunc():
        conn = sqlite3.connect("C:/My_Store/StoreDb.db")
        cur1 = conn.cursor()
        selected_item = TreeSellDebt.selection()[0]
        for selected_item in TreeSellDebt.selection():
            SlQueryEdit = """
            SELECT
            SLNOTE,
            SLDATE,
            SLPRICE,
            SLDAMOUNT,
            SLQTTY,
            SLMTYPE,
            SLADDR,
            SLFNAME,
            SLNAME
            FROM SellingDebtTable
            WHERE SLID=?
            """
            cur1.execute(
                SlQueryEdit,
                (TreeSellDebt.set(selected_item, "#10"),),
            )
            fetch1 = cur1.fetchall()
            for Row in fetch1:
                data0 = Row[0]
                data1 = Row[1]
                data2 = Row[2]
                data3 = Row[3]
                data4 = Row[4]
                data5 = Row[5]
                data6 = Row[6]
                data7 = Row[7]
                data8 = Row[8]
                SlClear()
                SlEditEnt8.delete(0, END)
                SlEditEnt1.insert(0, data8)
                SlEditEnt2.insert(0, data7)
                SlEditEnt3.insert(0, data6)
                SlEditEnt4.insert(0, data5)
                SlEditEnt5.insert(0, data4)
                SlEditEnt6.insert(0, data3)
                SlEditEnt7.insert(0, data2)
                SlEditEnt8.insert(0, data1)
                SlEditEnt9.insert(0, data0)

        cur1.close()
        conn.close()
        SlEditEnt1.focus()


    def SaveUpdateFuncSl():
        if SlEditEnt1.get() == "":
            messagebox.showerror("Space4", "نوعیت نا مشخص")
        else:
            if SlEditEnt1.get() != "":
                dt1 = SlEditEnt1.get()
                dt2 = SlEditEnt2.get()
                dt3 = SlEditEnt3.get()
                dt4 = SlEditEnt4.get()
                dt5 = SlEditEnt5.get()
                dt6 = SlEditEnt6.get()
                dt7 = SlEditEnt7.get()
                dt8 = SlEditEnt8.get()
                dt9 = SlEditEnt9.get()
                for selected_item in TreeSellDebt.selection():
                    conn = sqlite3.connect("C:/My_Store/StoreDb.db")
                    cur = conn.cursor()
                    UpdQueryL = """
                    UPDATE SellingDebtTable
                    SET
                    SLNAME=?,
                    SLFNAME=?,
                    SLADDR=?,
                    SLMTYPE=?,
                    SLQTTY=?,
                    SLPRICE=?,
                    SLDAMOUNT=?,
                    SLDATE=?,
                    SLNOTE=?
                    WHERE SLID=?
                    """
                    cur.execute(
                        UpdQueryL,
                        (
                            dt1,
                            dt2,
                            dt3,
                            dt4,
                            dt5,
                            dt6,
                            dt7,
                            dt8,
                            dt9,
                            TreeSellDebt.set(selected_item, "#10"),
                        ),
                    )

                    SlClear()
                    messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                    conn.commit()
                    conn.close()
                    ReRef()
                    SellEditRoot.destroy()
            else:
                messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")


    SlttlLabel1 = ctk.CTkLabel(
        SellEditRoot,
        text="ویرایش کردن",
        justify=RIGHT,
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
    )
    SlttlLabel1.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

    SlLabel1 = ctk.CTkLabel(
        master=SellEditRoot,
        text="نام",
        font=default_font_bold,
    )
    SlLabel1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

    SlLabel2 = ctk.CTkLabel(
        master=SellEditRoot,
        text="نام پدر",
        font=default_font_bold,
    )
    SlLabel2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)
    SlLabel3 = ctk.CTkLabel(
        master=SellEditRoot,
        text="آدرس",
        font=default_font_bold,
    )
    SlLabel3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)
    SlLabel4 = ctk.CTkLabel(
        master=SellEditRoot,
        text="جنس",
        font=default_font_bold,
    )
    SlLabel4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)
    SlLabel5 = ctk.CTkLabel(
        master=SellEditRoot,
        text="تعداد",
        font=default_font_bold,
    )
    SlLabel5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)
    SlLabel6 = ctk.CTkLabel(
        master=SellEditRoot,
        text="مقدار باقی",
        font=default_font_bold,
    )
    SlLabel6.grid(row=6, column=1, padx=5, pady=5, sticky=NE)
    SlLabel7 = ctk.CTkLabel(
        master=SellEditRoot,
        text="قرض اولیه",
        font=default_font_bold,
    )
    SlLabel7.grid(row=7, column=1, padx=5, pady=5, sticky=NE)
    SlLabel8 = ctk.CTkLabel(
        master=SellEditRoot,
        text="تاریخ",
        font=default_font_bold,
    )
    SlLabel8.grid(row=8, column=1, padx=5, pady=5, sticky=NE)
    SlLabel9 = ctk.CTkLabel(
        master=SellEditRoot,
        text="نوت",
        font=default_font_bold,
    )
    SlLabel9.grid(row=9, column=1, padx=5, pady=5, sticky=NE)

    #--------- Entry ------------
    SlEditEnt1 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt1.focus()
    SlEditEnt1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

    SlEditEnt2 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt3 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt4 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt5 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt6 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt6.grid(row=6, column=0, padx=5, pady=5, sticky=NE)
    SlEditEnt7 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt7.grid(row=7, column=0, padx=5, pady=10, sticky=NE)
    SlEditEnt8 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt8.grid(row=8, column=0, padx=5, pady=10, sticky=NE)
    SlEditEnt9 = ctk.CTkEntry(
        master=SellEditRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    SlEditEnt9.grid(row=9, column=0, padx=5, pady=10, sticky=NE)
    SellSaveBtn = ctk.CTkButton(
        SellEditRoot,
        text="انجام",
        font=default_font_bold,
        fg_color=TEXT_COL_1,
        hover_color=BGLIGHTGREEN,
        command=SaveUpdateFuncSl
    )
    SellSaveBtn.grid(row=10, column=0, padx=5, pady=10, sticky=NE)
    SellEditRoot.after(500, InsertAfterFunc)
    SellEditRoot.mainloop()
# ============== Sell Debt Tree view =====================
# ============== Sell Debt Tree view =====================

SellDebtLabel1 = ctk.CTkLabel(
    master=SellDebtFrame1,
    text="لیست قرضداران",
    font=default_font_bold,
    text_color=("teal", BGLIGHTGREEN),
    justify=RIGHT,
)
SellDebtLabel1.grid(row=2, column=0, padx=20, pady=5, sticky=NE)


TreeSellDebtFrm = ctk.CTkFrame(SellDebtFrame1)
TreeSellDebtFrm.grid(row=3, column=0, padx=5, sticky=NE)
TreeSellDebt = ttk.Treeview(
    TreeSellDebtFrm,
    columns=(
        "L1",
        "L2",
        "L3",
        "L4",
        "L5",
        "L6",
        "L7",
        "L8",
        "L9",
        "L10"
        ),
    selectmode="browse",
    height=18,
)
TreeSellDebt.heading("L1", text="نوت", anchor=E)
TreeSellDebt.heading("L2", text="تاریخ", anchor=E)
TreeSellDebt.heading("L3", text="مقدار", anchor=E)
TreeSellDebt.heading("L4", text="باقی", anchor=E)
TreeSellDebt.heading("L5", text="تعداد", anchor=E)
TreeSellDebt.heading("L6", text="جنس", anchor=E)
TreeSellDebt.heading("L7", text="آدرس", anchor=E)
TreeSellDebt.heading("L8", text="نام پدر", anchor=E)
TreeSellDebt.heading("L9", text="نام مشتری", anchor=E)
TreeSellDebt.heading("L10", text="نمبر", anchor=E)


TreeSellDebt.column("#0", stretch=NO, minwidth=0, width=0)
TreeSellDebt.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#2", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#3", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#6", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#7", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#8", stretch=NO, minwidth=0, width=100, anchor=E)
TreeSellDebt.column("#9", stretch=NO, minwidth=0, width=120, anchor=E)
TreeSellDebt.column("#10", stretch=NO, minwidth=0, width=60, anchor=E)
TreeSellDebt.grid(padx=0, pady=0)


TreeSellDebt.delete(*TreeSellDebt.get_children())
TreeSellDebtConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeSellDebtCor = TreeSellDebtConn.execute(
    """
    SELECT
    SLNOTE,
    SLDATE,
    SLPRICE,
    SLDAMOUNT,
    SLQTTY,
    SLMTYPE,
    SLADDR,
    SLFNAME,
    SLNAME,
    SLID
    FROM SellingDebtTable
    ORDER BY SLID DESC
    """
)
fetchTreeSellDebt = TreeSellDebtCor.fetchall()
for indexSellD in fetchTreeSellDebt:
    TreeSellDebt.insert("", "end", values=indexSellD)
TreeSellDebtCor.close()
TreeSellDebtConn.close()

#--------------------------------
def SellDebtPop(event):
    try:
        selectedRow = TreeSellDebt.selection()[0]
        SellMenu = Menu(
            TreeSellDebt,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        SellMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=TreeSellDebtDeleteFunc
        )
        SellMenu.add_command(
            compound=LEFT,
            image=RefreshImg_1,
            label="تجدید",
            command=ReRef
        )
        SellMenu.add_command(
            compound=LEFT,
            image=EditImg_1,
            label="ویرایش",
            command=TreeSellEditFunc
        )
        try:
            SellMenu.tk_popup(event.x_root, event.y_root)
        finally:
            SellMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeSellDebt.bind("<Button-3>", SellDebtPop)

#=----------- Popup end---------------




#========================= Tab1_3 ============================
#========================= Tab1_3 ============================
#========================= Tab1_3 ============================
#========================= Tab1_3 ============================


# =-------------- Sql3 activation functions -------------

def CorrRef():
    TreeCorr.delete(*TreeCorr.get_children())
    TreeCorrConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeCorrCor = TreeCorrConn.execute(
        """
        SELECT
        CSHDATE,
        CSHQTTY,
        CSHREALPRICE,
        CSHAMOUNT,
        CSHID
        FROM CashTable
        ORDER BY CSHID DESC
        """
    )
    fetchTreeCorr = TreeCorrCor.fetchall()
    for dataTreeCorr in fetchTreeCorr:
        TreeCorr.insert("", "end", values=(dataTreeCorr))
    TreeCorrCor.close()
    TreeCorrConn.close()
    #_---------------- End ------------


def CorrDeleteFunc():
    selected_item = TreeCorr.selection()
    if selected_item:
        for selected_item in TreeCorr.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM CashTable WHERE CSHID=?",
                    (TreeCorr.set(selected_item, "#5"),),
                )
                conn.commit()
                TreeCorr.delete(selected_item)
                conn.close()
                CorrRef()
    else:
        messagebox.showerror("Space4", "لطفاً ریکارد مورد نظر را انتخاب کنید")


def CorrDeleteAllFunc():
    conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "هشدار", "؟آیا میخواهید تمام داده ها را حذف کنید"
    )
    if messageDelete > 0:
        messageDeletelast = messagebox.askyesno("اختطار", "اطلاعات قابل بازیابی نخواهد بود\n\
            بهرحال ادامه میدهید")
        if messageDeletelast > 0:
            cur.execute("DELETE FROM CashTable")
            conn.commit()
            conn.close()
            CorrRef()


def CorrEditFunc():
    CorrRoot = ctk.CTkToplevel(root)
    CorrRoot.title("ویرایش اطلاعات")
    CorrRoot.iconbitmap("Space4.ico")
    CorrRoot.resizable(0, 0)
    CorrRoot.grab_set()

    def CorrClearFunc():
        CorrEnt1.delete(0, END)
        CorrEnt2.delete(0, END)
        CorrEnt3.delete(0, END)
        CorrEnt1.focus()

    def CorrInsertEditFunc():
        conn = sqlite3.connect("C:/My_Store/StoreDb.db")
        cur1 = conn.cursor()
        selected_item = TreeCorr.selection()[0]
        for selected_item in TreeCorr.selection():
            SlQueryEdit = """
            SELECT
            CSHQTTY,
            CSHREALPRICE,
            CSHAMOUNT
            FROM CashTable
            WHERE CSHID=?
            """
            cur1.execute(
                SlQueryEdit,
                (TreeCorr.set(selected_item, "#5"),),
            )
            fetch1 = cur1.fetchall()
            for Row in fetch1:
                data0 = Row[0]
                data1 = Row[1]
                data2 = Row[2]
                CorrClearFunc()
                CorrEnt1.insert(0, data2)
                CorrEnt2.insert(0, data1)
                CorrEnt3.insert(0, data0)

        cur1.close()
        conn.close()
        CorrEnt1.focus()


    def SaveUpdateFuncCorr():
        if CorrEnt1.get() == "":
            messagebox.showerror("Space4", "نوعیت نا مشخص")
        else:
            if CorrEnt1.get() != "":
                dt1 = CorrEnt1.get()
                dt2 = CorrEnt2.get()
                dt3 = CorrEnt3.get()
                for selected_item in TreeCorr.selection():
                    conn = sqlite3.connect("C:/My_Store/StoreDb.db")
                    cur = conn.cursor()
                    UpdQueryL = """
                    UPDATE CashTable
                    SET
                    CSHAMOUNT=?,
                    CSHREALPRICE=?,
                    CSHQTTY=?
                    WHERE CSHID=?
                    """
                    cur.execute(
                        UpdQueryL,
                        (
                            dt1,
                            dt2,
                            dt3,
                            TreeCorr.set(selected_item, "#5"),
                        ),
                    )

                    CorrClearFunc()
                    messagebox.showinfo("Space4 Software", "! آپدیت موفقانه انجام شد")
                    conn.commit()
                    conn.close()
                    CorrRef()
                    CorrRoot.destroy()
            else:
                messagebox.showinfo("اوووه", "!!!ریکارد ذخیره نشد")


    CorrTtlLbl = ctk.CTkLabel(
        CorrRoot,
        text="ویرایش کردن",
        justify=RIGHT,
        font=default_font_bold,
        text_color=BGLIGHTGREEN,
    )
    CorrTtlLbl.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

    CorrLbl1 = ctk.CTkLabel(
        master=CorrRoot,
        text="مقدار",
        font=default_font_bold,
    )
    CorrLbl1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

    CorrLbl2 = ctk.CTkLabel(
        master=CorrRoot,
        text="قیمت تمام شد",
        font=default_font_bold,
    )
    CorrLbl2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)
    CorrLbl3 = ctk.CTkLabel(
        master=CorrRoot,
        text="تعداد",
        font=default_font_bold,
    )
    CorrLbl3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)



    #--------- Entry ------------
    CorrEnt1 = ctk.CTkEntry(
        master=CorrRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    CorrEnt1.focus()
    CorrEnt1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

    CorrEnt2 = ctk.CTkEntry(
        master=CorrRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    CorrEnt2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)
    CorrEnt3 = ctk.CTkEntry(
        master=CorrRoot,
        font=default_font_bold,
        width=200,
        justify=RIGHT,
    )
    CorrEnt3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

    CorrSaveBtn = ctk.CTkButton(
        CorrRoot,
        text="انجام",
        font=default_font_bold,
        fg_color=TEXT_COL_1,
        hover_color=BGLIGHTGREEN,
        command=SaveUpdateFuncCorr
    )
    CorrSaveBtn.grid(row=10, column=0, padx=5, pady=10, sticky=NE)
    CorrRoot.after(500, CorrInsertEditFunc)
    CorrRoot.mainloop()


#=---------------- Correction Frames ----------------

FrameTab1_3_Top = ctk.CTkFrame(tab1_3)
FrameTab1_3_Top.grid(row=0, column=0, sticky=EW)
FrameTab1_3_Bot = ctk.CTkFrame(tab1_3)
FrameTab1_3_Bot.grid(row=1, column=0, sticky=EW)

FrameTab1_3_Btns = ctk.CTkFrame(tab1_3)
FrameTab1_3_Btns.place(x=10, y=10)

# ============= Debtor Treeview ============
CorrRefButton = ctk.CTkButton(
    master=FrameTab1_3_Btns,
    text="تجدید",
    font=default_font_bold,
    width=100,
    command=CorrRef
)
CorrRefButton.grid(row=0, column=0, padx=5, pady=2)

CorrEditBtn = ctk.CTkButton(
    master=FrameTab1_3_Btns,
    text="ویرایش",
    font=default_font_bold,
    width=100,
    command=CorrEditFunc
)
CorrEditBtn.grid(row=0, column=1, padx=5, pady=2)

CorrDeleteBtn = ctk.CTkButton(
    master=FrameTab1_3_Btns,
    text="حذف",
    font=default_font_bold,
    width=100,
    command=CorrDeleteFunc
)
CorrDeleteBtn.grid(row=0, column=2, padx=5, pady=2)

CorrDeleteAllBtn = ctk.CTkButton(
    master=FrameTab1_3_Btns,
    text="حذف همه",
    font=default_font_bold,
    width=100,
    command=CorrDeleteAllFunc
)
CorrDeleteAllBtn.grid(row=0, column=3, padx=5, pady=2)


TreeCorrTtlLbl = ctk.CTkLabel(
    master=FrameTab1_3_Top,
    text="پیگیری نقده",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
    justify=RIGHT,
)
TreeCorrTtlLbl.grid(row=0, column=1, padx=20, pady=10, sticky=NE)


TreeCorrFrame = ctk.CTkFrame(FrameTab1_3_Top)
TreeCorrFrame.grid(row=1, column=1, padx=5, sticky=NE)
TreeCorr = ttk.Treeview(
    TreeCorrFrame,
    columns=("L1", "L2", "L3", "L4", "L5"),
    selectmode="extended",
    height=10,
)
TreeCorr.heading("L1", text="تاریخ", anchor=E)
TreeCorr.heading("L2", text="تعداد", anchor=E)
TreeCorr.heading("L3", text="قیمت تمام شد", anchor=E)
TreeCorr.heading("L4", text="مقدار", anchor=E)
TreeCorr.heading("L5", text="ID", anchor=E)

TreeCorr.column("#0", stretch=NO, minwidth=0, width=0)
TreeCorr.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TreeCorr.column("#2", stretch=NO, minwidth=0, width=120, anchor=E)
TreeCorr.column("#3", stretch=NO, minwidth=0, width=120, anchor=E)
TreeCorr.column("#4", stretch=NO, minwidth=0, width=120, anchor=E)
TreeCorr.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeCorr.grid(padx=0, pady=0)


TreeCorr.delete(*TreeCorr.get_children())
TreeCorrConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeCorrCor = TreeCorrConn.execute(
    """
    SELECT
    CSHDATE,
    CSHQTTY,
    CSHREALPRICE,
    CSHAMOUNT,
    CSHID
    FROM CashTable
    ORDER BY CSHID DESC
    """
)
fetchTreeCorr = TreeCorrCor.fetchall()
for dataTreeCorr in fetchTreeCorr:
    TreeCorr.insert("", "end", values=(dataTreeCorr))
TreeCorrCor.close()
TreeCorrConn.close()


# --------------- Bindings ----------------

def CorrectionFunc(event):
    try:
        selectedRowCorr = TreeCorr.selection()[0]
        CorrMenu = Menu(
            TreeCorr,
            tearoff=0,
            font=default_font_bold1,
            bg=CTKDARK,
            fg=CTKLIGHT,
            activebackground=BGLIGHTGREEN,
        )
        CorrMenu.add_command(
            compound=LEFT,
            image=RefreshImg_1,
            label="تجدید",
            command=CorrRef
        )
        CorrMenu.add_command(
            compound=LEFT,
            image=EditImg_1,
            label="ویرایش",
            command=CorrEditFunc
        )
        CorrMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف",
            command=CorrDeleteFunc
        )
        CorrMenu.add_command(
            compound=LEFT,
            image=DeleteImg_1,
            label="حذف همه",
            command=CorrDeleteAllFunc
        )
        try:
            CorrMenu.tk_popup(event.x_root, event.y_root)
        finally:
            CorrMenu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! ریکارد را انتخاب کنید لطفاً")


TreeCorr.bind("<Double-Button-1>", CorrectionFunc)






#========================= Tab 2 ============================
#========================= Tab 2 ============================
#========================= Tab 2 ============================
#========================= Tab 2 ============================
#========================= Tab 2 ============================
#========================= Tab 2 ============================
#========================= Tab 2 ============================


FTYPE = StringVar()
FCOSTTYPE = StringVar()
FAMOUNT = StringVar()
FNOTE = StringVar()
Tree3_SHOW_BY_DATE_FROM = StringVar()
Tree3_SHOW_BY_DATE_TO = StringVar()

ITYPE = StringVar()
IINCTYPE = StringVar()
IAMOUNT = StringVar()
IDATE = StringVar()
INOTE = StringVar()

FDATE = StringVar()
REGTYPE_VAR = StringVar()
INCTYPE_VAR = StringVar()
# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================


# ============== This is for the income table to ===============





def MFRef():
    Tree3.delete(*Tree3.get_children())
    Tree3Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    Tree3Cor = Tree3Conn.execute(
        """
        SELECT
        FNOTE,
        FDATE,
        FAMOUNT,
        FCOSTTYPE,
        FTYPE,
        FTID
        FROM FCostTable
        """
    )
    fetchTree3 = Tree3Cor.fetchall()
    for dataTree3 in fetchTree3:
        Tree3.insert("", "end", values=(dataTree3))
    Tree3Cor.close()
    Tree3Conn.close()


def MFInClearFunc():
    Inc_Entry1.delete(0, END)
    Inc_Entry2.delete(0, END)
    Inc_Entry3.delete(0, END)
    Inc_Entry4.delete(0, END)
    Inc_Entry1.focus()


# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================
# ================ Rent,Tax,ElecBill,etc contents ================
def FSubmit():
    import datetime

    DateNow = datetime.date.today()
    FConn1 = sqlite3.connect("C:/My_Store/StoreDb.db")
    Fcur1 = FConn1.cursor()
    if Finance_MngEntry3.get() == "":
        messagebox.showerror("Space4", "مقدار نمیتواند خالی باشد")
    else:
        if REGTYPE_VAR.get() == DAILY_VAL:
            Fcur1.execute(
                f"insert into FCostTable (FTYPE,\
                FCOSTTYPE,FAMOUNT,FDATE,FNOTE) values ('{REGTYPE_VAR.get()}',\
                '{FCOSTTYPE.get()}','{FAMOUNT.get()}',\
                '{FDATE.get()}','{FNOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

        if REGTYPE_VAR.get() == MONTHLY_VAL:
            Fcur1.execute(
                f"insert into FCostTable (FTYPE,\
                FCOSTTYPE,FAMOUNT,FDATE,FNOTE) values ('{REGTYPE_VAR.get()}',\
                '{FCOSTTYPE.get()}','{FAMOUNT.get()}',\
                '{FDATE.get()}','{FNOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

        if REGTYPE_VAR.get() == YEARLY_VAL:
            Fcur1.execute(
                f"insert into FCostTable (FTYPE,\
                FCOSTTYPE,FAMOUNT,FDATE,FNOTE) values ('{REGTYPE_VAR.get()}',\
                '{FCOSTTYPE.get()}','{FAMOUNT.get()}',\
                '{FDATE.get()}','{FNOTE.get()}')"
            )
            messagebox.showinfo("Space4", "ثبت انجام شد")

    FConn1.commit()
    FConn1.close()

    Finance_MngEntry4.delete(0, END)
    Finance_MngEntry3.delete(0, END)
    Finance_MngEntry5.delete(0, END)
    Finance_MngEntry2.focus()
    FRef()
    Finance_MngEntry4.insert(0, DateNow)


def FClearFunc():
    Finance_MngEntry4.delete(0, END)
    Finance_MngEntry2.set("انتخاب نوع")
    Finance_MngEntry3.delete(0, END)
    Finance_MngEntry5.delete(0, END)
    Finance_MngEntry2.focus()
    Finance_MngEntry4.insert(0, DateNow)



def FRef():
    BalanceDisplayFunc()
    # AutoUpdateBankFunc()
    # -------------------------------------
    # -------------------------------------
    Tree0.delete(*Tree0.get_children())
    Tree0Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    query0 = """
    SELECT
        SUM(FAMOUNT) AS SM0
    FROM
        FCostTable
    WHERE
        FDATE BETWEEN date(?, '-1 month') AND date(?, '+1 day')
        AND FTYPE LIKE '%' || ? || '%'
    """

    Tree0Cor = Tree0Conn.execute(
        query0, (A_Between_EntryFrom.get(), A_Between_EntryFrom.get(), "روزانه")
    )
    fetchTree0 = Tree0Cor.fetchall()
    for dataTree0 in fetchTree0:
        try:
            CalcProfit = int(dataTree0[0])
            Tree0.insert("", "end", values=(CalcProfit,))
        except:
            Tree0.insert("", "end", values=("هیچ",))
    Tree0Cor.close()
    Tree0Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree1.delete(*Tree1.get_children())
    Tree1Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    query1 = """
    SELECT
        SUM(FAMOUNT) AS SM0
    FROM
        FCostTable
    WHERE
        FDATE BETWEEN date(?, '-1 month') AND date(?, '+1 day')
        AND FTYPE LIKE '%' || ? || '%'
    """
    Tree1Cor = Tree1Conn.execute(
        query1, (B_Between_EntryFrom.get(), B_Between_EntryFrom.get(), "ماهانه")
    )
    fetchTree1 = Tree1Cor.fetchall()
    for dataTree1 in fetchTree1:
        try:
            CalcProfit = int(dataTree1[0])
            Tree1.insert("", "end", values=(CalcProfit,))
        except:
            Tree1.insert("", "end", values=("هیچ",))
    Tree1Cor.close()
    Tree1Conn.close()

    # -------------------------------------
    # -------------------------------------
    Tree2.delete(*Tree2.get_children())
    Tree2Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    query2 = """
    SELECT
        SUM(FAMOUNT) AS SM00
    FROM
        FCostTable
    WHERE
        FDATE BETWEEN date(?, '-12 month') AND date(?, '+1 day')
        AND FTYPE LIKE '%' || ? || '%'
    """
    Tree2Cor = Tree2Conn.execute(
        query2,(C_Between_EntryFrom.get(),C_Between_EntryFrom.get(),"سالانه")
    )
    fetchTree2 = Tree2Cor.fetchall()
    for dataTree2 in fetchTree2:
        Tree2.insert("", "end", values=(dataTree2))
    Tree2Cor.close()
    Tree2Conn.close()


    # -------------------------------------
    # -------------------------------------
    Tree3.delete(*Tree3.get_children())
    Tree3Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    Tree3Cor = Tree3Conn.execute(
        """
        SELECT
        FNOTE,
        FDATE,
        FAMOUNT,
        FCOSTTYPE,
        FTYPE,
        FTID
        FROM FCostTable
        ORDER BY FTID DESC
        """
    )
    fetchTree3 = Tree3Cor.fetchall()
    for dataTree3 in fetchTree3:
        Tree3.insert("", "end", values=(dataTree3))
        #----- Totaling ---------
        cur_01 = Tree3Conn.execute(
            """
            SELECT
            SUM(FAMOUNT)
            FROM FCostTable
            """
        )
        fch_01 = cur_01.fetchall()
        for dt_01 in fch_01:
            dt_1_1 = dt_01[0]
            Ttl_01_lbl.configure(text=f"{dt_1_1} :مجموعه هزینه ها")
        cur_01.close()
        #------ End of totaling --------
    Tree3Cor.close()
    Tree3Conn.close()



    #----------------- Balance Display ---------------
def BalanceDisplayFunc():
    connBalance = sqlite3.connect("C:/My_Store/StoreDb.db")
    curBalance = connBalance.cursor()
    curBalance.execute("SELECT BALANCE FROM BankTable WHERE BNKID=1")
    balance = curBalance.fetchall()
    for data in balance:
        data0 = data[0]
        DisplayBalanceLbl1.configure(text=f"{data0} :بیلانس شما")
    connBalance.close()



def FDeleteFunc():  # This is for deleting in cases. looking at multi selections and then deleting
    selected_item = Tree3.selection()
    if selected_item:
        for selected_item in Tree3.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM FCostTable WHERE FTID=?",
                    (Tree3.set(selected_item, "#6"),),
                )
                conn.commit()
                Tree3.delete(selected_item)
                conn.close()

    else:
        messagebox.showerror("Space4", "! لطفاً ریکارد مورد نظر را انتخاب کنید")


def DepositFunc():
    if WithDrawEnt1.get() != "":
        dt1 = int(WithDrawEnt1.get())
        conn = sqlite3.connect("C:/My_Store/StoreDb.db")
        cur = conn.cursor()
        cur.execute("SELECT BALANCE FROM BankTable WHERE BNKID=1")
        fetch = cur.fetchall()
        success = False
        for data in fetch:
            data0 = data[0]
            try:
                addm = int(data0) + dt1
                cur.execute("UPDATE BankTable SET BALANCE=? WHERE BNKID=1", (addm,))
                success = True
                WithDrawEnt1.delete(0, END)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        if success:
            messagebox.showinfo("Space4 Software", f"افغانی موفقانه به دخل افزوده شد: {dt1}\nموجودی فعلی شما: افغانی {addm}")
        try:
            conn.commit()
            conn.close()
            FRef()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showinfo("اوووه", "ورودی خالی است")


def WithDrawFunc():
    if WithDrawEnt1.get() != "":
        dt1 = int(WithDrawEnt1.get())
        conn = sqlite3.connect("C:/My_Store/StoreDb.db")
        cur = conn.cursor()
        cur.execute("SELECT BALANCE FROM BankTable WHERE BNKID=1")
        fetch = cur.fetchall()
        for data in fetch:
            data0 = data[0]
            try:
                if dt1 > int(data0):
                    messagebox.showwarning("Space4", "ببخشید، موجودی دخل شما کمتر از مقدار مورد نیاز شماست")
                else:
                    try:
                        addm = int(data0) - dt1
                        cur.execute("UPDATE BankTable SET BALANCE=? WHERE BNKID=1", (addm,))
                        WithDrawEnt1.delete(0, END)
                        messagebox.showinfo("Space4 Software", f"افغانی از دخل برداشته شد: {dt1}\n\
                            موجودی فعلی شما: افغانی {addm}")
                        conn.commit()
                    except ValueError:
                        pass
                break  # Exit the loop after the first iteration
            except ValueError:
                messagebox.showerror("برداشت", "فقط عدد وارد کنید")
        conn.close()
        FRef()
    else:
        messagebox.showinfo("اوووه", "ورودی خالی است")




# def AutoUpdateBankFunc():
#     conn = sqlite3.connect("C:/My_Store/StoreDb.db")
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT
#         (SELECT IFNULL(SUM(HFAMOUNT), 0) FROM HalfPayTable) AS HalfPaySum,
#         (SELECT IFNULL(SUM(CSHAMOUNT * CSHQTTY), 0) FROM CashTable) AS CashTableSum,
#         (SELECT IFNULL(SUM(HFAMOUNT), 0) FROM HalfPayTable) + (SELECT IFNULL(SUM(CSHAMOUNT * CSHQTTY), 0) FROM CashTable) AS TotalResult
#         """)
#     fetch = cur.fetchall()
#     success = False
#     for data in fetch:
#         HalfPaySum = data[0]
#         CashTableSum = data[1]
#         TotalResult = data[2]

#         # ---------- TO sum both values from previus and new value -------
#         curBalance = conn.cursor()
#         curBalance.execute("SELECT BALANCE FROM BankTable WHERE BNKID=1")
#         balance = curBalance.fetchall()
#         for blcData in balance:
#             data0 = blcData[0]

#         try:
#             addm = int(TotalResult) + int(data0)
#             print(data0, addm)
#             cur.execute("UPDATE BankTable SET BALANCE=? WHERE BNKID=1", (addm,))
#             success = True
#         except ValueError:
#             pass
#     if success:
#         pass
#     conn.commit()
#     conn.close()




Type_Values = [
    "غذا",
    "ابزاراولیه",
    "کرایه_دوکان",
    "بل_برق",
    "تکس",
    "دیگر مالیات",
    "هزینه تبلیغات",
    "لوازم داخلی",
]


def RadioFunc1():
    DateNow = datetime.date.today()
    Finance_MngEntry4.delete(0, END)
    Finance_MngEntry2.configure(state=NORMAL, border_width=2)
    Finance_MngEntry3.configure(state=NORMAL, border_width=2)
    Finance_MngEntry4.configure(state=NORMAL, border_width=2)
    Finance_MngEntry4.insert(0, DateNow)
    Finance_MngEntry5.configure(state=NORMAL, border_width=2)
    FCOSTTYPE.set("انتخاب نوع")
    Finance_MngEntry2.focus()


def RadioFuncInc1():
    Inc_Entry1.configure(state=NORMAL, border_width=2)
    Inc_Entry2.configure(state=NORMAL, border_width=2)
    Inc_Entry3.configure(state=NORMAL, border_width=2)
    Inc_Entry4.configure(state=NORMAL, border_width=2)
    Inc_Entry1.focus()


# =========== Main Frames Opened ===========
Tab3_Frame_InTop = ctk.CTkFrame(tab2)
Tab3_Frame_InTop.grid(row=0, column=0, padx=5, pady=10, sticky=NE)
Tab3_Frame_InBot = ctk.CTkFrame(tab2)
Tab3_Frame_InBot.grid(row=1, column=0, padx=5, pady=10, sticky=NE)

MainFrame_BOT_L_T3 = ctk.CTkFrame(Tab3_Frame_InTop)
MainFrame_BOT_L_T3.grid(row=0, column=0, padx=5, pady=10, sticky=NE)
MainFrame_RIGHT_T3 = ctk.CTkFrame(Tab3_Frame_InTop)
MainFrame_RIGHT_T3.grid(row=0, column=1, padx=10, pady=10, sticky=NE)
MainButFrame1 = ctk.CTkFrame(Tab3_Frame_InTop)
MainButFrame1.grid(row=1, column=1, padx=5, pady=10, sticky=NE)

# =========== Main Frames Closed ===========
Count_labSalary = ctk.CTkLabel(
    master=MainFrame_BOT_L_T3,
    text="",
    text_color=BGYELLOW
)
Count_labSalary.place(x=400, y=0)

Finance_MngLabel0 = ctk.CTkLabel(
    MainFrame_RIGHT_T3,
    text="حالت مصرف",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
    justify=RIGHT,
)
Finance_MngLabel0.grid(row=0, column=1, sticky=E, padx=10, pady=10)


Finance_MngLabel1 = ctk.CTkLabel(
    MainFrame_RIGHT_T3, text="نوع هزینه", font=default_font_bold, justify=RIGHT
)
Finance_MngLabel1.grid(row=1, column=1, sticky=E, padx=10, pady=5)

Finance_MngLabel2 = ctk.CTkLabel(
    MainFrame_RIGHT_T3,
    text="مقدار / افـ",
    font=default_font_bold,
    justify=RIGHT
)
Finance_MngLabel2.grid(row=2, column=1, sticky=E, padx=10, pady=5)

Finance_MngLabel3 = ctk.CTkLabel(
    MainFrame_RIGHT_T3, text="تاریخ", font=default_font_bold, justify=RIGHT
)
Finance_MngLabel3.grid(row=3, column=1, sticky=E, padx=10, pady=5)

Finance_MngLabel4 = ctk.CTkLabel(
    MainFrame_RIGHT_T3, text="نوت", font=default_font_bold, justify=RIGHT
)
Finance_MngLabel4.grid(row=4, column=1, sticky=E, padx=10, pady=5)


DAILY_VAL = "روزانه"
MONTHLY_VAL = "ماهانه"
YEARLY_VAL = "سالانه"

RadioTypeFrame = ctk.CTkFrame(MainFrame_RIGHT_T3, corner_radius=5)
RadioTypeFrame.grid(row=0, column=0, padx=10, sticky=E)
FinanceRadio1_1 = ctk.CTkRadioButton(
    RadioTypeFrame,
    variable=REGTYPE_VAR,
    font=default_font_bold1,
    text="روزانه",
    width=30,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    command=RadioFunc1,
    value=DAILY_VAL,
)
FinanceRadio1_1.grid(row=0, column=0, sticky=E, padx=10)
FinanceRadio1_2 = ctk.CTkRadioButton(
    RadioTypeFrame,
    variable=REGTYPE_VAR,
    font=default_font_bold1,
    text="ماهانه",
    width=30,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    command=RadioFunc1,
    value=MONTHLY_VAL,
)
FinanceRadio1_2.grid(row=0, column=1, sticky=E, padx=10)
FinanceRadio1_3 = ctk.CTkRadioButton(
    RadioTypeFrame,
    variable=REGTYPE_VAR,
    font=default_font_bold1,
    text="سالانه",
    width=30,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    command=RadioFunc1,
    value=YEARLY_VAL,
)
FinanceRadio1_3.grid(row=0, column=2, sticky=E, padx=10)

Finance_MngEntry2 = ctk.CTkComboBox(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    values=Type_Values,
    variable=FCOSTTYPE,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry2.grid(row=1, column=0, padx=10, sticky=E)

Finance_MngEntry3 = ctk.CTkEntry(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=FAMOUNT,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry3.grid(row=2, column=0, padx=10, sticky=E)
Finance_MngEntry4 = ctk.CTkEntry(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=FDATE,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry4.grid(row=3, column=0, padx=10, sticky=E)
Finance_MngEntry4.insert(0, DateNow)
Finance_MngEntry5 = ctk.CTkEntry(
    MainFrame_RIGHT_T3,
    width=200,
    font=default_font_bold,
    justify=RIGHT,
    textvariable=FNOTE,
    state=DISABLED,
    border_width=False,
)
Finance_MngEntry5.grid(row=4, column=0, padx=10, sticky=E)





# -------------------- Buttons Tab2 -------------------
FSaveBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=SaveImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="ذخیره",
    width=40,
    font=default_font_bold1,
    command=FSubmit,
)
FSaveBtn1.grid(row=0, column=5, padx=5, pady=5)
FClearBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=ClearImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="پاک کردن",
    width=40,
    font=default_font_bold1,
    command=FClearFunc,
)
FClearBtn1.grid(row=0, column=4, padx=5, pady=5)
FEditBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=EditImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="ویرایش",
    width=40,
    font=default_font_bold1,
)
FEditBtn1.grid(row=0, column=3, padx=5, pady=5)
FBillGenBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=PrintImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="صدور بل",
    width=40,
    font=default_font_bold1,
)
FBillGenBtn1.grid(row=0, column=2, padx=5, pady=5)
FRefreshBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=RefreshImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="تجدید ",
    width=40,
    font=default_font_bold1,
    command=FRef,
)
FRefreshBtn1.grid(row=0, column=1, padx=5, pady=5)
FDeleteBtn1 = ctk.CTkButton(
    MainButFrame1,
    image=DeleteImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="حذف",
    width=40,
    font=default_font_bold1,
    command=FDeleteFunc,
)
FDeleteBtn1.grid(row=0, column=0, padx=5, pady=5)



# -------------------- Buttons Tab3 Frame In Bot -------------------


A_YM_Date = time.strftime("%Y-%m-%d")
A_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
A_Between_EntryFrom.grid(row=0, column=0, sticky=E, padx=10, pady=5)
A_Between_EntryFrom.insert(0, A_YM_Date)


B_YM_Date = time.strftime("%Y-%m-%d")
B_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
B_Between_EntryFrom.grid(row=0, column=1, sticky=E, padx=10, pady=5)
B_Between_EntryFrom.insert(0, B_YM_Date)


C_YM_Date = time.strftime("%Y-%m-%d")
C_Between_EntryFrom = ctk.CTkEntry(
    MainFrame_BOT_L_T3,
    width=100,
    height=20,
    font=default_font_bold1,
    justify=RIGHT
)
C_Between_EntryFrom.grid(row=0, column=2, sticky=E, padx=10, pady=5)
C_Between_EntryFrom.insert(0, C_YM_Date)

# -------------- TreeView Right Title Name --------------


#==============================================
Tree0Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree0Frame.grid(row=1, column=0, padx=10, pady=10, sticky=W)
Tree0 = ttk.Treeview(Tree0Frame, columns=("L1"), selectmode="none", height=1)
Tree0.heading("L1", text="مصارف روزانه", anchor=E)
Tree0.column("#0", stretch=NO, minwidth=0, width=0)
Tree0.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
Tree0.grid()


Tree0.delete(*Tree0.get_children())
Tree0Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
query0 = """
SELECT
    SUM(FAMOUNT) AS SM0
FROM
    FCostTable
WHERE
    FDATE BETWEEN date(?, '-1 month') AND date(?, '+1 day')
    AND FTYPE LIKE '%' || ? || '%'
"""

Tree0Cor = Tree0Conn.execute(
    query0, (B_Between_EntryFrom.get(), B_Between_EntryFrom.get(), "روزانه")
)
fetchTree0 = Tree0Cor.fetchall()
for dataTree0 in fetchTree0:
    try:
        CalcProfit = int(dataTree0[0])
        Tree0.insert("", "end", values=(CalcProfit,))
    except:
        Tree0.insert("", "end", values=("هیچ",))
Tree0Cor.close()
Tree0Conn.close()


#==============================================
Tree1Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree1Frame.grid(row=1, column=1, padx=10, pady=10, sticky=W)
Tree1 = ttk.Treeview(Tree1Frame, columns=("L1"), selectmode="none", height=1)
Tree1.heading("L1", text="مصارف ماهانه", anchor=E)
Tree1.column("#0", stretch=NO, minwidth=0, width=0)
Tree1.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
Tree1.grid()


Tree1.delete(*Tree1.get_children())
Tree1Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
query1 = """
SELECT
    SUM(FAMOUNT) AS SM0
FROM
    FCostTable
WHERE
    FDATE BETWEEN date(?, '-1 month') AND date(?, '+1 day')
    AND FTYPE LIKE '%' || ? || '%'
"""
Tree1Cor = Tree1Conn.execute(
    query1, (B_Between_EntryFrom.get(), B_Between_EntryFrom.get(), "ماهانه")
)
fetchTree1 = Tree1Cor.fetchall()
for dataTree1 in fetchTree1:
    try:
        CalcProfit = int(dataTree1[0])
        Tree1.insert("", "end", values=(CalcProfit,))
    except:
        Tree1.insert("", "end", values=("هیچ",))
Tree1Cor.close()
Tree1Conn.close()



#==============================================
Tree2Frame = ctk.CTkFrame(MainFrame_BOT_L_T3)
Tree2Frame.grid(row=1, column=2, padx=10, pady=10, sticky=W)
Tree2 = ttk.Treeview(
    Tree2Frame,
    columns=("L1"),
    selectmode="none",
    height=1
)
Tree2.heading("L1", text="مصارف سالانه", anchor=E)
Tree2.column("#0", stretch=NO, minwidth=0, width=0)
Tree2.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
Tree2.grid()


Tree2.delete(*Tree2.get_children())
Tree2Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
query2 = """
SELECT
    SUM(FAMOUNT) AS SM00
FROM
    FCostTable
WHERE
    FDATE BETWEEN date(?, '-12 month') AND date(?, '+1 day')
    AND FTYPE LIKE '%' || ? || '%'
"""
Tree2Cor = Tree2Conn.execute(
    query2, (C_Between_EntryFrom.get(), C_Between_EntryFrom.get(), "سالانه")
)
fetchTree2 = Tree2Cor.fetchall()
for dataTree2 in fetchTree2:
    Tree2.insert("", "end", values=(dataTree2))
Tree2Cor.close()
Tree2Conn.close()



#---------- Withdrawing Frame --------------
WithDrawFrm = ctk.CTkFrame(Tab3_Frame_InTop)
WithDrawFrm.place(x=20, y=130)

WithDrawTitle = ctk.CTkLabel(
    master=WithDrawFrm,
    text="برداشتن/افزودن-دخل",
    font=default_font_bold1,
    text_color=BGLIGHTGREEN
)
WithDrawTitle.grid(row=0, column=1, padx=10, pady=10)
DisplayBalanceLbl1 = ctk.CTkLabel(
    master=WithDrawFrm,
    text="",
    font=default_font_bold,
    text_color=BGORANGE
)
DisplayBalanceLbl1.grid(row=0, column=0, padx=10, pady=10)

WithDrawLbl1 = ctk.CTkLabel(
    master=WithDrawFrm,
    text="مقدار/افغانی",
    font=default_font_bold
)
WithDrawLbl1.grid(row=1, column=1, padx=10, pady=10)

WithDrawEnt1 = ctk.CTkEntry(
    master=WithDrawFrm,
    placeholder_text="مقدار را وارد کنید",
    font=default_font_bold,
    justify=RIGHT
)
WithDrawEnt1.grid(row=1, column=0, padx=10, pady=10)

WithDrawBtn = ctk.CTkButton(
    master=WithDrawFrm,
    image=WithdrawImg,
    text="برداشتن",
    font=default_font_bold,
    command=WithDrawFunc
)
WithDrawBtn.grid(row=2, column=0, padx=10, pady=10)
DepostBtn = ctk.CTkButton(
    master=WithDrawFrm,
    image=DepositImg,
    text="افزودن",
    font=default_font_bold,
    command=DepositFunc
)
DepostBtn.grid(row=2, column=1, padx=10, pady=10)
# -------------- TreeView Left Title Name --------------


# ================== apart from bottom  ======================
Ttl_01_lbl = ctk.CTkLabel(
    master=Tab3_Frame_InBot,
    text="",
    text_color=BGYELLOW,
    font=default_font_bold
)
Ttl_01_lbl.place(x=0, y=0)

TreeVTitle7 = ctk.CTkLabel(
    Tab3_Frame_InBot,
    text="همه هزینه ها",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
    justify=RIGHT,
)
TreeVTitle7.grid(row=0, column=2, sticky=E, padx=20, pady=10)


Tree3Frame = ctk.CTkFrame(Tab3_Frame_InBot)
Tree3Frame.grid(row=1, column=2, padx=5, sticky=W)
Tree3 = ttk.Treeview(
    Tree3Frame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6"),
    selectmode="browse",
    height=8,
)
Tree3.heading("L1", text="نوت", anchor=E)
Tree3.heading("L2", text="تاریخ", anchor=E)
Tree3.heading("L3", text="مقدار / اف", anchor=E)
Tree3.heading("L4", text="نوع هزینه", anchor=E)
Tree3.heading("L5", text="نوع ثبت", anchor=E)
Tree3.heading("L6", text="ID", anchor=E)

Tree3.column("#0", stretch=NO, minwidth=0, width=0)
Tree3.column("#1", stretch=NO, minwidth=0, width=200, anchor=E)
Tree3.column("#2", stretch=NO, minwidth=0, width=130, anchor=E)
Tree3.column("#3", stretch=NO, minwidth=0, width=100, anchor=E)
Tree3.column("#4", stretch=NO, minwidth=0, width=130, anchor=E)
Tree3.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
Tree3.column("#6", stretch=NO, minwidth=0, width=62, anchor=E)
Tree3.grid(padx=0, pady=0)


Tree3.delete(*Tree3.get_children())
Tree3Conn = sqlite3.connect("C:/My_Store/StoreDb.db")
Tree3Cor = Tree3Conn.execute(
    """
    SELECT
    FNOTE,
    FDATE,
    FAMOUNT,
    FCOSTTYPE,
    FTYPE,
    FTID
    FROM FCostTable
    ORDER BY FTID DESC
    """
)
fetchTree3 = Tree3Cor.fetchall()
for dataTree3 in fetchTree3:
    Tree3.insert("", "end", values=(dataTree3))
    #----- Totaling ---------
    cur_01 = Tree3Conn.execute(
        """
        SELECT
        SUM(FAMOUNT)
        FROM FCostTable
        """
    )
    fch_01 = cur_01.fetchall()
    for dt_01 in fch_01:
        dt_1_1 = dt_01[0]
        Ttl_01_lbl.configure(text=f"{dt_1_1} :مجموعه هزینه ها")
    cur_01.close()
    #------ End of totaling --------
Tree3Cor.close()
Tree3Conn.close()



#========================= Tab 3 ============================
#========================= Tab 3 ============================
#========================= Tab 3 ============================
#========================= Tab 3 ============================
#========================= Tab 3 ============================
#========================= Tab 3 ============================
#========================= Tab 3 ============================

LDRLENDER = StringVar()
LDRBEHALF = StringVar()
LDRAMOUNT = StringVar()
LDRDATE = StringVar()
LDRNOTE = StringVar()

DBTDEBTOR = StringVar()
DBTBEHALF = StringVar()
DBTAMOUNT = StringVar()
DBDATE = StringVar()
DBTNOTE = StringVar()


# ========= Debtor Funcs ================
# ========= Debtor Funcs ================
# ========= Debtor Funcs ================


def DebSubmit():
    DebConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    DebCur = DebConn.cursor()
    if DebtorEntry1.get() == "" or DebtorEntry2.get() == "" or DebtorEntry3.get() == "":
        messagebox.showerror(
            "ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود."
        )
    else:
        DebCur.execute(
            f"insert into DebtorTable (DBTDEBTOR,DBTBEHALF,DBTAMOUNT,DBDATE,\
            DBTNOTE) values ('{DBTDEBTOR.get()}','{DBTBEHALF.get()}',\
            '{DBTAMOUNT.get()}','{DBDATE.get()}','{DBTNOTE.get()}')"
        )
    DebConn.commit()
    DebConn.close()
    DebtorEntry1.delete(0, END)
    DebtorEntry2.delete(0, END)
    DebtorEntry3.delete(0, END)
    DebtorEntry4.delete(0, END)
    DebtorEntry4.insert(0, DateNow)
    DebtorEntry5.delete(0, END)
    DebtorEntry1.focus()
    DebRef()


def DebRef():
    TreeDeb.delete(*TreeDeb.get_children())
    TreeDebConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeDebCor = TreeDebConn.execute(
        """
        SELECT
        DBTNOTE,
        DBDATE,
        DBTAMOUNT,
        DBTBEHALF,
        DBTDEBTOR,
        DBTID
        FROM DebtorTable
        ORDER BY DBTID DESC
        """
    )
    fetchTreeDeb = TreeDebCor.fetchall()
    for dataTreeDeb in fetchTreeDeb:
        TreeDeb.insert("", "end", values=(dataTreeDeb))
    TreeDebCor.close()
    TreeDebConn.close()

    # -==========================================
    SumTreeDeb.delete(*SumTreeDeb.get_children())
    SumTreeDebConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    SumTreeDebCor = SumTreeDebConn.execute(
        """
        SELECT
        SUM(DBTAMOUNT) 
        FROM DebtorTable
        """
    )
    ftsl = SumTreeDebCor.fetchall()
    for dtsl in ftsl:
        SumTreeDeb.insert("", "end", values=(dtsl))
    SumTreeDebCor.close()
    SumTreeDebConn.close()


def DebClear():
    DebtorEntry1.delete(0, END)
    DebtorEntry2.delete(0, END)
    DebtorEntry3.delete(0, END)
    DebtorEntry4.delete(0, END)
    DebtorEntry4.insert(0, DateNow)
    DebtorEntry5.delete(0, END)
    DebtorEntry1.focus()


def DebDelete():
    DebSelected_item = TreeDeb.selection()
    if DebSelected_item:
        for DebSelected_item in TreeDeb.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM DebtorTable WHERE DBTID=?",
                    (TreeDeb.set(DebSelected_item, "#6"),),
                )
                conn.commit()
                TreeDeb.delete(DebSelected_item)
                conn.close()
                DebRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")



def RefundDebtFunc():
    if RefundEnt1.get() == "":
        messagebox.showerror("Space4", "لطفاً مقدار را وارد کنید")
    else:
        if RefundEnt1.get() != "":
            for selected_item in TreeDeb.selection():
                dt1 = RefundEnt1.get()
                conn = sqlite3.connect("C:/My_Store/StoreDb.db")
                cur = conn.cursor()
                conn1 = cur.execute(
                    "SELECT DBTAMOUNT FROM DebtorTable WHERE DBTID=?",
                    (TreeDeb.set(selected_item, "#6"),),
                )
                fetch = cur.fetchall()
                for data in fetch:
                    data0 = data[0]
                    addm = int(data0) - int(dt1)

                    cur.execute(
                        "UPDATE DebtorTable SET DBTAMOUNT=? WHERE DBTID=?",
                        (addm, TreeDeb.set(selected_item, "#6")),
                    )

                    RefundEnt1.delete(0, END)
                    messagebox.showinfo(
                        "Space4 Software", "! عملیه پرداخت موفقانه انجام شد"
                    )
                    conn.commit()
                    conn1.close()
                    conn.close()
                    root.after(500, DebRef)

        else:
            messagebox.showinfo("اوووه", "دریافت ثبت نشد")


# ========= Lender Funcs ================
# ========= Lender Funcs ================
# ========= Lender Funcs ================


def LenSubmit():
    LenConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    LenCur = LenConn.cursor()
    if LenderEntry1.get() == "" or LenderEntry2.get() == "" or LenderEntry3.get() == "":
        messagebox.showerror(
            "ببخشید", "الزامی است که ورودی ها قبل از ذخیره پر شود."
        )
    else:
        LenCur.execute(
            f"insert into LenderTable (LDRLENDER,LDRBEHALF,LDRAMOUNT,LDRDATE,\
            LDRNOTE) values ('{LDRLENDER.get()}','{LDRBEHALF.get()}',\
            '{LDRAMOUNT.get()}','{LDRDATE.get()}','{LDRNOTE.get()}')"
        )
    LenConn.commit()
    LenConn.close()
    LenderEntry4.delete(0, END)
    LenderEntry1.delete(0, END)
    LenderEntry2.delete(0, END)
    LenderEntry3.delete(0, END)
    LenderEntry4.insert(0, DateNow)
    LenderEntry5.delete(0, END)
    LenderEntry1.focus()
    LenRef()


def LenRef():
    TreeLen.delete(*TreeLen.get_children())
    TreeLenConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeLenCor = TreeLenConn.execute(
        """
        SELECT
        LDRNOTE,
        LDRDATE,
        LDRAMOUNT,
        LDRBEHALF,
        LDRLENDER,
        LDRID
        FROM LenderTable
        ORDER BY LDRID DESC
        """
    )
    fetchTreeLen = TreeLenCor.fetchall()
    for dataTreeLen in fetchTreeLen:
        TreeLen.insert("", "end", values=(dataTreeLen))
    TreeLenCor.close()
    TreeLenConn.close()

    # =================================
    TreeSumLen.delete(*TreeSumLen.get_children())
    TreeSumLenConn = sqlite3.connect("C:/My_Store/StoreDb.db")
    TreeSumLenCor = TreeSumLenConn.execute(
        """
        SELECT
        SUM(LDRAMOUNT) 
        FROM LenderTable
        """
    )
    ftsl = TreeSumLenCor.fetchall()
    for dtsl in ftsl:
        TreeSumLen.insert("", "end", values=(dtsl))
    TreeSumLenCor.close()
    TreeSumLenConn.close()


def LenClear():
    LenderEntry4.delete(0, END)
    LenderEntry1.delete(0, END)
    LenderEntry2.delete(0, END)
    LenderEntry3.delete(0, END)
    LenderEntry4.Insert(0, DateNow)
    LenderEntry5.delete(0, END)
    LenderEntry1.focus()


def LenDelete():
    LenSelected_item = TreeLen.selection()
    if LenSelected_item:
        for LenSelected_item in TreeLen.selection():
            conn = sqlite3.connect("C:/My_Store/StoreDb.db")
            cur = conn.cursor()
            messageDelete = messagebox.askyesno(
                "هشدار", "؟آیا میخواهید این داده را حذف کنید"
            )
            if messageDelete > 0:
                cur.execute(
                    "DELETE FROM LenderTable WHERE LDRID=?",
                    (TreeLen.set(LenSelected_item, "#6"),),
                )
                conn.commit()
                TreeLen.delete(LenSelected_item)
                conn.close()
                LenRef()
    else:
        messagebox.showwarning("Space4", "ریکارد انتخاب نشده")



def PayLenFunc():
    if PayEnt1.get() == "":
        messagebox.showerror("Space4", "لطفاً مقدار را وارد کنید")
    else:
        if PayEnt1.get() != "":
            for selected_item in TreeLen.selection():
                dt1 = PayEnt1.get()
                conn = sqlite3.connect("C:/My_Store/StoreDb.db")
                cur = conn.cursor()
                conn1 = cur.execute(
                    "SELECT LDRAMOUNT FROM LenderTable WHERE LDRID=?",
                    (TreeLen.set(selected_item, "#6"),),
                )
                fetch = cur.fetchall()
                for data in fetch:
                    data0 = data[0]
                    addm = int(data0) - int(dt1)

                    cur.execute(
                        "UPDATE LenderTable SET LDRAMOUNT=? WHERE LDRID=?",
                        (addm, TreeLen.set(selected_item, "#6")),
                    )

                    PayEnt1.delete(0, END)
                    messagebox.showinfo(
                        "Space4 Software", "! عملیه پرداخت موفقانه انجام شد"
                    )
                    conn.commit()
                    conn1.close()
                    conn.close()
                    root.after(500, LenRef)

        else:
            messagebox.showinfo("اوووه", "ثبت نشدن پرداخت . از بروز مشکل تخنیکی برنامه\n\
                ارتباط با سازنده: hcrgroup.info@gmail.com")
# ========== Frames Lender ===========


DebtorFrame_Top_R = ctk.CTkFrame(tab3)
DebtorFrame_Top_R.grid(row=0, column=3, padx=5, pady=5, sticky=NE)
DebtorFrame_CEN_R = ctk.CTkFrame(tab3)
DebtorFrame_CEN_R.grid(row=0, column=2, padx=5, pady=5, sticky=SE)
DebtorFrame_Bot_R = ctk.CTkFrame(tab3)
DebtorFrame_Bot_R.grid(
    row=1,
    column=1,
    padx=5,
    pady=5,
    sticky=NE,
    columnspan=4
)


LenderFrame_Top_L = ctk.CTkFrame(tab3)
LenderFrame_Top_L.grid(row=0, column=1, padx=5, pady=5, sticky=NE)
LenderFrame_CEN_L = ctk.CTkFrame(tab3)
LenderFrame_CEN_L.grid(row=0, column=0, padx=5, pady=5, sticky=SE)
LenderFrame_Bot_L = ctk.CTkFrame(tab3)
LenderFrame_Bot_L.grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky=NE,
    columnspan=2
)


# ======= Debtor Labels ============

DebtorLbl0 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="بدهکار",
    font=default_font_bold,
    text_color=BGLIGHTGREEN
)
DebtorLbl0.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl1 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="نام",
    font=default_font_bold,
)
DebtorLbl1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl2 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="بابت",
    font=default_font_bold,
)
DebtorLbl2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl3 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="مقدار",
    font=default_font_bold,
)
DebtorLbl3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl4 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="تاریخ",
    font=default_font_bold,
)
DebtorLbl4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)

DebtorLbl5 = ctk.CTkLabel(
    master=DebtorFrame_Top_R,
    text="نوت",
    font=default_font_bold,
)
DebtorLbl5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)


# ================ Entry Part ===============
DebtorEntry1 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTDEBTOR,
)
DebtorEntry1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry2 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTBEHALF,
)
DebtorEntry2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry3 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTAMOUNT,
)
DebtorEntry3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

DebtorEntry4 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBDATE,
)
DebtorEntry4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
DebtorEntry4.insert(0, DateNow)

DebtorEntry5 = ctk.CTkEntry(
    master=DebtorFrame_Top_R,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=DBTNOTE,
)
DebtorEntry5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)


# ======== Debtor Buttons ===============

DebSaveBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=SaveImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="ذخیره",
    width=40,
    font=default_font_bold1,
    command=DebSubmit,
)
DebSaveBtn1.grid(row=0, column=3, padx=7, pady=2)
DebClearBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=ClearImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="پاک کردن",
    width=40,
    font=default_font_bold1,
    command=DebClear,
)
DebClearBtn1.grid(row=0, column=2, padx=7, pady=2)
DebRefreshBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=RefreshImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="تجدید ",
    width=40,
    font=default_font_bold1,
    command=DebRef,
)
DebRefreshBtn1.grid(row=0, column=1, padx=7, pady=2)
DebDeleteBtn1 = ctk.CTkButton(
    DebtorFrame_CEN_R,
    image=DeleteImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="حذف",
    width=40,
    font=default_font_bold1,
    command=DebDelete,
)
DebDeleteBtn1.grid(row=0, column=0, padx=7, pady=2)



# ---------- Refund -------------
# ---------- Refund -------------
# ---------- Refund -------------

RefundFrame1 = ctk.CTkFrame(
    DebtorFrame_Bot_R,
    corner_radius=5,
    fg_color=CTKDARK_FRM
    )
RefundFrame1.place(x=150,y=10)

RefundBtn1 = ctk.CTkButton(
    master=RefundFrame1,
    text="تایید",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=RefundDebtFunc
    )
RefundBtn1.grid(row=0,column=0,sticky=NE,padx=10)

RefundEnt1 = ctk.CTkEntry(
    master=RefundFrame1,
    placeholder_text="درج مقدار دریافتی",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
RefundEnt1.grid(row=0,column=1,sticky=NE,padx=2)


# ============= Debtor Treeview ============

TreeDebLbl = ctk.CTkLabel(
    master=DebtorFrame_Bot_R,
    text="لیست بدهکاران",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
    justify=RIGHT,
)
TreeDebLbl.grid(row=0, column=0, padx=20, pady=10, sticky=NE)


TreeDebFrame = ctk.CTkFrame(DebtorFrame_Bot_R)
TreeDebFrame.grid(row=1, column=0, padx=5, sticky=NE)
TreeDeb = ttk.Treeview(
    TreeDebFrame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6"),
    selectmode="browse",
    height=11,
)
TreeDeb.heading("L1", text="نوت", anchor=E)
TreeDeb.heading("L2", text="تاریخ", anchor=E)
TreeDeb.heading("L3", text="مقدار", anchor=E)
TreeDeb.heading("L4", text="بابت", anchor=E)
TreeDeb.heading("L5", text="نام", anchor=E)
TreeDeb.heading("L6", text="ID", anchor=E)

TreeDeb.column("#0", stretch=NO, minwidth=0, width=0)
TreeDeb.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeDeb.column("#2", stretch=NO, minwidth=0, width=90, anchor=E)
TreeDeb.column("#3", stretch=NO, minwidth=0, width=80, anchor=E)
TreeDeb.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeDeb.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeDeb.column("#6", stretch=NO, minwidth=0, width=50, anchor=E)
TreeDeb.grid(padx=0, pady=0)


TreeDeb.delete(*TreeDeb.get_children())
TreeDebConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeDebCor = TreeDebConn.execute(
    """
    SELECT
    DBTNOTE,
    DBDATE,
    DBTAMOUNT,
    DBTBEHALF,
    DBTDEBTOR,
    DBTID
    FROM DebtorTable
    ORDER BY DBTID DESC
    """
)
fetchTreeDeb = TreeDebCor.fetchall()
for dataTreeDeb in fetchTreeDeb:
    TreeDeb.insert("", "end", values=(dataTreeDeb))
TreeDebCor.close()
TreeDebConn.close()


# ======== Mini Sum Debtor Tree =============
SumDebTree = ctk.CTkFrame(tab3)
SumDebTree.place(x=590, y=10)
SumTreeDeb = ttk.Treeview(SumDebTree, columns=("L1"), selectmode=None, height=1)
SumTreeDeb.heading("L1", text="باقی از دوکان", anchor=E)
SumTreeDeb.column("#0", stretch=NO, minwidth=0, width=0)
SumTreeDeb.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
SumTreeDeb.grid()

SumTreeDeb.delete(*SumTreeDeb.get_children())
SumTreeDebConn = sqlite3.connect("C:/My_Store/StoreDb.db")
SumTreeDebCor = SumTreeDebConn.execute(
    """
    SELECT
    SUM(DBTAMOUNT) 
    FROM DebtorTable
    """
)
ftsl = SumTreeDebCor.fetchall()
for dtsl in ftsl:
    SumTreeDeb.insert("", "end", values=(dtsl))
SumTreeDebCor.close()
SumTreeDebConn.close()



def PersonSearchFunc1():
    if SearchEntDeb1.get() != "":
        TreeDeb.delete(*TreeDeb.get_children())
        Sconn = sqlite3.connect("C:/My_Store/StoreDb.db")
        Scur = Sconn.execute(
            """
            SELECT
            DBTNOTE,
            DBDATE,
            DBTAMOUNT,
            DBTBEHALF,
            DBTDEBTOR,
            DBTID
            FROM DebtorTable
            WHERE DBTDEBTOR LIKE?
            """,
            ("%" + str(SearchEntDeb1.get()) + "%",),
        )
        Sfetch = Scur.fetchall()
        for Sdata in Sfetch:
            TreeDeb.insert("", "end", values=(Sdata))

            #----- Sum Cur Search --------------------
            SumTreeDeb.delete(*SumTreeDeb.get_children())
            Scur1 = Sconn.execute(
                """
                SELECT
                SUM(DBTAMOUNT)
                FROM DebtorTable
                WHERE DBTDEBTOR LIKE?
                """,
                ("%" + str(SearchEntDeb1.get()) + "%",),
            )
            Sfetch1 = Scur1.fetchall()
            for Sdata1 in Sfetch1:
                SumTreeDeb.insert("", "end", values=(Sdata1))
    else:
        messagebox.showinfo("Space4", "لطفاً نام شخص مرود نظر را وارد کنید")


def PersonSearchFunc2():
    if SearchEntDeb2.get() != "":
        TreeLen.delete(*TreeLen.get_children())
        Sconn = sqlite3.connect("C:/My_Store/StoreDb.db")
        Scur = Sconn.execute(
            """
            SELECT
            LDRNOTE,
            LDRDATE,
            LDRAMOUNT,
            LDRBEHALF,
            LDRLENDER,
            LDRID
            FROM LenderTable
            WHERE LDRLENDER LIKE?
            """,
            ("%" + str(SearchEntDeb2.get()) + "%",),
        )
        Sfetch = Scur.fetchall()
        for Sdata in Sfetch:
            TreeLen.insert("", "end", values=(Sdata))

            #----- Sum Cur Search --------------------
            TreeSumLen.delete(*TreeSumLen.get_children())
            Scur1 = Sconn.execute(
                """
                SELECT
                SUM(LDRAMOUNT)
                FROM LenderTable
                WHERE LDRLENDER LIKE?
                """,
                ("%" + str(SearchEntDeb2.get()) + "%",),
            )
            Sfetch1 = Scur1.fetchall()
            for Sdata1 in Sfetch1:
                TreeSumLen.insert("", "end", values=(Sdata1))
    else:
        messagebox.showinfo("Space4", "لطفاً نام شخص مرود نظر را وارد کنید")



# ========= Lender Part ============
# ========= Lender Part ===========


# ======= Lender Labels ============

LenderLbl0 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="طلبکار",
    font=default_font_bold,
    text_color=BGLIGHTGREEN
)
LenderLbl0.grid(row=0, column=1, padx=5, pady=5, sticky=NE)

LenderLbl1 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="نام",
    font=default_font_bold,
)
LenderLbl1.grid(row=1, column=1, padx=5, pady=5, sticky=NE)

LenderLbl2 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="بابت",
    font=default_font_bold,
)
LenderLbl2.grid(row=2, column=1, padx=5, pady=5, sticky=NE)

LenderLbl3 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="مقدار",
    font=default_font_bold,
)
LenderLbl3.grid(row=3, column=1, padx=5, pady=5, sticky=NE)

LenderLbl4 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="تاریخ",
    font=default_font_bold,
)
LenderLbl4.grid(row=4, column=1, padx=5, pady=5, sticky=NE)

LenderLbl5 = ctk.CTkLabel(
    master=LenderFrame_Top_L,
    text="نوت",
    font=default_font_bold,
)
LenderLbl5.grid(row=5, column=1, padx=5, pady=5, sticky=NE)

# ================ Entry Part ===============
LenderEntry1 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRLENDER,
)
LenderEntry1.grid(row=1, column=0, padx=5, pady=5, sticky=NE)

LenderEntry2 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRBEHALF,
)
LenderEntry2.grid(row=2, column=0, padx=5, pady=5, sticky=NE)

LenderEntry3 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRAMOUNT,
)
LenderEntry3.grid(row=3, column=0, padx=5, pady=5, sticky=NE)

LenderEntry4 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRDATE,
)
LenderEntry4.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
LenderEntry4.insert(0, DateNow)

LenderEntry5 = ctk.CTkEntry(
    master=LenderFrame_Top_L,
    font=default_font_bold,
    width=200,
    justify=RIGHT,
    textvariable=LDRNOTE,
)
LenderEntry5.grid(row=5, column=0, padx=5, pady=5, sticky=NE)


# ======== Lender Buttons ===============

LenSaveBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=SaveImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="ذخیره",
    width=40,
    font=default_font_bold1,
    command=LenSubmit,
)
LenSaveBtn1.grid(row=0, column=3, padx=7, pady=2)
LenClearBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=ClearImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="پاک کردن",
    width=40,
    font=default_font_bold1,
    command=LenClear,
)
LenClearBtn1.grid(row=0, column=2, padx=7, pady=2)
LenRefreshBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=RefreshImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="تجدید ",
    width=40,
    font=default_font_bold1,
    command=LenRef,
)
LenRefreshBtn1.grid(row=0, column=1, padx=7, pady=2)
LenDeleteBtn1 = ctk.CTkButton(
    LenderFrame_CEN_L,
    image=DeleteImg,
    compound=TOP,
    hover_color=BGLIGHTGREEN,
    fg_color=TEXT_COL_1,
    text="حذف",
    width=40,
    font=default_font_bold1,
    command=LenDelete,
)
LenDeleteBtn1.grid(row=0, column=0, padx=7, pady=2)



# ---------- Pay -------------
# ---------- Pay -------------
# ---------- Pay -------------
PayFrame1 = ctk.CTkFrame(
    LenderFrame_Bot_L,
    corner_radius=5,
    fg_color=CTKDARK_FRM
    )
PayFrame1.place(x=140,y=10)

PayBtn1 = ctk.CTkButton(
    master=PayFrame1,
    text="تایید",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=PayLenFunc
    )
PayBtn1.grid(row=0,column=0,sticky=NE,padx=10)

PayEnt1 = ctk.CTkEntry(
    master=PayFrame1,
    placeholder_text="درج مقدار پرداختی",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
PayEnt1.grid(row=0,column=1,sticky=NE,padx=2)
# ============= Lender Treeview ============

TreeLenLbl = ctk.CTkLabel(
    master=LenderFrame_Bot_L,
    text="لیست طلب کاران",
    font=default_font_bold,
    text_color=BGLIGHTGREEN,
    justify=RIGHT,
)
TreeLenLbl.grid(row=0, column=0, padx=20, pady=10, sticky=NE)


TreeLenFrame = ctk.CTkFrame(LenderFrame_Bot_L)
TreeLenFrame.grid(row=1, column=0, padx=5, sticky=NE)
TreeLen = ttk.Treeview(
    TreeLenFrame,
    columns=("L1", "L2", "L3", "L4", "L5", "L6"),
    selectmode="browse",
    height=11,
)
TreeLen.heading("L1", text="نوت", anchor=E)
TreeLen.heading("L2", text="تاریخ", anchor=E)
TreeLen.heading("L3", text="مقدار", anchor=E)
TreeLen.heading("L4", text="بابت", anchor=E)
TreeLen.heading("L5", text="نام", anchor=E)
TreeLen.heading("L6", text="ID", anchor=E)

TreeLen.column("#0", stretch=NO, minwidth=0, width=0)
TreeLen.column("#1", stretch=NO, minwidth=0, width=100, anchor=E)
TreeLen.column("#2", stretch=NO, minwidth=0, width=90, anchor=E)
TreeLen.column("#3", stretch=NO, minwidth=0, width=80, anchor=E)
TreeLen.column("#4", stretch=NO, minwidth=0, width=100, anchor=E)
TreeLen.column("#5", stretch=NO, minwidth=0, width=100, anchor=E)
TreeLen.column("#6", stretch=NO, minwidth=0, width=50, anchor=E)
TreeLen.grid(padx=0, pady=0)


TreeLen.delete(*TreeLen.get_children())
TreeLenConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeLenCor = TreeLenConn.execute(
    """
    SELECT
    LDRNOTE,
    LDRDATE,
    LDRAMOUNT,
    LDRBEHALF,
    LDRLENDER,
    LDRID
    FROM LenderTable
    ORDER BY LDRID DESC
    """
)
fetchTreeLen = TreeLenCor.fetchall()
for dataTreeLen in fetchTreeLen:
    TreeLen.insert("", "end", values=(dataTreeLen))
TreeLenCor.close()
TreeLenConn.close()


# ======== Mini Sum Lender Tree =============
SumLenTree = ctk.CTkFrame(tab3)
SumLenTree.place(x=80, y=10)
TreeSumLen = ttk.Treeview(
    SumLenTree,
    columns=("L1"),
    selectmode=None,
    height=1
)
TreeSumLen.heading("L1", text="باقیات خود دوکان", anchor=E)
TreeSumLen.column("#0", stretch=NO, minwidth=0, width=0)
TreeSumLen.column("#1", stretch=NO, minwidth=0, width=120, anchor=E)
TreeSumLen.grid()

TreeSumLen.delete(*TreeSumLen.get_children())
TreeSumLenConn = sqlite3.connect("C:/My_Store/StoreDb.db")
TreeSumLenCor = TreeSumLenConn.execute(
    """
    SELECT
    SUM(LDRAMOUNT) 
    FROM LenderTable
    """
)
ftsl = TreeSumLenCor.fetchall()
for dtsl in ftsl:
    TreeSumLen.insert("", "end", values=(dtsl))
TreeSumLenCor.close()
TreeSumLenConn.close()


# ---------- Search 1 -------------
# ---------- Search 1 -------------
SearchDeb1Frm = ctk.CTkFrame(
    tab3,
    corner_radius=5,
    fg_color=CTKDARK_FRM
    )
SearchDeb1Frm.place(x=540, y=80)

SearchBtnDeb1 = ctk.CTkButton(
    master=SearchDeb1Frm,
    text="جستجو",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=PersonSearchFunc1
    )
SearchBtnDeb1.grid(row=0,column=0,sticky=NE,padx=10)

SearchEntDeb1 = ctk.CTkEntry(
    master=SearchDeb1Frm,
    placeholder_text="نام قرضدار را وارد کنید",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
SearchEntDeb1.grid(row=0,column=1,sticky=NE,padx=2)



# ---------- Search 2 -------------
# ---------- Search 2 -------------
SearchDeb2Frm = ctk.CTkFrame(
    tab3,
    corner_radius=5,
    fg_color=CTKDARK_FRM
    )
SearchDeb2Frm.place(x=20, y=80)

SearchBtnDeb2 = ctk.CTkButton(
    master=SearchDeb2Frm,
    text="جستجو",
    font=default_font_bold,
    width=70,
    fg_color=TEXT_COL_1,
    command=PersonSearchFunc2
    )
SearchBtnDeb2.grid(row=0,column=0,sticky=NE,padx=10)

SearchEntDeb2 = ctk.CTkEntry(
    master=SearchDeb2Frm,
    placeholder_text="نام گیرنده را وارد کنید",
    justify=RIGHT,
    font=default_font_bold,
    width=150
    )
SearchEntDeb2.grid(row=0,column=1,sticky=NE,padx=2)




#========================= Tab 4 ============================
#========================= Tab 4 ============================
#========================= Tab 4 ============================
#========================= Tab 4 ============================
#========================= Tab 4 ============================
#========================= Tab 4 ============================
#========================= Tab 4 ============================





def RecallGraphFunc1():
    plot_income_and_expenses_graph()

def fetch_income_data(year):
    G_conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    G_query = """
    SELECT
        strftime('%m', SOLDDATE) AS G_date,
        SUM(SOLDPRICE * SOLDQTT)
    FROM StorageSoldTable
    WHERE strftime('%Y', SOLDDATE) = ?
    GROUP BY G_date
    """
    G_cur = G_conn.execute(G_query, (year,))
    G_fetch = G_cur.fetchall()
    income_per_month = {}
    income = [0] * 12
    for row in G_fetch:
        month = row[0]
        income_value = row[1]
        month_index = int(month) - 1
        income[month_index] = income_value
        income_per_month[month] = income_value
    G_cur.close()
    G_conn.close()
    return income_per_month, income


def fetch_expenses_data(year):
    Ex_conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    Ex_exQuery = """
    SELECT
        strftime('%m', FDATE) AS Ex_date,
        SUM(FAMOUNT) AS EXSUM
    FROM FCostTable
    WHERE strftime('%Y', FDATE) = ?
    GROUP BY Ex_date
    """
    Ex_cur = Ex_conn.execute(Ex_exQuery, (year,))
    Ex_fetch = Ex_cur.fetchall()
    expenses_per_month = {}
    expenses = [0] * 12  # Initialize expenses list with zeros for all months
    for row in Ex_fetch:
        month = row[0]
        expenses_value = row[1]
        month_index = int(month) - 1
        expenses[month_index] = expenses_value
        expenses_per_month[month] = expenses_value
    Ex_cur.close()
    Ex_conn.close()
    return expenses_per_month, expenses


def fetch_profit_data(year):
    Pf_conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    Pf_cur = Pf_conn.cursor()
    Pf_exQuery = """
    SELECT
    strftime('%m', CSHDATE) AS Month,
    SUM((CSHAMOUNT - CSHREALPRICE) * CSHQTTY)
    FROM CashTable
    WHERE strftime('%Y', CSHDATE) = ?
    GROUP BY Month
    """
    Pf_cur.execute(Pf_exQuery, (year,))
    Pf_fetch = Pf_cur.fetchall()
    profit_per_month = {}
    profit = [0] * 12  # Initialize profit list with zeros for all months
    for row in Pf_fetch:
        month = row[0]
        SUM1 = row[1]
        try:
            profit_value = int(SUM1)
            month_index = int(month) - 1
            profit[month_index] = profit_value
            profit_per_month[month] = profit_value
        except:
            messagebox.showerror("Space4", "عاید خالص در دسترس نیست")

    Pf_cur.close()
    Pf_conn.close()
    return profit_per_month, profit


def plot_income_and_expenses_graph(year):
    income_per_month, income = fetch_income_data(year)
    expenses_per_month, expenses = fetch_expenses_data(year)
    profit_per_month, profit = fetch_profit_data(year)

    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    fig = Figure(figsize=(12, 7), dpi=80, facecolor="#333333")
    plot = fig.add_subplot(111)
    plot.spines["bottom"].set_color("orange")
    plot.spines["top"].set_color("orange")
    plot.spines["left"].set_color("red")
    plot.spines["right"].set_color("orange")
    plot.xaxis.label.set_color("yellow")
    plot.yaxis.label.set_color("yellow")
    plot.tick_params(axis="x", colors="white")
    plot.tick_params(axis="y", colors="white")
    plot.title.set_color("white")
    plot.set_facecolor("#333333")
    # Plot income
    # plot.bar(months, income,color="lightgray")
    plot.plot(
        months,
        income,
        color="green",
        marker="^",
        markersize=8,
        markerfacecolor="lightgreen",
    )
    # Plot expenses
    plot.plot(
        months,
        expenses,
        color=BGRED,
        marker="v",
        markersize=8,
        markerfacecolor=BGORANGE,
    )
    # Plot Profits
    plot.plot(
        months,
        profit,
        color=BGBLUE,
        marker="o",
        markersize=8,
        markerfacecolor=BGWHITE,
    )
    plot.set_xlabel(
        "A long the year",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.set_ylabel(
        "Amount per / Af",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.set_title(
        f"Income and Expenses Per Month - {YCGE.get()}",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.legend(labels=["Income", "Expense"])

    canvas = FigureCanvasTkAgg(fig, master=GraphFrame_TOP_R_1)
    canvas.draw()
    canvas.get_tk_widget().pack(anchor=W)


#-------------- Separator--------------
GraphFrame_TOP_R_1 = ctk.CTkFrame(tab4)
GraphFrame_TOP_R_1.grid(row=0, column=0, padx=10, pady=10, sticky=NE)
# ------------- Graphs ----------------
# ------------- Graphs ----------------
# ------------- Graphs ----------------


YCGE = StringVar()


def fetch_income_data():
    G_conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    G_query = """
    SELECT
        strftime('%m', SOLDDATE) AS G_date,
        SUM(SOLDPRICE * SOLDQTT)
    FROM StorageSoldTable
    WHERE strftime('%Y', SOLDDATE) = ?
    GROUP BY G_date
    """
    G_cur = G_conn.execute(G_query, (YCGE.get(),))
    G_fetch = G_cur.fetchall()
    income_per_month = {}
    income = [0] * 12
    for row in G_fetch:
        month = row[0]
        income_value = row[1]
        month_index = int(month) - 1
        income[month_index] = income_value
        income_per_month[month] = income_value
    G_cur.close()
    G_conn.close()
    return income_per_month, income


def fetch_expenses_data():
    Ex_conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    Ex_exQuery = """
    SELECT
        strftime('%m', FDATE) AS Ex_date,
        SUM(FAMOUNT) AS EXSUM
    FROM FCostTable
    WHERE strftime('%Y', FDATE) = ?
    GROUP BY Ex_date
    """
    Ex_cur = Ex_conn.execute(Ex_exQuery, (YCGE.get(),))
    Ex_fetch = Ex_cur.fetchall()
    expenses_per_month = {}
    expenses = [0] * 12  # Initialize expenses list with zeros for all months
    for row in Ex_fetch:
        month = row[0]
        expenses_value = row[1]
        month_index = int(month) - 1
        expenses[month_index] = expenses_value
        expenses_per_month[month] = expenses_value
    Ex_cur.close()
    Ex_conn.close()
    return expenses_per_month, expenses


# ------------- Profit ----------------
def fetch_profit_data():
    Pf_conn = sqlite3.connect("C:/My_Store/StoreDb.db")
    Pf_cur = Pf_conn.cursor()
    Pf_exQuery = """
    SELECT
    strftime('%m', CSHDATE) AS Month,
    SUM((CSHAMOUNT - CSHREALPRICE) * CSHQTTY)
    FROM CashTable
    WHERE strftime('%Y', CSHDATE) = ?
    GROUP BY Month
    """
    Pf_cur.execute(Pf_exQuery, (YCGE.get(),))
    Pf_fetch = Pf_cur.fetchall()
    profit_per_month = {}
    profit = [0] * 12  # Initialize profit list with zeros for all months
    for row in Pf_fetch:
        month = row[0]
        SUM1 = row[1]
        try:
            profit_value = int(SUM1)
            month_index = int(month) - 1
            profit[month_index] = profit_value
            profit_per_month[month] = profit_value
        except:
            messagebox.showerror("Space4", "عاید خالص در دسترس نیست")

    Pf_cur.close()
    Pf_conn.close()
    return profit_per_month, profit


def plot_income_and_expenses_graph():
    income_per_month, income = fetch_income_data()
    (
        expenses_per_month,
        expenses,
    ) = fetch_expenses_data()  # Replace with your expense data fetching function
    profit_per_month, profit = fetch_profit_data()
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    fig = Figure(figsize=(12, 7), dpi=80, facecolor="#333333")
    plot = fig.add_subplot(111)
    plot.spines["bottom"].set_color("orange")
    plot.spines["top"].set_color("orange")
    plot.spines["left"].set_color("red")
    plot.spines["right"].set_color("orange")
    plot.xaxis.label.set_color("yellow")
    plot.yaxis.label.set_color("yellow")
    plot.tick_params(axis="x", colors="white")
    plot.tick_params(axis="y", colors="white")
    plot.title.set_color("white")
    plot.set_facecolor("#333333")
    # Plot income
    # plot.bar(months, income,color="lightgray")
    plot.plot(
        months,
        income,
        color="green",
        marker="^",
        markersize=8,
        markerfacecolor="lightgreen",
    )
    # Plot expenses
    plot.plot(
        months,
        expenses,
        color=BGRED,
        marker="v",
        markersize=8,
        markerfacecolor=BGORANGE,
    )
    # Plot Profits
    plot.plot(
        months,
        profit,
        color=BGBLUE,
        marker="o",
        markersize=8,
        markerfacecolor=BGWHITE,
    )
    plot.set_xlabel(
        "A long the year",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.set_ylabel(
        "Amount per / Af",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.set_title(
        f"Income, Expenses and Profit monthly in - {YCGE.get()}",
        fontdict={"weight": "bold", "fontfamily": "Tahoma"}
    )
    plot.legend(labels=["Income", "Expense", "All Profit"])

    canvas = FigureCanvasTkAgg(fig, master=GraphFrame_TOP_R_1)
    canvas.draw()
    canvas.get_tk_widget().pack(anchor=W)
# plot_income_and_expenses_graph()

Value_Y1 = [
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "2025",
    "2026",
    "2027",
    "2028",
    "2029",
    "2030"
]
YCGE.set(strftime('%Y'))


YearChooseGraphEnt = ctk.CTkComboBox(
    master=GraphFrame_TOP_R_1,
    width=100,
    variable=YCGE,
    values=Value_Y1
)
YearChooseGraphEnt.place(x=65, y=5)
OkBtn1 = ctk.CTkButton(
    master=GraphFrame_TOP_R_1,
    text="OK",
    width=50,
    command=RecallGraphFunc1
)
OkBtn1.place(x=5, y=5)
graphLogoBot = Label(
    master=GraphFrame_TOP_R_1,
    image=GraphImg,
    text="",
    bg="#333333"
)
graphLogoBot.place(x=20, y=50)

# ============== Welcomed window Blur background =========================
# ============== the other option of this event is near the root window =========
main_image_welwin = ImageTk.PhotoImage(ImageGrab.grab().filter(ImageFilter.BLUR))
blur_overlay_welwin = Label(root, image=main_image_welwin)
blur_overlay_welwin.place(x=0, y=0, relwidth=1, relheight=1)
blur_overlay_welwin.image = main_image_welwin

# force_resize(root)
#------------- Welocmed window -------------------
welcomeWin = Toplevel(root)
welcomeWin.overrideredirect(True)
welcomeWin.geometry("+350+80")
# welcomeWin.wm_attributes("-topmost", True)
# welcomeWin.attributes("-alpha", 0.9)

def welcomeDest():
    welcomeWin.destroy()
    blur_overlay_welwin.destroy()

Img4Logo = Image.open("PsysDataDir/WelcomedImg.png")
Img4_4Logo = Img4Logo.resize((600, 600))
WelcomedImg = ImageTk.PhotoImage(Img4_4Logo)

LogoLabel = Label(welcomeWin, image=WelcomedImg,bg="#333333")
LogoLabel.pack()
welcomeWin.wm_attributes('-transparentcolor', LogoLabel['bg'])
welcomeWin.wm_attributes("-topmost", True)

welcomeWin.after(5000, welcomeDest)
#-----------------------------




root.mainloop()
