# ========================= Ensure Imports =========================

import subprocess
import sys

def EnsureImports():
    required_modules = [
        "os",
        "time",
        "PIL",
        "colorama",
        "random",
        "datetime"
    ]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])


EnsureImports()

# ========================= Modules =========================

import os
import time
import random
from datetime import datetime
from PIL import Image
from colorama import *

# ========================= Utilities =========================

def CurrentLocalTime():
    return datetime.now().strftime("%H:%M:%S")

reset = Fore.RESET
white = Fore.WHITE
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED

start = f"{red}[{white}"
end = f"{red}]"

SUCCESS = lambda: f"{start + CurrentLocalTime() + end} {start}+{end}{white}"
FAILED = lambda: f"{start + CurrentLocalTime() + end} {start}x{end}{white}"
ERROR = lambda: f"{start + CurrentLocalTime() + end} {start}!{end}{white}"
LOADING = lambda: f"{start + CurrentLocalTime() + end} {start}~{end}{white}"
INPUT = lambda: f"{start + CurrentLocalTime() + end} {start}>{end}{white}"
INFORMATION = lambda: f"{start + CurrentLocalTime() + end} {start}?{end}{white}"
CHOICE = lambda: f"{start + CurrentLocalTime() + end} {start}#{end}{white}"

def Clear():
    os.system("cls")

def SetTitle(text):
    os.system(f"title {text}")

def TypeWriterInput(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()

def TypeWriterPrint(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return print()

def Scroll(text):
    for line in text.split("\n"):
        print(line)
        time.sleep(0.04)
time.sleep(0.5)

def ScrollGradient(text):
    for line in Gradient(text).split("\n"):
        print(line)
        time.sleep(0.04)
time.sleep(0.5)

def Gradient(text):
    start_color = (223, 5, 5)
    end_color = (121, 3, 3)

    num_steps = 15

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    colors += list(reversed(colors[:-1]))

    fancy_chars = "|\\()_$'╗║═╔╚╝"

    def color_text(r, g, b, char):
        return f"\033[38;2;{r};{g};{b}m{char}"

    lines = text.split("\n")
    result = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in fancy_chars:
                color = colors[(i + j) % len(colors)]
                result.append(color_text(*color, char))
            else:
                result.append(char)
        result.append("\033[0m\n")

    return "".join(result)

def InvalidChoice():
    print(f"{FAILED()} Invalid choice, please try again.")
    time.sleep(1)
    iConverterMenu()

# ========================= Convert Image =========================

def ConvertImg():
    SetTitle("iConverter Tool - By RyzenGT")
    Clear()
    iConverter = rf"""
{red}               /$$  /$$$$$$                                                      /$$                        
{red}              |__/ /$$__  $$                                                    | $$                        
{red}               /$$| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
{red}              | $$| $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
{red}              | $$| $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/
{red}              | $$| $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$_____/| $$      
{red}              | $$|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$      
{red}              |__/ \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \_______/|__/

{red}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{red}║                 {white}V1.0 {red}// {white}github.com/RyzenGT/iConverter-Tool {red}// {white}Made By RyzenGT {red}// {white}Image Converter Tool                {reset}║
{red}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

                   {start}01{end}{white} Convert To JPEG                                     {start}06{end}{white} Convert To TIFF
                   {start}02{end}{white} Convert To JPG                                      {start}07{end}{white} Convert To WEBP
                   {start}03{end}{white} Convert To PNG                                      {start}08{end}{white} Convert To ICO
                   {start}04{end}{white} Convert To GIF                                      {start}09{end}{white}
                   {start}05{end}{white} Convert To BMP                                      {start}10{end}{white}"""
    ScrollGradient(iConverter)
    ChoiceConvert = TypeWriterInput(f"{INPUT()} Enter Your Conversion {red}->{reset} ").strip().lstrip("0")
    if ChoiceConvert == "1":
        print(f"{LOADING()} Converting to JPEG..")
        time.sleep(random.uniform(1, 2))
        ConvertToJPEG()
    elif ChoiceConvert == "2":
        print(f"{LOADING()} Converting to JPG..")
        time.sleep(random.uniform(1, 2))
        ConvertToJPG()
    elif ChoiceConvert == "3":
        print(f"{LOADING()} Converting to PNG..")
        time.sleep(random.uniform(1, 2))
        ConvertToPNG()
    elif ChoiceConvert == "4":
        print(f"{LOADING()} Converting to GIF..")
        time.sleep(random.uniform(1, 2))
        ConvertToGIF()
    elif ChoiceConvert == "5":
        print(f"{LOADING()} Converting to BMP..")
        time.sleep(random.uniform(1, 2))
        ConvertToBMP()
    elif ChoiceConvert == "6":
        print(f"{LOADING()} Converting to TIFF..")
        time.sleep(random.uniform(1, 2))
        ConvertToTIFF()
    elif ChoiceConvert == "7":
        print(f"{LOADING()} Converting to WEBP..")
        time.sleep(random.uniform(1, 2))
        ConvertToWEBP()
    elif ChoiceConvert == "8":
        print(f"{LOADING()} Converting to ICO..")
        time.sleep(random.uniform(1, 2))
        ConvertToICO()
    else:
        InvalidChoice()
    
# ========================= Conversion Functions =========================

def GetImagePath():
    return ImgToConvert

def SaveImage(img, out_path, format=None):
    output_dir = "Converted-Image"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = os.path.basename(out_path)
    out_path = os.path.join(output_dir, filename)
    save_kwargs = {}
    if format in ["JPEG", "JPG"]:
        save_kwargs["quality"] = 100
        save_kwargs["subsampling"] = 0
        save_kwargs["optimize"] = True
    elif format == "PNG":
        save_kwargs["compress_level"] = 0
    elif format == "WEBP":
        save_kwargs["quality"] = 100
        save_kwargs["lossless"] = True
    try:
        img.save(out_path, format=format, **save_kwargs)
        print(f"{SUCCESS()} Saved as {red}->{reset} {out_path}")
    except Exception as e:
        print(f"{FAILED()} Failed to save {red}->{reset} {e}")
    input(f"\n{INFORMATION()} Press Enter to continue {red}->{reset} ")
    iConverterMenu()

def ConvertToJPEG():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".jpeg"
        SaveImage(img.convert("RGB"), out_path, "JPEG")

def ConvertToJPG():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".jpg"
        SaveImage(img.convert("RGB"), out_path, "JPEG")

def ConvertToPNG():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".png"
        SaveImage(img, out_path, "PNG")

def ConvertToGIF():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".gif"
        SaveImage(img, out_path, "GIF")

def ConvertToBMP():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".bmp"
        SaveImage(img, out_path, "BMP")

def ConvertToTIFF():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".tiff"
        SaveImage(img, out_path, "TIFF")

def ConvertToWEBP():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".webp"
        SaveImage(img, out_path, "WEBP")

def ConvertToICO():
    path = GetImagePath()
    with Image.open(path) as img:
        out_path = os.path.splitext(path)[0] + ".ico"
        SaveImage(img, out_path, "ICO")

# ========================= Main Menu =========================

def iConverterMenu():
    global ImgToConvert
    SetTitle("iConverter Tool - By RyzenGT")
    Clear()
    iConverter = rf"""
{red}               /$$  /$$$$$$                                                      /$$                        
{red}              |__/ /$$__  $$                                                    | $$                        
{red}               /$$| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
{red}              | $$| $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
{red}              | $$| $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/
{red}              | $$| $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$_____/| $$      
{red}              | $$|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$      
{red}              |__/ \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \_______/|__/

{red}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{red}║                 {white}V1.0 {red}// {white}github.com/RyzenGT/iConverter-Tool {red}// {white}Made By RyzenGT {red}// {white}Image Converter Tool                {reset}║
{red}╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
    ScrollGradient(iConverter)
    ImgToConvert = TypeWriterInput(f"{INPUT()} Enter Image Path {red}->{reset} ").strip(' "&')
    if not os.path.exists(ImgToConvert):
        print(f"{ERROR()} Image path not found")
        time.sleep(1)
        iConverterMenu()
    try:
        with Image.open(ImgToConvert) as img:
            img.verify()  
            img_format = img.format
        if img_format not in ["JPEG", "JPG", "PNG", "GIF", "BMP", "TIFF", "WEBP", "ICO", "HEIF", "HEIC", "SVG", "RAW"]:
            print(f"{ERROR()} This file is not a supported image type.")
            time.sleep(1)
            iConverterMenu()
    except Exception:
        print(f"{ERROR()} This is not a valid image.")
        time.sleep(1)
        iConverterMenu()
    if os.path.exists(ImgToConvert):
        ConvertImg()

if __name__ == "__main__":
    iConverterMenu()