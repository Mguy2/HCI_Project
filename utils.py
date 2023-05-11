# _____                           _       
# |_   _|                         | |      
#   | | _ __ ___  _ __   ___  _ __| |_ ___ 
#   | || '_ ` _ \| '_ \ / _ \| '__| __/ __|
#  _| || | | | | | |_) | (_) | |  | |_\__ \
#  \___/_| |_| |_| .__/ \___/|_|   \__|___/
#                | |                       
#                |_|        


def import_exception() -> None:
    with open("launch_log.txt", "r+") as log:
        cont = log.readlines()
        if cont:
            log.truncate(0)
            print("-> Import Error, Resetting Launch Log and Attempting to Reinstall Packages.")


# Local Imports
import constants


try:
    
    # Library Imports              
    from PIL import Image, ImageTk
    import tkinter
    import customtkinter
    import sys, os
    import subprocess

    # Platform-Dependent Import
    if sys.platform == "win32":
        from win32api import GetSystemMetrics
    
except:
    import_exception()


#  _ ___           _      
# /  __ \         | |     
# | /  \/ ___   __| | ___ 
# | |    / _ \ / _` |/ _ \
# | \__/\ (_) | (_| |  __/
#  \____/\___/ \__,_|\___|


def get_last_word(string):
    words = string.split()
    if words:
        last_word = words[-1]
    else:
        last_word = ""
    return last_word


def install_dep() -> None:
    tries = 3
    success = False
    while tries > 0:
        try:
            with open("./requirements.txt", "r") as tbi:
                read = tbi.readlines()
                for pack in read:
                    status = subprocess.check_output(pack, shell=True)
                    print(f"-> Checking Package {get_last_word(pack)} \n-> STATUS: \n-> {status}\n WOW SO FANCY, LOVE FROM MIKE")
                print("-> All Done installing packages, quitting now, please re-launch.")
                success = True
        except:
            if not success:
                print(f"-> Unexpected Error, Please Contact Group 42, attempts remaining: {tries}")
                tries -= 1
        if success:
            sys.exit()


def check_launch() -> None:
    with open("launch_log.txt", "r+") as log:
        cont = log.readlines()
        if cont:
            return
        else:
            log.write("launched")
    output = subprocess.check_output(constants.Constants.PYTH_VERSION, shell=True)
    print(f"-> Currently running Python version: {output}")
    install_dep()


def parse_size(size: str) -> tuple:
    return int(size.split("x")[0]), int(size.split("x")[1])


def revert_size_to_string(size :tuple) -> str:
    return f"{size[0]}x{size[1]}"


def resize_Image(image, maxsize):
    r1 = image.size[0]/maxsize[0] # width ratio
    r2 = image.size[1]/maxsize[1] # height ratio
    ratio = max(r1, r2)
    newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio))
    image = image.resize(newsize, Image.ANTIALIAS)
    return image


def get_good_size(image, maxsize):
    r1 = image.size[0]/maxsize[0] # width ratio
    r2 = image.size[1]/maxsize[1] # height ratio
    ratio = max(r1, r2)
    return (int(image.size[0]/ratio), int(image.size[1]/ratio))


def size_up_window(image, gui) -> tuple:
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    r1 = image.size[0]/width # width ratio
    r2 = image.size[1]/height # height ratio
    ratio = max(r1, r2)
    return (int(image.size[0]/ratio), int(image.size[1]/ratio))


def set_up_window() -> tuple:
    if sys.platform == "win32":
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
    else:
        try:
            out = os.popen2("xdpyinfo | grep 'dimensions:'")[1].read()
            out = out.replace("  dimensions:    ","")
            i = out.find(" pixels")
            out = out[:i]
            out = out.split("x") # Yes I know this is double, just leave it like this for me. 
            width=int(out[0])
            height=int(out[1])
        except:
            pass
    return revert_size_to_string((width, height))