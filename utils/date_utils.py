from datetime import datetime

def countdown_text(date_time):
    now = datetime.now()
    delta = date_time.date() - now.date()

    if delta.days < 0:
        return "Termin vorbei!"
    elif delta.days == 0:
        return "Heute"
    elif delta.days == 1:
        return "1 Tag"
    else:
        return f"{delta.days} Tage"
