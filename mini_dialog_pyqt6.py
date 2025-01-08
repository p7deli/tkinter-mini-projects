import sys
from PyQt6.QtWidgets import QApplication
from VPyFormGenerator.VPyGUIGenerator import VPyGUIGenerator


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def __str__(self):
        return f'{self.name} -- {self.family} -- {self.age}'


per = Person('poria', 'deli', 27)

app = QApplication(sys.argv)

dialog = VPyGUIGenerator.create_gui(per)
dialog.show()

app.exec()
print(per)