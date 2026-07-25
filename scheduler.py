import time
import sys
from datetime import datetime, timedelta
from notifier import trigger_notification

def format_timedelta(td: timedelta) -> str:
    """Formats a timedelta into HH:MM:SS string."""
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def wait_for_alarm(target_time: datetime, title: str, message: str):
    """
    Blocks the main thread and waits until the target_time is reached.
    Updates the console with a countdown.
    """
    print(f"Alarm set for: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Message: {message}\n")
    print("Press Ctrl+C to cancel.")

    try:
        while True:
            now = datetime.now()
            remaining = target_time - now
            
            if remaining.total_seconds() <= 0:
                break
                
            # Print countdown on the same line
            sys.stdout.write(f"\rTime remaining: {format_timedelta(remaining)} ")
            sys.stdout.flush()
            
            # Sleep for 1 second (or less if close to target)
            sleep_time = min(1.0, remaining.total_seconds())
            time.sleep(sleep_time)

        # Clear the countdown line
        sys.stdout.write("\r" + " " * 30 + "\r")
        sys.stdout.flush()
        
        print("⏰ Alarm finished!")
        trigger_notification(title, message)
        
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled by user.")
        sys.exit(0)
