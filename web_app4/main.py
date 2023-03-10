import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices\*")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {invoice_date}", ln=1)
    pdf.ln()

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=8, style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
    total = df["total_price"].sum()
    pdf.cell(w=30, h=8, txt=str(), border=1)
    pdf.cell(w=70, h=8, txt=str(), border=1)
    pdf.cell(w=30, h=8, txt=str(), border=1)
    pdf.cell(w=30, h=8, txt=str(), border=1)
    pdf.cell(w=30, h=8, txt=str(f"{total}"), border=1, ln=1)
    pdf.ln()
    pdf.set_font(family="Times", style="I", size=15)
    pdf.cell(w=30, h=8, txt=f"The total price is {total} Euros", ln=1)
    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=30,h=8, txt="PythonHow")
    pdf.image("pythonhow.png", w=8)

    pdf.output(f"PDFs/{filename}.pdf")



