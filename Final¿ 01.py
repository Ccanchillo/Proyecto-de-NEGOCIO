import re
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog

def convertir_a_markdown(texto):
    texto = re.sub(r'^1(?=\S)', '# ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^2(?=\S)', '## ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^3(?=\S)', '### ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^4(.+)4$', r'**\1**', texto, flags=re.MULTILINE)
    texto = re.sub(r'(?<!\*)4([^\s\d]+)', r'**\1**', texto)
    texto = re.sub(r'^5(.+)5$', r'*\1*', texto, flags=re.MULTILINE)
    texto = re.sub(r'(?<!\*)5([^\s\d]+)', r'*\1*', texto)
    texto = re.sub(r'7([^7]+)7([^\s7]+)7', r'[\1](\2)', texto)
    texto = re.sub(r'8([^8]+)8([^\s8]+)', r'![\1](\2)', texto)
    texto = re.sub(r'^6\s*([^\s]*)$', lambda m: f'```{m.group(1)}'.rstrip(), texto, flags=re.MULTILINE)
    texto = re.sub(r'^6$', '```', texto, flags=re.MULTILINE)
    return texto

def convertir():
    texto = entrada.get("1.0", tk.END)
    if not texto.strip():
        messagebox.showwarning("Aviso", "El área de texto está vacía.")
        return
    resultado = convertir_a_markdown(texto)
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, resultado)

def guardar_archivo():
    contenido = salida.get("1.0", tk.END)
    if not contenido.strip():
        messagebox.showwarning("Aviso", "No hay contenido para guardar.")
        return
    ruta = filedialog.asksaveasfilename(defaultextension=".md",
                                       filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        messagebox.showinfo("Guardado", f"Archivo guardado en:\n{ruta}")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Conversor a Markdown")

# Área de texto entrada
tk.Label(ventana, text="Texto original (usa tus códigos):").pack()
entrada = scrolledtext.ScrolledText(ventana, width=80, height=15)
entrada.pack(padx=10, pady=5)

# Botón convertir
btn_convertir = tk.Button(ventana, text="Convertir a Markdown", command=convertir)
btn_convertir.pack(pady=10)

# Área de texto salida
tk.Label(ventana, text="Texto en Markdown:").pack()
salida = scrolledtext.ScrolledText(ventana, width=80, height=15)
salida.pack(padx=10, pady=5)

# Botón guardar
btn_guardar = tk.Button(ventana, text="Guardar como archivo .md", command=guardar_archivo)
btn_guardar.pack(pady=10)

ventana.mainloop()