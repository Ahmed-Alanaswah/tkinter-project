from tkinter import  *
import tkinter as tk
import  PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from tkinter import PhotoImage
import os
window = tk.Tk()
window.title('gameStaion')
window.geometry('800x650')
window.config(bg="white")
window.iconbitmap("favicon.ico")

pic=r"C:\Users\STUDENT\Desktop\game\car-race-python-game-master\car-race-python-game-master\game.jpg"
pic1=p.Image.open(pic)
photo = ptk.PhotoImage(pic1)

label1= tk.Label(window,image = photo)

def open_game():
    # my_promgram = filedialog.askopenfilename()
    # my_label.config(text=my_promgram)
    # os.system('"%s"' % my_promgram)
    game= r'C:\Users\STUDENT\Desktop\game\car-race-python-game-master\car-race-python-game-master\game.pyw'
    os.system('"%s"' % game)


my_label=tk.Label(window,text='')
# lbl = tk.Label(text='0',font=('arial bold',50))
my_label.pack()


# my_text = tk.Label(text="Welcome!",font=('Helvetica',50),fg="white")
# my_text.pack(pady=50)



label1.place(x=0,y=0,relwidth=1,relheight=1)

btn = tk.Button(text='start game' ,command = open_game,font=("arial 20"))
btn.pack(pady=300)




window.mainloop()