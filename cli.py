import argparse

def get_args():
    """
    Sets up the argument parser for the CLI clock.
    """
    parser = argparse.ArgumentParser(
        description="A native Python CLI Alarm Clock for Windows.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "time",
        help="The time for the alarm.\n"
             "Relative: 10s, 5m, 2h\n"
             "Absolute: 14:30, 08:15:00"
    )
    
    parser.add_argument(
        "-m", "--message",
        default="Your alarm is finished!",
        help="The message to display when the alarm goes off."
    )
    
    parser.add_argument(
        "-t", "--title",
        default="Python Alarm",
        help="The title of the notification."
    )
    
    return parser.parse_args()
