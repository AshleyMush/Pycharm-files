import os
from PyPDF2 import PdfReader
from safeguard_words import safeguarding_words




# care_log_dir = "C:\\Users\\Ashley\\Desktop\\Carer Notes Feedback\\Care_Logs_0708"
care_log_dir = "C:\\Users\\Ashley\\Desktop\\Carer Notes Feedback\\Carelogs\\06_08\\Thames"

for filename in os.listdir(care_log_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(care_log_dir, filename)
        reader = PdfReader(pdf_path)
        page = reader.pages[0]
        text = page.extract_text()

        # Extract carer name
        visit_line = None
        for line in text.split("\n"):
            if "Visit by" in line:
                visit_line = line
                break

        if visit_line:
            carer_name = visit_line.split("Visit by")[-1].strip()
        else:
            carer_name = "Carer name not found"

        # Extract notes
        notes_start = None
        for line in text.split("\n"):
            if "Notes:" in line:
                notes_start = text.index(line)
                break

        if notes_start is not None:
            notes = text[notes_start:].strip()
        else:
            notes = "Notes not found"

        # Extract date
        date_line = text.split("\n")[1]
        date_parts = date_line.split("@")
        if len(date_parts) >= 2:
            date = date_parts[0].strip()
        else:
            date = "Date not found"

        # Extract client name
        client_name = text.split("\n")[-1]

        if any(word in text for word in safeguarding_words):
            print(f"""
            Birdie Care Log for {client_name},
            Visit by {carer_name},
            Check-in: {date},
            Notes: {notes}

            """)
