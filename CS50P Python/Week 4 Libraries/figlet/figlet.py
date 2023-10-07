from pyfiglet import Figlet
import random
import sys



# two arguments for selecting the font. arg#1 is -f and arg#2 is the name of the font

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] in ["-f", "--font"]) and (sys.argv[2] in fonts):
    font = sys.argv[2]
else:
    sys.exit("Invalid usage. Please provide zero or two command-line arguments. If specifying a font, use '-f' or '--font' followed by the font name.")

# prompt for a str of text
text = input("Input: ")
figlet.setFont(font=font)
# output text is the desired font
print("Output:")
print(figlet.renderText(text))