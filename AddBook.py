from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import conn

def bookRegister():
    """function executes an SQL command to insert data into the table
       and commit the changes.
    """
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)
    add_book_screen.destroy()

def addBook():
    """function connects to the MySql server and creates a window for
       new text fields that collects information from user and and then calls
       bookRegister() function to add books to the table.
    """
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    add_book_screen = Tk()
    add_book_screen.title("Add Book")
    add_book_screen.minsize(width=400,height=400)
    add_book_screen.geometry("600x500")

    #setting up a db connection
    con = conn.con
    cur = conn.cur

    # Table Name
    bookTable = ""
    Canvas1 = Canvas(add_book_screen)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(add_book_screen,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(add_book_screen,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(add_book_screen,text="SUBMIT",bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(add_book_screen,text="Quit",bg='#f7f1e3', fg='black', command=add_book_screen.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    add_book_screen.mainloop()


