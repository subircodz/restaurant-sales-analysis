# =======================================
# RESTAURANT SALES AND ORDERS ANALYSIS
# AUTHOR: Subir Sutradhar
# Date: 9 July 2026
# ======================================= 

import preprocessing as prep
import analysis



def main():
    # Store important business findings
    findings = []
    observations = []

    # -------------------------------
    # Phase 1: Load the data
    # -------------------------------
    df = prep.load_data()

    # -------------------------------
    # Phase 1: Understanding the data
    # -------------------------------
    prep.explore_data(df, findings)

    # -------------------------------
    # Phase 2: Cleaning the data
    # -------------------------------
    df = prep.data_cleaning(df, findings)

    # -------------------------------
    # Phase 3: Validating the data
    # -------------------------------
    df = prep.data_validation(df, findings)

    # -------------------------------
    # Phase 4: Create attributes for revenue, day_name, month, weekend
    # -------------------------------
    cleaned_df = analysis.create_attributes(df, findings)

    # -------------------------------
    # Phase 5: Performing Business analysis
    # -------------------------------
    cleaned_df = analysis.business_analysis(cleaned_df, observations)



if __name__ == "__main__":
    main()