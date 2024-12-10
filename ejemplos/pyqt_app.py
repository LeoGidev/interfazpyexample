from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton

def enviar():
    mensaje = entrada.text()
    print(f"Mensaje ingresado: {mensaje}")

app = QApplication([])
ventana = QWidget()
ventana.setWindowTitle("Ejemplo PyQt")