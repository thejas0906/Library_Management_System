from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as sql
from tkinter import ttk
from datetime import date 
mycon=sql.connect(host='localhost',user='root',passwd='root')
root=Tk()
root.geometry("1440x900")
mycur=mycon.cursor()
query='create database if not exists libmanagement'
mycur.execute(query)
query='use libmanagement'
mycur.execute(query)
d={'Username':'Admin','Password':'Admin'}
photo = PhotoImage(file ='lib.png')
bg3img = Label(root, image=photo)
bg3img.pack()
t={'background':'black','foreground':'Red','font':('Nirmala UI',15)}
x=Label(root,text='Username:',**t)
x.place(x=500,y=350)
y=Label(root,text='Password:',**t)
e1=Entry(root,width=30)
e2=Entry(root,width=30)
y.place(x=500,y=400)
e1.place(x=610,y=360)
e2.place(x=610,y=410)

query='create table if not exists library(Book_code varchar(8) primary key,Name varchar(20),Publication varchar(30),Category varchar(20),Quantity int(10),Status varchar(25))'
mycur.execute(query)
query='create table if not exists issued(Book_code varchar(8) primary key ,Name_of_reciver varchar(20),DOI date,DOR date)'
mycur.execute(query)
def back():
    root.deiconify()
    t.destroy()
def back2():
    t1.destroy()
    t.deiconify()
def check_pass():
    return e1.get() and e2.get()

def add_book():
    def add_detail():
        a=e1.get()
        b=e2.get()
        c=e3.get()
        d=e4.get()
        e=e5.get()
        f=menu.get()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        menu.set('Select Status')
        q1='insert into library values("{}","{}","{}","{}","{}","{}")'.format(a,b,c,d,e,f)
        mycur.execute(q1)
        mycon.commit()
    global t1,e1,e2,e3,e4,e5,menu
    t.withdraw()
    t1=Toplevel()
    t1.geometry("1440x900")
    global photo7
    photo7 = PhotoImage(file ='lib.png')
    bg4img = Label(t1, image=photo7)
    bg4img.pack()
    b={'foreground':'black','font':('Nirmala UI',15)}
    e1=Entry(t1,width=30)  
    e2=Entry(t1,width=30)
    e3=Entry(t1,width=30)
    e4=Entry(t1,width=30)
    e5=Entry(t1,width=30)
##    e6=Entry(t1,width=30)
    menu= StringVar()
    menu.set("Select Status")
    drop= OptionMenu(t1, menu,"Available","Not Avalable")
    drop.place(x=635,y=350)
    e1.place(x=635,y=100)
    e2.place(x=635,y=150)
    e3.place(x=635,y=200)
    e4.place(x=635,y=250)
    e5.place(x=635,y=300)
##    e6.place(x=635,y=350)
    c=Label(t1,text='Book Code',**b)
    n=Label(t1,text='Book name',**b)
    p=Label(t1,text='Publication',**b)
    ca=Label(t1,text='Category',**b)
    q=Label(t1,text='Quantity',**b)
    stat=Label(t1,text='Status',**b)
    c.place(x=530,y=90)
    n.place(x=530,y=140)
    p.place(x=530,y=190)
    ca.place(x=530,y=240)
    q.place(x=530,y=290)
    stat.place(x=530,y=340)
    a=Button(t1,text='Add',command=add_detail)
    a.place(x=625,y=400)
    b=Button(t1,text='goback',fg='black',bg='white',command=back2)   
    b.place(x=700,y=400)



def update_stock():
    def update():
         a=e1.get()
         b=e2.get()
         c=e3.get()
         d=e4.get()
         e=e5.get()
         f=e6.get()
         e1.delete(0,END)
         e2.delete(0,END)
         e3.delete(0,END)
         e4.delete(0,END)
         e5.delete(0,END)
         menu.set('Select Status')
         query='update  library set name="{}",publication="{}",category="{}",quantity={},status="{}" where book_code="{}"'.format(f,e,d,c,b,a)
         mycur.execute(query)
         mycon.commit()
    
    global t1
    t1=Toplevel()
    t1.geometry("1440x900")
    global e1,e2,e3,e4,e5,e6
    global photo4
    photo4 = PhotoImage(file ='lib.png')
    bg3img = Label(t1, image=photo4)
    bg3img.pack()
    e1=Entry(t1,width=30)
    e2=Entry(t1,width=30)
    e3=Entry(t1,width=30)
    e4=Entry(t1,width=30)
    e5=Entry(t1,width=30)
##    e6=Entry(t1,width=30)
    e1.place(x=625,y=100)
    e2.place(x=625,y=150)
    e3.place(x=625,y=200)
    e4.place(x=625,y=250)
    e5.place(x=625,y=300)
    menu= StringVar()
    menu.set("Select Status")
    drop= OptionMenu(t1, menu,"Available","Not Avalable")
    drop.place(x=635,y=350)
##    e6.place(x=625,y=350)
    c=Label(t1,text='Book Code')
    n=Label(t1,text='Book name')
    p=Label(t1,text='Publication')
    ca=Label(t1,text='Category')
    q=Label(t1,text='Quantity')
    stat=Label(t1,text='Status')
    c.place(x=525,y=100)
    n.place(x=525,y=150)
    p.place(x=525,y=200)
    ca.place(x=525,y=250)
    q.place(x=525,y=300)
    stat.place(x=525,y=350)
    C=Button(t1,text='Update',command=update)
    C.place(x=600,y=550)
    b1=Button(t1,text='goback',command=back2)
    b1.place(x=700,y=550)
   

def display_books():
    global t1
    t1=Toplevel()
    t1.geometry('1920x1080')
##    t1.configure(bg='black')
    global photo0 
##    photo0 = PhotoImage(file ='lib.png')
##    bg3img = Label(t1, image=photo0)
##    bg3img.place(x=0,y=0,relwidth=1,relheight=1)
    l=Label(t1,text='BOOKS IN LIBRARY',fg='black',bg='white',font=('Nirmala UI',25),width=1000)
    l.pack(side=TOP,anchor=CENTER)
    query="select * from library"
    mycur.execute(query)
    data=mycur.fetchall()
    mid=Frame(t1,width=1000,height=100)
    mid.place(relx=0.5,rely=0.5,anchor=CENTER)
    columns=('Book_code','Name','Publication','Category','Quantity','Status')
    table=ttk.Treeview(mid,columns=columns,show='headings',height=25)
    table.column('Book_code',anchor=CENTER,width=325)
    table.column('Name',anchor=CENTER,width=325)
    table.column('Publication',anchor=CENTER,width=325)
    table.column('Category',anchor=CENTER,width=325)
    table.column('Quantity',anchor=CENTER,width=325)
    table.column('Status',anchor=CENTER,width=325)
    table.heading('Book_code',text='Bookcode',anchor=CENTER)  
    table.heading('Name', text='Name',anchor=CENTER)
    table.heading('Publication', text='Publication',anchor=CENTER)
    table.heading('Category',text='Category',anchor=CENTER)
    table.heading('Quantity',text='Quantity',anchor=CENTER)
    table.heading('Status',text='Status',anchor=CENTER)
    for i in range(len(data)):
        list1=[(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5])]
        for i in list1:
            table.insert('',END,values=i)
    table.pack()
    b=Button(t1,text='goback',command=back2,width=30,height=2,font=('Nirmala UI',12))
    b.place(x=0,y=100)

def delete_book():
    def delb():
        b=e1.get()
        e1.delete(0,END)
        q="delete from library where book_code='{}'".format(b)
        mycur.execute(q)
        mycon.commit()
    global t1,e1
    t1=Toplevel()
    t1.geometry('1440x900')
    t1.configure(bg='black')
    global photo8 
    photo8 = PhotoImage(file ='lib.png')
    bg3img = Label(t1, image=photo8)
    bg3img.pack()
    pt=Label(t1,text='Enter Book no:',bg='black',fg='Red',font=('Nirmala UI',15))
    pt.place(x=700,y=400)
    e1=Entry(t1)
    e1.place(x=850,y=400)
    b=Button(t1,text='submit',font=('Nirmala UI',15),bg='black',fg='Red',command=delb)
    b.place(x=900,y=500)
    b1=Button(t1,text='goback',font=('Nirmala UI',15),bg='black',fg='Red',command=back2)
    b1.place(x=1000,y=500)

def find_status():
    def check():
        a=e9.get()
        q="select quantity from library where Book_code='{}'".format(a)
        mycur.execute(q)
        data=mycur.fetchone()
        print(data)
        if data[0]>0:
            mb.showinfo('','Book Available')
        else:
            mb.showinfo('','Book Not Available')
    global t1,photo6,e9
    t.withdraw()
    t1=Toplevel()
    t1.geometry('1440x900')
    photo6 = PhotoImage(file ='lib.png')
    bg3img = Label(t1, image=photo6)
    bg3img.pack()
    l1=Label(t1,text='Enter book code',font=('Nirmala UI',15),bg='black',fg='Red')
    l1.place(x=450,y=350)
    e9=Entry(t1,width=30)
    e9.place(x=610,y=360)
    b1=Button(t1,text='Submit',font=('Nirmala UI',15),command=check)
    b1.place(x=610,y=410)
    b2=Button(t1,text='goback',font=('Nirmala UI',15),command=back2)
    b2.place(x=750,y=410)
    
def issue_book():
    def backend_issue():
        a=e.get()
        b=e1.get()
        c=e2.get()
        d=e3.get()
        q='select * from library where Book_code="{}"'.format(a)
        mycur.execute(q)
        data=mycur.fetchone()

        k=0
        if data==None:
            k=0
            mb.showinfo('','Enter valid book code')
        else:
            k=1
        if k==1:
                if data[0]==a and data[4]>0:
                    mycur.execute('update library set quantity=quantity-1 where Book_code="{}"'.format(a))
                    mycur.execute('insert into issued values("{}","{}","{}","{}")'.format(a,b,c,d))
                    mycon.commit()
                elif data[4]<0:
                    mb.showinfo('','Book not available')
           
           

    
        
        
    t.withdraw()
    global t1,e,e2,e1,e3
    t1=Toplevel()
    t1.geometry('1440x900')
    global photo11
    photo11 = PhotoImage(file ='lib.png')
    bg5img = Label(t1, image=photo11)
    bg5img.pack()
    l=Label(t1,text='Enter Book Code',font=('Nirmala UI',15),bg='black',fg='Red')
    l.place(x=450,y=350)
    l1=Label(t1,text='Enter Book reciver name',font=('Nirmala UI',15),bg='black',fg='Red')
    l1.place(x=450,y=400)
    l2=Label(t1,text='Enter Date of Issue',font=('Nirmala UI',15),bg='black',fg='Red')
    l2.place(x=450,y=450)
    l3=Label(t1,text='Enter Date of Return',font=('Nirmala UI',15),bg='black',fg='Red')
    l3.place(x=450,y=500)
    e=Entry(t1,width=20)
    e1=Entry(t1,width=20)
    e2=Entry(t1,width=20)
    e3=Entry(t1,width=20)
    e.place(x=700,y=350)
    e1.place(x=700,y=400)
    e2.place(x=700,y=450)
    e3.place(x=700,y=500)
    b2=Button(t1,text='submit',command=backend_issue)
    b2.place(x=600,y=550)
    b1=Button(t1,text='goback',command=back2)
    b1.place(x=700,y=550)
def b_r():
    def book_return():
        a=e.get()
        b=e1.get()
        q="select * from issued where book_code ='{}'and name_of_reciver='{}'".format(a,b)
        print(q)
        mycur.execute(q)
        data=mycur.fetchone()
        k=0
        c=0
        fine=20
        if data==None:
            print(k)
            k=0
            mb.showinfo('','Enter valid book code') 
        else:
            k=1
            ds=str(data[3])
            print(data)
            s=str(date)
        if k==1:
                if date>data[3]:
                    dd=int(s[8]+s[9])-int(ds[8]+ds[9])
                    mb.showinfo('Fine',dd*fine)
                    q2="update library set quantity=quantity+1 where book_code='{}'".format(a)
                    mycur.execute(q2)
                    mycon.commit()
                    
        
                q1="delete from issued where book_code='{}'and name_of_reciver='{}'".format(a,b)
                mycur.execute(q1)
                mycon.commit()
                print(q1)
                

        
    
    t.withdraw()
    global t1,e,e1,e3,date
    date=date.today()
    t1=Toplevel()
    t1.geometry('1440x900')
    global photo12
    photo12 = PhotoImage(file ='lib.png')
    bg6img = Label(t1, image=photo12)
    bg6img.pack()
    l=Label(t1,text='Enter Book Code',font=('Nirmala UI',15),bg='black',fg='Red')
    l.place(x=450,y=350)
    l1=Label(t1,text='Enter Book reciver name',font=('Nirmala UI',15),bg='black',fg='Red')
    l1.place(x=450,y=400)
    e=Entry(t1,width=20)
    e1=Entry(t1,width=20)
    e.place(x=700,y=350)
    e1.place(x=700,y=400)
    b2=Button(t1,text='submit',command=book_return)
    b2.place(x=600,y=550)
    b1=Button(t1,text='goback',command=back2)
    b1.place(x=700,y=550)
        
def welcome_screen():
    global t
    root.withdraw()
    t=Toplevel()
    global photo2
    t.geometry("1440x900")
    photo2 = PhotoImage(file ='lib.png')
    bg3img = Label(t, image=photo2)
    bg3img.pack()
    c={'foreground':'bLack','font':('Nirmala UI',15)}
    a=Button(t,text='Add a book',command=add_book,**c)
    a.place(x=625,y=100)
    b=Button(t,text='Display all books',command=display_books,**c)
    b.place(x=625,y=150)
    C=Button(t,text='Update stock',command=update_stock,**c)
    C.place(x=625,y=200)
    D=Button(t,text='Delete book',command=delete_book,**c)
    D.place(x=625,y=250)
    e=Button(t,text='Find status',command=find_status,**c)
    e.place(x=625,y=300)
    f=Button(t,text='LogOut',command=back,**c)
    f.place(x=625,y=450)
    r=Button(t,text='Issue a Book',command=issue_book,**c)
    r.place(x=625,y=350)
    br=Button(t,text='Book Return',command=b_r,**c)
    br.place(x=625,y=400)
    t.mainloop()

def crct_credentials():
    if check_pass():
        x=e1.get()
        y=e2.get()
        if x==d['Username']:
            if y==d['Password']:
                welcome_screen()
            else:
                mb.showinfo("",'Incorrect password')
        else:
             mb.showinfo("",'Invalid username ')

b=Button(text='Login',command=crct_credentials)
b.place(x=610,y=450)             
