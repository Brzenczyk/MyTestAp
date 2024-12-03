# mytest_terminal.py

import argparse

def handle_terminal_args(args):
    if args.command == "help":
        print("Available commands:")
        print("- IPv4 Info: Prints IPv4 information")
        print("- Proxy Info: Checks proxy settings")
        print("- System Info: Prints system info")
        print("- BIOS Version: Prints BIOS version")
        print("- Host Name: Prints the host name")
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MyTest Command Line Interface")
    parser.add_argument(
        "command",
        type=str,
        nargs="?",
        default="help",  # Domyślny argument to "help"
        help="Command to execute"
    )
    args = parser.parse_args()
    handle_terminal_args(args)
