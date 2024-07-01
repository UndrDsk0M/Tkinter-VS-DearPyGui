from tkinter import *
import tkinter.font as tkFont
page = Tk()
page.title("Login")
page.geometry("400x600")
page.resizable(False, False)

mainframe = Frame(page)
mainframe.pack()

welcomeSign_font = tkFont.Font(family='./digital-7.ttf', size=38)

def progress():
    print(username.get())
    print(phone.get())
    print(password.get())
    page.quit()


sign = Label(mainframe, text="Login", font=welcomeSign_font)
sign.pack(pady=20)
username = Entry(mainframe, width=30)
username_lbl = Label(mainframe, text="username")
username_lbl.pack()
username.pack()


phone = Entry(mainframe, width=30)
username_lbl = Label(mainframe, text="phone")
username_lbl.pack()
phone.pack()

password = Entry(mainframe, width=30, show="*")
username_lbl = Label(mainframe, text="password")
username_lbl.pack()
password.pack(pady=40)

login = Button(mainframe, text="Login", command=progress)
login.pack()





page.mainloop()