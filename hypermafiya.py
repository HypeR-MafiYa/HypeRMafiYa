import os, sys

# Colors
R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"
C = "\033[96m"; W = "\033[97m"; RESET = "\033[0m"

def banner():
    os.system("clear")
    with open("logo.txt", "r") as f:
        print(f.read())

def menu():
    print(f"{Y}[1]{W} Bruteforce Demo")
    print(f"{Y}[2]{W} Phishing Demo")
    print(f"{Y}[3]{W} IP Tracker")
    print(f"{Y}[4]{W} Credits")
    print(f"{Y}[0]{W} Exit")

def main():
    while True:
        banner()
        menu()
        choice = input(f"\n{G}[+]{W} Select an option: ")

        if choice == "1":
            print(f"{R}[!] Bruteforce Demo not added yet.{RESET}")
        elif choice == "2":
            print(f"{R}[!] Phishing Demo not added yet.{RESET}")
        elif choice == "3":
            print(f"{R}[!] IP Tracker not added yet.{RESET}")
        elif choice == "4":
            print(f"{G}Created by: TanviR AhmmEd{RESET}")
        elif choice == "0":
            print(f"{Y}Exiting...{RESET}")
            sys.exit()
        else:
            print(f"{R}Invalid choice!{RESET}")

        input(f"\n{C}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    main()
