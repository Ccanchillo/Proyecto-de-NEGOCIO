import re

def convertir_a_markdown(texto):
    # Títulos
    texto = re.sub(r'^1(?=\S)', '# ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^2(?=\S)', '## ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^3(?=\S)', '### ', texto, flags=re.MULTILINE)

    # Negrita
    texto = re.sub(r'^4(.+)4$', r'**\1**', texto, flags=re.MULTILINE)  # Toda la línea entre 4...4
    texto = re.sub(r'(?<!\*)4([A-Za-z0-9_]+)', r'**\1**', texto)       # Solo palabra iniciada por 4

    # Cursiva
    texto = re.sub(r'5([A-Za-z0-9_]+)', r'*\1*', texto)

    # Enlaces: 7Texto7URL7 → [Texto](URL)
    texto = re.sub(r'7([^7]+)7([^\s7]+)7', r'[\1](\2)', texto)

    # Imágenes: 8Alt8Ruta → ![Alt](Ruta)
    texto = re.sub(r'8([^8]+)8([^\s8]+)', r'![\1](\2)', texto)

    # Bloques de código: 6 o 6 lenguaje (con o sin espacio)
    texto = re.sub(r'^6\s*([^\s]*)$', lambda m: f'```{m.group(1)}'.rstrip(), texto, flags=re.MULTILINE)

    return texto


def leer_entrada_multilinea():
    print("✍️ Escribe tu texto personalizado. Escribe 'FIN' en una línea para terminar.\n")
    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)
    return "\n".join(lineas)


def guardar_como_markdown_desde_consola(nombre_archivo="documentacion.md"):
    texto = leer_entrada_multilinea()
    markdown = convertir_a_markdown(texto)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ Markdown generado en: {nombre_archivo}")

# Ejecutar el script
if __name__ == "__main__":
    guardar_como_markdown_desde_consola()