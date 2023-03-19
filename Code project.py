import csv #csv reader
from tkinter import * # mor GUI stuff
from tkinter import ttk #my GUI
import math #math
import numpy as np #math stuff for graphing
import matplotlib.pyplot as plt #graph plotting libary
import sympy #eqution rearanging libary
import tkinter.font as font#imports the ability to change font

#creates and formats the GUI window
window = Tk() 
window.geometry("800x750")

#changes my GUI's theme
style = ttk.Style()
#print(style.theme_names())
style.theme_use('xpnative')
style.configure('big.TButton', font=(None, 25))

#size of the grid
win_col_x = int(10)
win_row_y = int(10)

#creates the gird
for x in range(win_col_x):
    Grid.columnconfigure(window,x,weight = 1)
for x in range(win_row_y):
    Grid.rowconfigure(window,x,weight = 1)

#clears the window of all tabs
def clear_window():
    widgets = window.winfo_children()
    for item in widgets:
        item.grid_forget()
    but_home.grid(column=1,row=0,ipadx=10,ipady=10,columnspan=2)
    but_settings.grid(column=3,row=0,ipadx=10,ipady=10,columnspan=2)
    but_graphing.grid(column=5,row=0,ipadx=10,ipady=10,columnspan=2)
    but_create_calc.grid(column=7,row=0,ipadx=10,ipady=10,columnspan=2)
#loads the home screen with hte main buttons
def load_home():
    clear_window()
    nav_load_screen("Mods")
    but_home.grid(column=1,row=0,ipadx=10,ipady=10,columnspan=2)
    but_settings.grid(column=3,row=0,ipadx=10,ipady=10,columnspan=2)
    but_graphing.grid(column=5,row=0,ipadx=10,ipady=10,columnspan=2)
    but_create_calc.grid(column=7,row=0,ipadx=10,ipady=10,columnspan=2)


#all of my widgets that are not object orintaited. 
#key buttons
but_home = ttk.Button(window,text="Home",command=load_home,style="big.TButton")
but_settings = ttk.Button(window,text="Settings",command=load_home,style="big.TButton")
but_graphing = ttk.Button(window,text="graphs",command=load_home,style="big.TButton")
but_create_calc = ttk.Button(window,text="Create",command=load_home,style="big.TButton")
but_chap_1 = ttk.Button(window,text="Chapter 1",command=load_home)
but_mod_1 = ttk.Button(window,text="Module 1",command=load_home)
#SUVAT
en_SUVAT_S = ttk.Entry(window)
en_SUVAT_U = ttk.Entry(window)
en_SUVAT_V = ttk.Entry(window)
en_SUVAT_A = ttk.Entry(window)
en_SUVAT_T = ttk.Entry(window)
#unit_SUVAT_S = ttk.OptionMenu(window)
#unit_SUVAT_U = ttk.OptionMenu(window)
#unit_SUVAT_V = ttk.OptionMenu(window)
#unit_SUVAT_A = ttk.OptionMenu(window)
#unit_SUVAT_T = ttk.OptionMenu(window)


#creating all the lists for my navigation menu
Mods = {}
module_1 = {}
module_2 = {}
module_3 = {}
module_4 = {}
module_5 = {}
module_6 = {}
chap1 = {}
chap2 = {}
chap3 = {}
chap4 = {}
chap5 = {}
chap6 = {}
chap7 = {}
chap8 = {}
chap9 = {}
chap10 = {}
chap11 = {}
chap12 = {}
chap13 = {}
chap14 = {}
chap15 = {}
chap16 = {}
chap17 = {}
chap18 = {}
chap19 = {}
chap20 = {}
#chap21 = {}
#chap22 = {}
#chap23= {}
home = {}
#putting the modules in a dctionary

#filling in the modules with the chapters
Mods = {"links_too":["module_1","module_2","module_3","module_5","module_6"],"Buttons":[],"prev":"Home"}
module_1 = {"links_too":[],"Buttons":[],"prev":"Mods"}
module_2 = {"links_too":["chap1","chap2"],"Buttons":[],"prev":"Mods"}
module_3 = {"links_too":["chap3","chap4","chap5","chap6","chap7"],"Buttons":[],"prev098":"Mods"}
module_4 = {"links_too":["chap8","chap9","chap10","chap11","chap12","chap13"],"Buttons":[],"prev":"Mods"}
module_5 = {"links_too":["chap14","chap15","chap16","chap17","chap18"],"Buttons":[],"prev":"Mods"}
module_6 = {"links_too":[],"Buttons":[],"prev":"Mods"}

#filling in chapters
chap1 = {"links_too":[],"Buttons":[],"prev":"module_2"}
chap2 = {"links_too":[],"Buttons":[],"prev":"module_2"}

chap3 = {"links_too":[],"Buttons":[],"prev":"module_3"}
chap4 = {"links_too":[],"Buttons":[],"prev":"module_3"}
chap5 = {"links_too":[],"Buttons":[],"prev":"module_3"}
chap6 = {"links_too":[],"Buttons":[],"prev":"module_3"}
chap7 = {"links_too":[],"Buttons":[],"prev":"module_3"}

chap8 = {"links_too":[],"Buttons":[],"prev":"module_4"}
chap9 = {"links_too":[],"Buttons":[],"prev":"module_4"}
chap10 = {"links_too":[],"Buttons":[],"prev":"module_4"}
chap11 = {"links_too":[],"Buttons":[],"prev":"module_4"}
chap12 = {"links_too":[],"Buttons":[],"prev":"module_4"}
chap13 = {"links_too":[],"Buttons":[],"prev":"module_4"}

chap14 = {"links_too":[],"Buttons":[],"prev":"module_5"}
chap15 = {"links_too":[],"Buttons":[],"prev":"module_5"}
chap16 = {"links_too":[],"Buttons":[],"prev":"module_5"}
chap17 = {"links_too":[],"Buttons":[],"prev":"module_5"}
chap18 = {"links_too":[],"Buttons":[],"prev":"module_5"}
chap19 = {"links_too":[],"Buttons":[],"prev":"module_5"}
chap20 = {"links_too":[],"Buttons":[],"prev":"module_5"}

all_dics = (Mods,module_1,module_2,module_3,module_4,module_5,module_6)#,chap1,chap2,chap3,chap4,chap5,chap6,chap7,chap8,chap9,chap10,chap11,chap12,chap13,chap14,chap15,chap16,chap17,chap18,chap19,chap20)


#loads the buttons from whatever dictionary has been chosen

#Mods.load_buttons()


def nav_load_screen(x):
    clear_window() #clears window of widgets
    y = globals()[x]["Buttons"][0]
    x.grid(column = 0,row = 1)
    axis_x = 0
    axis_y = 2
    #for every button in the buttons list of the dic
    for but in globals()[x]["Buttons"]:
        #place the button
        but.grid(column=axis_x,row=axis_y)
        #iterate the grid system
        if axis_x == 9:
            axis_x = 0
            axis_y = axis_y + 1
        else:
            axis_x = axis_x + 1

#creates all the buttons for the navigation menue
def create_menu_buttons():
    #for every dictionary in the list
    for y in all_dics:
        prev_dic_name = y
        prev_dic_name = prev_dic_name["prev"]
        but_name = [prev_dic_name + "_button"]
        print(but_name ,"was made")
        but_name = ttk.Button(window,text = "Go Back")
        but_name.config(command = lambda prev_dic_name=prev_dic_name:nav_load_screen(prev_dic_name))
        y["Buttons"].append(but_name)
        

        #for every dictionary in the links too create a button for that 
        for x in y["links_too"]:
            dic_name = x
            button_name = [x + "_button"]
            button_name = ttk.Button(window,text=dic_name)
            button_name.config(command=lambda dic_name=dic_name:nav_load_screen(dic_name))
            y["Buttons"].append(button_name)
        #print(y["Buttons"])


    
create_menu_buttons()
nav_load_screen("Mods")
#grid size force buttons
B00= ttk.Label(window,text="")
B00.grid(column=0,row=0,ipadx=5,ipady=5)
B10 = ttk.Label(window,text="")
B10.grid(column=1,row=0,ipadx=5,ipady=5)
B20 = ttk.Label(window,text="")
B20.grid(column=2,row=0,ipadx=5,ipady=5)
B30 = ttk.Label(window,text="")
B30.grid(column=3,row=0,ipadx=5,ipady=5)
B40 = ttk.Label(window,text="")
B40.grid(column=4,row=0,ipadx=5,ipady=5)
B50 = ttk.Label(window,text="")
B50.grid(column=5,row=0,ipadx=5,ipady=5)
B60 = ttk.Label(window,text="")
B60.grid(column=6,row=0,ipadx=5,ipady=5)
B70 = ttk.Label(window,text="")
B70.grid(column=7,row=0,ipadx=5,ipady=5)
B80 = ttk.Label(window,text="")
B80.grid(column=8,row=0,ipadx=5,ipady=5)
B90 = ttk.Label(window,text="")
B90.grid(column=9,row=0,ipadx=5,ipady=5)
B51 = ttk.Label(window,text="5,1")
B51.grid(column=5,row=1,ipadx=5,ipady=5)



#opens the home screen
window.mainloop()
#this comment has escaped the matrix