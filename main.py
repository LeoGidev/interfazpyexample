import subprocess
import sys

def ejecutar_ejemplo(nombre):
    """Ejecuta el archivo de ejemplo correspondiente"""
    try:
        subprocess.Popen([sys.executable, f"ejemplos/{nombre}_app.py"])
    except Exception as e:
        print(f"Error al abrir {nombre}: {e}")
