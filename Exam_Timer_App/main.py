from tkinter import *
import math
import pyttsx3
from pyttsx3.drivers import sapi5
import datetime as dt
import time
from parameters import *
from helptext import *
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 145)
def clock():
    h=time.strftime("%H")
    m=time.strftime("%M")
    s=time.strftime("%S")
    format_date ="Local time: "+h+":"+m+":"+s
    w.config(text=format_date)
    w.after(1000,clock)
# Fuction for time resetting. The activities of the function defined here
def reset_timer():
    global sttime
    global reps
    global sb
    global lb
    global chktxt
    chktxt=""
    window.after_cancel(timer)
    title_label2.config(text="")
    title_label3.config(text="",bg=YELLOW)
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text=chktxt)
    pause_button.config(text="Pause")
    reps=0
    sb=0
    lb=0
    sttime=True
# Pause Function
def pause():
    global pcb
    if pcb == False:
        window.after_cancel(timer)
        pause_button.config(text="Play")
        pcb = True
    else:
        pause_button.config(text="Pause")
        count_down(pct)
        pcb = False
# Definition of timer/ Time mechanism

def start_timer():
    global reps
    global sttime
    global sb
    global lb
    global ew
    global chktxt
    if sttime == True:
        reps += 1
        work_sec=WORK_MIN*60
        short_sce=SHORT_BREAK_MIN*60
        lng_break=LONG_BREAK_MIN*60
        sttime=False
        if (reps >= 1 and reps <= 3) and sb == 0 :
            engine.say("Exam is starting")
            engine.runAndWait()
            ew= True
            count_down(work_sec)
            sb=1
            lb+=1
            chktxt += "✓"
            check_mark.config(text=chktxt)
            title_label2.config(text="Exam is running")

        elif (reps > 1 and reps <= 3) and sb == 1:
            engine.say("Exam is over. Short break is starting")
            engine.runAndWait()
            count_down(short_sce)
            sb=0
            lb+=1
            title_label2.config(text="Short Break is running")
        elif lb > 2:
            engine.say("Exam is over. Long break is starting")
            engine.runAndWait()
            count_down(lng_break)
            reps=0
            lb=0
            sb=0
            title_label2.config(text="Long Break is running")
    else:
        title_label3.config(text="Already running. Please reset to strat again",bg="red")
# COUNTDOWN MECHANISM
def count_down(count):
    global chktxt
    global pct
    global sttime
    global ew
    pct=count
    count_min=math.floor(count/60)
    count_sec=(count%60)
    if count == 60 and ew==True:
        engine.say("Exam is over in 1 minute")
        engine.runAndWait()
        ew=False
    if count_sec<10:
        count_sec="0"+str(count_sec)

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        sttime = True
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Exam Timer")
window.config(padx=50,pady=100,bg=YELLOW)


format_date = ""
w = Label(window, text=format_date, fg="white", bg="black", font=("helvetica", 20))
w.grid(column=1,row=0)
clock()

def help_window ():
    helpwin=Tk()
    helplabel=Label(helpwin,text=help_text)
    helplabel.pack()
help_button=Button(text="help",command = help_window)
help_button.grid(column=3,row=0)
title_label=Label(text="Exam Timer APP",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
title_label.grid(column=1,row=1)
title_label2=Label(text="",fg=RED, bg=YELLOW,font=(FONT_NAME,20,"bold"))
title_label2.grid(column=1,row=2)
canvas=Canvas(width=200, height=225,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="./hrg.png")
canvas.create_image(100,113,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="black",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=3)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=6)
pause_button=Button(text="Pause",command=pause)
pause_button.grid(column=1,row=7)
reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=6)
check_mark=Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,24,"bold"))
check_mark.grid(column=1,row=6)
title_label3=Label(text="",bg=YELLOW)
title_label3.grid(column=1,row=8)

def new_window ():
    global sttime
    if sttime == True:
        popwin=Tk()
        popl1=Label(popwin,text="Please set the time and press OK")
        popl1.grid(column=1,row=0)
        popl2=Label(popwin,text="Exam time (minutes): ")
        popl2.grid(column=0,row=1)
        exam_time=Entry(popwin)
        exam_time.grid(column=1,row=1)
        popl3 = Label(popwin, text="Short break (minutes): ")
        popl3.grid(column=0, row=2)
        short_break = Entry(popwin)
        short_break.grid(column=1, row=2)
        popl4 = Label(popwin, text="Long break (minutes): ")
        popl4.grid(column=0, row=3)
        long_break = Entry(popwin)
        long_break.grid(column=1, row=3)

        def close_win():
            global sttime
            global WORK_MIN
            global SHORT_BREAK_MIN
            global LONG_BREAK_MIN
            WORK_MIN = int(exam_time.get())
            SHORT_BREAK_MIN = int(short_break.get())
            LONG_BREAK_MIN = int(long_break.get())
            title_label2.config(text="")
            title_label3.config(text="")
            canvas.itemconfig(timer_text, text="00:00")
            check_mark.config(text="")
            sttime = True
            popwin.destroy()

        pop_close_button= Button(popwin, text="OK", command=close_win)
        pop_close_button.grid(column=1, row=4)
    else:
        title_label3.config(text="Already running. Please reset to strat again", bg=RED)

date = dt.datetime.now()
wd= date.strftime("%a")
dt=date.strftime("%d")
mnth=date.strftime("%b")
tr=date.strftime("%Y")
date12="Date: "+wd+" "+dt+", "+mnth+" "+tr
date_label = Label(window, text=date12, fg="black", bg=YELLOW, font=("helvetica", 10))
date_label.grid(column=3,row=12)

button = Button(text="Set Time", command=new_window)
button.grid(column=1, row=10)


window.mainloop()