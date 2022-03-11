from tkinter import *
from tkinter import messagebox
import pymysql

mypass = ""
mydatabase = ""

con = pymysql.connect(host="", user="",
                      password=mypass, database=mydatabase)
cur = con.cursor()

issueTable = "books_issued"

def issuedBook():
    issued_books_screen = Tk()
    issued_books_screen.title("Issued Books")
    issued_books_screen.minsize(width=400, height=400)
    issued_books_screen.geometry("600x500")

    issued_books_canvas = Canvas(issued_books_screen)
    issued_books_canvas.config(bg="#12a4d9")
    issued_books_canvas.pack(expand=True, fill=BOTH)

    headingFrame = Frame(issued_books_screen, bg="#FFBB00", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame, text="View Books",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(issued_books_screen, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-50s%-90s" % ('BID', 'Issuedto'),
                                    bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from "+issueTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-50s%-90s" %
                  (i[0], i[1]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quit_button = Button(issued_books_screen, text="Quit", bg='#f7f1e3',
                     fg='black', command=issued_books_screen.destroy)
    quit_button.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    issued_books_screen.mainloop()

