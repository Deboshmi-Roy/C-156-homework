from tkinter import *
import random
from PIL import ImageTk,Image
root=Tk()

root.title("Pokemon Game")
root.geometry("500x500")

root.configure(background="dark turquoise")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1=Label(root,text="Player1",bg="Pink1",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="Player2",bg="Pink1",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score_label=Label(root,bg="Floral White",fg="white")
player1_score_label.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_score_label=Label(root,bg="Floral White",fg="white")
player2_score_label.place(relx=0.9,rely=0.4,anchor=CENTER)

random_dice_label=Label(root,bg="Red",fg="white")
random_dice_label.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()