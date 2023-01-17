from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format="A4")
pdf.set_auto_page_break(auto="False", margin=0)


df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    #Set the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)
    #Set the footer for master page
    pdf.ln(270)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=6, txt=row["Topic"], ln=0, align="R")

    for value in range(row["Pages"] - 1):
        pdf.add_page()
        #Set the footer for the other pages
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=6, txt=row["Topic"], ln=0, align="R")


pdf.output("output.pdf")
