import os
import PyPDF2
import re


class PDFExtractor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._load_pdf()

    def _load_pdf(self):
        """Load the PDF and return its text content."""
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text_list = [page.extract_text() for page in reader.pages]
            return ' '.join(text_list)

    def extract_client_name(self):
        """Extract the client's name."""
        match = re.search(r"Birdie Care Log for\s*(.*?)(?=\sDownloaded:)", self.text, re.IGNORECASE)
        return match.group(1).strip() if match else ""

    def extract_carer_name(self):
        """Extract the carer's name."""
        # The regex pattern is updated to handle potential line breaks and other variability
        match = re.search(r"Visit by\s*([\w\s]+?)(?:,|\n)", self.text)
        return match.group(1).strip() if match else ""

    def extract_check_in_time(self):
        """Extract the check-in time."""
        match = re.search(r"@ (\d+:\d+ [apmAPM]{2})", self.text)
        return match.group(1) if match else ""

    def extract_notes(self):
        """Extract the notes section."""
        match = re.search(r"Notes\s+(.*?)(?:Food|$)", self.text, re.DOTALL)
        return match.group(1).strip() if match else ""

    def extract_all_details(self):
        """Extract and print all the required details."""
        client_name = self.extract_client_name()
        carer_name = self.extract_carer_name()
        check_in_time = self.extract_check_in_time()
        notes = self.extract_notes()

        print(f"""
        Birdie Care Log for {client_name},
        Visit by {carer_name},
        Check-in: {check_in_time},
        Notes: {notes}
        """)

    def has_empty_notes(self):
        """Check if the notes section is empty."""
        return not bool(self.extract_notes())



