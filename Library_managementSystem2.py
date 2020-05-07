from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import sqlite3 as db
from datetime import datetime


con=db.connect("Library.db")
c=con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS library(ID TEXT NOT NULL ,Title text not null, First text not null,Last text not null,Class text not null,
                   Roll int not null, BookID text not null,Book text not null,BookAuthors text not null,BookPrice text not null,BookBorrow text not null,
                   BookReturn text not null,BookSubmit text );''')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def iExist():
    iExit=tkinter.messagebox.askyesno("Library Management System","Confirm if you want to Exit")
    if iExit>0:
        root.destroy()
        return

def submit():
    #boxData.insert(END,ID.get()+"\t\t"+First.get()+"\t\t"+Last.get()+"\t\t"+Book.get()+"\t\t"+BookPrice.get()+"\t\t"+BookPrice.get()+"\n")
    
    v1=ID.get()
    v2=Title.get()
    v3=First.get()
    v4=Last.get()
    v5=Class.get()
    v6=Roll.get()
    v7=BookID.get()
    v8=Book.get()
    v9=BookAuthor.get()
    v10=BookPrice.get()
    v11=BookBorrow.get()
    v12=BookReturn.get()
    
    if (v1 or v5 or v8)=="":
        tkinter.messagebox.showinfo('Fail!','Fill the Content!')
    else:   
            c.execute('INSERT INTO library(ID,Title,First,Last,Class,Roll, BookID ,Book,BookAuthors,BookPrice,BookBorrow,BookReturn) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12))
            con.commit()

            tkinter.messagebox.showinfo('Success!','Account Created!')
    
    bk=ID.get()
    c.execute('select ID,First,Last,Book from library where ID=?',(bk,))
    result=c.fetchall()
    a=1
    for i in result:
        tree.insert("",1,text=a,value=i)
        print(i)
        a=a+1




def Reset():
            ID.set("")
            Title.set("")
            First.set("")
            Last.set("")
            Class.set("")
            Roll.set("")
            BookID.set("")
            Book.set("")
            BookAuthor.set("")
            BookPrice.set("")
            BookBorrow.set("")
            BookReturn.set("")

def check():

    def sub():
        v13 = SubmitDate.get()
        v14 = SubmitId.get()
        v15 = BookName.get()
        print(v13)
        print(v14)
        print(v15)
        c.execute('select * from library where ID=? AND Book=?',(v14,v15))
        bookch=c.fetchall()
        c.execute('select ID,First,Last,Class,BookID,Book,BookBorrow,BookReturn,BookSubmit from library where ID=? AND book=?',(v14,v15))
        if(bookch==0):
            tkinter.messagebox.showwarning('Fail!','Fill the Content!')
        else:   
                c.execute('UPDATE library SET BookSubmit = ?  WHERE ID = ?',(v13,v14))
                con.commit()

                c.execute('select BookReturn from library where ID=? AND Book=?',(v14,v15))
                bookch=c.fetchall()
                print(bookch)
                for returnDate in bookch:
                    for j in returnDate:
                        Rdate = j
                        print(Rdate)
                Rdate = datetime.strptime(Rdate,"%d/%m/%Y")
                v13 = datetime.strptime(v13,"%d/%m/%Y")
                Days = ((v13-Rdate).days)
                print(Days)

                if(Days<=0):
                    fine= 0
                    print(f"Fine = {fine}")

                else:
                    fine = Days * 2
                    print(f"Fine = {fine}")

                
                records = c.fetchall()
                for row in records:
                    print("Id = ", row[0], )
                    print("Name = ", row[1])
                    
                    
                
        c.execute('select ID,First,Last,Class,BookID,Book,BookBorrow,BookReturn,BookSubmit from library where ID=? AND book=?',(v14,v15))
        fineResult=c.fetchall()
        a=1
        for i in fineResult:
            tree.insert("",1,text=a,value=i)
            a+=1
            

    WindowS=Toplevel(root)
    WindowS.overrideredirect(1)
    WindowS.config(bg="royalblue")
    WindowS.geometry('%sx%s+%s+%s' % ((width), (height-180),8,210))
    
    SubmitDate=StringVar()
    BookName = StringVar()
    SubmitId = StringVar()
    
    UpperFrame2 = Frame(WindowS,bg="royalblue",width=width,height=height,bd=15,relief=SUNKEN)
    UpperFrame2.pack(side=TOP)

    UpperFrame3 = Frame(WindowS,bg="royalblue",width=1400,height=20,bd=15,relief=SUNKEN)
    UpperFrame3.pack(side=TOP)

    LowerFrame = Frame(WindowS,bg="yellow",width=1660,height=100,bd=15,relief=SUNKEN)
    LowerFrame.pack(side=BOTTOM)

    lblStudentId=Label(UpperFrame2,text="Student Card No.",font=('arial',15,'bold'),bg="royalblue",padx=2)
    lblStudentId.grid(row=0,column=0,padx=20,pady=5)
    txtStudentId=Entry(UpperFrame2,font=('arial',18,'bold'),width=15,textvariable=SubmitId)
    txtStudentId.grid(row=0,column=1,padx=20,pady=3)

    lblDate=Label(UpperFrame2,text="Submit Date:",font=('arial',15,'bold'),bg="royalblue",padx=2)
    lblDate.grid(row=0,column=3,padx=20,pady=5)
    txtDate=Entry(UpperFrame2,font=('arial',18,'bold'),width=22,textvariable=SubmitDate)
    txtDate.grid(row=0,column=4,padx=20,pady=3)

    lblBookName=Label(UpperFrame2,text="Book Name:",font=('arial',15,'bold'),bg="royalblue",padx=2)
    lblBookName.grid(row=0,column=5,padx=20,pady=5)
    txtBookName=Entry(UpperFrame2,font=('arial',18,'bold'),width=22,textvariable=BookName)
    txtBookName.grid(row=0,column=6,padx=20,pady=3)

    style=ttk.Style(UpperFrame3)
    style.theme_use("clam")
    style.configure("Treeview",background="white",fieldbackground="white",foreground="white",font=(None,10))
    style.configure("mystyle.Treeview.Heading",font=(None,11))    
    tree = ttk.Treeview(UpperFrame3,style="mystyle.Treeview")
    tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten")
    tree.column("#0",width=70)
    tree.column("one", width=70)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.column("four",width=70)
    tree.column("five",width=70)
    tree.column("six",width=100)
    tree.column("seven",width=110)
    tree.column("eight",width=110)
    tree.column("nine",width=110)
    tree.column("ten",width=70)
    
    tree.heading("#0",text="Sr.No")
    tree.heading("one", text="S.ID")
    tree.heading("two", text="First Name")
    tree.heading("three",text="Last Name")
    tree.heading("four",text="Class")
    tree.heading("five",text="Book Id")
    tree.heading("six",text="Book Name")
    tree.heading("seven",text="Borrow Date")
    tree.heading("eight",text="Return Date")
    tree.heading("nine",text="Submit Date")
    tree.heading("ten",text="Fine")
    tree.pack(ipadx=250,ipady=85)
   

    btnSubmit1 = Button(LowerFrame,text="SUBMIT",bd=7,fg="black",font=('arial',16,'bold'),width=25,height=2,command=sub)
    btnSubmit1.grid(row=0,column=0,columnspan=4)

    btnSubmit2 = Button(LowerFrame,text="CHECK",bd=7,fg="black",font=('arial',16,'bold'),width=25,height=2)
    btnSubmit2.grid(row=0,column=5,columnspan=4)

    btnSubmit3 = Button(LowerFrame,text="CLEAR",bd=7,fg="black",font=('arial',16,'bold'),width=25,height=2)
    btnSubmit3.grid(row=0,column=10,columnspan=3)

    btnSubmit4 = Button(LowerFrame,text="Exit",bd=7,fg="black",font=('arial',16,'bold'),width=25,height=2,command=iExist)
    btnSubmit4.grid(row=0,column=14,columnspan=3)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#main_function()
root = Tk()
root.title('Library Managment System')
width = (root.winfo_screenwidth()-15)    
height = (root.winfo_screenheight()-80)
#root.geometry('%sx%s+%s+%s' % (width, height,0,-1))
root.configure(background='black')



MainFrame = Frame(root)
MainFrame.grid()

UpperFrame = Frame(MainFrame,bg="yellow",width=100,height=150,bd=15,relief=SUNKEN)
UpperFrame.pack(side=TOP,fill='x')

UpperFrame2 = Frame(MainFrame,bg="royalblue",width=1600,height=660,bd=15,relief=SUNKEN)
UpperFrame2.pack(side=TOP,fill='x')

LeftFrame = Frame(UpperFrame2,bg="royalblue",width=440,height=660,bd=15,relief=RIDGE)
LeftFrame.pack(side=LEFT,fill='x')

LeftFrame2 = Frame(UpperFrame2,bg="royalblue",width=740,height=660,bd=15,relief=RIDGE)
LeftFrame2.pack(side=LEFT,fill='x')

RightFrame = Frame(UpperFrame2,bg="royalblue",width=440,height=660,bd=15,relief=RIDGE)
RightFrame.pack(side=LEFT,fill='x')

BottomFrame = Frame(MainFrame,bg="royalblue",width=width,height=90,bd=15,relief=RIDGE)
BottomFrame.pack(side=BOTTOM,fill='x')


lblCompany=Label(UpperFrame,text="RIZVI COLLEGE OF ARTS SCIENCE AND COMMERCE",font=('algerian',40,'bold'),bg="yellow",fg="orangered")
lblCompany.grid(row=0,column=2,columnspan=8,padx=0)

lblCompany=Label(UpperFrame,text="Library Managment System",font=('arial',38,'bold'),bg="yellow",fg="blue")
lblCompany.grid(row=1,column=4,columnspan=9)

global ID
ID = StringVar()
Title = StringVar()
First = StringVar()
Last = StringVar()
Class = StringVar()
Roll = StringVar()
BookID = StringVar()
global Book
Book = StringVar()
BookAuthor = StringVar()
BookPrice = StringVar()
BookBorrow = StringVar()
BookReturn = StringVar()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

lblStudent=Label(LeftFrame,text="STUDENT DETAIL:",font=('arial',25,'bold'),bg="royalblue",padx=2)
lblStudent.grid(padx=10,pady=10,row=0,column=0,columnspan=3)

lblID=Label(LeftFrame,text="Student Card No.",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblID.grid(padx=12,pady=12,row=1,column=0,sticky=W)
txtID = Entry(LeftFrame,font=('arial',18,'bold'),width=22,textvariable=ID)
txtID.grid(padx=10,pady=10,row=1,column=1)

lblTitle=Label(LeftFrame,text="Title:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblTitle.grid(padx=10,pady=10,row=2,column=0,sticky=W)
cboTitle = ttk.Combobox(LeftFrame,width=21,state='readonly',font=('arial',17,'bold'),textvariable=Title)
cboTitle['value'] = ('','Mr.','Mrs.')
cboTitle.current(0)
cboTitle.grid(padx=10,pady=10,row=2,column=1)

lblFirst=Label(LeftFrame,text="First Name:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblFirst.grid(padx=10,pady=10,row=3,column=0,sticky=W)
txtFirst = Entry(LeftFrame,font=('arial',18,'bold'),width=22,textvariable=First)
txtFirst.grid(padx=10,pady=10,row=3,column=1)

lblLast=Label(LeftFrame,text="Last Name:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblLast.grid(padx=10,pady=10,row=4,column=0,sticky=W)
txtLast = Entry(LeftFrame,font=('arial',18,'bold'),width=22,textvariable=Last)
txtLast.grid(padx=10,pady=10,row=4,column=1)

lblClass=Label(LeftFrame,text="Class:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblClass.grid(padx=10,pady=10,row=5,column=0,sticky=W)
cboClass = ttk.Combobox(LeftFrame,width=21,state='readonly',font=('arial',17,'bold'),textvariable=Class)
cboClass['value'] = ('','FYCS','SYCS','TYCS','FYIT','SYIT','TYIT')
cboClass.current(0)
cboClass.grid(padx=10,pady=10,row=5,column=1)

lblRoll=Label(LeftFrame,text="Roll Number:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblRoll.grid(padx=10,pady=10,row=6,column=0,sticky=W)
txtRoll = Entry(LeftFrame,font=('arial',18,'bold'),width=22,textvariable=Roll)
txtRoll.grid(padx=10,pady=10,row=6,column=1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
lblStudent=Label(LeftFrame2,text="BOOK DETAIL:",font=('arial',25,'bold'),bg="royalblue",padx=2)
lblStudent.grid(padx=10,pady=10,row=0,column=0,columnspan=3)


lblBookID=Label(LeftFrame2,text="Book ID:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblBookID.grid(padx=10,pady=10,row=1,column=0,sticky=W)
txtBookID = Entry(LeftFrame2,font=('arial',18,'bold'),width=22,textvariable=BookID)
txtBookID.grid(padx=10,pady=10,row=1,column=1)

lblBook=Label(LeftFrame2,text="Book Name:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblBook.grid(padx=10,pady=10,row=2,column=0,sticky=W)
txtBook = Entry(LeftFrame2,font=('arial',18,'bold'),width=22,textvariable=Book)
txtBook.grid(padx=10,pady=10,row=2,column=1)

lblBookAuthor=Label(LeftFrame2,text="Book Author:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblBookAuthor.grid(padx=10,pady=10,row=3,column=0,sticky=W)
txtBookAuthor = Entry(LeftFrame2,font=('arial',18,'bold'),width=22,textvariable=BookAuthor)
txtBookAuthor.grid(padx=10,pady=10,row=3,column=1)

lblBookPrice=Label(LeftFrame2,text="Book Price:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblBookPrice.grid(padx=10,pady=10,row=4,column=0,sticky=W)
txtBookPrice = Entry(LeftFrame2,font=('arial',18,'bold'),width=22,textvariable=BookPrice)
txtBookPrice.grid(padx=10,pady=10,row=4,column=1)

lblBookBorrow=Label(LeftFrame2,text="Borrow Date:",font=('arial',15,'bold'),bg="royalblue",pady=2)
lblBookBorrow.grid(padx=10,pady=10,row=5,column=0,sticky=W)
txtBookBorrow = Entry(LeftFrame2,font=('arial',18,'bold'),width=22,textvariable=BookBorrow)
txtBookBorrow.grid(padx=10,pady=10,row=5,column=1)

lblBookReturn=Label(LeftFrame2,text="Return Date:",font=('arial',15,'bold'),bg="royalblue",padx=2)
lblBookReturn.grid(padx=10,pady=10,row=6,column=0,sticky=W)
txtBookReturn = Entry(LeftFrame2,font=('arial',18,'bold'),width=22,textvariable=BookReturn)
txtBookReturn.grid(padx=10,pady=10,row=6,column=1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
style=ttk.Style(RightFrame)
style.theme_use("clam")
style.configure("Treeview",background="white",fieldbackground="white",foreground="white",font=(None,10))
style.configure("mystyle.Treeview.Heading",font=(None,11))    
tree = ttk.Treeview(RightFrame,style="mystyle.Treeview")
tree["columns"]=("one","two","three","four")
tree.column("#0",width=40)
tree.column("one", width=40)
tree.column("two", width=70)
tree.column("three",width=70)
tree.column("four",width=70)
tree.heading("#0",text="Sr.No")
tree.heading("one", text="S.ID")
tree.heading("two", text="First Name")
tree.heading("three",text="Last Name")
tree.heading("four",text="Book Name")
tree.pack(ipadx=80,ipady=80)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btnSumit = Button(BottomFrame,text="SUBMIT",bd=4,fg="black",font=('arial',16,'bold'),width=26,height=3,command=submit,bg='powder blue')
btnSumit.grid(row=0,column=0,padx=12)

btnCheck = Button(BottomFrame,text="CHECK",bd=4,fg="black",font=('arial',16,'bold'),width=26,height=3,bg='powder blue',command=check)
btnCheck.grid(row=0,column=1,padx=8)

btnReset = Button(BottomFrame,text="RESET",bd=4,fg="black",font=('arial',16,'bold'),width=26,height=3,command=Reset,bg='powder blue')
btnReset.grid(row=0,column=2,padx=8)

btnExit = Button(BottomFrame,text="EXIT",bd=4,fg="black",font=('arial',16,'bold'),width=26,height=3,command=iExist,bg='red')
btnExit.grid(row=0,column=3,padx=8)

#================================================================================================================================================================================================
label = Label(root,text="@PAWAN SERVICE \n Some rights reserved \n logo © 2019  ",bg='black',fg='white',font=('arial',10,'bold')).grid(padx=35,pady=35)

root.mainloop()
