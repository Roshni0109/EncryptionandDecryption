
from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()  # Remove any trailing newline characters
        encode_message = message.encode("ascii")  # Encode the string to bytes
        base64_bytes = base64.b64decode(encode_message)  # Decode from base64
        decrypt_message = base64_bytes.decode("utf-8")  # Decode from bytes to string

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=10)
        text3 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text3.place(x=10, y=40, width=380, height=150)

        text3.insert(END, decrypt_message)

    elif password == "":
        messagebox.showerror("decryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("decryption", "Invalid password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("utf-8")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=10)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt_message)

    elif password=="":
        messagebox.showerror("encryption","Input Password")
    elif password!="1234":
        messagebox.showerror("encryption","Invalid password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encrypt&Decrypt")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for Encryption and Decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)

    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
