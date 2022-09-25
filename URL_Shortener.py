import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.config(bg="#262626")
url = StringVar()
url_address = StringVar()


def URL_Shortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)
def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="My URL Shortener",font="poppins").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root,text="Generate Short URL",command=URL_Shortener).pack(pady=7)
Entry(root,textvariable=url_address).pack(pady=5)
Button(root,text="Copy URL",command=copy_url).pack(pady=7)

root.mainloop()