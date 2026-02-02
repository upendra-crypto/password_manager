from tkinter import *
from tkinter import messagebox
class SavePassword:
    def save_to_file(self,web,email,password):
        if len(web) == 0 and len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please Enter the details")
        else:
            u_choice = messagebox.askokcancel(title=f"{web}",message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nis it ok to save?")
            if u_choice:
                with open("password_data.txt", "a") as fp:
                    fp.write(f"{web} | {email} | {password}\n")
                    fp.close()
