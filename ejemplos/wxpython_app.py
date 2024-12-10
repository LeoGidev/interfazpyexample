import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Ejemplo wxPython")
        panel = wx.Panel(frame)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label="Hola Mundo"), flag=wx.ALL, border=10)

        self.text_input = wx.TextCtrl(panel)
        sizer.Add(self.text_input, flag=wx.EXPAND | wx.ALL, border=10)

        enviar_btn = wx.Button(panel, label="Enviar")
        enviar_btn.Bind(wx.EVT_BUTTON, self.enviar)
        sizer.Add(enviar_btn, flag=wx.ALL, border=10)

        panel.SetSizer(sizer)
        frame.Show()
        return True

    def enviar(self, event):
        print(f"Mensaje ingresado: {self.text_input.GetValue()}")

app = MyApp()
app.MainLoop()
