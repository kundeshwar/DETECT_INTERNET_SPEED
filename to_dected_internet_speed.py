from tkinter import *
import speedtest_cli
#it gives some error beacuse crashing of labriry
def speed():
    sp = speedtest_cli.Speedtest() 
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lb_d.config(text=down)
    lb_u.config(text=up)

a = Tk()
a.config(bg="Black")
a.title("SPEED DETECTOR")
a.geometry("500x500")

lb = Label(a,text="INTERNET SPEED TEST",font=("Time New Roman",28,"bold"),bg="Aqua")
lb.place(x=25,y=10,height=70,width=450)
#-----------------------------------------
lb = Label(a,text="DOWNLOAD SPEED",font=("Time New Roman",28,"bold"),bg="Aqua")
lb.place(x=50,y=130,height=50,width=400)
lb_d = Label(a,text="000000000",font=("Time New Roman",28,"bold"),bg="Aqua")
lb_d.place(x=100,y=190,height=50,width=300)
#-------------------------------------------
lb = Label(a,text="UPLOAD SPEED",font=("Time New Roman",28,"bold"),bg="Aqua")
lb.place(x=50,y=280,height=50,width=400)
lb_u = Label(a,text="000000000",font=("Time New Roman",28,"bold"),bg="Aqua")
lb_u.place(x=100,y=340,height=50,width=300)
#------------------------------------------
butt = Button(a,text="START",font=("Time New Roman",28,"bold"),bg="Aqua",command=speed)
butt.place(x=175,y=430,height=50,width=150)
#------------------------------------------
a.mainloop()