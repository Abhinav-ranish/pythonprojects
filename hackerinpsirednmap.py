import subprocess
import os
import time
import random

def print_with_effects(text, delay=0.05):
    """Print text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ascii_banner():
    """Print a hacker-themed ASCII banner."""
    banner = """
    ███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
    ████╗  ██║████╗ ████║██╔══██╗██╔══██╗
    ██╔██╗ ██║██╔████╔██║███████║██████╔╝
    ██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
    ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║       
    ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝      
    """
    print(banner)

def fake_logs():
    """Generate hacker-style logs."""
    fake_messages = [
        "[SYS] Connecting to target...",
        "[NET] Establishing secure backdoor...",
        "[HACK] Injecting payload...",
        "[SCAN] Mapping open ports...",
        "[INFO] Collecting system info...",
    ]
    for _ in range(10):
        log = random.choice(fake_messages)
        print_with_effects(log, delay=0.02)
        time.sleep(0.5)

def run_nmap(target):
    """Run an Nmap scan on the specified target."""
    print_with_effects("[HACK] Initiating Nmap scan...", delay=0.02)
    time.sleep(1)
    try:
        # Run an Nmap scan
        result = subprocess.check_output(["nmap", "-A", target], stderr=subprocess.STDOUT, text=True)
        print_with_effects("[HACK] Scan complete!", delay=0.02)
        print_with_effects("[RESULT] Parsing scan results...", delay=0.02)
        time.sleep(1)
        print("\n=== SCAN RESULTS ===")
        print(result)
    except subprocess.CalledProcessError as e:
        print_with_effects("[ERROR] Failed to execute Nmap scan.", delay=0.02)
        print(e.output)
    except FileNotFoundError:
        print_with_effects("[ERROR] Nmap is not installed. Please install it and try again.", delay=0.02)

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    ascii_banner()
    print_with_effects("Welcome to the Hacker Nmap Scanner!", delay=0.05)
    target = input("Enter the target IP or domain: ")
    fake_logs()
    run_nmap(target)

if __name__ == "__main__":
    main()
