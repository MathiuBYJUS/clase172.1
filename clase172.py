from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
from datetime import datetime 
import pytz 
import time


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



class clase():
    
    
        
    def asia(self):
        asia1=pytz.timezone("Asia/Kolkata")
        asia2=datetime.now(asia1)
        var1=asia2.strftime("%H:%M:%S")
        label_6["text"]="Tiempo " + var1
        label_6.after(100,self.asia)
        
    def us(self):
        us1=pytz.timezone("Us/Central")
        us2=datetime.now(us1)
        var2=us2.strftime("%H:%M:%S")
        label_7["text"]="Tiempo " + var2
        label_7.after(100,self.us)
        
    def japan(self):
        japon1=pytz.timezone("Japan")
        japon2=datetime.now(japon1)
        var3=japon2.strftime("%H:%M:%S")
        label_8["text"]="Tiempo " + var3
        label_8.after(100,self.japan)
        
    def India(self):
        india1=pytz.timezone("Asia/Kolkata")
        india2=datetime.now(india1)
        var4=india2.strftime("%H:%M:%S")
        label_9["text"]="Tiempo " + var4
        label_9.after(100,self.India)
        
        
        


def a():
    label_2["image"]=image1
    label_3["image"]=image2
    label_4["image"]=image3
    label_5["image"]=image4







vclase=clase()   

button_1=Button(root,text="Dame click para ver las imagenes",command=a)
button_1.place(relx=0.5,rely=0.2,anchor=CENTER)
button_2=Button(root,text="Dame click para ver la hora",command=vclase.asia)
button_2.place(relx=0.5,rely=0.3,anchor=CENTER)
label_6=Label(root,text="a")
label_6.place(relx=0.8,rely=0.23,anchor=CENTER)
label_7=Label(root,text="b")
label_7.place(relx=0.8,rely=0.52,anchor=CENTER)
button_3=Button(root,text="Dame click para ver la hora",command=vclase.us)
button_3.place(relx=0.5,rely=0.4,anchor=CENTER)
label_8=Label(root,text="c")
label_8.place(relx=0.8,rely=0.92,anchor=CENTER)
button_4=Button(root,text="Dame click para ver la hora",command=vclase.japan)
button_4.place(relx=0.5,rely=0.5,anchor=CENTER)
label_9=Label(root,text="d")
label_9.place(relx=0.3,rely=0.8,anchor=CENTER)
button_5=Button(root,text="Dame click para ver la hora",command=vclase.India)
button_5.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()

