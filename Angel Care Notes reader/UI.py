import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from AuditReport import AuditReport
import os

YELLOW = "#FFFF00"

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BIRDIE READER")
        self.root.config(padx=100, pady=150, bg=YELLOW)
        self.root.geometry("800x800")

        self.routes = [
            "Chipping_Norton_SH", "Chipping_Norton_DH", "Banbury_DH", "Banbury_SH",
            "Witney_DH", "Witney_AH", "Witney_JB", "Thame", "Enysham",
            "Bampton", "Abingdon", "Burford", "Wantage","Bicester","Oxford","Carer_Notes", "ALL WITNEY", "ALL CHIPPING NORTON", "ALL BANBURY","All_Clients"
        ]

        # Define the keywords_filepath here
        self.keywords_filepath = "C:/Users/Ashley/PycharmProjects/PDF_READER/keywords.txt"

        rows = 4
        cols = 4

        for idx, route in enumerate(self.routes):
            row = idx // cols
            col = idx % cols
            btn = tk.Button(self.root, text=route, command=lambda r=route: self.set_route(r), bg="white")
            btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

        for i in range(rows):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(cols):
            self.root.grid_columnconfigure(j, weight=1)

        self.root.mainloop()

    def set_route(self, route):
        Angel_Drive = "C:/Users/Ashley/OneDrive - Angel Care Group Limited/Documents/Audits"
        # current_date = datetime.now().date()
        # previous_date = current_date - timedelta(days=1)
        # previous_date_str = previous_date.strftime('%Y%m%d')

        # Get the current date
        current_date = datetime.now().date()

        # Subtract one day from it
        previous_date_str = current_date - timedelta(days=0)#TODO INCREASE TO GO BACK IN DAYS 1 = YESTERDAY
        # previous_date_str = current_date

        DIRECTORY_FILEPATH = f"{Angel_Drive}/{route}/Audit_{previous_date_str}"
        WORD_DOC_FILEPATH = f"{DIRECTORY_FILEPATH}/Audits_{previous_date_str}.docx"

        AuditReport.ROUTE_NAME = route

        # Check if the directory already exists. If not, create it.
        if not os.path.exists(DIRECTORY_FILEPATH):
            os.makedirs(DIRECTORY_FILEPATH)

        # Check if there's any PDF in the directory
        pdf_files = [file for file in os.listdir(DIRECTORY_FILEPATH) if file.lower().endswith('.pdf')]

        if pdf_files:
            audit_report = AuditReport(DIRECTORY_FILEPATH, self.keywords_filepath, WORD_DOC_FILEPATH, route_name=route,
                                       directory_filepath=DIRECTORY_FILEPATH)
            audit_report.generate_report()
        else:
            self.show_error_message("No PDFs found in the directory. Making Directory")

    def show_error_message(self, msg="Error"):
        messagebox.showerror(msg)