import tkinter as Tk
from tkinter import *
from crack import crack


def encrypt(inp, s):
    result = ""

    for i in range(len(inp)):
        char = inp[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def printInput():
    inp = plain.get(1.0, "end-1c")
    shift = int(s.get())
    encrypted = encrypt(inp, shift)
    cipher.delete("1.0","end")
    cipher.insert(END, encrypted)
    return encrypted

fenetre = Tk()
fenetre.title("Cesar Cipher")
fenetre.geometry("910x480")
fenetre.resizable(False, False)

frame1 = Frame(fenetre)
frame1.grid(row=0,column=0)

frame2 = Frame(fenetre)
frame2.grid(row=1,column=0)

frame3 = Frame(fenetre)
frame3.grid(row=1,column=2)

frame4 = Frame(fenetre)
frame4.grid(row=2,column=1)

menubar = Menu(fenetre)


menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Brute force", command=lambda:crack())

menubar.add_cascade(label="Tools", menu=menu2)


fenetre.config(menu=menubar)


plain = Text(frame1, width= 45, height=20)
plain.insert(END, "Entrez le texte en clair")
plain.grid(row=1, column=0, pady=10, padx=10)
Plabel = Label(frame1, text="Texte en clair").grid(row = 2, column=0, pady=10)


valuecipher = StringVar()
cipher = Text(frame1, width= 45, height=20)
cipher.grid(row=1, column=2, pady=10, padx=10)
Plabel = Label(frame1, text="Texte chiffré").grid(row = 2, column=2, pady=10)


Slabel = Label(frame1, text="Shift").grid(row = 2, column=1, pady=10)

s = Spinbox(frame1, from_=0, to=25)
s.grid(row=3, column=1, pady=10)







crypt = Button(frame2, text="Encrypt", command=lambda:printInput())
crypt.grid(row=3, column=1, pady=10)


if __name__ =='__main__':
    fenetre.mainloop()