#for importing library 
from tkinter import messagebox              #for using messagbox in tkinter
from tkinter import *                       #importing tkinter library
from tkinter import ttk,filedialog         
global x
x='£'
#Main class declared
class Main:
    #importing self made files 
    from handler.FormattedData import FormatData
    from handler.record import Record
    from handler.hireRecord import hRecord
    
#This method is used for validating 
    def validate(self):
        self.count = 0
        self.RealData = ["timepass yes","timepass yes","lalit nothing","kap frn","lalit nothing"]
        self.RealData = self.FormatData.ReadData("handler/database.csv") #this is for reading data from saved database
        self.log_user = str(self.raw_user.get())
        self.log_password = str(self.raw_pass.get())
        if (len(self.log_user)!=0) and (len(self.log_password) != 0):
            for self.Entry in self.RealData:
                if self.log_user in self.Entry and self.log_password in self.Entry:
                    self.count=self.count+1
            if self.count > 0:
                self.Record().write(self.log_user)
                self.g()
            else:
                messagebox.showinfo("Error","Sorry filled username or password is worng.")
                self.loginn()

        else:
            messagebox.showinfo("Error","You must fill all the feilds.")
            self.loginn()
        
#---------------------------------------------------------------------------------------------      
            
              
            
        
#This method is used for login window
    def loginn(self):
        #for login function
        self.root.destroy()# to destroy previous root
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')#declaring size of new window
        self.root.resizable(False,False)# making new window iresizeable
        self.Can = Canvas(self.root)#inserting image
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="Back",command=self.s)#placing a button named back which on clicking goes to s function in same class
        self.Back.place(x=0,y=0)#declaring the place of the button
        self.root.title("LOGIN")
        self.frame=Frame(self.root)#creating frame inside self.root
        self.frame.pack(pady=120)#packing frame
        
        self.userL=Label(self.root,text="Username",font=('Courier',30))#creating label named Username
        self.userL.pack(pady=10)#packing username and declaring its position
        self.raw_user = StringVar()
        self.User=Entry(self.root,font=('Courier',30),textvariable=self.raw_user).pack(padx=18,ipadx=50,ipady=5)#creating entry box
        
        self.PasswordLog=Label(self.root,text="Password",font=('Courier',30))#creating label named password
        self.PasswordLog.pack(pady=10)#packing it
        self.raw_pass =StringVar()
        self.PasswordLogin=Entry(self.root,show='*',font=('Courier',30),textvariable=self.raw_pass).pack(padx=20,ipadx=50,ipady=5)#storing password in a variable
        
        self.login=ttk.Button(self.root,text='LOGIN',command=self.validate)
        self.login.pack(ipady=5,ipadx=10,pady=10)
        #login.config(command= on)
        self.Can.pack()#packing image
        self.root.mainloop()#executing root
        #----------------------------------------------------------------------------------------------------------------------------------
#this is for saving username and password of the user
    def saveData(self):
        self.username = str(self.raw_username.get())
        self.password = str(self.raw_password.get())
        self.NewUser = [self.FormatData(self.username,self.password),]
        
        if (len(self.password)!=0) and (len(self.username) != 0):
            self.FormatData.SaveData("handler/database.csv",self.NewUser)
            self.loginn()
        else:
            print(self.username,self.password,"this is cool")
            messagebox.showinfo("Error","You must fill all the feilds.")
            self.register()
 #-------------------------------------------------------------------------------------------------
#This method is used for registring account of the user and owner
    def register(self):
        #to register account
        self.root.destroy()# destroying previous root
        global root #declaring as a global variable
        self.root=Tk()#initialing new window
        self.root.title("Sign in")#assigning title of window
        self.root.geometry('1080x675+0+0')# size of window
        self.root.resizable(False,False)# making it irresizeable
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="BACK",command= self.s)
        self.Back.place(x=0,y=0)

        self.title=Label(self.root,text="Sign up Portal")# declaring label
        self.title.pack()#packing label
        
        self.frame1=Frame(self.root,width=400, height=500)#declaring frame 1
        self.frame1.pack(pady=(100,0),ipadx=50,ipady=100)#packing frame 1
        
        self.fcan = Canvas(self.frame1)#inserting img in frame 1
        self.bgimg = PhotoImage(file="fb.png")
        self.imglab = Label(self.frame1, image=self.bgimg)
        self.imglab.place(x=0, y=0, relwidth=1, relheight=1)
        self.nameL=Label(self.frame1,text="First Name:",font=("Currior",15))#label named first name
        self.nameL.place(x=0,y=20)
        self.name = Entry(self.frame1,font=("Currior",13)).place(x=200,y=20)#entry for user
       
        self.lastL=Label(self.frame1,text="Last Name:",font=("Currior",15)).place(x=0,y=60)#label named last name
        self.last = Entry(self.frame1,font=("Currior",13)).place(x=200,y=60)#entry for user

        self.phoneL = Label(self.frame1,text="Phone no:",font=("Currior",15))#label named phone no
        self.phoneL.place(x=0,y=100)#packing label
        self.phone=Entry(self.frame1,font=("Currior",13))#entry for user
        self.phone.place(x=200,y=100)

        self.usernameL=Label(self.frame1,text="Username:",font=("Currior",15))#label named username
        self.usernameL.place(x=0,y=140)#packing label
        self.raw_username  = StringVar()
        self.username=Entry(self.frame1,font=("Currior",13),textvariable=self.raw_username).place(x=200,y=140)#entry for user
        

        self.passwordL=Label(self.frame1,text="Password:",font=("Currior",15))#label named password
        self.passwordL.place(x=0,y=180)#packing label
        self.raw_password = StringVar() 
        self.Password=Entry(self.frame1,font=("Currior",13),show='*',textvariable=self.raw_password).place(x=200,y=180)#entry for user
        


        self.EmailL=Label(self.frame1,text="Email:",font=("Currior",15))#label named email
        self.EmailL.place(x=0,y=220)#packing label
        self.Email = Entry(self.frame1,font=("Currior",13)).place(x=200,y=220)#entry for user


        self.genderL=Label(self.frame1,text="Gender",font=("Currior",15))#label named gender
        self.genderL.place(x=0,y=260)#packing label
        
        ttk.Radiobutton(self.frame1,text="Female",value=1).place(x=300,y=260)#initializing radiobuttion named female
        ttk.Radiobutton(self.frame1,text="Male", value=0).place(x=200,y=260)#initializing radiobutton named male

        
        self.registerr=ttk.Button(self.frame1,text="REGISTER",command=self.saveData)#creating button named register followed by self.saveData
        self.registerr.place(x=100,y=320)#packing button
        self.fcan.pack()#packing image inside frame
        self.Can.pack()#packing image in root
        self.root.mainloop()
       #------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
    
#Constructor for the welcome window
    def __init__(self):
        # for deafult geometry, background, title and the window
        self.root= Tk()
        self.c=0
        self.frame=Frame(self.root,bg="blue").pack(fill=BOTH)
        Label(self.frame,text="Welcome to the Log in Portal").pack(side=TOP)
        Label(self.frame,text="Select Log in if you have already register").pack(side=TOP)
        self.root.title('Login/Register')
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root, bg="blue")
        self.filename = PhotoImage(file="sp.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #-------------------------------------------------------------------------------
        
        self.frame2=Frame(self.root)
        self.frame2.pack()
        self.signin=ttk.Button(self.root,text='SIGN UP')
        self.signin.pack(side=LEFT,padx=200)
          #for background image in signup button
        img1 = PhotoImage(file="butup2.png")
        self.signin.config(image=img1)
        self.login=ttk.Button(self.root,text='LOGIN')
        self.login.pack(side=RIGHT,padx=200)
      #for background image in signin buttom
        img2 = PhotoImage(file="butin2.png")
        self.login.config(image=img2)
        self.signin.config(command=self.register)
        self.login.config(command=self.loginn)
        self.Can.pack()
        self.root.mainloop()
    #for destroying current window and retrive to Dicission class
    def g(self):
        self.root.destroy()
        Decission()
    #------------------------------------------
    #for destroying current window and retrive to Main class
    def s(self):
        self.root.destroy()
        Main()
        
   #For Decission class 
class Decission:
    #Import file and classes for file handling
    from handler.insurancefile import insurance
    from handler.hireRecord import hRecord
    from handler.insurancefile import insurance
    #---------------------------------------------
    
    def __init__(self):
        #------------------------------------------------------------------
        self.insurance().write("Booking Available")     #for resetting the availablity of the tools
        # for deafult geometry, background, title and the window
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="LOG OUT",command= self.c)
        self.Back.place(x=0,y=0)
        self.root.title('Decission')
        #---------------------------------------------------------------------------------------------------
        #for for the labels
        Label(self.root,text="Now you have to choose are you Owner or User").pack(pady=(110,0))
        Label(self.root,text="Select Owner if you have to lend the tool and User if you have to use the tool from other").pack()
        self.frame2=Frame(self.root)
        self.frame2.pack(pady=50)
        self.owner=ttk.Button(self.root,text='OWNER',command=self.a)
        self.owner.pack(pady=80)
        self.user=ttk.Button(self.root,text='USER',command=self.b)
        self.user.pack(pady=80)
        self.Can.pack()
        self.root.mainloop()
    #Methods for destroy root and redirecting to the Owner class
    def a(self):
        self.root.destroy()
        Owner()
   #--------------------------------------------------------------
    #Method for destroy root and redirecting to the user class
    def b(self):
        self.root.destroy()
        User()
   #--------------------------------------------------------------------
    #Method for destroying and redirecting to the welcome login page
    def c(self):
        self.root.destroy()
        Main()
   #------------------------------------------------------------
#Owner class decleared
class Owner:
   #for importing ownfile for file handing
    from handler.record import Record
    from handler.hireRecord import hRecord
    from handler.record import Record
   #---------------------------------------------------------
    def __init__(self):
        # for deafult geometry, background, title and the window
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
   #for the back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.c)
        self.Back.place(x=0,y=0)
   #------------------------------------------------------------------------------------------
    #For the bars Menu of the wind
        Label(self.root,text="You are the Owner of the tools",font=('Courier',30)).pack(pady=(200,0))
        self.mb = Menu(self.root)
        self.root.config(menu=self.mb)
  
        self.fm = Menu(self.mb, tearoff=0)
        self.mb.add_cascade(label="File", menu=self.fm)
        self.fm.add_command(label="Open", command=self.fopen)
        self.fm.add_command(label="Save", command=self.fsave)
        self.fm.add_command(label="Save As", command=self.fsaveAs)
        self.fm.add_separator()
        self.fm.add_command(label="Exit", command=self.root.quit)
        
        self.search=Menu(self.mb)
        self.mb.add_cascade(label="Search tool",menu=self.search)
        self.search.add_command(label='Drill',command=self.drill)
        self.search.add_command(label='Screw Driver',command=self.screw)
        self.search.add_command(label='Wire cutter',command=self.wirecutter)
        
        self.about=Menu(self.mb,tearoff=0) 
        self.mb.add_cascade(label="About",menu=self.about)
        self.about.add_command(label="Insurance",command=self.insu)
        self.about.add_command(label="About Us",command=self.us)
        
        self.record = Menu(self.mb,tearoff=0)
        self.mb.add_cascade(label="Hiring Records",menu=self.record)
        self.record.add_command(label="Records", command=self.Records)
        

        
        self.root.config(menu=self.mb)
        self.root.mainloop()
#-----------------------------------------------------------------------------------------------
#Record method the recording the hired tools 
    def Records(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="BACK",command= self.c)
        self.Back.place(x=0,y=0)
        #----------------------------------------------------------------------------------
        #variable decleared
        self.last_info = StringVar()
        self.full_info = StringVar()
        self.full_info = self.hRecord().readFull()
        self.last_info = self.hRecord().read()
        #---------------------------------------------------------------------------------
        #last Hired
        Label(self.root, text="Last Hired", font=('Courier',15)).pack(pady=(200,0))
        Label(self.root,text=self.last_info, font=('Courier',12)).pack(pady=(10,0))
        #-----------------------------------------------------------------------------------
        #for full hired records
        Label(self.root, text="Full Hired record", font=('Courier',15)).pack(pady=(20,0))
        Label(self.root,text=self.full_info, font=('Courier',12)).pack(pady=(10,0))
        #-------------------------------------------------------------------------------------
        

        
        self.root.config(menu=self.mb)
        self.root.mainloop()

     #destroy root and redirect to Discussion
    def c(self):
        self.root.destroy()
        Decission()
    #---------------------------------------------------------------
    #for terms and condition of the insurence
    def insu(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="BACK",command= self.back)
        self.Back.place(x=0,y=0)
        self.we=Label(self.root,text="Insurance simply represent the damages of the tool \n if the tool is damage and it has no physiical damage then you can claim\nfor the insurance after applying for the insurance company will investigate and pays the \n revinue if the terms and conditions are satisfied as per the rule of the company",font=("Currior",18))
        self.we.pack(pady=(300,0))
#-------------------------------------------------------------------------------------------------------------
#for information about the shared power
    def us(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="BACK",command= self.back)
        self.Back.place(x=0,y=0)
        self.label=Label(self.root,text="Shared Power is one of the leading software company \n in the world it gives platform for the people\n to lend and use their unused appliences or tool\n it is one of the best site to lend and \n hire tools for certain period of time",font=('Courier',20))
        self.label.pack(pady=(200,0))
        #for redirecting to Owner and destroy data
    def back(self):
        self.root.destroy()
        Owner()
   #----------------------------------------------------------
#for opening file

    def fopen(self):
        global txt
        global fl
        global fp
        global values
        global title

        if len(self.root.winfo_children()) == 1:
            self.fl = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
            self.fp = open(self.fl, 'r+')
            self.txt = Text(root)
            self.values = txt.get("1.0", END)
            self.txt.insert(INSERT, fp.read())
            self.txt.pack()
            self.fp.close()
        else:
            self.fl = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
            if self.fl:
                self.root.destroy()
                self.root=Tk()
                self.root.geometry('1080x675+0+0')
                
                self.fp = open(self.fl, 'r')
                self.txt = Text(self.root)
                self.values = self.txt.get("1.0", END)
                self.txt.insert(INSERT, self.fp.read())
                self.txt.pack()
                self.fp.close()
                
        self.title= self.fl.split('/')[-1]
        self.root.title( self.title)
#------------------------------------------------------------------------------------------
#for saving file
    def fsave(self):
        
        self.fp = open(self.fl, 'w')
        self.v = self.txt.get("1.0", END)
        self.fp.writelines(v)
        self.fp.close()
#----------------------------------------------
#for the save as file
    def fsaveAs(self):
        self.file = filedialog.asksaveasfile(mode='w', filetypes=[("Text files","*.txt")])
        if self.file != None:
            self.data = self.txt.get('1.0', END + '-1c')
            self.file.write(data)
            self.file.close()
     #------------------------------------------------
    #for the information of drills
    def drill(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('Drill')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="drills.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #--------------------------------------------------------------------------------------
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)                #for get back to system
        #information of drill
        self.label1=Label(self.root,text='This is a drill machine which is used to \n make a hole in a concrete and wood',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        self.label2=Label(self.root,text="You are the Owner",font=('Courier',20))
        self.label2.pack(pady=(50,0))
        perday='50'
        perhalf='30'
        self.label4=Label(self.root,text="Per Day",font=('Courier',15))
        self.label4.place(x=100,y=500)
        self.label6=Label(self.root,text=x+perday,font=('Courier',15))
        self.label6.place(x=200,y=500)
        self.label5=Label(self.root,text="Per Half Day",font=('Courier',15))
        self.label5.place(x=700,y=500)
        self.label7=Label(self.root,text=x+perhalf,font=('Courier',15))
        self.label7.place(x=870,y=500)
        self.label3=Label(self.root,text="Your items has been succesfully posted to be hired",font=('Courier',20))
        self.label3.pack(pady=(100,0))
        self.Can.pack()
        self.root.mainloop()
        #------------------------------------------------------------------------
        
    def screw(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('ScrewDriver')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="screwdrivers.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #----------------------------------------------------------------------------
        #for back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        #---------------------------------------------------------------
        #information about the the screwdriver
        self.label1=Label(self.root,text='This is a Screwdriver which is used to \n tighten a nail or a knot in a concrete or wood',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        self.label2=Label(self.root,text="You are the Owner",font=('Courier',20))
        self.label2.pack(pady=(50,0))
        perday='40'
        perhalf='25'
        self.label4=Label(self.root,text="Per Day",font=('Courier',15))
        self.label4.place(x=100,y=500)
        self.label6=Label(self.root,text=x+perday,font=('Courier',15))
        self.label6.place(x=200,y=500)
        self.label5=Label(self.root,text="Per Half Day",font=('Courier',15))
        self.label5.place(x=700,y=500)
        self.label7=Label(self.root,text=x+perhalf,font=('Courier',15))
        self.label7.place(x=870,y=500)
        self.label3=Label(self.root,text="Your items has been succesfully posted to be hired",font=('Courier',20))
        self.label3.pack(pady=(100,0))
        self.Can.pack()
        self.root.mainloop()
      #for the information about the wirecutter
    def wirecutter(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('Wirecutter')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="wire.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #------------------------------------------------------------------
        #for back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        #---------------------------------------------------------------------------
        self.label1=Label(self.root,text='This is a wirecutter which is used to \n cut the wire',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        self.label2=Label(self.root,text="You are the Owner",font=('Courier',20))
        self.label2.pack(pady=(50,0))
        perday='40'
        perhalf='25'
        self.label4=Label(self.root,text="Per Day",font=('Courier',15))
        self.label4.place(x=100,y=500)
        self.label6=Label(self.root,text=x+perday,font=('Courier',15))
        self.label6.place(x=200,y=500)
        self.label5=Label(self.root,text="Per Half Day",font=('Courier',15))
        self.label5.place(x=700,y=500)
        self.label7=Label(self.root,text=x+perhalf,font=('Courier',15))
        self.label7.place(x=870,y=500)
        self.label3=Label(self.root,text="Your items has been succesfully posted to be hired",font=('Courier',20))
        self.label3.pack(pady=(100,0))
        self.Can.pack()
        self.root.mainloop()
     #for destroying window and redirect to Owner
    def a(self):
        self.root.destroy()
        Owner()
     #----------------------------------------------
     #for showing information of booking to user
    def answer(self):
        self.u_name = StringVar()
        self.u_name = self.Record().read()
        messagebox.showinfo("Booking done","Dear {0}, your booking is done for 6 weeks".format(self.u_name))

    def free(self):
        self.u_name = StringVar()
        self.u_name = self.Record().read()
        messagebox.showinfo("Booking done","Dear {0}, your booking is done for 3 days".format(self.u_name))
   #---------------------------------------------------------------------------------------------------------------
#for declearing user class
class User:
    #for importing the file and using classes for file handling
    from handler.insurancefile import insurance
    from handler.record import Record
    from handler.hireRecord import hRecord
    
#----------------------------------------------------------------------
    
    def __init__(self):
        # for deafult geometry, background, title and the window
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #-------------------------------------------------------------------
        #for back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.c)
        #----------------------------------------------------------------------------
        self.Back.place(x=0,y=0)
        
        #for menu of the window
        Label(self.root,text="You are the User of the tools",font=('Courier',20)).pack(pady=(200,0))
        self.mb = Menu(self.root)
        self.root.config(menu=self.mb)
        #-------------------------------------------------------------------
       #for submenu
        self.fm = Menu(self.mb, tearoff=0)
        self.mb.add_cascade(label="File", menu=self.fm)
        self.fm.add_command(label="Open", command=self.fopen)
        self.fm.add_command(label="Save", command=self.fsave)
        self.fm.add_command(label="Save As", command=self.fsaveAs)
        self.fm.add_separator()
        self.fm.add_command(label="Exit", command=self.root.quit)
#------------------------------------------------------------------------
#for submenu return tools
        self.Return=Menu(self.mb)
        self.mb.add_cascade(label="Return tool",menu=self.Return)
        self.Return.add_command(label='Drill',command=self.Rdrill)
        self.Return.add_command(label='Screw Driver',command=self.Rscrew)
        self.Return.add_command(label='Wire cutter',command=self.Rwirecutter)
        self.root.config(menu=self.mb)
   #--------------------------------------------------------
#for submenu of search tool
        self.search=Menu(self.mb)
        self.mb.add_cascade(label="Search tool",menu=self.search)
        self.search.add_command(label='Drill',command=self.drill)
        self.search.add_command(label='Screw Driver',command=self.screw)
        self.search.add_command(label='Wire cutter',command=self.wirecutter)
 #----------------------------------------------------------
#for submenu of about us
        self.about=Menu(self.mb,tearoff=0)
        self.mb.add_cascade(label="About",menu=self.about)
        self.about.add_command(label="Insurance",command=self.insu)
        self.about.add_command(label="About Us",command=self.us)
        self.root.config(menu=self.mb)
   #------------------------------------------
        self.root.mainloop()
    #for destroy window and redirect information
    def c(self):
        self.root.destroy()
        Decission()
    #for the terms and policy of the insurance
    def insu(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="BACK",command= self.back)
        self.Back.place(x=0,y=0)
        self.we=Label(self.root,text="Insurance simply represent the damages of the tool \n if the tool is damage and it has no physiical damage then you can claim\nfor the insurance after applying for the insurance company will investigate and pays the \n revinue if the terms and conditions are satisfied as per the rule of the company",font=("Currior",18))
        self.we.pack(pady=(300,0))
#------------------------------------------------------------------------------------
#for the inormation about the company
    def us(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.resizable(False,False)
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Back=ttk.Button(self.root,text="BACK",command= self.back)
        self.Back.place(x=0,y=0)
        self.label=Label(self.root,text="Shared Power is one of the leading software company \n in the world it gives platform for the people\n to lend and use their unused appliences or tool\n it is one of the best site to lend and \n hire tools for certain period of time",font=('Courier',20))
        self.label.pack(pady=(200,0))
        #-------------------------------------------------------------------------
        #for back button
    def back(self):
        self.root.destroy()
        Owner()
  #------------------------------------------------------
#for opening file
    def fopen(self):
        global txt
        global fl
        global fp
        global values
        global title

        if len(self.root.winfo_children()) == 1:
            self.fl = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
            self.fp = open(self.fl, 'r+')
            self.txt = Text(root)
            self.values = txt.get("1.0", END)
            self.txt.insert(INSERT, fp.read())
            self.txt.pack()
            self.fp.close()
        else:
            self.fl = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
            if self.fl:
                self.root.destroy()
                self.root=Tk()
                self.root.geometry('1080x675+0+0')
                
                self.fp = open(self.fl, 'r')
                self.txt = Text(self.root)
                self.values = self.txt.get("1.0", END)
                self.txt.insert(INSERT, self.fp.read())
                self.txt.pack()
                self.fp.close()

        self.title= self.fl.split('/')[-1]
        self.root.title( self.title)
#for saving file 
    def fsave(self):
        
        self.fp = open(self.fl, 'w')
        self.v = self.txt.get("1.0", END)
        self.fp.writelines(v)
        self.fp.close()
#------------------------------------------
#for save as file
    def fsaveAs(self):
        self.file = filedialog.asksaveasfile(mode='w', filetypes=[("Text files","*.txt")])
        if self.file != None:
            self.data = self.txt.get('1.0', END + '-1c')
            self.file.write(data)
            self.file.close()
  #---------------------------------------------------------
#for showing information of drills
    def drill(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window 
        self.root.geometry('1080x675+0+0')
        self.root.title('Drill')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="drills.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #for back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        #------------------------------------------------------------------------
        self.label1=Label(self.root,text='This is a drill machine which is used to \n make a hole in a concrete and wood',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        perday='50'
        perhalf='30'
        self.label4=Label(self.root,text="Per Day",font=('Courier',15))
        self.label4.place(x=100,y=500)
        self.label6=Label(self.root,text=x+perday,font=('Courier',15))
        self.label6.place(x=200,y=500)
        self.label5=Label(self.root,text="Per Half Day",font=('Courier',15))
        self.label5.place(x=700,y=500)
        self.label7=Label(self.root,text=x+perhalf,font=('Courier',15))
        self.label7.place(x=870,y=500)
        self.book = StringVar()
        self.book = self.insurance().read()
        Label(self.root,text=self.book).pack(pady=(50,0))  #To get avilablity of the tools
        
        self.paid=ttk.Button(self.root,text="Paid Booking",command=self.paid) #for paid booking
        self.paid.pack(side=LEFT,padx=(100,0),ipadx=15,ipady=5)
        self.free=ttk.Button(self.root,text="Free Booking,",command=self.free)
        self.free.pack(side=RIGHT,padx=(0,100),ipadx=15,ipady=5)
        self.Can.pack()
        self.root.mainloop()
        #--------------------------------------------------------------------
        #method for screw info
    def screw(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('ScrewDriver')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="screwdrivers.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
     #----------------------------------------------------------------------
    #for back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
    #--------------------------------------------------------------------------
    #information about screw
        self.label1=Label(self.root,text='This is a Screwdriver which is used to \n tighten a nail or a knot in a concrete or wood',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        perday='40'
        perhalf='25'
        self.label4=Label(self.root,text="Per Day",font=('Courier',15))
        self.label4.place(x=100,y=500)
        self.label6=Label(self.root,text=x+perday,font=('Courier',15))
        self.label6.place(x=200,y=500)
        self.label5=Label(self.root,text="Per Half Day",font=('Courier',15))
        self.label5.place(x=700,y=500)
        self.label7=Label(self.root,text=x+perhalf,font=('Courier',15))
        self.label7.place(x=870,y=500)
        self.book = StringVar()
        self.book = self.insurance().read()
        Label(self.root,text=self.book).pack(pady=(50,0))
        self.paid=ttk.Button(self.root,text="Paid Booking",command=self.paid)
        self.paid.pack(side=LEFT,padx=(100,0),ipadx=15,ipady=5)
        self.free=ttk.Button(self.root,text="Free Booking",command=self.free)
        self.free.pack(side=RIGHT,padx=(0,100),ipadx=15,ipady=5)
        self.Can.pack()
        self.root.mainloop()
#-------------------------------------------------------------------
#method for information about the wirecutter
    def wirecutter(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('Wirecutter')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="wire.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
 #----------------------------------------------------------------------------------
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        self.label1=Label(self.root,text='This is a wirecutter which is used to \n cut the wire',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        perday='40'
        perhalf='25'
        self.label4=Label(self.root,text="Per Day",font=('Courier',15))
        self.label4.place(x=100,y=500)
        self.label6=Label(self.root,text=x+perday,font=('Courier',15))
        self.label6.place(x=200,y=500)
        self.label5=Label(self.root,text="Per Half Day",font=('Courier',15))
        self.label5.place(x=700,y=500)
        self.label7=Label(self.root,text=x+perhalf,font=('Courier',15))
        self.label7.place(x=870,y=500)
        self.book = StringVar()
        self.book = self.insurance().read()             #to check where tool is available or not
        
        Label(self.root,text=self.book).pack(pady=(50,0))
        self.paid=ttk.Button(self.root,text="Paid Booking",command=self.paid)
        self.paid.pack(side=LEFT,padx=(100,0),ipadx=15,ipady=5)
        self.free=ttk.Button(self.root,text="Free Booking",command=self.free)
        self.free.pack(side=RIGHT,padx=(0,100),ipadx=15,ipady=5)
        self.Can.pack()
        self.root.mainloop()
        #--------------------------------------------------------------------------------------------
        #destroy and redirect to ther User class
    def a(self):
        self.root.destroy()
        User()
     #---------------------------------------------------
    
     #added code Rdrill
    def Rdrill(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('Drill')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="drills.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #------------------------------------------------------------------------------
        #back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        #-------------------------------------------------------------
        
        self.label1=Label(self.root,text='This is a drill machine which is used to \n make a hole in a concrete and wood',font=('Courier',20))
        self.label1.pack(pady=(320,0),padx=(50,0))
        
        Label(self.root,text="Booking Unavailable",font=('Courier',20)).pack(pady=(100,0))
        
        self.paid=ttk.Button(self.root,text="Return Now",command=self.return_ans_1)
        self.paid.pack(pady=(120,0))
            
        self.Can.pack()
        self.root.mainloop()

        #method for returning screw
    def Rscrew(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('ScrewDriver')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="screwdrivers.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #--------------------------------------------------------------------------
        #Back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        #--------------------------------------------------------------------
        self.label1=Label(self.root,text='This is a Screwdriver which is used to \n tighten a nail or a knot in a concrete or wood',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        Label(self.root,text="Booking Unavailable",font=('Courier',20)).pack(pady=(50,0))
        self.paid=ttk.Button(self.root,text="Return Now",command=self.return_ans_2)
        self.paid.pack(pady=(120,0))
        self.Can.pack()
        self.root.mainloop()
#Method for returning wirecutter
    def Rwirecutter(self):
        # for deafult geometry, background, title and the window
        self.root.destroy()
        self.root=Tk()#create a blank window
        self.root.geometry('1080x675+0+0')
        self.root.title('Wirecutter')
        self.root.resizable(False,False)
        self.Can =Canvas(self.root)
        self.file = PhotoImage(file="wire.png",width = 1080, height=675)
        self.background_label = Label(self.root,image=self.file)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #------------------------------------------------------------------------
        #back button
        self.Back=ttk.Button(self.root,text="BACK",command= self.a)
        self.Back.place(x=0,y=0)
        #-----------------------------------------------------------------------------
        self.label1=Label(self.root,text='This is a wirecutter which is used to \n cut the wire',font=('Courier',20))
        self.label1.pack(pady=(300,0),padx=(50,0))
        Label(self.root,text="Booking Unavailable",font=('Courier',20)).pack(pady=(50,0))
        self.paid=ttk.Button(self.root,text="Return Now",command=self.return_ans_3)
        self.paid.pack(pady=(120,0))

        self.Can.pack()
        self.root.mainloop()
     #for getting condition and showing information for returning drill   
    def return_ans_1(self):
        self.ans_1 = messagebox.askyesno("Urgency","Is it urgent for the owner?")
        if self.ans_1:
            self.ans_01 = messagebox.askyesno("Insurance","Is this tool is damaged?")
            if self.ans_01:
                self.insurance().write("Booking unavailable")
                self.z()
            else:
                self.returned()
        else:
            self.ans_2 = messagebox.askyesno("Hire Again","Do you want to hire tools again?")
            if self.ans_2:
                self.a()
            else:
                self.returned()
       #-------------------------------------------------------------------
     #for getting condition and showing information for returning screw
    def return_ans_2(self):
        self.ans_1 = messagebox.askyesno("Urgency","Is it urgent for the owner?")
        if self.ans_1:
            self.ans_01 = messagebox.askyesno("Insurance","Is this tool is damaged?")
            if self.ans_01:
                self.insurance().write("Booking unavailable")
                self.z()
            else:
                self.b()
        else:
            self.ans_2 = messagebox.askyesno("Hire Again","Do you want to hire tools again?")
            if self.ans_2:
                self.a()
            else:
                self.returned()
     #-----------------------------------------------------------------------------
    #for getting condition and showing information for returning wirecutter
    def return_ans_3(self):
        self.ans_1 = messagebox.askyesno("Urgency","Is it urgent for the owner?")
        if self.ans_1:
            self.ans_01 = messagebox.askyesno("Insurance","Is this tool is damaged?")
            if self.ans_01:
                self.insurance().write("Booking unavailable")
                self.z()
            else:
                self.returned()
        else:
            self.ans_2 = messagebox.askyesno("Hire Again","Do you want to hire tools again?")
            if self.ans_2:
                self.a()
            else:
                self.b()
    #--------------------------------------------------------------------------------------
    #for destroying window and redirecting Insurnace
    def z(self):
        self.root.destroy()
        Insurance()
    #for destroying window and redirecting User
    def d(self):
        self.root.destroy()
        User()
   #-----------------------------------------------------------
     #for destroying window and redirecting to user
    def a(self):
        self.root.destroy()
        User()
        #added code
#----------------------------------------------------------

    def returned(self):
        #for getting condition and showing information
        self.root.destroy()
        self.root= Tk()
        
        self.frame=Frame(self.root,bg="blue").pack(fill=BOTH)
        Label(self.frame,text="Items Returned").pack(side=TOP)
        Label(self.frame,text="Item Returned").pack(side=TOP)
        self.root.title('Successfully returned')
        self.root.geometry('1080x675+0+0')
        
        self.root.resizable(False,False)
        
        self.Can = Canvas(self.root, bg="blue")
        self.filename = PhotoImage(file="sp.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #----------------------------------------------------------------------------------
        self.Back=ttk.Button(self.root,text="HOME",command= self.d)
        self.Back.pack()
        
          #Greeting customer 
        Label(self.root, text="This item is successfully returned.",font=("Currior",25)).pack(pady=(320,0))
        Label(self.root, text="Thanks for giving us chance to serve.",font=("Currior",25)).pack(pady=(0,0))

        self.Can.pack()
        self.root.mainloop()
        #----------------------------------------------------------------------
        #showing booking information
    def free(self):
        self.ok=messagebox.showinfo("Booking done","dear costumer your booking is done for 3 days")
        if self.ok:
            self.done()
        #----------------------------------------------
        #for destroying root and redirect to User
    def done(self):
        self.root.destroy()
        User()
     #--------------------------------------------
    #Method for paid information
    def paid(self):
        #for getting condition and showing information
        self.root.destroy()
        self.root= Tk()
        self.root.geometry('1080x675+0+0')
        self.root.title("Information")
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #-----------------------------------------------------------
        #for calculating total price
        self.days=IntVar()
        self.price=IntVar()
        self.label=Label(self.root,text='Days',font=('Courier',15))
        self.label.place(x=50,y=150)
        Entry(self.root,text=self.days,font=('Courier',15)).place(x=150,y=150)
        Label(self.root,text='Price',font=('Courier',15)).place(x=50,y=200)
        self.entry1=Entry(self.root,text=self.price,font=('Courier',15))
        self.entry1.place(x=150,y=200)
        self.button=ttk.Button(self.root,text='Total',command=self.total).place(x=175,y=250)
    def total(self):
        obt_price =int(self.price.get()) #for getting price 
        obt_day =int(self.days.get())    #for getting day
        
        self.answer=obt_day*obt_price           #for calculating anser
        self.total=Label(self.root,text='Price',font=('Courier',15))
        self.total.place(x=50,y=300)
        Label(self.root,text=self.answer,font=('Courier',15)).place(x=150,y=300)
        self.button=ttk.Button(self.root,text='Pay',command=self.yes).place(x=175,y=250)
        #---------------------------------------------------
        #for ask for user confirmation
    def yes(self):
        self.f=messagebox.askyesno('Confirmation','Are you sure you want to pay the bill?')
        if self.f:
            self.u_name = StringVar()
            self.u_name = self.Record().read()   #for getting username
        
            self.hRecord().write(self.u_name)
            messagebox.showinfo('PAYMENT INFORMATION','Thank you {0} for the payment'.format(self.u_name)) #Greeting information
            self.done()
    #Insurance class for validating insurance condition 
class Insurance:
    def __init__(self):
        #for getting condition and showing information
        self.root= Tk()
        self.root.geometry('1080x675+0+0')
        self.root.title("Pay Fine")
        self.Can = Canvas(self.root)
        self.filename = PhotoImage(file="back.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #--------------------------------------------------------------------
        #verification
        self.ans_4=messagebox.askyesno("Insurance","Does the damage covers the insurance policy?")
        self.Can.pack()
        if self.ans_4:
            self.thank()
        else:
            self.pay()
        
        self.root.mainloop()  
        #------------------------------------
        #Last greeting for confirmation of the user
    def thank(self):
        #for getting condition and showing information
        self.root.destroy()
        self.root= Tk()
        
        self.frame=Frame(self.root,bg="blue").pack(fill=BOTH)
        Label(self.frame,text="Items Returned").pack(side=TOP)
        Label(self.frame,text="Item Returned").pack(side=TOP)
        self.root.title('Successfully returned')
        self.root.geometry('1080x675+0+0')
        
        self.root.resizable(False,False)
        
        self.Can = Canvas(self.root, bg="blue")
        self.filename = PhotoImage(file="sp.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #--------------------------------------------------------------------
        #for back button
        self.Back=ttk.Button(self.root,text="HOME",command= self.e)
        self.Back.pack()
        #--------------------------------------------------------
        #for confirming user information
        messagebox.showinfo("Booking Unavailable","Booking for the same tool is unavailable for certain period of time while it is being repaired")
        
          #For greeting user
        Label(self.root, text="This item is successfully returned.",font=("Currior",25)).pack(pady=(320,0))
        Label(self.root, text="Thanks for giving us chance to serve.",font=("Currior",25)).pack(pady=(0,0))

        self.Can.pack()
        self.root.mainloop()
#-------------------------------------------------------------
#destroy root and redirect to the User class
    def e (self):
        self.root.destroy()
        User()
#-------------------------------------
#destroying root and for paying fine
    def pay(self):
        #for getting condition and showing information
        self.root.destroy()
        self.root= Tk()
        
        self.frame=Frame(self.root,bg="blue").pack(fill=BOTH)
        Label(self.frame,text="Items Returned").pack(side=TOP)
        Label(self.frame,text="Item Returned").pack(side=TOP)
        self.root.title('Successfully returned')
        self.root.geometry('1080x675+0+0')
        
        self.root.resizable(False,False)
        
        self.Can = Canvas(self.root, bg="blue")
        self.filename = PhotoImage(file="sp.png",width = 1080, height=675)
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #------------------------------------------------------------
        #Back button 
        self.Back=ttk.Button(self.root,text="HOME",command= self.e)
        self.Back.pack()
        #------------------------------------------------------------------------
          #For showing label
        Label(self.root, text="Sorry! you have to pay  the fine",font=("Currior",25)).pack(pady=(120,0))
        Label(self.root, text="Successfully Negotiated with the User",font=("Currior",25)).pack(pady=(130,0))
        Label(self.root, text="Thanks for giving us chance to serve.",font=("Currior",25)).pack(pady=(150,0))
        messagebox.showinfo("Booking Unavailable","Booking for the same tool is unavailable for certain period of time while it is being repaired")


        self.Can.pack()
        self.root.mainloop()
        #----------------------------------------------
  #for calling Main class
Main()
