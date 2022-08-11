from tkinter import *
from turtle import color
from pytube import YouTube
from downloader import YTDownloader

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Hloader")

link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)

status = Label(root, text = 'Please Enter Link', font = 'arial 15 bold')
status.place(x= 0 , y = 0)

def Download():
    # checking link if it is valid or not
    link_check = link.get()
    if link_check == '':
        status.config(text='Please Enter Link!', fg = 'red' )
    elif 'youtube' and 'watch?v=' in link_check:
        YTDownloader(link_check)
    else:
        status.config(text="Link Not Supported", fg = 'red')
    # checking what is the source of the link0
    


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Download).place(x=180 ,y = 150)
root.mainloop()
