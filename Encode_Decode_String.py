from tkinter import *
import random
import time
import datetime
import base64

def main():
    def encode(key, clear):
        enc = []        
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)                        
            enc.append(enc_c)            
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def decode(key, enc):
        dec = []        
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)                                
            dec.append(dec_c)
        return "".join(dec)

    def Ref():
        clear = Msg.get()
        k = key.get()
        if not k or not clear:
            return
        m = value_inside.get()
        
        try:
            if (m == 'Encode'):
                Result.set(encode(k, clear))
            else:
                Result.set(decode(k, clear))
        except:
            Reset()

    def Reset():
        Msg.set("")
        key.set("")
        Result.set("")
        
    # GUI
    root = Tk()
    root.title("Encode Decode")

    Msg = StringVar()
    key = StringVar()
    mode = StringVar()
    Result = StringVar()

    options_list = ["Encode", "Decode"]
    value_inside = StringVar(root)
    value_inside.set("Encode") 
    question_menu = OptionMenu(root, value_inside, *options_list).grid(row = 1, column = 0, columnspan = 2, sticky = 'ew')

    lblMsg = Label(root, text = "String:", anchor = "e").grid(row = 2, column = 0, sticky = 'ew')
    txtMsg = Entry(root, textvariable = Msg, justify = 'left').grid(row = 2, column = 1, sticky = 'ew')

    lblkey = Label(root, text = "Key:", anchor = "e").grid(row = 3, column = 0, sticky = 'ew')
    txtkey = Entry(root, textvariable = key, justify = 'left').grid(row = 3, column = 1, sticky = 'ew')

    lblService = Label(root, text = "Result:", anchor = "e").grid(row = 4, column = 0, sticky = 'ew')
    txtService = Entry(root, textvariable = Result, justify = 'left').grid(row = 4, column = 1, sticky = 'ew')

    btnTotal = Button(root, text = "Encode / Decode", command = Ref).grid(row = 5, column = 0, columnspan = 2, sticky = 'ew')
    btnReset = Button(root, text = "Reset", command = Reset).grid(row = 6, column = 0, columnspan = 2, sticky = 'ew')


    # keeps window alive
    root.mainloop()

if __name__ == '__main__':
    main()