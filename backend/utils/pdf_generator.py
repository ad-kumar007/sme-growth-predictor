"""
PDF Report Generator for SME Growth Predictions
Uses ReportLab for PDF generation
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend


def generate_prediction_report(prediction_data: dict) -> BytesIO:
    """
    Generate a PDF report for a prediction
    
    Args:
        prediction_data: Dictionary containing prediction details
        
    Returns:
        BytesIO: PDF file in memory
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Container for PDF elements
    elements = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=12,
        spaceBefore=20
    )
    
    # Title
    title = Paragraph("SME Growth Prediction Report", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.2*inch))
    
    # Report metadata
    timestamp = prediction_data.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    metadata_data = [
        ['Report ID:', f"#{prediction_data.get('id', 'N/A')}"],
        ['Generated:', timestamp],
        ['Report Type:', 'SME Growth Assessment']
    ]
    
    metadata_table = Table(metadata_data, colWidths=[2*inch, 4*inch])
    metadata_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#374151')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(metadata_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Prediction Result Section
    elements.append(Paragraph("Prediction Result", heading_style))
    
    prediction = prediction_data.get('prediction', 'Unknown')
    confidence_scores = prediction_data.get('confidence_scores', {})
    
    # Color based on prediction
    pred_color = {
        'High': colors.HexColor('#10b981'),
        'Medium': colors.HexColor('#f59e0b'),
        'Low': colors.HexColor('#ef4444')
    }.get(prediction, colors.grey)
    
    result_data = [
        ['Predicted Growth Category:', prediction],
        ['Confidence Level:', f"{confidence_scores.get(prediction, 0)*100:.2f}%"]
    ]
    
    result_table = Table(result_data, colWidths=[2.5*inch, 3.5*inch])
    result_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TEXTCOLOR', (1, 0), (1, 0), pred_color),
        ('FONTSIZE', (1, 0), (1, 0), 16),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(result_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Confidence Breakdown
    elements.append(Paragraph("Confidence Breakdown", heading_style))
    
    confidence_data = [['Category', 'Confidence', 'Percentage']]
    for category in ['High', 'Medium', 'Low']:
        score = confidence_scores.get(category, 0)
        confidence_data.append([
            category,
            '█' * int(score * 20),  # Visual bar
            f"{score*100:.2f}%"
        ])
    
    confidence_table = Table(confidence_data, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    confidence_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e5e7eb')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1f2937')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elements.append(confidence_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Input Data Summary
    elements.append(Paragraph("Enterprise Profile", heading_style))
    
    input_data = prediction_data.get('input_data', {})
    
    profile_data = [
        ['Enterprise Size:', input_data.get('Small/Medium/Large', 'N/A')],
        ['Enterprise Age:', f"{input_data.get('Enterprise_Age', 'N/A')} years"],
        ['Location Code:', str(input_data.get('Location', 'N/A'))],
    ]
    
    profile_table = Table(profile_data, colWidths=[2.5*inch, 3.5*inch])
    profile_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(profile_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Key Metrics
    elements.append(Paragraph("Key Business Metrics", heading_style))
    
    metrics_data = [['Metric', 'Score']]
    metric_fields = [
        ('About Enterprises, Owners Motivation', 'Owner Motivation'),
        ('Enabler 1: Effortable Digital technologies', 'Digital Technologies'),
        ('Outcome : Growth and Effeciency', 'Growth & Efficiency'),
        ('Enabler 2 :Certification &Standarization', 'Certification'),
        ('Challenges 2: Skill Gap ,Retaining resources and workforce Management', 'Skill Gap Challenges'),
    ]
    
    for field, label in metric_fields:
        value = input_data.get(field, 'N/A')
        metrics_data.append([label, str(value)])
    
    metrics_table = Table(metrics_data, colWidths=[4*inch, 2*inch])
    metrics_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e5e7eb')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1f2937')),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elements.append(metrics_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Interpretation
    elements.append(Paragraph("Interpretation & Recommendations", heading_style))
    
    interpretation = {
        'High': "Your SME shows strong indicators for high growth potential. Focus on scaling operations, "
                "maintaining momentum, and seeking expansion opportunities. Consider investment in technology "
                "and workforce development to sustain growth trajectory.",
        'Medium': "Your SME demonstrates moderate growth potential with room for improvement. Consider addressing "
                  "key operational challenges, improving digital adoption, and strengthening workforce capabilities. "
                  "Focus on efficiency improvements and strategic planning to move toward high growth.",
        'Low': "Your SME may face significant growth challenges. Priority should be given to improving operational "
               "efficiency, addressing financial constraints, and building foundational capabilities. Consider "
               "seeking support programs, mentorship, and targeted interventions to overcome barriers."
    }.get(prediction, "Unable to provide interpretation.")
    
    interp_para = Paragraph(interpretation, styles['Normal'])
    elements.append(interp_para)
    elements.append(Spacer(1, 0.3*inch))
    
    # Footer
    elements.append(Spacer(1, 0.5*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    footer_text = "This report is generated by SME Growth Predictor AI System | For informational purposes only"
    footer = Paragraph(footer_text, footer_style)
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    
    return buffer


def generate_chart_image(confidence_scores: dict) -> BytesIO:
    """Generate a chart image for confidence scores"""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    categories = list(confidence_scores.keys())
    values = [confidence_scores[cat] * 100 for cat in categories]
    colors_map = {'High': '#10b981', 'Medium': '#f59e0b', 'Low': '#ef4444'}
    bar_colors = [colors_map.get(cat, '#6b7280') for cat in categories]
    
    ax.bar(categories, values, color=bar_colors)
    ax.set_ylabel('Confidence (%)')
    ax.set_title('Prediction Confidence Breakdown')
    ax.set_ylim(0, 100)
    
    # Add value labels on bars
    for i, v in enumerate(values):
        ax.text(i, v + 2, f'{v:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
    
    # Save to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    plt.close()
    
    return buffer
