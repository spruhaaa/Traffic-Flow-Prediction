from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(mae, rmse, r2):
    doc = SimpleDocTemplate("Traffic_Flow_Prediction_Report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    flow = []

    flow.append(Paragraph("<b>Traffic Flow Prediction for Smart Cities</b>", styles["Title"]))
    flow.append(Spacer(1, 20))

    flow.append(Paragraph("<b>Objective:</b>", styles["Heading2"]))
    flow.append(Paragraph("Analyze traffic data (sensor readings, weather conditions, and historical patterns) "
                          "to forecast traffic conditions and suggest optimal routes.", styles["Normal"]))
    flow.append(Spacer(1, 15))

    flow.append(Paragraph("<b>Results:</b>", styles["Heading2"]))
    flow.append(Paragraph(f"- MAE: {mae:.2f}", styles["Normal"]))
    flow.append(Paragraph(f"- RMSE: {rmse:.2f}", styles["Normal"]))
    flow.append(Paragraph(f"- R2: {r2:.3f}", styles["Normal"]))
    flow.append(Spacer(1, 15))

    flow.append(Paragraph("<b>Visualizations:</b>", styles["Heading2"]))
    try:
        flow.append(Paragraph("Actual vs Predicted Speeds", styles["Normal"]))
        flow.append(Image("artifacts/fig_scatter.png", width=400, height=400))
    except:
        flow.append(Paragraph("⚠️ Missing fig_scatter.png", styles["Normal"]))

    flow.append(Spacer(1, 15))
    try:
        flow.append(Paragraph("Feature Importance", styles["Normal"]))
        flow.append(Image("artifacts/fig_feature_importance.png", width=400, height=250))
    except:
        flow.append(Paragraph("⚠️ Missing fig_feature_importance.png", styles["Normal"]))

    flow.append(Spacer(1, 15))
    flow.append(Paragraph("<b>Conclusion:</b>", styles["Heading2"]))
    flow.append(Paragraph("The Random Forest model predicts traffic speeds effectively. "
                          "Cities can use such models to manage congestion and optimize traffic flow.", styles["Normal"]))

    doc.build(flow)
    print("📄 PDF report generated: Traffic_Flow_Prediction_Report.pdf")
