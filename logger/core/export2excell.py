from pathlib import Path
import re
import openpyxl
from openpyxl.styles import Alignment
from config import LOG_DIR
from utils.inputValidator import reqInput as ri

def export_to_excel():
    print("Insert '!' to return to main menu")            
    filename = ri("Input the file you want to export to excel: ").strip().lower()
    log_path = log_dir / f"{filename}.txt"
    
    if not log_path.exists():
        print(f"File '{filename}.txt' not found in logs.")
        return

    # Create a new Excel workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Log Export"

    # Set headers
    headers = ["Timestamp", "Task", "Status", "Progress", "Name", "Detail"]
    ws.append(headers)

    # Align headers
    for cell in ws[1]:
        cell.alignment = Alignment(horizontal='center')

    # Read log file and extract entries
    with open(log_path, "r") as file:
        content = file.read()

    entries = re.split(r"-{5,}", content)  # Split by lines like "-----"

    for entry in entries:
        lines = entry.strip().splitlines()
        if len(lines) < 5:
            continue  # Skip empty or malformed entries

        timestamp = re.search(r"(.*?)", lines[0])
        task = re.search(r"Task ?: ?(.*)", lines[1])
        status = re.search(r"Status ?: ?(.*)", lines[2])
        progress = re.search(r"Progress ?: ?(.*)", lines[3])
        detail = re.search(r"Detail ?: ?(.*)", lines[4])

        # Fallback if name line exists
        name = ""
        for line in lines:
            if "[Name]" in line:
                name_match = re.search(r"Name ?: ?(.*)", line)
                if name_match:
                    name = name_match.group(1)

        ws.append([
            timestamp.group(1) if timestamp else "",
            task.group(1) if task else "",
            status.group(1) if status else "",
            progress.group(1) if progress else "",
            name,
            detail.group(1) if detail else ""
        ])

    # Save Excel
    excel_path = log_dir / f"{filename}.xlsx"
    wb.save(excel_path)
    print(f"Excel file saved as '{filename}.xlsx' in logs.")
