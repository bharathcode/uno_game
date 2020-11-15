import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
import tkinter.messagebox as mb 

#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="game")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    mb.showinfo('Information', "All Fields Are Required")

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    number_info = mobile.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    elif number_info == "":
        error()
    else:
        print(number_info)
        sql = "insert into uno_det(user,passs,mobileno) values(%s,%s,%s)"
        t = (username_info, password_info, number_info)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        mb.showinfo('Information', "Registration Successfull")
        regback()
        



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("500x500")
    global username
    global password
    global mobile
    username = StringVar()
    password = StringVar()
    mobile = StringVar()
    title = tk.Label(root1, text ="UNO Register",font=("Helvetica",25) ) 
    title.place(x = 150, y = 100)

    lblfrstrow = tk.Label(root1, text ="Email -", ) 
    lblfrstrow.place(x = 70, y = 200) 

    Username = tk.Entry(root1, textvariable=username , width = 35) 
    Username.place(x = 170, y = 200, width = 200) 

    lblsecrow = tk.Label(root1, text ="Password -") 
    lblsecrow.place(x = 70, y = 250) 

    password = tk.Entry(root1, textvariable=password,show="*", width = 35) 
    password.place(x = 170, y = 250, width = 200)

    phone = tk.Label(root1, text ="Mobile No -") 
    phone.place(x = 70, y = 300) 

    phoneno = tk.Entry(root1, textvariable=mobile, width = 35) 
    phoneno.place(x = 170, y = 300, width = 200) 

    submitbtn = tk.Button(root1, text ="Regsiter", 
					bg ='lightblue', command = register_user) 
    submitbtn.place(x = 190, y = 370, width = 55)
    backbtn = tk.Button(root1, text ="Back", 
					bg ='lightblue', command = regback) 
    backbtn.place(x = 270, y = 370, width = 55)
    end = tk.Label(root1, text ="Developed By Bharath",font=("Helvetica",10) ) 
    end.place(x = 190, y = 450)

def regback():
        root1.destroy()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("UNO")
    root2.geometry("500x500")
    global username_varify
    global password_varify
    username_varify = StringVar()
    password_varify = StringVar()
    title = tk.Label(root2, text ="UNO Login",font=("Helvetica",25) ) 
    title.place(x = 150, y = 150)

    lblfrstrow = tk.Label(root2, text ="Username -", ) 
    lblfrstrow.place(x = 70, y = 250) 

    Username = tk.Entry(root2, textvariable=username_varify , width = 35) 
    Username.place(x = 170, y = 250, width = 200) 

    lblsecrow = tk.Label(root2, text ="Password -") 
    lblsecrow.place(x = 70, y = 300) 

    password = tk.Entry(root2, textvariable=password_varify, show="*" ,width = 35) 
    password.place(x = 170, y = 300, width = 200) 

    submitbtn = tk.Button(root2, text ="Login", 
					bg ='lightblue', command = login_varify) 
    submitbtn.place(x = 190, y = 370, width = 55)
    backbtn = tk.Button(root2, text ="Back", 
					bg ='lightblue', command = loginbackscreen) 
    backbtn.place(x = 270, y = 370, width = 55)
    end = tk.Label(root2, text ="Developed By Bharath",font=("Helvetica",10) ) 
    end.place(x = 190, y = 450)


def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()
        
def loginbackscreen():
        root2.destroy()
def logged():
    root2.destroy()


def failed():
    mb.showinfo('Information', "Invalid credentials...")

def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from uno_det where user = %s and passs = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            mb.showinfo('Information', "Login Successfull")
            root.destroy()
            rules_reg()
            break
    else:
        root2.destroy()
        failed()
def rules_reg():
    global logg
    logg = tk.Tk()
    logg.geometry("900x500")
    logg.title("Rules and Regulations")
    title = tk.Label(logg, text ="UNO Rules And Regulations",font=("Helvetica",22) ) 
    title.place(x = 220, y = 100)
    T = tk.Text(logg, height=15, width=100)
    T.place(x=30,y=150)
    T.insert(tk.END, "1. The player must warn that he has one card left and maybe he will finish the game soon \n2. Laying out the penultimate card (while he has not released it yet ")
    T.insert(tk.END,"\n3. the player must have time to say UNO! (which means one in Italian). \n4. If the player does not do this, good friends (or one friend) can notice this and remind UNO \n5. Friends must have time to do this from the moment the player releases his penultimate card before the next player starts turn (laying out the card or drawing the card from the deck). \n6. For forgetfulness, a player who did not say Uno! on time takes two cards (blindly) from the Widdie deck \n7. Players do not have the right to hide the number of cards in their hand (that is, collect a stack or hide under the table). \n8. Friends should be always known quantity of the card to help a forgetful player \n9. With a large number of errors and inattention, an additional rule can be introduced - for any erroneously laid out card, false shout, etc. the player takes two cards from the Widdie deck (blindly)")
    gamebut = tk.Button(logg, text ="Start UNO",bg ='lightblue', command = startuno)
    gamebut.place(x = 350, y = 410, width = 120)


def startuno():
    logg.destroy()
    
    
def mainsc():
    global root
    root =  tk.Tk() 
    root.geometry("500x500") 
    root.title("Uno game Welcome Page") 
    C = Canvas(root, bg ="blue", height = 250, width = 300) 

# Definging the first row

    title = tk.Label(root, text ="UNO Welcomes You",font=("Helvetica",25) ) 
    title.place(x = 100, y = 150)
    loginbtn = tk.Button(root, text ="Login",bg ='lightblue', command = login)
    loginbtn.place(x = 180, y = 250, width = 120)
    signbtn = tk.Button(root, text ="Register",bg ='lightblue', command = registration)
    signbtn.place(x = 180, y = 300, width = 120)
    end = tk.Label(root, text ="Developed By Bharath",font=("Helvetica",10) ) 
    end.place(x = 170, y = 450)
    







mainsc()
root.mainloop()
