from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import conn

# Connecting to the MySql server 
con = conn.con
cur = conn.cur

# Table Name
issueTable = "books_issued"
bookTable = "books"
allBid = []

def returnn():
    """function fetches the desired book ID and store it into bid 
    """
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status

    bid = bookInfo1.get()
    extractBid = "select bid from "+issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")


    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"

    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            return_book_screen.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")


    allBid.clear()
    return_book_screen.destroy()

def returnBook():
    """create and place a headingFrame and an input field for taking input of the books’ ID
       create and add two buttons named SubmitBtn and quitBtn
    """
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,return_book_screen,labelFrame, lb1

    return_book_screen = Tk()
    return_book_screen.title("Return Book")
    return_book_screen.minsize(width=400,height=400)
    return_book_screen.geometry("600x500")

    same = True
    n = .25

    #add a background image
    background_image = Image.open('./images/viewbook.jpg')
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n)
    else:
        newImageSizeHeigth = int(imageSizeHeight/n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(return_book_screen)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="#006B38", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(return_book_screen,bg="#00ffff",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(return_book_screen,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(return_book_screen,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(return_book_screen,text="Quit",bg='#ff0000', fg='black', command=return_book_screen.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    return_book_screen.mainloop()

