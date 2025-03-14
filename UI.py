from tkinter import *
from tkinter import messagebox
import database
win = Tk()
win.title('Login Form')
win.geometry('600x380')
db1=database.Database('c:/Baran/mydata.db')
#=======Function===========
def sign_up():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    if email == '' or password == '':
        messagebox.showerror('Error', 'Email and Password are required!')
        return
    else:
        db1.insert(fname, lname, email, password)
        messagebox.showinfo('Success', 'User added successfully!')
        clear()

def sign_in():
    email = ent_email.get()
    password = ent_password.get()
    if email == '' or password == '':
        messagebox.showerror('Error', 'Email and Password are required!')
        return
    else:
        data = db1.find_user(email, password)
        if data:
            messagebox.showinfo('Welcome', f'{data[0]} {data[1]}, welcome!')
            clear()
        else:
            messagebox.showerror('Error', 'Invalid email or password.')
        

def clear():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_email.delete(0, END)
    ent_password.delete(0, END)
    ent_fname.focus_set()

#=======Widget===========

lbl_fname = Label(win, text='Fname: ',font='centaur 14')
lbl_fname.place(x=70,y=40)
ent_fname = Entry(win,font='centaur 12',width=45)
ent_fname.place(x=150,y=45)
 
lbl_lname = Label(win, text='Lname: ',font='centaur 14')
lbl_lname.place(x=70,y=90)
ent_lname = Entry(win,font='centaur 12',width=45)
ent_lname.place(x=150,y=95)

lbl_email = Label(win, text='*  Email: ',font='centaur 14')
lbl_email.place(x=55,y=140)
ent_email = Entry(win,font='centaur 12',width=45)
ent_email.place(x=150,y=145)

lbl_password = Label(win, text='*  Password: ',font='centaur 14')
lbl_password.place(x=55,y=190)
ent_password = Entry(win,font='centaur 12',width=45)
ent_password.place(x=150,y=195)


btn_sign1 = Button(win, text='sign up',font='cenatur 12 bold',width=15,command=sign_up)
btn_sign1.place(x=130,y=270)

btn_sign2 = Button(win, text='sign in',font='cenatur 12 bold',width=15,command=sign_in)
btn_sign2.place(x=340,y=270)

win.mainloop()