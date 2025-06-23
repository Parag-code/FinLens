from fpdf import FPDF
import datetime

def generate_pdf_report(df, anomalies, sentiment, score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, "FinLens Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, f"Total Entries: {len(df)}", ln=True)
    pdf.cell(200, 10, f"Detected Anomalies: {len(anomalies)}", ln=True)
    pdf.cell(200, 10, f"News Sentiment: {sentiment}", ln=True)
    pdf.cell(200, 10, f"Fraud Risk Score: {score:.2f}/100", ln=True)
    pdf.cell(200, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    out_path = "finlens_report.pdf"
    pdf.output(out_path)
    return out_path