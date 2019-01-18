from tkinter import *
h=Tk()
h.geometry("300x200")
mes=StringVar()
mes.set("Hey!!! Let's play a quiz...")
l=Label(h,textvariable=mes)
l.pack()



mes1=StringVar()
mes1.set("Lets workout with the BRAIN..")
l1=Label(h,textvariable=mes1)
l1.pack()

mes1=StringVar()
mes1.set("THERE ARE SOME LIST OF QUIZ")
l1=Label(h,textvariable=mes1,font=("arial",10,"bold"))
l1.pack()

Lb1=Listbox(h,width=20,height=3)
Lb1.insert(1,"GK QUIZ")
Lb1.insert(2,"COMPUTER QUIZ")
Lb1.place(x=80,y=80)




def hello():
    top=Tk()
    top.geometry("300x300")
    L2=Label(top,text="Enter Your Name",font=("arial",8,"bold"))
    L2.place(x=10,y=5)
    E1=Entry(top,bd=5)
    E1.place(x=10,y=25)
    L3=Label(top,text="Age",font=("arial",8,"bold"))
    L3.place(x=10,y=55)
    s=Spinbox(top, from_=0, to=80)
    s.place(x=10,y=75)
    b=Label(top,text="SELECT WHICH QUIZ YOU WANT TO PLAY",font=("arial",9,"bold"))
    b.place(x=16,y=130)
    C1=Checkbutton(top,text="GENERAL KNOWLEDGE",height=3,command=food)
    C2=Checkbutton(top,text="COMPUTER QUIZ",height=3,command=by)
    C1.place(x=25,y=150)
    C2.place(x=25,y=200)
    


def food():
    f=Tk()
    f.geometry("500x500")
    f.title("General Knowledge")
    
    q1=Label(f,text="1)  What is the ideal temperature for Pathogens to flourish?",font=("arial",8,"bold"))
    q1.grid(row=1,sticky=W)
    r1=Radiobutton(f,text="10 degrees")
    r1.grid(row=2,column=0,sticky=W)
    r2=Radiobutton(f,text="37 degrees")
    r2.grid(row=3,column=0,sticky=W)
    r3=Radiobutton(f,text="55 degrees")
    r3.grid(row=4,column=0,sticky=W)
    r4=Radiobutton(f,text="90 degrees")
    r4.grid(row=5,column=0,sticky=W)

    q2=Label(f,text="2)  Which of these is not a cheese?",font=("arial",8,"bold"))
    q2.grid(row=6,sticky=W)
    r5=Radiobutton(f,text="Paneer")
    r5.grid(row=7,column=0,sticky=W)
    r6=Radiobutton(f,text="Vouvray")
    r6.grid(row=8,column=0,sticky=W)
    r7=Radiobutton(f,text="Manchego")
    r7.grid(row=9,column=0,sticky=W)
    r8=Radiobutton(f,text="Scamorze")
    r8.grid(row=10,column=0,sticky=W)

    q3=Label(f,text="3)  Element essential for photolysis of water is",font=("arial",8,"bold"))
    q3.grid(row=11,sticky=W)
    r9=Radiobutton(f,text="Nitrogen")
    r9.grid(row=12,column=0,sticky=W)
    r10=Radiobutton(f,text="Oxygen")
    r10.grid(row=13,column=0,sticky=W)
    r11=Radiobutton(f,text="Chlorine")
    r11.grid(row=14,column=0,sticky=W)
    r12=Radiobutton(f,text="Carbon")
    r12.grid(row=15,column=0,sticky=W)


    b5=Button(f,text="SUBMIT",command=ans,bg="black",fg="white")
    b5.place(x=400,y=400)


def ans():
    a=Tk()
    a.geometry("200x150")
    mes4=Label(a,text="Thank You For Playing The Quiz....",font=("arial",9,"bold"))
    mes4.place(x=5,y=60) 
    

def by():
      g=Tk()
      g.geometry("500x500")
      g.title("Computer Quiz")
      q1=Label(g,text="1)  DNS refers to",font=("arial",8,"bold"))
      q1.grid(row=1,sticky=W)
      r1=Radiobutton(g,text="Data Number Sequence")
      r1.grid(row=2,column=0,sticky=W)
      r2=Radiobutton(g,text="Digital Network Service")
      r2.grid(row=3,column=0,sticky=W)
      r3=Radiobutton(g,text="Domain Name System")
      r3.grid(row=4,column=0,sticky=W)
      r4=Radiobutton(g,text="Disk Numbering System")
      r4.grid(row=5,column=0,sticky=W)
    
      q2=Label(g,text="2)  The unit of speed used for super computer id ",font=("arial",8,"bold"))
      q2.grid(row=8,sticky=W)
      r5=Radiobutton(g,text="KELOPS")
      r5.grid(row=9,column=0,sticky=W)
      r6=Radiobutton(g,text="GELOPS")
      r6.grid(row=10,column=0,sticky=W)
      r7=Radiobutton(g,text="MELOPS")
      r7.grid(row=11,column=0,sticky=W)
      r8=Radiobutton(g,text="None")
      r8.grid(row=12,column=0,sticky=W)

      q3=Label(g,text="3)  Whose treadmark is the operating system UNIX?",font=("arial",8,"bold"))
      q3.grid(row=15,sticky=W)
      r9=Radiobutton(g,text="Motorola")
      r9.grid(row=16,column=0,sticky=W)
      r10=Radiobutton(g,text="Microsoft")
      r10.grid(row=17,column=0,sticky=W)
      r11=Radiobutton(g,text="BELL Laboratories")
      r11.grid(row=18,column=0,sticky=W)
      r12=Radiobutton(g,text="AshtonTate")
      r12.grid(row=19,column=0,sticky=W)

      b6=Button(g,text="SUBMIT",command=ans1,bg="black",fg="white")
      b6.place(x=400,y=400)

def ans1():
    u=Tk()
    u.geometry("200x150")
    mes9=Label(u,text="Thank You For Playing The Quiz....",font=("arial",9,"bold"))
    mes9.place(x=5,y=60) 
        
b=Button(h,text="NEXT>",command=hello,fg="white",bg="black")
b.place(x=210,y=150)

h.mainloop()







