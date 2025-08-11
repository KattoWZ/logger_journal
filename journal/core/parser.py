def parse_journal(raw_text):
    lines = raw_text.strip().splitlines()
    
    data = {
        "Title": None,
        "Date of Creation": None,
        "Author": None,
        "Content": []
    }

    current_entry = {}
    in_entries = False

    for line in lines:
        line = line.strip()

        # Parse Title
        if line.startswith("JOURNAL"):
            data["Title"] = line

        # Parse Metadata
        elif line.startswith("[Date of Creation]"):
            data["Date of Creation"] = line.split(":", 1)[1].strip()

        elif line.startswith("[Author]"):
            data["Author"] = line.split(":", 1)[1].strip()

        # Start of a new entry
        elif line.startswith("[") and "]" in line and ":" not in line:
            # Save current entry if it's not empty
            if current_entry:
                data["Content"].append(current_entry)
                current_entry = {}

            current_entry["Time"] = line.strip("[]")

        # Parse fields inside an entry
        elif line.startswith("[ID]"):
            current_entry["ID"] = line.split(":", 1)[1].strip()

        elif line.startswith("[Tags]"):
            current_entry["Tags"] = line.split(":", 1)[1].strip()

        elif line.startswith("[Journal]"):
            current_entry["Journal"] = line.split(":", 1)[1].strip()

    # Don't forget the last entry!
    if current_entry:
        data["Content"].append(current_entry)

    return [data]
