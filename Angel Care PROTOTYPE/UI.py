import tkinter as tk
from tkinter import ttk  # For enhanced widgets and styling
from tkinter import messagebox
from datetime import datetime, timedelta
from AuditReport import AuditReport
import os
from tkcalendar import Calendar

# Defined Colors and Font
YELLOW = "#FFFF00"
BUTTON_BG = "#4CAF50"
BUTTON_FG = "white"
FONT_NAME = "Arial"
FONT_SIZE = 12

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BIRDIE READER")
        self.root.config(padx=100, pady=50, bg=YELLOW)
        self.root.geometry("900x900")  # Increased the window size

        self.routes = [
            "Chipping_Norton_SH", "Chipping_Norton_DH", "Banbury_DH", "Banbury_SH",
            "Witney_DH", "Witney_AH", "Witney_JB", "Thame", "Enysham",
            "Bampton", "Abingdon", "Burford", "Wantage","Bicester","Oxford","Carer_Notes", "ALL WITNEY", "ALL CHIPPING NORTON", "ALL BANBURY","All_Clients"
        ]

        # Define the keywords_filepath here
        self.keywords_filepath = "C:/Users/Ashley/PycharmProjects/PDF_READER/keywords.txt"

        rows = 4
        cols = 4

        # Frame for Calendar Section
        calendar_frame = ttk.Frame(self.root, padding="10")
        calendar_frame.grid(row=rows - 1, rowspan=2, columnspan=cols, pady=(0, 20), sticky="nsew")

        # Label for the calendar section inside the frame
        tk.Label(calendar_frame, text="Select Date", bg=YELLOW, font=(FONT_NAME, 14, "bold")).pack(pady=10)

        # Calendar widget inside the frame
        self.calendar = Calendar(calendar_frame)
        self.calendar.pack(pady=10)

        # Additional button to set the selected date from the calendar inside the frame
        date_btn = tk.Button(calendar_frame, text="Set Date", command=self.set_date, bg=BUTTON_BG, fg=BUTTON_FG,
                             font=(FONT_NAME, FONT_SIZE))
        date_btn.pack(pady=10)

        # Separator
        ttk.Separator(self.root, orient='horizontal').grid(row=rows + 2, columnspan=cols, sticky="ew", pady=20)

        for idx, route in enumerate(self.routes):
            row = idx // cols + 5
            col = idx % cols
            btn = tk.Button(self.root, text=route, command=lambda r=route: self.set_route(r), bg=BUTTON_BG,
                            fg=BUTTON_FG, font=(FONT_NAME, FONT_SIZE), padx=10, pady=10)
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        for i in range(rows + 5):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(cols):
            self.root.grid_columnconfigure(j, weight=1)

        print("UI Initialized!")

        self.root.mainloop()

    def set_date(self):
        selected_date_str = self.calendar.get_date()
        # Parse the date string into a datetime object
        selected_date_obj = datetime.strptime(selected_date_str, '%m/%d/%y')
        # Convert the datetime object to the desired format
        self.selected_date = selected_date_obj.strftime('%Y-%m-%d')
        print(f"Set Date called. Selected Date: {self.selected_date}")

    def set_route(self, route):
        Angel_Drive = "C:/Users/Ashley/OneDrive - Angel Care Group Limited/Documents/Audits"

        # Check if the selected_date attribute exists, if it doesn't default to today's date
        current_date = getattr(self, 'selected_date', datetime.now().date())

        DIRECTORY_FILEPATH = f"{Angel_Drive}/{route}/Audit_{current_date}"
        WORD_DOC_FILEPATH = f"{DIRECTORY_FILEPATH}/Audits_{current_date}.docx"

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
        print(f"Set Route called for: {route}")
        print(f"Number of PDFs found: {len(pdf_files)}")


    def show_error_message(self, msg="Error"):
        messagebox.showerror(msg)