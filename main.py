# _____                           _       
# |_   _|                         | |      
#   | | _ __ ___  _ __   ___  _ __| |_ ___ 
#   | || '_ ` _ \| '_ \ / _ \| '__| __/ __|
#  _| || | | | | | |_) | (_) | |  | |_\__ \
#  \___/_| |_| |_| .__/ \___/|_|   \__|___/
#                | |                       
#                |_|       


# Local Imports
import utils, dashboard, login_gui, constants
from resources import *
from handlebars import *

try:
    # Library Imports
    import tkinter
    import customtkinter
    from PIL import Image, ImageTk
except:
    utils.import_exception()


#  _ ___           _      
# /  __ \         | |     
# | /  \/ ___   __| | ___ 
# | |    / _ \ / _` |/ _ \
# | \__/\ (_) | (_| |  __/
#  \____/\___/ \__,_|\___|


def gui_application():
    pass


class Pane():
    pass


class Gui_creation():
    def __init__(self, name: str, window_size: str) -> None:
        self.gui = customtkinter.CTk()
        self.gui.geometry(window_size)
        self.name = name
        self.gui.title(name)
        self.window_size = window_size
        self.window_size_t = utils.parse_size(window_size)
        
    def __str__(self) -> str:
        return self.name
    
    def get_interface(self) -> object:
        return self.gui
    
    def set_size(self, newsize) -> None:
        self.window_size = newsize
        self.window_size_t = utils.parse_size(newsize)
    
    def set_background(self, path: str = None) -> None:
        if path:
            bg = Image.open(path)
            bg = bg.resize((self.window_size_t), Image.Resampling.LANCZOS)
            bg = ImageTk.PhotoImage(bg)
            bgl = tkinter.Label(image=bg)
            bgl.image = bg
            bgl.place(x=-1, y=-1)
            print("-> New Background Image Set")
        else:
            self.gui.configure(bg="white")
            print("-> Background Set to White")

    def spawn_button(self, text: str, position: str, size: str, command: callable, image_path=None):
        if image_path:
            image = Image.open(image_path)
            image_size = utils.parse_size(size)
            new_image = image.resize((1000,1000))
            image = customtkinter.CTkImage(new_image)
            new_button = customtkinter.CTkButton(self.gui, text = text, command=command, compound="left", bg_color="black", image=image, width=int(image_size[0]), height=int(image_size[1]))
        else:
            new_button = tkinter.Button(self.gui, text = text, command=command)
        pos = utils.parse_size(position)
        new_button.place(x=pos[0], y=pos[1])
        print(f"-> Button [{text}] created at position {position} for command {command} with path {image_path}")


def login_process() -> int:
    try:
        login_gui = Gui_creation(name="Login_Gui", window_size=utils.set_up_window())
        login_gui.set_background("./resources/gui_login_background_1.PNG")
        login_gui.spawn_button("", "0x160", "200x100", None, "./resources/gui_login_button_login.PNG")
        login_gui.get_interface().mainloop()
        return 0
    except:
        return 1
    
    

# Starting Point of the Apllication
def main():
    print("======= Program Launched ========")
    utils.check_launch()
    print("======= Interface Launched ========")
    login_process()


# Innit the main
if __name__ == '__main__':
    main()