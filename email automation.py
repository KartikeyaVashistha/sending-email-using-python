from tkinter import *
from smtplib import *
from PIL import ImageTk,Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

main=Tk()
main.title("Email sender")
main.iconbitmap("Z:\PYTHON\EMAIL AUTOMATION\gmail.ico")
main.geometry("1080x720")

def open():
    # global myimgs
    global simage
    from PIL import ImageTk,Image
    import smtplib

    def send():

        from_=efrom.get()
        to_=eto.get()
        msg=MIMEMultipart()
        msg['From']=from_
        msg['To']=to_
        msg['subject']=esub.get()
        body=ebody.get()
        print("DATA COLLECTED")
        msg.attach(MIMEText(body,'plain'))

        email=str(efrom.get())
        password=str(epass.get())

        mail=smtplib.SMTP('smtp.gmail.com',587)
        # mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        print("CONNECTION OK")
        text=msg.as_string()
        mail.sendmail(from_,to_,body)
        print("MESSAGE SENT")
        mail.quit() 

        efrom.delete(0,END)
        eto.delete(0,END)
        epass.delete(0,END)
        esub.delete(0,END)
        ebody.delete(0,END)
 


    top=Toplevel()
    top.iconbitmap("Z:\PYTHON\EMAIL AUTOMATION\gmail.ico")
    top.geometry("1080x720")
    lfrom=Label(top,text="From")
    lfrom.grid(row=1,column=0)
    efrom=Entry(top,borderwidth=0,width=50)
    efrom.grid(row=1,column=1)

    lto=Label(top,text="To")
    lto.grid(row=3,column=0)
    eto=Entry(top,borderwidth=0,width=50)
    eto.grid(row=3,column=1)

    lsub=Label(top,text="Subject")
    lsub.grid(row=4,column=0)
    esub=Entry(top,borderwidth=0,width=50)
    esub.grid(row=4,column=1)

    lbody=Label(top,text="body")
    lbody.grid(row=5,column=0)
    ebody=Entry(top,borderwidth=0,width=50)
    ebody.config(font=("Courier", 20))
    ebody.grid(row=5,column=1)

    lpass=Label(top,text="Password")
    lpass.grid(row=6,column=0)
    epass=Entry(top,borderwidth=0,width=50)
    epass.config(show="*")
    epass.grid(row=6,column=1)


    # simage=Image.open("Z:\PYTHON\EMAIL AUTOMATION\send-mail.ico")
    # # simage=image.resize((50,50))
    # myimgs=ImageTk.PhotoImage(simage)
    sendbutton=Button(top,image=myimg,background=None,borderwidth=0,command=send)
    sendbutton.grid(row=8,column=1)

gmail=Image.open("Z:\PYTHON\EMAIL AUTOMATION\gmail.png")
mygmail=ImageTk.PhotoImage(gmail)
lbmain=Label(main,image=mygmail).place(x=300,y=100)


image=Image.open("Z:\PYTHON\EMAIL AUTOMATION\send-mail.png")
image=image.resize((50,50))
myimg=ImageTk.PhotoImage(image)
send=Button(main,image=myimg,background=None,borderwidth=0,command=open).place(x=525,y=600)
main.mainloop()