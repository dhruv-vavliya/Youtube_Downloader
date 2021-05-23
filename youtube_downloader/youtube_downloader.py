
from tkinter import *
from tkinter import ttk
import os
from pytube import YouTube
from tkinter import messagebox as m_box,filedialog


def browse():
    path.set(filedialog.askdirectory(initialdir='your downloading path..'))

def start():
    os.startfile(str(path.get()))

def onClick():
    got_link = str(link.get())
    got_path = str(path.get())
    try:
        yt = YouTube(got_link)
        if resolution.get()==str('high'):
            vid=yt.streams.get_highest_resolution()
        elif resolution.get()==str('no_audio'):
            vid=yt.streams.get_audio_only()
        else:
            vid=yt.streams.get_by_resolution(str(resolution.get()))
    except:
        m_box.showerror("Error", "Connection Problem !")
    else:
        status.set('downloading...')
        try:
            vid.download(got_path)
            status.set('video downloaded successfully.')
            statusbar.update()
            return m_box.showinfo('Successfully Downloaded.',
                                  f"Your YouTube Vidoe Downloaded Successfully at {got_path}/{yt.title}")
        except:
            m_box.showwarning('Format not Found...','Oops!please choose other clearity...')


win=Tk()
win.geometry("780x454")
win.title("YouTube Video Downloader")
win.wm_iconbitmap('youtube.ico')
win.config(background='#33C0FF')


frame = ttk.LabelFrame(win)
frame.grid(row=0, padx=140, pady=30,sticky=W)

label1 = ttk.Label(frame, text="Enter YouTube Video Link : ")
label1.grid(row=1, column=0, sticky=W,pady=10)

link = StringVar()

box1 = ttk.Entry(frame, width=60, textvariable=link)
box1.grid(row=2, column=0, padx=0)
box1.focus()


resolution= StringVar()
resolution.set('high')

Label(frame, text = "which clearity you want to choose?",font="lucida 10 bold",
      justify=LEFT).grid(row=3,column=0,pady=10,sticky=W)

radio = Radiobutton(frame, text="144px", variable=resolution, value="144p").grid(row=4,column=0,sticky=W,padx=30)
radio = Radiobutton(frame, text="240px", variable=resolution, value="240p").grid(row=5,column=0,sticky=W,padx=30)
radio = Radiobutton(frame, text="360px", variable=resolution, value="360p").grid(row=6,column=0,sticky=W,padx=30)
radio = Radiobutton(frame, text="480px", variable=resolution, value="480p").grid(row=4,padx=100)
radio = Radiobutton(frame, text="720px", variable=resolution, value="720p").grid(row=5,padx=150)
radio = Radiobutton(frame, text="1080px", variable=resolution, value="1080p").grid(row=6,padx=150)
radio = Radiobutton(frame, text="Only Audio Clip", variable=resolution, value="no_audio").grid(row=7,column=0,sticky=W,padx=30)
radio = Radiobutton(frame, text="Highest Quality", variable=resolution, value="high").grid(row=8,column=0,sticky=W,padx=30)

label2 = ttk.Label(frame, text="Enter Downloading Path : ")
label2.grid(row=9, column=0,pady=10, sticky=W)

path = StringVar()

box2 = ttk.Entry(frame, width=45, textvariable=path)
box2.grid(row=10,padx=0,sticky=W)

btn1=ttk.Button(frame,text='Browse',
                width=10,command=browse)
btn1.grid(row=10,padx=10,sticky=E)

btn2 = ttk.Button(frame, text="Download Video",
                  width=15, command=onClick)
btn2.grid(row=11,padx=10,pady=10,sticky=W)

btn3 = ttk.Button(frame,text='Enjoy Video',width=15,command=start)
btn3.grid(row=11,padx=10,sticky=E,pady=10)

status=StringVar()
status.set('data collecting...')
statusbar=Label(win,textvariable=status,anchor='w',width=70,relief=SUNKEN)
statusbar.grid(sticky=SW)
copyright=Label(win,text='©COPYRIGHT 2020. All Rights Reserved By Dhruv Vavliya.',background='yellow',anchor='center',width=120,relief=SUNKEN)
copyright.grid(sticky=SW)

win.mainloop()