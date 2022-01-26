import tkinter
import tkinter.messagebox
window = tkinter.Tk()
window.title("Dogs Age")
label1 = tkinter.Label(window, text="Welcome to Dogs Age Calculator").grid()
label2 = tkinter.Label(window, text="By Nicholas Beard").grid()

age_var = tkinter.StringVar()
age_lab = tkinter.Label(window, text='Enter Dogs Age').grid(row=3, column=0)
age_entry = tkinter.Entry(window, textvariable=age_var, font=('calibre', 10, 'normal'))
age_entry.grid(row=3, column=1)


def calc():
    human_age = int(age_var.get()) * 7
    tkinter.messagebox.showinfo('title', f"your dog is {human_age} years old in human years")


calc_button = tkinter.Button(window, text="calculate", command=calc)
calc_button.grid(row=5, column=1)

window.mainloop()
