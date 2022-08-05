

import webbrowser
from tkinter import *

BASE_URL = "https://developer.api.autodesk.com/authentication/v1/authorize"
RESPONSE_TYPE = "code"
CLIENT_ID = "Ap9x3NhxgxSYAPcSwb8xfwdyAQ5mn2uu"
REDIRECT_URI = "http://localhost:8000/callback/"
SCOPE = "data:read data:write"
URL = BASE_URL + "?response_type=" + RESPONSE_TYPE + "&client_id=" + CLIENT_ID + "&redirect_uri=" + REDIRECT_URI + "&scope=" + SCOPE

def go():
    print("go")
    open_url(URL)


# open a url in a browser
def open_url(url):

    webbrowser.open(url)








# make a sample tkinter window with buttons and a label
root = Tk()
root.title("Hello World")
root.geometry("200x100")
# create a label widget
label = Label(root, text="Hello World")
label.pack()
# create a button widget
button = Button(root, text="Click Me", command=go)
button.pack()
# create a quit button
quit_button = Button(root, text="Quit", command=root.quit)
quit_button.pack()
# start the event loop
root.mainloop()


