from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# connection to mysql server
mypass = ""
mydatabase=""
con = pymysql.connect (host="",user="",password=mypass,database=mydatabase)
cur = con.cursor()

# Table Name
issueTable = "books_issued"
bookTable = "books" #Book Table

def deleteBook():
    """function checks if the bid (book id) exists in the book table,
        if it does, it executes the necessary command to remove it.
    """
    bid = bookInfo1.get()

    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    print(bid)
    bookInfo1.delete(0, END)
    delete_book_screen.destroy()

def delete():
    """function creates a window for accommodating a text input field.
       fetch details of a book from the user and then call deleteBook() fun to 
       remove the book record from the table
    """
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root

    delete_book_screen = Tk()
    delete_book_screen.title("Delete Book")
    delete_book_screen.minsize(width=400,height=400)
    delete_book_screen.geometry("600x500")

    Canvas1 = Canvas(delete_book_screen)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(delete_book_screen,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(delete_book_screen,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(delete_book_screen,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    #quitBtn
    quitBtn = Button(delete_book_screen,text="Quit",bg='#f7f1e3', fg='black', command=delete_book_screen.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    delete_book_screen.mainloop()

