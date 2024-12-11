import re

NOMBRE_DEL_ARCHIVO = 'chat_pascuales.txt'

def encontrar_bds(archivo_path):
    with open(archivo_path, 'r', encoding='utf-8') as file:
        text = file.read()

    palabras = re.findall(r'\b\w+\b', text)

    bds = []
    for i in range(len(palabras) - 1):
        if palabras[i].startswith('B') and palabras[i + 1].startswith('D'):
            bds.append((palabras[i], palabras[i + 1]))

    return bds

def main():
    try:
        bds = encontrar_bds(NOMBRE_DEL_ARCHIVO)
        if bds:
            print("Bds encontrados:")
            for bd in bds:
                print(f"{bd[0]} {bd[1]}")
        else:
            print("No se encontraron bds.")
    except UnicodeDecodeError as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    main()