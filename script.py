#Imporing required libraries
import cv2
from random import randint
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

#Tkinter Window
window = Tk()
window.title('Video Frames Generator')
window.geometry('400x600')
window.eval('tk::PlaceWindow . center')

#Function for getting Input Video File Path
def select_video():
    global filepath
    filepath = filedialog.askopenfilename(title="Choose Video File",filetype=(('Video', '.mp4 .flv .avi'),('All Files','*.*')))
    label1.config(text="Video: "+filepath)

#Function for getting Output Folder Path
def select_folder():
    global folderpath
    folderpath = filedialog.askdirectory()
    label2.config(text="Output: "+folderpath)

#Function for generating Video Frames
def get_frames():
    try:
        #If no video or folder is selected, then give error
        if filepath == "":
            messagebox.showerror(title="ERROR",message="Video File Not Selected")
        elif folderpath == "":
            messagebox.showerror(title="ERROR",message="Output Folder Not Selected")

        #Generate the Frames
        count = 0
        vidcap = cv2.VideoCapture(filepath)
        while True:
            count += 1
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
            success,image = vidcap.read()
            if not success:
                break
            #Save the frames in output folder
            cv2.imwrite(folderpath+"/frame{:d}.jpg".format(count), image)
        messagebox.showinfo(title="Frames Generated",message=str(count-1)+" Frames were Generated from the Video")

        #For showing a random frame
        imagefile = Image.open(folderpath+"/frame"+str(randint(1, count-1))+".jpg")
        imagefile.thumbnail((350,350))
        imagefile = ImageTk.PhotoImage(imagefile)
        label3.config(image=imagefile)
        label3.image = imagefile
    except:
        messagebox.showerror(title="ERROR",message="Select A Video and Choose Output Folder First")

#Title
label0 = Label(window,width=40,height=2,text="Video Frames Generator", font=("Ariel",20))
label0.pack()

#Button - Choose Video
button1 = Button(text="Choose Video", font=("Ariel",15), bg="gray", command=select_video, height=2, width=30).pack(pady=5)

#Display the Video File Path
label1 = Label(window,width=40,wraplength=250)
label1.pack()

#Button - Choose Output Folder
button2 = Button(text="Select Output Folder", font=("Ariel",15), bg="gray", command=select_folder, height=2, width=30).pack(pady=5)

#Display the Output Folder Path
label2 = Label(window,width=40,wraplength=250)
label2.pack()

#Button - Generate Frames
button3 = Button(text="Generate Frames", font=("Ariel",15), bg="gray", command=get_frames, height=2, width=30).pack(pady=5)

#Show a random frame
label3 = Label(window)
label3.pack()

window.mainloop()