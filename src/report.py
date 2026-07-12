"""
Report module for the Restaurant Sales Analysis project.

This module contains functions for:
- Displaying the findings and observations
- Saving all findings and observations as pdf report 

"""

from config import REPORT_DIR
from reportlab.pdfgen import canvas

# ===============================
# Displaying findings and observations
# ===============================

def print_reports(data_quality_findings: list, data_corrections: list, engineering_performed: list, business_observations: list, investigation_performed: list, recommended_investigation: list) -> None:
    '''
    Displays the findings, corrections made, engineering performed, business observations, investigations performed and recommended_investigation

    Args:
        data_quality_findings: to print the data quality findings
        data_corrections: to print the data corrections
        engineering_performed: to print the engineering performed tasks
        business_observations: to print the observations founf from the business
        investigation_performed: to print the performed investigation tasks
        recommended_investigation: to print the recommended investigations
    '''
    print("=" * 70)
    print("Data Quality Findings")
    print("=" * 70)
    sr_num = 1
    for finding in data_quality_findings:
        if finding.startswith(" "):
            print(f"{finding}")
        else:
            print(f"{sr_num}. {finding}")
            sr_num += 1

    
    print("=" * 70)
    print("Data Correction")
    print("=" * 70)
    sr_num = 1
    for corrections in data_corrections:
        if corrections.startswith(" "):
            print(f"{corrections}")
        else:
            print(f"{sr_num}. {corrections}")
            sr_num += 1


    print("=" * 70)
    print("Engineering Features")
    print("=" * 70)
    sr_num = 1
    for engineering in engineering_performed:
        if engineering.startswith(" "):
            print(f"{engineering}")
        else:
            print(f"{sr_num}. {engineering}")
            sr_num += 1


    print("=" * 70)
    print("Business Observations")
    print("=" * 70)
    sr_num = 1
    for observation in business_observations:
        if observation.startswith(" "):
            print(f"{observation}")
        else:
            print(f"{sr_num}. {observation}")
            sr_num += 1
    
    print("=" * 70)
    print("Investigations Performed")
    print("=" * 70)
    sr_num = 1
    for investigations in investigation_performed:
        if investigations.startswith(" "):
            print(f"{investigations}")
        else:
            print(f"{sr_num}. {investigations}")
            sr_num += 1


    print("=" * 70)
    print("Recommended Investigations")
    print("=" * 70)
    sr_num = 1
    for recommends in recommended_investigation:
        if recommends.startswith(" "):
            print(f"{recommends}")
        else:
            print(f"{sr_num}. {recommends}")
            sr_num += 1
            

    return None


# ===============================
# Save report as pdf
# ===============================
def generate_pdf_report(
    data_quality_findings: list,
    data_corrections: list,
    engineering_performed: list,
    business_observations: list,
    investigation_performed: list,
    recommended_investigation: list
) -> None:
    """
    Generate a PDF report containing all findings, observations,
    investigations, and recommendations.

    Args:
        data_quality_findings: List of data quality findings.
        data_corrections: List of data cleaning and correction steps.
        engineering_performed: List of feature engineering tasks.
        business_observations: List of business observations.
        investigation_performed: List of investigations performed.
        recommended_investigation: List of recommended future investigations.
    """

    pdf = canvas.Canvas(
        str(REPORT_DIR / "restaurant_analysis_report.pdf")
    )

    start_margin = 780

    pdf.setFont("Courier-Bold", 18)
    pdf.drawString(
        50,
        start_margin,
        "RESTAURANT ANALYSIS REPORT"
    )

    def write_section(title: str, data: list) -> int:
        nonlocal start_margin

        pdf.setFont("Courier-Bold", 13)
        start_margin -= 30
        pdf.drawString(
            50,
            start_margin,
            title
        )

        pdf.setFont("Courier", 10)
        start_margin -= 30

        sr_num = 1

        for item in data:

            if item.startswith(" "):
                line = item
            else:
                line = f"{sr_num}. {item}"
                sr_num += 1

            if start_margin < 40:
                pdf.showPage()
                start_margin = 780
                pdf.setFont("Courier", 10)

            pdf.drawString(
                50,
                start_margin,
                line
            )

            start_margin -= 20

    write_section(
        "DATA QUALITY FINDINGS",
        data_quality_findings
    )

    write_section(
        "DATA CORRECTIONS",
        data_corrections
    )

    write_section(
        "ENGINEERING FEATURES",
        engineering_performed
    )

    write_section(
        "BUSINESS OBSERVATIONS",
        business_observations
    )

    write_section(
        "INVESTIGATIONS PERFORMED",
        investigation_performed
    )

    write_section(
        "RECOMMENDED INVESTIGATIONS",
        recommended_investigation
    )

    pdf.save()

    return None