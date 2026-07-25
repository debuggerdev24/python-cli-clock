# Python CLI Alarm Clock

A lightweight, purely native Python command-line alarm clock built specifically for Windows. This tool uses zero third-party dependencies (no `pip install` required) and utilizes Windows native PowerShell commands to deliver Toast notifications and audio alerts when your alarm is finished.

## Features

- **Zero External Dependencies:** Built entirely with Python Standard Library (`argparse`, `datetime`, `subprocess`, `winsound`).
- **Native Notifications:** Triggers a native Windows 11 Toast / Balloon notification using a `.NET` bridge via PowerShell.
- **Audio Alerts:** Plays a standard Windows system beep alongside the notification.
- **Flexible Time Parsing:** Set alarms using both relative and absolute time formats.
- **Live Terminal Countdown:** Displays a cleanly updating remaining-time countdown directly in your CLI.
- **Customizable Alerts:** Add custom titles and messages to your alarm notifications.

## Requirements

- Python 3.x
- Windows OS (Windows 10 / 11) with PowerShell available.

## Usage

Run the alarm clock from your terminal using `main.py`.

```bash
python main.py <time> [options]
```

### 1. Relative Time Alarms
Set an alarm to go off in a specific amount of time.
Supported units: `s` (seconds), `m` (minutes), `h` (hours).

```bash
# Alarm in 10 seconds
python main.py 10s

# Alarm in 5 minutes
python main.py 5m

# Alarm in 2 hours
python main.py 2h
```

### 2. Absolute Time Alarms
Set an alarm for a specific time of day (24-hour format `HH:MM` or `HH:MM:SS`).
*Note: If the time you enter has already passed today, the alarm will automatically schedule for that time tomorrow.*

```bash
# Alarm at 2:30 PM today
python main.py 14:30

# Alarm at exactly 8:15 and 30 seconds AM
python main.py 08:15:30
```

### 3. Custom Titles and Messages
You can customize the notification popup using the `-t` (`--title`) and `-m` (`--message`) flags.

```bash
python main.py 5m -t "Meeting Reminder" -m "Time to join the daily standup!"
```

## How to Cancel

To cancel a running alarm, simply press `Ctrl+C` in your terminal. The application will catch the interruption and exit gracefully.

## Architecture

The codebase is strictly modularized for clean architecture:
- `main.py`: Entry point that ties all modules together.
- `cli.py`: Uses `argparse` to handle terminal arguments and help menus.
- `parser.py`: Translates relative/absolute string inputs into a target `datetime` object.
- `scheduler.py`: Handles the real-time wait loop and terminal countdown updating.
- `notifier.py`: Invokes OS-level APIs (via PowerShell subprocess and `winsound`) to alert the user.
