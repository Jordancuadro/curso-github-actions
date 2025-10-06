import os

def main():
    lenguaje = os.getenv("LANGUAGE")
    nombre = os.getenv("USERNAME")
    print(f"Hola, {nombre}! desde Github! y con {lenguaje}!")

main()