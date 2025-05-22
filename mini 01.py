import re

def convertir_a_markdown(texto):
    reemplazos = {
        '1': '#',
        '2': '##',
        '3': '###',
        '~(': '**',
        '~)': '**',
        '_(': '*',
        '_)': '*',
        '@(': '[',
        ']:': '](',
        '@)': ')',
        '¡(': '![', 
        '¡)': ')',
        '```': '```'
    }

    texto = re.sub(r'^1(?=\S)', '# ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^2(?=\S)', '## ', texto, flags=re.MULTILINE)
    texto = re.sub(r'^3(?=\S)', '### ', texto, flags=re.MULTILINE)

    for clave, valor in reemplazos.items():
        if clave not in ('1', '2', '3'):
            texto = texto.replace(clave, valor)

    return texto

def leer_entrada_multilinea():
    print("Escribe tu texto personalizado. Escribe 'FIN' en una línea para terminar.\n")
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

# USO
guardar_como_markdown_desde_consola()