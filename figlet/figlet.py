import sys
from pyfiglet import Figlet

def main():
    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font_name = None
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Specific font specified
        font_name = sys.argv[2]
    else:
        print("Usage: python figlet.py [-f|--font FONT_NAME]")
        sys.exit(1)

    # Prompt the user for text input
    text = input("Enter text: ")

    # Initialize the Figlet object with the specified font, if any
    figlet = Figlet(font=font_name) if font_name else Figlet()

    # Render and print the ASCII art text
    ascii_art = figlet.renderText(text)
    print(ascii_art)

if __name__ == "__main__":
    main()
