import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Simple wxPython App")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a text control
        self.text_ctrl = wx.TextCtrl(panel, size=(200, 100))
        sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # Create a button
        button = wx.Button(panel, label="Click Me")
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        # Bind the button event
        button.Bind(wx.EVT_BUTTON, self.on_button_click)

        panel.SetSizer(sizer)
        self.Show()

    def on_button_click(self, event):
        self.text_ctrl.SetValue("Button Clicked!")

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        return True

# Run the application
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
