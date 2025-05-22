import os
from spellchecker import SpellChecker

spell = SpellChecker(language='es')

listado_path = "F:/Proyecto de NEGOCIO/listado.txt"
archivo_salida = "F:/Proyecto de NEGOCIO/documento.md"

os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

with open(listado_path, "r", encoding="utf-8") as f:
    palabras_sugeridas = [line.strip() for line in f if line.strip()]

print("Escribe tu texto línea por línea.")
print("Usa '*' para autocompletar (ej: docu*).")
print("Escribe 'SALIR' para terminar.\n")

with open(archivo_salida, "w", encoding="utf-8") as f:
    while True:
        try:
            linea = input("> ").strip()
        except EOFError:
            break

        if linea.upper() == 'SALIR':
            print("Guardado.")
            break

        palabras = linea.split()
        nueva_linea = []

        for palabra in palabras:
            if palabra.endswith("*"):
                base = palabra[:-1]
                coincidencias = [p for p in palabras_sugeridas if p.startswith(base)]
                if coincidencias:
                    if len(coincidencias) == 1:
                        print(f"Sugerencia: usando '{coincidencias[0]}'")
                        nueva_linea.append(coincidencias[0])
                    else:
                        print(f"Varias coincidencias para '{base}':")
                        for i, c in enumerate(coincidencias):
                            print(f"  {i+1}. {c}")
                        try:
                            seleccion = int(input(f"Elige número (1 - {len(coincidencias)}): "))
                            if 1 <= seleccion <= len(coincidencias):
                                nueva_linea.append(coincidencias[seleccion - 1])
                            else:
                                print("Opción inválida, usando la primera.")
                                nueva_linea.append(coincidencias[0])
                        except ValueError:
                            print("Entrada inválida, usando la primera.")
                            nueva_linea.append(coincidencias[0])
                else:
                    print(f"No hay sugerencia para '{base}', corrigiendo...")
                    corregida = spell.correction(base)
                    palabra_final = corregida if corregida else base
                    print(f"Usando '{palabra_final}'")
                    nueva_linea.append(palabra_final)
            else:
                corregida = spell.correction(palabra)
                palabra_final = corregida if corregida else palabra
                if palabra != palabra_final:
                    print(f"Corregido: '{palabra}' → '{palabra_final}'")
                nueva_linea.append(palabra_final)

        linea_final = " ".join(nueva_linea)
        f.write(linea_final + "\n")