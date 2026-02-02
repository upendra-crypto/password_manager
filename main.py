from tkinter import *
from save_password import *
s_password=SavePassword()
from password_generator import *
pgenerate=PGenerator()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0,END)
    password=pgenerate.p_generate()
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # showwarning(title="No Entry",message="you didn't enter the details")
    s_password.save_to_file(web,email,password)
    website_entry.delete(0, END)
    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Password Manager")
# windows.geometry("400x400")
windows.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)
#labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
#entry
website_entry=Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'upendrauddagiri030@gmail.com')
password_entry=Entry(width=22)
password_entry.grid(row=3,column=1)
#buttons
generate_button=Button(text="Generate Password",command=generate)
generate_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

windows.mainloop()