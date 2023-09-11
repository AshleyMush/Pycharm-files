import os
from PyPDF2 import PdfReader
import dateparser
from safeguard_words import safeguarding_words

care_log_dir = "C:\\Users\\Ashley\\Desktop\\Carer Notes Feedback\\Care_Logs"


def parse_care_log(pdf_text):
    care_log = {}

    # Extract carer name
    lines = pdf_text.split("\n")
    for line in lines:
        if "Visit by" in line:
            care_log['carer_name'] = line.split("Visit by")[-1].strip()
            break
    else:
        care_log['carer_name'] = "Carer name not found"

    # Extract and parse date
    lines = pdf_text.split("\n")
    if len(lines) > 1:
        date_line = lines[1]
        parts = date_line.split("@")
        if len(parts) > 1:
            date_str = parts[0].strip()
            care_log['date'] = dateparser.parse(date_str)
        else:
            care_log['date'] = "Date not found"

    # Extract client name
    lines = pdf_text.split("\n")
    if lines:
        care_log['client_name'] = lines[-1]
    else:
        care_log['client_name'] = "Client name not found"

    # Extract notes
    lines = pdf_text.split("\n")
    for idx, line in enumerate(lines):
        if "Notes:" in line:
            care_log['notes'] = "\n".join(lines[idx + 1:])
            break
    else:
        care_log['notes'] = "Notes not found"

    return care_log


for filename in os.listdir(care_log_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(care_log_dir, filename)
        pdf_text = get_pdf_text(pdf_path).lower()

        care_log = parse_care_log(pdf_text)

        if care_log:
            if check_for_safeguarding_words(care_log['notes']):
                print_care_log(care_log)


def get_pdf_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        page = reader.pages[0]
        return page.extract_text()
    except:
        print(f"Error parsing {pdf_path}")


def check_for_safeguarding_words(notes):
    keywords = ["abuse", "injured"]
    for word in keywords:
        if word in notes:
            return True
    return False


def print_care_log(care_log):
    print(f"""
  Care Log for {care_log['client_name']}
  Visit by {care_log['carer_name']} on {care_log['date']} 
  Notes:
  {care_log['notes']}
  """)