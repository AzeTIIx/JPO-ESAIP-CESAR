import string
from tkinter import *

def crack():

    ws = Toplevel()
    ws.title("Cesar cipher brute force")
    ws.geometry("840x480")

    alphabet = string.ascii_lowercase
    ascii_lenght = len(string.ascii_lowercase)
    ascii_lenght_neg = - ascii_lenght

    def decrypt(enc_string, encryption_key):
        """Decrypt ciphertext."""
        enc_string = enc_string.lower()
        decrypted_letters = []
        for letter in enc_string:
            if letter not in alphabet:
                decrypted_letters.append(letter)
            elif letter in alphabet:
                plain_letter_index = alphabet.index(letter)
                decrypted_letter_index = plain_letter_index - encryption_key
                if decrypted_letter_index >= 0:
                    decrypted_letters.append(alphabet[decrypted_letter_index])
                else:
                    try:
                        decrypted_letter_index += ascii_lenght
                        decrypted_letters.append(alphabet[decrypted_letter_index])
                    except IndexError:
                            while decrypted_letter_index <= ascii_lenght_neg:
                                decrypted_letter_index = decrypted_letter_index + ascii_lenght
                            decrypted_letters.append(alphabet[decrypted_letter_index])
        decrypted_message = ''.join(decrypted_letters)
        return decrypted_message

    def brute(ascii_lenghts = ascii_lenght):
        enc_string = cipher.get("1.0", "end-1c")
        dec.delete("1.0","end")
        for ascii_lenght in range(1, ascii_lenghts):
            texte = decrypt(enc_string, ascii_lenght)
            res = f"Plain text = {texte} - Encryption key {ascii_lenght} \n"
            dec.insert(END,  res)


    cipher = Text(ws, width= 45, height=20)
    cipher.insert(END, "Entrez le texte à casser")
    cipher.grid(row=1, column=0, pady=10, padx=10)
    cipher.event_add('<<Paste>>', '<Control-v>')
    Clabel = Label(ws, text="Texte en chiffré").grid(row = 2, column=0, pady=10)


    dec = Text(ws, width= 45, height=20)
    dec.grid(row=1, column=2, pady=10, padx=10)
    dlabel = Label(ws, text="Texte décrypté").grid(row = 2, column=2, pady=10)



    dcrypt = Button(ws, text="Brute Force", command=lambda:brute())
    dcrypt.grid(row=3, column=1, pady=10)



    ws.mainloop()