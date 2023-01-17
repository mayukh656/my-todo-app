from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    for value in range(row["Pages"] - 1):
        pdf.add_page()


pdf.output("output.pdf")
