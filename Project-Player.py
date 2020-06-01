from tkinter import*
from pygame import mixer

root = Tk()

mixer.init()

middleframe = Frame(root)
middleframe.pack()

root.geometry("350x300")
root.title("Project-Music Player")
text = Label(root,text = "Let's make some noise")
text.pack()

photo = PhotoImage(file='button.png')
stopphoto = PhotoImage(file='stop-button.png')
pausephoto = PhotoImage(file='pause.png')

def play_btn():
    mixer.music.load("song.mp3")
    print("Start")
    mixer.music.play()

def stop_btn():
    mixer.music.stop()
    print("Stop")

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)
    print(volume, val)

#def pause():
#    print("Pause")
#    mixer.music.pause()

stopbtn = Button(middleframe, image = stopphoto, command=stop_btn)
stopbtn.pack()

btn = Button(middleframe, image = photo, command=play_btn)
btn.pack()

#pausebtn = Button(middleframe, image = pausephoto, command=pause)
#pausebtn.pack()

scale = Scale(middleframe,from_ = 0, to = 120, orient= HORIZONTAL, command=set_vol)
scale.pack()

root.mainloop()

