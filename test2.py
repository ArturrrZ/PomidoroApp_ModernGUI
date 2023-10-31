#pip install customtkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window=customtkinter.CTk()
window.geometry("500x500")


def print2():

    print('h')

test_button=customtkinter.CTkButton(master=window,text='Text',command=print2)
test_button.grid(column=0,row=0)





window.mainloop()


