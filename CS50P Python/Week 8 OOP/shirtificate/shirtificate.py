from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 56)
        self.cell(0, 60, "CS50 Shirtificate", align='C')

    def add_image(self, image_path, x, y, w, h):
        self.image(image_path, x, y, w, h)

    def add_lettering(self, name):
        self.set_font("helvetica", "", 20)
        self.set_text_color(255, 255, 255)
        text_width = self.get_string_width(f"{name} took CS50")
        x = (210 - text_width) / 2
        self.text(x, 130, f"{name} took CS50")

def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.add_image("./shirtificate.png", x=25, y=80, w=160, h=160)
    pdf.add_lettering(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
