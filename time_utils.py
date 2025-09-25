from datetime import datetime, timezone

def now_utc():
    return datetime.now(timezone.utc)

def to_iso(dt):
    return dt.astimezone(timezone.utc).isoformat()
