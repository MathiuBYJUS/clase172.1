from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image

root=Tk()
root.geometry("750x900")
root.config(bg="lightgreen")

label_1=Label(root,text="La hora")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
label_2=Label(root,text="a")
label_2.place(relx=0.8,rely=0.4,anchor=CENTER)
label_3=Label(root,text="b")
label_3.place(relx=0.8,rely=0.1,anchor=CENTER)
label_4=Label(root,text="c")
label_4.place(relx=0.8,rely=0.8,anchor=CENTER)
label_5=Label(root,text="d")
label_5.place(relx=0.3,rely=0.6)

image1=ImageTk.PhotoImage(Image.open("usmap.jpeg"))
image2=ImageTk.PhotoImage(Image.open("india.jpeg"))
image3=ImageTk.PhotoImage(Image.open("japon.jpeg"))
image4=ImageTk.PhotoImage(Image.open("australia.jpeg"))

def a():
    label_2["image"]=image1
    label_3["image"]=image2
    label_4["image"]=image3
    label_5["image"]=image4

    

button_1=Button(root,text="Dame click para ver las horas",command=a)
button_1.place(relx=0.5,rely=0.2,anchor=CENTER)

root.mainloop()

