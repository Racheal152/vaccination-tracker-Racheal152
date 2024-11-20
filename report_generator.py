import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_csv_report(data):
    df = pd.DataFrame(data)
    report_path = 'vaccination_report.csv'
    df.to_csv(report_path, index=False)
    return report_path

def generate_pdf_report(data):
    c = canvas.Canvas("vaccination_report.pdf", pagesize=letter)
    c.setFont("Helvetica", 12)
    
    y_position = 750  # Starting y position for the report
    c.drawString(100, y_position, "Vaccination Report")
    
    for record in data:
        y_position -= 20
        c.drawString(100, y_position, f"Name: {record['Name']}")
        c.drawString(100, y_position-15, f"Vaccine Type: {record['Vaccine Type']}")
        c.drawString(100, y_position-30, f"Vaccination Date: {record['Vaccination Date']}")
        c.drawString(100, y_position-45, f"Status: {record['Status']}")
        y_position -= 60
    
    c.save()
    return "vaccination_report.pdf"
