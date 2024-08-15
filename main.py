from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics1.csv")
pdf.set_line_width(0.5)


def draw_lines(pdf, start_y, line_spacing=10):
    page_height = 297
    num_lines = int((page_height - start_y) / line_spacing)

    for y in range(num_lines):
        current_y = start_y + y * line_spacing
        pdf.line(x1=10, y1=current_y, x2=200, y2=current_y)


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    start_y = 30
    draw_lines(pdf, start_y)

    pdf.set_y(-15)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        draw_lines(pdf, start_y=10)

pdf.output("output.pdf")
