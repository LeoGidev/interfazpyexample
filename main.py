import subprocess
import sys

def ejecutar_ejemplo(nombre):
    """Ejecuta el archivo de ejemplo correspondiente"""
    try:
        subprocess.Popen([sys.executable, f"ejemplos/{nombre}_app.py"])
    except Exception as e:
        print(f"Error al abrir {nombre}: {e}")
if __name__ == "__main__":
    print("Selecciona el ejemplo:")
    print("1. Tkinter")
    print("2. PyQt")
    print("3. Kivy")
    print("4. wxPython")