


#mainGui - grafic user interface - modulo principal
import time
import tkinter as tk
#from tkinter import filedialog as fd

#def open_file():
#    return fd.askopenfilename()
serial_ok = 0

def check_Serial():
    if(serial_ok): #checar se serial esta ok
        print("Serial Ok")
        return True
    else:
        print("Validador nao encontrado")
        return False

def grava_v3695():
    #chama função que grava v3695
    print("Grava v3695")




window = tk.Tk()
label = tk.Label(text="UInkRibbon by ",
                 foreground="white",
                 background="black",
                 width=100,
                 height=10
                 )
label.pack()

button = tk.Button(
    text="Grava v3695",
    width=20,
    height=3,
    bg="black",
    fg="white",
    command=grava_v3695
)

#debug
#print(button.configure().keys())

button.pack()

#window.mainloop()
while True:
    window.update()
    print("Rodando..")
    if(check_Serial()):
        pass
        #seta o icone pra ok e habilita pra gravaçao
    else:
        pass
        #seta pra nok e desabilita a gravacao

    time.sleep(1)
