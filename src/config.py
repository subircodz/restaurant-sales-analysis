from pathlib import Path

# ===============================
# Application Settings
# ===============================

DEBUG = True
SAVE_REPORT = True
SAVE_CHARTS = True
SHOW_CHARTS = False
CHART_STYLE = "ggplot"

# ===============================
# Directory Paths
# ===============================

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = PROJECT_DIR / "output"
REPORT_DIR = OUTPUT_DIR / "reports"
CHART_DIR = OUTPUT_DIR / "charts"

