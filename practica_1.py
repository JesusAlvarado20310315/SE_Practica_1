import tkinter as tk
from tkinter import messagebox

def preguntar_sobre_clima():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    nublado = messagebox.askyesno("Clima", "¿Está nublado?")
    
    if not nublado:
        messagebox.showinfo("Pronóstico", "No parece que vaya a llover pronto.")
        root.destroy()  # Cerrar la ventana emergente
        return

    relampagos = messagebox.askyesno("Clima", "¿Hay relámpagos?")
    if relampagos:
        viento = messagebox.askyesno("Clima", "¿Hace viento?")
    else:
        viento = False

    if viento:
        frio = messagebox.askyesno("Clima", "¿Hace frío?")
    else:
        frio = False

    pronostico = decidir_si_llueve(nublado, relampagos, viento, frio)
    messagebox.showinfo("Pronóstico", pronostico)
    root.destroy()  # Cerrar la ventana emergente

def decidir_si_llueve(nublado, relampagos, viento, frio):
    """
    Función que decide si es probable que llueva basándose en observaciones directas del clima.
    """
    if not nublado:
        return "No parece que vaya a llover pronto."
    elif relampagos and viento:
        if frio:
            return "Cuidado, puede granizar."
        else:
            return "Es muy probable que llueva normal."
    elif relampagos or viento:
        return "Puede que llueva, pero no hay indicios claros."
    else:
        return "No hay suficientes datos para predecir si lloverá."

if __name__ == "__main__":
    preguntar_sobre_clima()