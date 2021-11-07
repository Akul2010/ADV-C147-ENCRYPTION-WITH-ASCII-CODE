from tkinter import *

root = Tk()
root.title("Encryptis")
root.geometry("400x400")
root.configure(background="bisque2")
root.grid_rowconfigure(1, weight=5)
root.grid_columnconfigure(1, weight=5)

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.5, anchor=CENTER)

label = Label(root,  text="Name in ASCII: ", bg="light yellow")


def asciitoencrypto():
    ascii = int(ord(enter_word))
    encrypt = ascii - 1

    for letter in ascii:
        label["text"] += str(chr(encrypt))


btn = Button(root, text="Encrypt", command=asciitoencrypto, bg="gold")
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
