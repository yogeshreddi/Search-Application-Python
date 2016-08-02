import tkinter as tk
import tkinter.messagebox as tm
from tkinter import *
from tkinter import ttk
import sys
import pandas as pd

#importing our other .py file whihc is used for scraping infomration from the webpages
import scrape

FONTT = ("Times", "12", "bold italic")

class myApp(tk.Tk): 
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.wm_title(self,"Python Project")
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        self.frames = {}
        for F in (LoginPage, SearchPage,CreateLogin):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0,column = 0,sticky = "nsew")
        
        self.show_frame(LoginPage)
        
    #Function to show the page required thorugh navigation in the application
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()    

def search(item,loc,cont):
    global data
    data = scrape.scrape_info(item,loc)
    display = tk.Tk()
	
    display.title("Search Results")
    
    nameHLabel = tk.Label(display,text = "Name",font = FONTT)
    streetHLabel = tk.Label(display,text = "Street",font = FONTT)        
    localityHLabel = tk.Label(display,text = "Locality",font = FONTT)
    regionHLabel = tk.Label(display,text = "State",font = FONTT)
    phoneHLabel = tk.Label(display,text = "Phone",font = FONTT)    

    nameHLabel.grid(row=1,column=1,padx =10,pady =10)
    streetHLabel.grid(row=1,column=2,padx =10,pady =10)
    localityHLabel.grid(row=1,column=3,padx =10,pady =10)
    regionHLabel.grid(row=1,column=4,padx =10,pady =10)
    phoneHLabel.grid(row=1,column=5,padx =10,pady =10)

    for i in range(10):

        nameLable = tk.Label(display,text = str(data.RestroName[i]))
        nameLable.grid(row=i+2,column=1,padx =5,pady =5)

        streetLable = tk.Label(display,text = str(data.Street[i]))
        streetLable.grid(row=i+2,column=2,padx =5,pady =5)

        LocalityLable = tk.Label(display,text = str(data.Locality[i]))
        LocalityLable.grid(row=i+2,column=3,padx =5,pady =5)

        RegionLable = tk.Label(display,text = str(data.Region[i]))
        RegionLable.grid(row=i+2,column=4,padx =5,pady =5)

        phoneLable = tk.Label(display,text = str(data.Phone[i]))
        phoneLable.grid(row=i+2,column=5,padx =5,pady =5) 
        
        
    closeButton = Button(display,text = "Close",command = display.destroy)
    closeButton.grid(column=2,padx =10,pady =10)

    display.mainloop()



#Function to validate the username and password entered by the user

def loginValidate(user,pwd,cont):
    users = pd.read_csv(r'users.csv')
    if(user in list(users.users) and pwd == list(users[users.users == "dinesh"]["password"])[0]):
        cont.show_frame(SearchPage)
    else:
        tm.showerror("Login error", "Incorrect username or password")

#Function for fetching the dataframe containing the scraped infomration


class LoginPage(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        usr_login = StringVar()
        pwd_login = StringVar()
        userLabel = tk.Label(self,text = "Name",font = FONTT )
        passwordLabel = tk.Label(self,text = "Password", font = FONTT)
        
        userEntry = tk.Entry(self, textvariable = usr_login, bd=5)
        passwordEntry = tk.Entry(self, textvariable=pwd_login,bd=5,show = "*")
        
        submitButton = ttk.Button(self,text = "Login",command = lambda: loginValidate(usr_login.get(),pwd_login.get(),controller))
        quitButton = ttk.Button(self,text = "Quit",command = self.exit)
        
        #createLogin1 = tk.Label(self,text = "Do no have a acount:")
        createLogin2 = tk.Label(self,text = "Click here" ,font = FONTT,cursor="hand2")
        #createLogin3 = tk.Label(self,text = "to create an account")
            
        userLabel.grid(row = 0,sticky = "E",padx =10,pady =10)
        passwordLabel.grid(row =1,sticky = "E",padx =10,pady =10)
        userEntry.grid(row=0,column=1,padx =10,pady =10)
        passwordEntry.grid(row=1,column=1,padx =10,pady =10)
        submitButton.grid(row =2,column =1,padx =10,pady =10)
        quitButton.grid(row=2,column=0,padx =10,pady =10)
        createLogin2.grid(row=2,column =2,padx =10,pady =10)
        
        createLogin2.bind("<Button-1>",controller.show_frame(CreateLogin))        
    
    def exit(self):
        exit()
        
class CreateLogin(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        usr_login = StringVar()
        pwd_login = StringVar()
        email_id = StringVar()
        userLabel = tk.Label(self,text = "Name",font = FONTT )
        passwordLabel = tk.Label(self,text = "Password", font = FONTT)
        confirmPwdLabel = tk.Label(self,text = "Confirm Password", font = FONTT)
        emailLabel = tk.Label(self,text = "EMail ID", font = FONTT)
        
        userEntry = tk.Entry(self, textvariable = usr_login, bd=5)
        passwordEntry = tk.Entry(self, textvariable=pwd_login,bd=5,show = "*")
        confirmPwdLabelEntry = tk.Entry(self,show = "*")
        emailLabelEntry = tk.Entry(self, textvariable = email_id, bd=5)
        
        submitButton = ttk.Button(self,text = "Login",command = lambda: loginValidate(usr_login.get(),pwd_login.get(),controller))
        quitButton = ttk.Button(self,text = "Quit",command = self.exit)
        
        #createLogin1 = tk.Label(self,text = "Do no have a acount:")
        createLogin2 = tk.Button(self,text = "Create" ,font = FONTT)
        #createLogin3 = tk.Label(self,text = "to create an account")
        
        #createLogin.bind("<Button-1>", controller.show_frame(CreateLogin))
        
        emailLabel.grid(row = 0,sticky = "E",padx =10,pady =10)
        userLabel.grid(row = 1,sticky = "E",padx =10,pady =10)
        passwordLabel.grid(row =2,sticky = "E",padx =10,pady =10)
        confirmPwdLabel.grid(row =3,sticky = "E",padx =10,pady =10)
        
        userEntry.grid(row=1,column=1,padx =10,pady =10)
        passwordEntry.grid(row=2,column=1,padx =10,pady =10)
        confirmPwdLabelEntry.grid(row=3,column=1,padx =10,pady =10)
        emailLabelEntry.grid(row=0,column=1,padx =10,pady =10)
        
        submitButton.grid(row =4,column =1,padx =10,pady =10)
        quitButton.grid(row=4,column=0,padx =10,pady =10)
        createLogin2.grid(row=4,column =2,padx =10,pady =10)
    def exit(self):
        exit()

class SearchPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        welcomeLabel = tk.Label(self,text = "Welcome User", font = FONTT)
        logoutButton = ttk.Button(self,text = "Logout", command = lambda: controller.show_frame(LoginPage))
        
        item_search = StringVar()
        loc_search = StringVar()        
        
        item = tk.Label(self,text = "Find?")
        location = tk.Label(self,text = "Location?")
        itemSearch = tk.Entry(self,bd =5,textvariable = item_search)
        locSearch = tk.Entry(self,bd =5,textvariable = loc_search)

        searchButton = ttk.Button(self,text = "Search",command = lambda: search(item_search.get(),loc_search.get(),controller) )
        
        welcomeLabel.grid(row = 0)
        logoutButton.grid(row = 0,column =2)
        

        
        item.grid(row=1,column=0,padx =10,pady =10)
        location.grid(row=2,column=0,padx =10,pady =10)
        itemSearch.grid(row=1,column=1,padx =10,pady =10)
        locSearch.grid(row=2,column=1,padx =10,pady =10)
        searchButton.grid(row=3,column=1,padx =10,pady =10)        
        
app = myApp()
app.mainloop()