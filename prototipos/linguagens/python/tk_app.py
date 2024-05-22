from dataclasses import dataclass, field
from os import system as shell
from tkinter import Tk, Button, Entry, Label
from types import NoneType
from typing import Callable, Dict, List, Union

# types
Null = NoneType
null: Null = None
Identifier = Union[int,str]
Widget = Union[Label,Button]

# tkinter widget wrapper
@dataclass
class Component:
    identifier: Identifier
    widget: Widget

# app rendering
class Renderer:
    window = Tk()
    components: List[Component] = []

    @staticmethod
    def setTitle(wndTitle: str):
        Renderer.window.title(wndTitle)

    @staticmethod
    def setDimensions(width:int,height:int):
        Renderer.window.geometry(f"{width}x{height}")

    @staticmethod
    def addButton(identifier: Identifier, btnText: str, btnCommand: Callable[[], Null]):
        _id = str(identifier)
        button = Button(Renderer.window, text=btnText, command=btnCommand)
        button.pack()
        component = Component(_id, button)
        Renderer.components.append(component)

    @staticmethod
    def addLabel(identifier: Identifier, lblText: str):
        _id = str(identifier)
        label = Label(Renderer.window, text=lblText)
        label.pack()
        component = Component(_id, label)
        Renderer.components.append(component)

    @staticmethod
    def addEntry(identifier: Identifier, defaultText: str = ""):
        _id = str(identifier)
        entry = Entry(Renderer.window)
        entry.insert(0, defaultText)
        entry.pack()
        component = Component(_id, entry)
        Renderer.components.append(component)

    @staticmethod
    def getComponent(identifier: Identifier) -> Component | Null:
        for component in Renderer.components:
            if component.identifier == str(identifier):
                return component
        return null

    @staticmethod
    def updateLabel(identifier: Identifier, newText: str):
        component = Renderer.getComponent(identifier)
        if component and isinstance(component.widget, Label):
            component.widget.config(text=newText)

    @staticmethod
    def start():
        Renderer.window.mainloop()

#debug
def testing():
    def clear_logs():
        shell("cls||clear")
    def parse_entry_01():
        _string = "{}".format(Renderer.getComponent("entry_01").widget.get())
        _string_0b = bin(int.from_bytes(_string.encode(), 'big'))[2:]
        print(_string_0b)
       # print((str(Renderer.getComponent("entry_01").widget.get())).encode().hex())
        #shell("{}".format(Renderer.getComponent("entry_01").widget.get()))
    Renderer.setTitle("Testing App")
    Renderer.setDimensions(700,350)
    Renderer.window.resizable(False, False)
    Renderer.addLabel(2, "Input")
    Renderer.addEntry("entry_01", "")
    Renderer.addButton("btn_send", "Send", parse_entry_01)
    Renderer.addButton("btn_clear_logs", "Clear logs", clear_logs)
    Renderer.start()

if __name__ == "__main__":
    shell("cls||clear")
    testing()