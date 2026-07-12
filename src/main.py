# Restaurant Sales Analysis
# Main Application Entry Point
#
# Author : Subir Sutradhar
# Created: 09 July 2026

import matplotlib.pyplot as plt

import preprocessing as prep
import analysis
import report
from config import CHART_STYLE

plt.style.use(CHART_STYLE)

start_banner = """
=====================================================================
Restaurant Sales Analysis
Business Analytics Pipeline

Author  : Subir Sutradhar
Version : 1.0

======================================================================

"""

end_banner = """
======================================================================
Pipeline Completed Successfully

Charts Generated
PDF Report Generated
Processed Dataset Saved

Thank you for using Restaurant Sales Analysis.

=======================================================================
"""

def main():

    print(start_banner)

    # ------------------------------------------------
    # Declaring collectors to store important messages
    # ------------------------------------------------
    data_quality_findings = []
    data_corrections = []
    engineering_performed = []
    business_observations = []
    investigation_performed = []
    recommended_investigation = []

    # -------------------------------
    # Phase 1: Data Loading
    # -------------------------------
    df = prep.load_data()

    # -------------------------------
    # Phase 2: Data Exploration
    # -------------------------------
    prep.explore_data(df, data_quality_findings)

    # -------------------------------
    # Phase 3: Data Cleaning
    # -------------------------------
    df = prep.data_cleaning(df, data_corrections)

    # -------------------------------
    # Phase 4: Data Validation
    # -------------------------------
    df = prep.data_validation(df, business_observations)

    # -------------------------------
    # Phase 5: Feature Engineering
    # -------------------------------
    cleaned_df = analysis.create_attributes(df, engineering_performed)

    # -------------------------------
    # Phase 5: Business Analysis
    # -------------------------------
    cleaned_df = analysis.business_analysis(cleaned_df, business_observations, investigation_performed, recommended_investigation)

    # -------------------------------
    # Phase 6: Reporting
    # -------------------------------
    report.print_reports(data_quality_findings, data_corrections, engineering_performed, business_observations, investigation_performed, recommended_investigation)

    # -------------------------------
    # Phase 7: PDF Generation
    # -------------------------------
    report.generate_pdf_report(data_quality_findings, data_corrections, engineering_performed, business_observations, investigation_performed, recommended_investigation)

    print(end_banner)


if __name__ == "__main__":
    main()