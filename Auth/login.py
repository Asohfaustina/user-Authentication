from tkinter import *

def log_in():
    with open('user-db.txt', 'r') as f:
        db = f.readlines()
    username = username2.get()
    password = pwd2.get()
    usercheck = username + password
    if len(usercheck) == 0:
        labelcheck.config(text='INCORRECT PASSWORD OR USERNAME', fg='red')


    else:
        for line in db:

            if usercheck in line :
                labelcheck.config(text='LOGGED IN SUCCESSFULLY', fg='light green')
                print(username)
            else:
                labelcheck.config(text='INCORRECT PASSWORD OR USERNAME', fg='red')

# FUNCTION FOR SIGNING IN


def sign_up():
    username = uname.get()
    password = pwd.get()

    if len(username) == 0 or len(password) == 0:
        label_okay.config(text='Please enter a valid name and password', fg='red')

    else:
        with open('user-db.txt', 'a') as file:
            file.write(username + password + "\n")
        label_okay.config(text='SIGN IN SUCCESSFUL')


root = Tk()

root.geometry('400x500')
labelhead = Label(root, text="Sign Up Page ", font='times 20', fg='light blue')
labelhead.pack(pady=10)
label1 = Label(root, text="Input Name ", font='times 12')
label1.pack(pady=10)
name = Entry(root, font='times 12')
name.pack(pady=10)
label2 = Label(root, text="Input Username ", font='times 12')
label2.pack(pady=10)
uname = Entry(root, font='times 12')
uname.pack(pady=10)
label3 = Label(root, text="Input Password ", font='times 12')
label3.pack(pady=10)
pwd = Entry(root, font='times 12')
pwd.pack(pady=10)
button_save = Button(root, text='Sign Up', width=12, bg='light blue', command=sign_up)
button_save.pack(pady=10)
label_okay = Label(root,  font='times 12', fg='light green')
label_okay.pack(pady=10)
#  SECOND WINDOW
save = Tk()
save.geometry('400x500')
label_head2 = Label(save, text="Login Page Page ", font='times 20', fg='light blue')
label_head2.pack(pady=10)
label_username = Label(save, text="Input Username ", font='times 12')
label_username.pack(pady=10)
username2 = Entry(save, font='times 12')
username2.pack(pady=10)
label_pwd = Label(save, text="Input Password ", font='times 12')
label_pwd.pack(pady=10)
pwd2 = Entry(save, font='times 12')
pwd2.pack(pady=10)
buttonsave = Button(save, text='Log In', width=12, bg='light blue', command=log_in)
buttonsave.pack(pady=10)
labelcheck = Label(save, font='times 12')
labelcheck.pack(pady=10)
save.mainloop()

root.mainloop()