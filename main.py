from tkinter import *
from PIL import ImageTk, Image
from AddBook import *
from ReturnBook import *
from DeleteBook import *
from issued_books import *
from issue_book import *
from view_book import *
import conn

#setting up a db connection
con = conn.con
cur = conn.cur

mainWindow = Tk()
mainWindow.title('Book Management')
mainWindow.minsize(width=400, height=400)
mainWindow.geometry('600x500')

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("./images/viewbook.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(mainWindow)

Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(mainWindow,bg="#00FFFF",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Manage your Books", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(mainWindow,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

btn2 = Button(mainWindow,text="Delete Book",bg='black', fg='white', command=deleteBook)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn3 = Button(mainWindow,text="View Book List",bg='black', fg='white', command=view_book)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn4 = Button(mainWindow,text="Issue Book to Student",bg='black', fg='white', command = issue)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn5 = Button(mainWindow, text="Issued Books", bg='black', fg='white', command= issuedBook)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(mainWindow,text="Return Book",bg='black', fg='white', command = returnn)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

quit_button = Button(mainWindow, text="Quit", bg='#FF0000',
                     fg='black', command=mainWindow.destroy)
quit_button.place(relx=.4, rely=0.92, relwidth=0.18, relheight=0.07)


mainWindow.mainloop()

