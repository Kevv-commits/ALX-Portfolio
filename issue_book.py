import pymysql
from PIL import ImageTk, Image
from tkinter import *
import conn

#setup a database connnection
con = conn.con
cur = conn.cur

#set tables to query
issue_table = 'books_issued'
book_table = 'books'

bookIds = []

def issue():
    """main function"""

    global issue_button,labelFrame,lb1,book_id,issue,quit_button,issue_book_screen,issue_book_canvas,status

    bid = book_id.get()
    issueto = issue.get()

    issue_button.destroy()
    labelFrame.destroy()
    lb1.destroy()
    book_id.destroy()
    issue.destroy()


    extractBid = "select bid from "+book_table
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            bookIds.append(i[0])

        if bid in allBid:
            availability = "select status from "+book_table+" where bid = '"+bid+"'"
            cur.execute(availability)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")

    issueSql = "insert into "+issue_table+" values ('"+bid+"','"+issueto+"')"
    show = "select * from "+issue_table

    updateStatus = "update "+book_table+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in bookIds and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            issue_book_screen.destroy()
        else:
            bookIds.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            issue_book_screen.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    print(bid)
    print(issueto)

    bookIds.clear()

def issue_book():
    """setting up the issue book gui window"""
     global issue_button,labelFrame,lb1,book_id,issue,quit_button,issue_book_screen,issue_book_canvas,status

    issue_book_screen = Tk()
    issue_book_screen.title("Issue Book")
    issue_book_screen.minsize(width=400,height=400)
    issue_book_screen.geometry("600x500")

    same = True
    n = .25

    #add a background image
    background_image = Image.open('./images/issue.jpg')
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n)
    else:
        newImageSizeHeigth = int(imageSizeHeight/n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    issue_book_canvas = Canvas(issue_book_screen)
    issue_book_canvas.create_image(300, 340, image=img)
    issue_book_canvas.config(bg="#D6ED17", width=newImageSizeWidth, height=newImageSizeHeight)
    issue_book_canvas.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(issue_book_screen,bg="#00ffff",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(issue_book_screen,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)

    book_id = Entry(labelFrame)
    book_id.place(relx=0.3,rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)

    issue = Entry(labelFrame)
    issue.place(relx=0.3,rely=0.4, relwidth=0.62)


    #Issue Button
    issue_button = Button(issue_book_screen,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issue_button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quit_button = Button(issue_book_screen,text="Quit",bg='#ff0000', fg='black', command=issue_book_screen.destroy)
    quit_button.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    issue_book_screen.mainloop()

