import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Andres app")
        self.set_border_width(10)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Button 1
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)

        # Button 2
        self.button2 = Gtk.Button(label="Exit")
        self.button2.connect("clicked", self.on_button2_clicked)

        # Add buttons to grid
        self.grid.add(self.button1)
        self.grid.attach(self.button1, 1, 0, 2, 1)
        self.grid.add(self.button2)
        self.grid.attach(self.button2, 1, 2, 1, 1)

    def on_button1_clicked(self, widget):
        print("Hello World")
    def on_button2_clicked(self, widget):
        print("Exit")
        Gtk.main_quit()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
