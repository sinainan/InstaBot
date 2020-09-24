from tkinter import *
from user import username, password, listname, useracc
from insta import insta

class main:
    def __init__(self, master):
        self.master = master
        master.title("Insta Bot")
        master.geometry("500x500")
        self.label = Label(master, text="Boost your Instagram Account")
        self.label.pack()

        self.label1 = Label(master, text="")
        self.label1.pack()

        self.label2 = Label(master, text="Username")
        self.label2.pack()

        self.e1 = Entry(master)
        self.e1.pack()
        
        self.label3 = Label(master, text="password")
        self.label3.pack()

        self.e2 = Entry(master)
        self.e2.pack()
        
        self.login_button = Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.label5 = Label(master, text="useracc")
        self.label5.pack()

        self.e4 = Entry(master)
        self.e4.pack()

        self.label4 = Label(master, text="Listname")
        self.label4.pack()

        self.e3 = Entry(master)
        self.e3.pack()

        self.list_button = Button(master, text="Get List", command=self.getFollowersList)
        self.list_button.pack()

        self.follow_button = Button(master, text="Get Follow", command=self.getFollow)
        self.follow_button.pack()

        self.unfollow_button = Button(master, text="Get Unfollow", command=self.getUnfollow)
        self.unfollow_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def getUser(self):
        useracc = self.e4.get()
        username = self.e1.get()
        password = self.e2.get()
        listname = self.e3.get()
        return useracc, username, password, listname

    def login(self):
        useracc = self.e4.get()
        username = self.e1.get()
        password = self.e2.get()
        listname = self.e3.get()
        instag = insta(username, password, listname, useracc)
        instag.signIn()
        print("LogIn Succesfull!")

    def getFollowersList(self):
        useracc = self.e4.get()
        username = self.e1.get()
        password = self.e2.get()
        listname = self.e3.get()
        instag = insta(username, password, listname, useracc)
        instag.signIn()
        instag.getFollowers()
        print("List Succesfull!")

    def getFollow(self):
        useracc = self.e4.get()
        username = self.e1.get()
        password = self.e2.get()
        listname = self.e3.get()
        instag = insta(username, password, listname, useracc)
        instag.signIn()
        instag.followUser(listname)
        print("Follow Succesfull!")

    def getUnfollow(self):
        useracc = self.e4.get()
        username = self.e1.get()
        password = self.e2.get()
        listname = self.e3.get()
        instag = insta(username, password, listname, useracc)
        instag.signIn()
        instag.unFollowUser(listname)
        print("Unfollow Succesfull!")

root = Tk()
my_gui = main(root)
root.mainloop()