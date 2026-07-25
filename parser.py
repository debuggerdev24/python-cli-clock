import re
from datetime import datetime, timedelta

def parse_time(time_str: str) -> datetime:
    """
    Parses a time string and returns the target datetime object for the alarm.
    
    Supports:
    - Relative time: e.g., '10s', '5m', '2h'
    - Absolute time: e.g., '14:30', '14:30:00'
    """
    time_str = time_str.strip().lower()

    # Regex for relative time (e.g., "10s", "5m", "2h")
    relative_match = re.match(r'^(\d+)\s*([smh])$', time_str)
    if relative_match:
        amount = int(relative_match.group(1))
        unit = relative_match.group(2)
        
        now = datetime.now()
        if unit == 's':
            return now + timedelta(seconds=amount)
        elif unit == 'm':
            return now + timedelta(minutes=amount)
        elif unit == 'h':
            return now + timedelta(hours=amount)

    # Regex for absolute time (e.g., "14:30", "14:30:00")
    # Simple check for HH:MM or HH:MM:SS
    absolute_match = re.match(r'^(\d{1,2}):(\d{2})(?::(\d{2}))?$', time_str)
    if absolute_match:
        hours = int(absolute_match.group(1))
        minutes = int(absolute_match.group(2))
        seconds = int(absolute_match.group(3)) if absolute_match.group(3) else 0

        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            raise ValueError(f"Invalid absolute time format: {time_str}")

        now = datetime.now()
        target_time = now.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)

        # If the target time is earlier than now, assume it's for tomorrow
        if target_time <= now:
            target_time += timedelta(days=1)
            
        return target_time

    raise ValueError(f"Unsupported time format: '{time_str}'. Try '5m', '1h', or '14:30'.")
