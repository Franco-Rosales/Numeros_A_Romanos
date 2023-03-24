import tkinter as tk

def numero_a_romano(numero):
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    resultado = ""
    i = 0
    while numero > 0:
        if numero - valores[i] >= 0:
            resultado += simbolos[i]
            numero -= valores[i]
        else:
            i += 1
    return resultado

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Conversor de Números a Romanos")
        
        self.lbl_numero = tk.Label(self.ventana, text="Introduce un número:")
        self.lbl_numero.pack()
        
        self.txt_numero = tk.Entry(self.ventana)
        self.txt_numero.pack()
        
        self.btn_convertir = tk.Button(self.ventana, text="Convertir a Romano", command=self.convertir_a_romano)
        self.btn_convertir.pack()
        
        self.lbl_romano = tk.Label(self.ventana, text="")
        self.lbl_romano.pack()
        
        self.ventana.mainloop()
        
    def convertir_a_romano(self):
        numero = int(self.txt_numero.get())
        romano = numero_a_romano(numero)
        self.lbl_romano.config(text=romano)


ventana = VentanaPrincipal()
