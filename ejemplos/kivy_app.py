from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Hola Mundo"))
        self.text_input = TextInput()
        layout.add_widget(self.text_input)
        boton = Button(text="Enviar")
        boton.bind(on_press=self.enviar)
        layout.add_widget(boton)
        return layout

    def enviar(self, instance):
        print(f"Mensaje ingresado: {self.text_input.text}")

MyApp().run()
