import tkinter
import customtkinter

def slider_event(value):
    print(value)
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())


init = customtkinter.CTk() 
slider = customtkinter.CTkSlider(master=init, from_=0, to=100, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
check_var = tkinter.StringVar()

checkbox = customtkinter.CTkCheckBox(master=init, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=20, pady=10)

init.mainloop()