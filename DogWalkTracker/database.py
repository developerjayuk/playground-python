entries = []


def add_entry(entry_content, entry_date):
    entries.append({"date": entry_date, "content": f"Dog walks today: {entry_content}"})


def get_entries():
    return entries
