from tkinter import *
from tkinter import messagebox
import sqlite3

def newuser():
    def newuser1():
        def pass1(a,b,c,d,e,f,g):
            list1=[a,b,c,d,e,f,g]
            conn=sqlite3.connect("test1.db")
            c=conn.cursor()
            c.execute("INSERT INTO PARK VALUES(?, ?, ?, ?, ?, ?, ?)",list1)
            conn.commit()
            def show():
                showinfo( "Submission", "Succefully submitted")
            window2.destroy()
            
        name=abc.get()
        regno=b.get()
        gen=g12.get()
        mobileno=m.get()
        emailid=e.get()
        user123=user12.get()
        pass123=pass12.get()
        pass1(name,regno,gen,mobileno,emailid,user123,pass123)
        
    window2=Toplevel(top)
    window2.title("New User")
    Name=Label(window2,text="Name:").grid(row=0,column=0)
    abc=StringVar(None)
    en1=Entry(window2,textvariable=abc,bd=5).grid(row=0,column=1)
    reg=Label(window2,text="Reg No:").grid(row=1,column=0)
    b=IntVar(None)
    en2=Entry(window2,textvariable=b,bd=5).grid(row=1,column=1)
    gen=Label(window2,text="Gender:").grid(row=3,column=0)
    g12=StringVar(None)
    g12.set(None)
    m1=Radiobutton(window2,text="Male",variable=g12,value="Male").grid(row=3,column=1)
    m2=Radiobutton(window2,text="Female",variable=g12,value="Female").grid(row=4,column=1)
    m=StringVar(None)
    mob=Label(window2,text="Mobile Number:").grid(row=5,column=0)
    en3=Entry(window2,textvariable=m,bd=5).grid(row=5,column=1)
    email=Label(window2,text="Email Id:").grid(row=6,column=0)
    e=StringVar(None)
    e4=Entry(window2,textvariable=e,bd=5).grid(row=6,column=1)
    user=Label(window2,text="Username:").grid(row=7,column=0)
    user12=StringVar(None)
    user1=Entry(window2,textvariable=user12,bd=5).grid(row=7,column=1)
    pass12=StringVar(None)
    pass123=Label(window2,text="Password:").grid(row=8,column=0)
    pass1234=Entry(window2,textvariable=pass12,bd=5,show="*").grid(row=8,column=1)
    submit=Button(window2,text="Submit",command=newuser1).grid(row=9,column=1)
    
def logincall():
    def login():
        username1=custname.get()
        password1=custpass.get()
        def connect(username1,password1):
            conn=sqlite3.connect("test1.db")
            c=conn.cursor()
            i=1
            for row in c.execute(" SELECT USERNAME,PASSWORD FROM PARK"):
                if(username1==row[0] and password1==row[1]):
                    window_main_frame()
                    showinfo("Found","Record Found")
                    i=1  
                else:
                    i=i+1
                    continue 
        connect(username1,password1)
        window1.destroy()
        
    window1=Toplevel(top)
    L1=Label(window1,text="Username").grid(row=0,column=0)
    custname=StringVar(None)
    E1=Entry(window1,textvariable=custname,bd=5).grid(row=0,column=1)
    L2=Label(window1,text="Password").grid(row=1,column=0)
    custpass=StringVar(None)
    E2=Entry(window1,textvariable=custpass,bd=5,show='*')
    E2.grid(row=1,column=1)
    s=Button(window1,text="Submit",command=login)
    s.grid(row=2,column=1)
    
def window_main_frame():
    def pakdet():
        regdata1=regdata.get()
        blockdata1=blockdata.get()
        vehicle1=vehicle.get()
        listpak=[regdata1,blockdata1,vehicle1]
        conn=sqlite3.connect("pakdet.db")
        c1=conn.cursor()
        c1.execute("INSERT INTO PAKDET VALUES(?,?,?)",listpak)
        conn.commit()
        showinfo("Save","Record Saved")
        window4.destroy()
        
    window4=Toplevel(top)
    labelpark=Label(window4,text="Registration No:").grid(row=0,column=0)
    regdata=IntVar()
    reg=Entry(window4,textvariable=regdata,bd=5).grid(row=0,column=1)
    labelpark2=Label(window4,text="Block No:").grid(row=1,column=0)
    blockdata=StringVar()
    blockdata.set(None)
    R1=Radiobutton(window4,text="Block 14",variable=blockdata,value="Block No 14").grid(row=1,column=1)
    R2=Radiobutton(window4,text="Block 29",variable=blockdata,value="Block No 29").grid(row=2,column=1)
    R3=Radiobutton(window4,text="Block 34",variable=blockdata,value="Block No 34").grid(row=3,column=1)
    R4=Radiobutton(window4,text="Block 56",variable=blockdata,value="Block No 56").grid(row=4,column=1)
    vehicle=StringVar()
    vehicle.set(None)
    vehicle1=Label(window4,text="Vehicle:").grid(row=5,column=0)
    R5=Radiobutton(window4,text="Bike:Charge Rs. 5",variable=vehicle,value="2 Wheeler:Charge Rs 5").grid(row=5,column=1)
    R6=Radiobutton(window4,text="Car:Charge Rs. 15",variable=vehicle,value="4 Wheeler:Charge Rs 15").grid(row=6,column=1)
    Sub=Button(window4,text="Submit",command=pakdet).grid(row=7,column=1)

def park1():
    def displaypark():
        r2=r.get()
        conn=sqlite3.connect("pakdet.db")
        c3=conn.cursor()
        i=1
        for row in c3.execute("SELECT * FROM PAKDET"):
            if(row[0]==r2):
                pak1=Label(frame1,text="Registration:").grid(row=0,column=0)
                pak2=Label(frame1,text=row[0]).grid(row=0,column=1)
                pak3=Label(frame1,text="Block:").grid(row=1,column=0)
                pak4=Label(frame1,text=row[1]).grid(row=1,column=1)
                pak5=Label(frame1,text="Price").grid(row=2,column=0)
                pak6=Label(frame1,text=row[2]).grid(row=2,column=1)
                i=1
            else:
                i=i+1
                continue
        window5.destroy()
        
    window5=Toplevel(top)
    r=IntVar()
    reg01label=Label(window5,text="Enter Reg No:").grid(row=0,column=0)
    reg01entry=Entry(window5,textvariable=r,bd=5).grid(row=0,column=1)
    subpak=Button(window5,text="Submit" ,command=displaypark).grid(row=1,column=1)
    
    


top=Tk()
top.geometry('700x500')
top.title('Client Page')
c=Canvas(top,height=250,width=250,bg="green")
frame=Frame(c)
frame1=Frame(c)
frame1.pack(side=TOP)
login=Button(frame,text="Login",bg="black",fg="white",command=logincall)
new=Button(frame,text="New User",bg="black", fg="white",command=newuser)
new.pack(side=RIGHT)
park=Button(frame,text="Parking Details",bg="black",fg="white",command=park1)
park.pack(side=LEFT)
login.pack(side=LEFT)
frame.pack(side=BOTTOM)
c.pack(expand=YES,fill=BOTH)
top.mainloop()



