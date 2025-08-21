import tkinter as tk
from tkinter import messagebox

def transformar_texto():
    """Transforma el texto reemplazando ` por -"""
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    if not texto_original:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")
        return
    
    # Reemplazar ` por -
    texto_transformado = texto_original.replace('`', '-')
    
    # Mostrar resultado en el campo de salida
    salida_texto.config(state=tk.NORMAL)
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, texto_transformado)
    salida_texto.config(state=tk.DISABLED)

def copiar_texto():
    """Copia el texto transformado al portapapeles"""
    texto_a_copiar = salida_texto.get("1.0", tk.END).strip()
    if not texto_a_copiar:
        messagebox.showwarning("Advertencia", "No hay texto que copiar.")
        return
    
    ventana.clipboard_clear()
    ventana.clipboard_append(texto_a_copiar)
    messagebox.showinfo("Copiado", "¡Texto copiado al portapapeles!")

def limpiar_texto():
    """Limpia ambos campos de texto"""
    entrada_texto.delete("1.0", tk.END)
    salida_texto.config(state=tk.NORMAL)
    salida_texto.delete("1.0", tk.END)
    salida_texto.config(state=tk.DISABLED)

def transformar_en_tiempo_real(event=None):
    """Transforma el texto automáticamente mientras se escribe"""
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    texto_transformado = texto_original.replace('`', '-')
    
    salida_texto.config(state=tk.NORMAL)
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, texto_transformado)
    salida_texto.config(state=tk.DISABLED)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Transformador de Texto - ` a -")
ventana.geometry("600x500")
ventana.resizable(True, True)
ventana.configure(bg="#f0f0f0")

# Título principal
titulo = tk.Label(ventana, text="Transformador de Texto", 
                 font=("Arial", 16, "bold"), 
                 bg="#f0f0f0", fg="#333")
titulo.pack(pady=15)

# Instrucciones
instrucciones = tk.Label(ventana, 
                        text="Escribe tu texto y los caracteres ` se convertirán automáticamente en -",
                        font=("Arial", 10), 
                        bg="#f0f0f0", fg="#666")
instrucciones.pack(pady=5)

# Frame para el texto de entrada
frame_entrada = tk.Frame(ventana, bg="#f0f0f0")
frame_entrada.pack(pady=10, padx=20, fill="x")

etiqueta_entrada = tk.Label(frame_entrada, text="Texto original:", 
                           font=("Arial", 12, "bold"), 
                           bg="#f0f0f0")
etiqueta_entrada.pack(anchor="w")

entrada_texto = tk.Text(frame_entrada, height=6, width=70, 
                       font=("Arial", 11), 
                       wrap=tk.WORD,
                       relief="solid", borderwidth=1)
entrada_texto.pack(pady=5, fill="x")

# Vincular evento para transformación en tiempo real
entrada_texto.bind('<KeyRelease>', transformar_en_tiempo_real)

# Frame para botones de acción
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=15)

boton_transformar = tk.Button(frame_botones, text="Transformar", 
                             command=transformar_texto,
                             font=("Arial", 11, "bold"), 
                             bg="#4CAF50", fg="white",
                             padx=20, pady=5,
                             relief="raised", borderwidth=2)
boton_transformar.grid(row=0, column=0, padx=10)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", 
                         command=limpiar_texto,
                         font=("Arial", 11), 
                         bg="#ff9800", fg="white",
                         padx=20, pady=5,
                         relief="raised", borderwidth=2)
boton_limpiar.grid(row=0, column=1, padx=10)

# Frame para el texto de salida
frame_salida = tk.Frame(ventana, bg="#f0f0f0")
frame_salida.pack(pady=10, padx=20, fill="x")

etiqueta_salida = tk.Label(frame_salida, text="Texto transformado:", 
                          font=("Arial", 12, "bold"), 
                          bg="#f0f0f0")
etiqueta_salida.pack(anchor="w")

salida_texto = tk.Text(frame_salida, height=6, width=70, 
                      font=("Arial", 11), 
                      wrap=tk.WORD,
                      state=tk.DISABLED,
                      relief="solid", borderwidth=1,
                      bg="#f9f9f9")
salida_texto.pack(pady=5, fill="x")

# Frame para botones finales
frame_botones_finales = tk.Frame(ventana, bg="#f0f0f0")
frame_botones_finales.pack(pady=15)

boton_copiar = tk.Button(frame_botones_finales, text="📋 Copiar", 
                        command=copiar_texto,
                        font=("Arial", 11, "bold"), 
                        bg="#2196F3", fg="white",
                        padx=25, pady=8,
                        relief="raised", borderwidth=2)
boton_copiar.grid(row=0, column=0, padx=15)

boton_salir = tk.Button(frame_botones_finales, text="❌ Salir", 
                       command=ventana.quit,
                       font=("Arial", 11), 
                       bg="#f44336", fg="white",
                       padx=25, pady=8,
                       relief="raised", borderwidth=2)
boton_salir.grid(row=0, column=1, padx=15)

# Ejemplo de uso
ejemplo = tk.Label(ventana, 
                  text="Ejemplo: 4525`455`456 → 4525-455-456",
                  font=("Arial", 9, "italic"), 
                  bg="#f0f0f0", fg="#888")
ejemplo.pack(pady=5)

# Centrar la ventana en la pantalla
ventana.update_idletasks()
width = ventana.winfo_width()
height = ventana.winfo_height()
pos_x = (ventana.winfo_screenwidth() // 2) - (width // 2)
pos_y = (ventana.winfo_screenheight() // 2) - (height // 2)
ventana.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

# Iniciar el bucle de la aplicación
if __name__ == "__main__":
    ventana.mainloop()