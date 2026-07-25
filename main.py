import sys
from cli import get_args
from parser import parse_time
from scheduler import wait_for_alarm

def main():
    try:
        args = get_args()
        
        # Parse the requested time
        target_time = parse_time(args.time)
        
        # Start the alarm loop
        wait_for_alarm(target_time, args.title, args.message)
        
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
