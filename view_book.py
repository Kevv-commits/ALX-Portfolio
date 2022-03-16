from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import conn

#setup a database connnection
con = conn.con
cur = conn.cur

#set table to query
book_table = 'books'


def view_book():
    """setting up the view book window"""

    view_book_screen = Tk()
    view_book_screen.title('View Books')
    view_book_screen.minsize(width=400, height=400)
    view_book_screen.geometry('600x500')

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

    view_book_canvas = Canvas(view_book_screen)
    view_book_canvas.create_image(300, 340, image = img)
    view_book_canvas.config(bg='#12a4d9', width=newImageSizeWidth, height=newImageSizeHeight)
    view_book_canvas.pack(expand=True, fill=BOTH)

    headingFrame = Frame(view_book_screen, bg='#00ffff', bd=5)
    headingFrame.place(relx=.25, rely=.1, relwidth=.5, relheight=.13)

    headingLabel = Label(headingFrame, text='View Books', bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(view_book_screen, bg='black')
    labelFrame.place(relx=.1, rely=.3, relwidth=.8, relheight=.5)

    y = .25

    Label(labelFrame, text='%-10s%-40s%-30s%-20s'%('BID', 'Title', 'Author', 'Status'), bg='black', fg='white').place(relx=.07, rely=.1)
    Label(labelFrame, text='----------------------------------------------------------------------------------', bg='black', fg='white').place(relx=.05, rely=.2)
    get_books = 'select * from ' + book_table
    try:
        cur.execute(get_books)
        con.commit()
        for i in cur:
            Label(labelFrame, text='%-10s%-30s%-30s%-20s'%(i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=.07, rely=y)
            y += .1
    except:
        messagebox.showinfo('Failed to fetch files from database')

    quit_button = Button(view_book_screen, text='Quit', bg='#ff0000', fg='black', command=view_book_screen.destroy)
    quit_button.place(relx=.4, rely=.9, relwidth=.18, relheight=.08)

    view_book_screen.mainloop()


