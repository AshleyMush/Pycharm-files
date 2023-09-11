from BarPlotVisualizer import BarPlotVisualizer
from AuditReport import AuditReport
from datetime import datetime, timedelta
import os

# Get the current date
current_date = datetime.now().date()

# Subtract one day from it
# previous_date = current_date - timedelta(days=1)
previous_date = current_date

# Convert it into the desired string format
previous_date_str = previous_date.strftime('%Y%m%d')

# Paths
Angel_Drive = "C:/Users/Ashley/OneDrive - Angel Care Group Limited/Documents/Audits"

CHIPPING_SH = f"{Angel_Drive}/Chipping_Norton_SH/Audit_{previous_date_str}"
CHIPPING_DH = f"{Angel_Drive}/Chipping_Norton_DH/Audit_{previous_date_str}"
BANBURY_DH = f"{Angel_Drive}/Banbury_DH/Audit_{previous_date_str}"
BANBURY_SH = f"{Angel_Drive}/Banbury_SH/Audit_{previous_date_str}"
WITNEY_DH = f"{Angel_Drive}/Witney_DH/Audit_{previous_date_str}"
WITNEY_AH = f"{Angel_Drive}/Witney_AH/Audit_{previous_date_str}"
WITNEY_JB = f"{Angel_Drive}/Witney_JB/Audit_{previous_date_str}"
THAME = f"{Angel_Drive}/Thame/Audit_{previous_date_str}"
ENYSHAM = f"{Angel_Drive}/Enysham/Audit_{previous_date_str}"
BAMPTON = f"{Angel_Drive}/Bampton/Audit_{previous_date_str}"
ABINGDON = f"{Angel_Drive}/Abingdon/Audit_{previous_date_str}"
BURFORD = f"{Angel_Drive}/Burford/Audit_{previous_date_str}"
WANTAGE = f"{Angel_Drive}/Wantage/Audit_{previous_date_str}"
BICESTER = f"{Angel_Drive}/Bicester/Audit_{previous_date_str}"
LATEST_STATS = f"{Angel_Drive}/LATEST_STATS/Audit_{previous_date_str}"


# File Paths
DIRECTORY_FILEPATH =WANTAGE    #TODO CHANGE ME through HARDCODING
KEYWORDS_FILEPATH = "C:/Users/Ashley/PycharmProjects/PDF_READER/keywords.txt"
WORD_DOC_FILEPATH = f"{WANTAGE }/Audits_{previous_date_str}.docx"#TODO CHANGE ME through HARDCODING

# Check if the directory already exists. If not, create it.
if not os.path.exists(DIRECTORY_FILEPATH):
    os.makedirs(DIRECTORY_FILEPATH)

# Check if there's any PDF in the directory
pdf_files = [file for file in os.listdir(DIRECTORY_FILEPATH) if file.lower().endswith('.pdf')]

if pdf_files:  # If the list is not empty, meaning there's at least one PDF
    audit_report = AuditReport(DIRECTORY_FILEPATH, KEYWORDS_FILEPATH, WORD_DOC_FILEPATH,route_name="WANTAGE " ) #TODO CHANGE ME
    audit_report.generate_report()
else:
    from UI import UI
    message_box = UI()
    message_box.show_error_mesage()






