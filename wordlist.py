import os
from datetime import datetime
import random
import string
import glob

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    banner = r"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗               ║
║   ██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝               ║
║   ██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   █████╗                 ║
║   ██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝                 ║
║   ╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗               ║
║    ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝               ║
║                                                                               ║
║                 ULTIMATE PASSWORD LIST GENERATOR v10.0                       ║
║                       Complete Professional Edition                           ║
║                  Only for Ethical Penetration Testing                         ║
║                                                                               ║
║                       Developed by @Mdnurnobirazz                              ║
║                        Made with ❤️ in Termux                                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    print(color(banner, "1;35"))
    print()

def open_url(url):
    if os.system(f"termux-open-url {url}") != 0:
        print(color(f"\n[!] Browser open failed. Manually visit: {url}", "1;31"))
        input(color("\nPress Enter to continue...", "1;37"))

def follow_us():
    while True:
        clear_screen()
        print_banner()
        print(color("                         🔗 FOLLOW & SUPPORT 🔗\n", "1;37"))
        print(color("   [1] 🌐 GitHub      → github.com/mdnurnobirazz", "1;34"))
        print(color("   [2] 📺 YouTube     → @mdnurnobirazz0", "1;34"))
        print(color("   [3] 💬 Telegram    → t.me/Modapkstudio", "1;34"))
        print(color("   [4] 📘 Facebook    → facebook.com/share/1C5bQssHfL/", "1;34"))
        print(color("   [5] 👨‍💻 Developer Info", "1;34"))
        print(color("   [6] 🔙 Back to Main Menu\n", "1;37"))

        try:
            choice = int(input(color("Select option (1-6): ", "1;33")))
            if choice == 1:
                open_url("https://github.com/mdnurnobirazz")
            elif choice == 2:
                open_url("https://youtube.com/@mdnurnobirazz0")
            elif choice == 3:
                open_url("https://t.me/Modapkstudio")
            elif choice == 4:
                open_url("https://www.facebook.com/share/1C5bQssHfL/")
            elif choice == 5:
                clear_screen()
                print_banner()
                print(color("                         👨‍💻 DEVELOPER INFO 👨‍💻\n", "1;37"))
                print(color("   Username     : @Mdnurnobirazz", "1;32"))
                print(color("   GitHub       : github.com/mdnurnobirazz", "1;34"))
                print(color("   YouTube      : @mdnurnobirazz0", "1;34"))
                print(color("   Telegram     : t.me/Modapkstudio", "1;34"))
                print(color("   Facebook     : facebook.com/share/1C5bQssHfL/", "1;34"))
                print(color("   Tool Version  : v10.0 Complete\n", "1;37"))
                input(color("Press Enter to go back...", "1;37"))
            elif choice == 6:
                return
            else:
                print(color("Invalid option!", "1;31"))
                input(color("Press Enter...", "1;37"))
        except ValueError:
            print(color("Please enter a number!", "1;31"))
            input(color("Press Enter...", "1;37"))

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=" for c in password):
        score += 1
    if score <= 2:
        return "Weak", "1;31"
    elif score <= 4:
        return "Medium", "1;33"
    elif score <= 5:
        return "Strong", "1;32"
    else:
        return "Very Strong", "1;32"

def random_password_generator():
    clear_screen()
    print_banner()
    print(color("                 🔐 Random Strong Password Generator\n", "1;37"))
    try:
        length = int(input(color("   Password length (8-50): ", "1;33")))
        if length < 8 or length > 50:
            print(color("Length must be between 8 and 50!", "1;31"))
            input(color("Press Enter...", "1;37"))
            return
        num = int(input(color("   How many passwords: ", "1;33")))
        if num < 1 or num > 100:
            print(color("Number must be between 1 and 100!", "1;31"))
            input(color("Press Enter...", "1;37"))
            return
    except ValueError:
        print(color("Please enter a number!", "1;31"))
        input(color("Press Enter...", "1;37"))
        return

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    print(color("\n   Generated passwords:\n", "1;32"))
    for i in range(num):
        pwd = ''.join(random.choice(chars) for _ in range(length))
        strength, ccode = password_strength(pwd)
        print(color(f"   {i+1}. {pwd}  [{strength}]", ccode))
    input(color("\nPress Enter to return...", "1;37"))

def strength_checker():
    clear_screen()
    print_banner()
    print(color("                 🔍 Password Strength Checker\n", "1;37"))
    pwd = input(color("   Enter password to check: ", "1;33"))
    if not pwd:
        print(color("No password entered!", "1;31"))
        input(color("Press Enter...", "1;37"))
        return
    strength, ccode = password_strength(pwd)
    print(color(f"\n   Strength: {strength}", ccode))
    input(color("\nPress Enter to return...", "1;37"))

def leet_converter():
    clear_screen()
    print_banner()
    print(color("                 🔤 Leet Speak Converter\n", "1;37"))
    word = input(color("   Enter word to convert: ", "1;33")).strip()
    if not word:
        print(color("No word entered!", "1;31"))
        input(color("Press Enter...", "1;37"))
        return
    leet_dict = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['5', '$'], 't': ['7'], 'b': ['8'], 'g': ['9']}
    variants = [word]
    for normal, leets in leet_dict.items():
        new = []
        for v in variants:
            for l in leets:
                new.append(v.replace(normal, l))
                new.append(v.replace(normal.upper(), l.upper()))
        variants.extend(new)
    unique = sorted(list(set(variants)))
    print(color(f"\n   Leet variations ({len(unique)}):\n", "1;32"))
    for v in unique[:50]:
        print(color(f"   • {v}", "1;37"))
    if len(unique) > 50:
        print(color("   ... (showing first 50)", "1;33"))
    input(color("\nPress Enter to return...", "1;37"))

def merge_custom_wordlist():
    clear_screen()
    print_banner()
    print(color("                 📄 Merge Custom Wordlist\n", "1;37"))
    custom_file = input(color("   Enter custom wordlist filename (in current folder): ", "1;33")).strip()
    if not custom_file.endswith(".txt"):
        custom_file += ".txt"
    if not os.path.exists(custom_file):
        print(color("File not found!", "1;31"))
        input(color("Press Enter...", "1;37"))
        return

    with open(custom_file, "r", encoding="utf-8") as f:
        custom_lines = [line.strip() for line in f if line.strip()]

    print(color(f"   Loaded {len(custom_lines)} passwords from {custom_file}\n", "1;32"))
    # এখানে তুমি চাইলে এগুলোকে মেইন লিস্টে মার্জ করতে পারো, কিন্তু সিম্পল রাখলাম
    print(color("   Custom list loaded! You can use it with main generator.", "1;33"))
    input(color("\nPress Enter to return...", "1;37"))

def view_last_list():
    clear_screen()
    print_banner()
    print(color("                 📜 View Last Generated List\n", "1;37"))
    files = sorted(glob.glob("wordlist_*.txt"), key=os.path.getmtime, reverse=True)
    if not files:
        print(color("No wordlist found!", "1;31"))
        input(color("Press Enter...", "1;37"))
        return
    last_file = files[0]
    print(color(f"   Last file: {last_file}\n", "1;32"))
    try:
        with open(last_file, "r", encoding="utf-8") as f:
            lines = f.readlines()[:50]
        print(color("   First 50 passwords:\n", "1;32"))
        for i, line in enumerate(lines, 1):
            print(color(f"   {i}. {line.strip()}", "1;37"))
        if len(lines) == 50:
            print(color("   ... (showing first 50)", "1;33"))
    except:
        print(color("Error reading file!", "1;31"))
    input(color("\nPress Enter to return...", "1;37"))

def clean_old_lists():
    clear_screen()
    print_banner()
    print(color("                 🗑️ Clean Old Lists\n", "1;37"))
    files = glob.glob("wordlist_*.txt")
    if not files:
        print(color("No old lists found!", "1;32"))
        input(color("Press Enter...", "1;37"))
        return
    print(color(f"   Found {len(files)} old lists:\n", "1;33"))
    for f in files:
        print(color(f"   • {f}", "1;37"))
    confirm = input(color("\n   Delete all? (y/n): ", "1;33")).lower()
    if confirm == 'y':
        for f in files:
            os.remove(f)
        print(color("\n   All old lists deleted!", "1;32"))
    else:
        print(color("   Operation cancelled.", "1;33"))
    input(color("\nPress Enter to return...", "1;37"))

def about_tool():
    clear_screen()
    print_banner()
    print(color("                         📖 ABOUT TOOL 📖\n", "1;37"))
    print(color("   Ultimate Password List Generator", "1;32"))
    print(color("   Version        : v10.0 Complete Professional", "1;37"))
    print(color("   Developer      : @Mdnurnobirazz", "1;32"))
    print(color("   Platform       : Termux / Python", "1;37"))
    print(color("   Purpose        : Ethical Penetration Testing Only", "1;33"))
    print(color("\n   Features:", "1;36"))
    print(color("   • Personal info based password list generation", "1;37"))
    print(color("   • Random strong password generator", "1;37"))
    print(color("   • Password strength checker", "1;37"))
    print(color("   • Leet speak converter", "1;37"))
    print(color("   • Custom wordlist merge", "1;37"))
    print(color("   • View & clean old lists", "1;37"))
    print(color("\n   Stay Ethical! Never use for illegal purposes.", "1;31"))
    input(color("\nPress Enter to return...", "1;37"))

def generate_wordlist():
    clear_screen()
    print_banner()
    print(color("[*] Enter Target Information (leave blank to skip):\n", "1;35"))

    first_name = input(color("   [+] First Name       : ", "1;37")).strip().lower()
    last_name = input(color("   [+] Last Name        : ", "1;37")).strip().lower()
    nickname = input(color("   [+] Nickname         : ", "1;37")).strip().lower()
    birth_date = input(color("   [+] Birth Date (dd/mm/yyyy) : ", "1;37")).strip()
    birth_year = input(color("   [+] Birth Year (yyyy or yy) : ", "1;37")).strip()
    phone_last = input(color("   [+] Phone Last Digits: ", "1;37")).strip()
    partner = input(color("   [+] Partner Name     : ", "1;37")).strip().lower()
    child = input(color("   [+] Child Name       : ", "1;37")).strip().lower()
    pet = input(color("   [+] Pet/Keyword      : ", "1;37")).strip().lower()
    favorite = input(color("   [+] Favorite Word    : ", "1;37")).strip().lower()

    base_words = [w for w in [first_name, last_name, nickname, partner, child, pet, favorite] if w]

    if not base_words:
        print(color("\n[!] No information provided! Exiting...", "1;31"))
        input(color("\nPress Enter to continue...", "1;37"))
        return

    extras = [
        "1", "12", "123", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890",
        "786", "000", "111", "2020", "2021", "2022", "2023", "2024", "2025", "2026",
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "!!", "@@", "##", "$$", "%%",
        "love", "baby", "king", "queen", "god", "allah", "password", "admin", "root", "user", "test", "abc", "xyz"
    ]

    wordlist = []

    for word in base_words:
        variants = [word, word.capitalize(), word.upper()]
        for v in variants:
            wordlist.append(v)
            for extra in extras:
                wordlist.extend([
                    v + extra,
                    extra + v,
                    v + extra + v,
                    extra + v + extra,
                    v + extra + extra,
                    extra + extra + v
                ])

    for w1 in base_words:
        for w2 in base_words:
            for w3 in base_words:
                combo = w1 + w2 + w3
                wordlist.extend([combo, combo.capitalize()])

    if birth_date:
        clean = birth_date.replace("/", "").replace("-", "").replace(".", "")
        wordlist.extend([birth_date, clean])
        for word in base_words:
            wordlist.extend([word + birth_date, word + clean, birth_date + word, clean + word])

    if birth_year:
        short = birth_year[-2:]
        wordlist.extend([birth_year, short])
        for word in base_words:
            wordlist.extend([word + birth_year, word + short, birth_year + word, short + word])

    if phone_last:
        wordlist.append(phone_last)
        for word in base_words:
            wordlist.extend([word + phone_last, phone_last + word])

    full_list = sorted(list(set(wordlist)))
    total = len(full_list)

    clear_screen()
    print_banner()
    print(color(f"[+] Total unique combinations generated: {total}\n", "1;32"))

    print(color("Select password list size:", "1;36"))
    print(color("   [1] 500 passwords", "1;37"))
    print(color("   [2] 1,000 passwords", "1;37"))
    print(color("   [3] 5,000 passwords", "1;37"))
    print(color("   [4] 10,000 passwords", "1;37"))
    print(color("   [5] 20,000 passwords", "1;37"))
    print(color("   [6] 40,000 passwords", "1;37"))
    print(color("   [7] 50,000 passwords", "1;37"))
    print(color("   [8] All available\n", "1;37"))

    options = {1: 500, 2: 1000, 3: 5000, 4: 10000, 5: 20000, 6: 40000, 7: 50000, 8: total}

    while True:
        try:
            choice = int(input(color("\nSelect option (1-8): ", "1;33")))
            if choice in options:
                limit = options[choice]
                break
            else:
                print(color("Invalid choice!", "1;31"))
        except ValueError:
            print(color("Please enter a number!", "1;31"))

    final_list = full_list[:limit]

    filename = f"wordlist_{first_name or 'target'}_{limit}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for item in final_list:
            f.write(item + "\n")

    clear_screen()
    print_banner()
    print(color("✅ Password list successfully created!", "1;32"))
    print(color(f"   📄 File: {filename}", "1;37"))
    print(color(f"   🔢 Passwords: {len(final_list)}", "1;37"))
    print(color(f"   📂 Location: {os.getcwd()}/{filename}\n", "1;37"))
    input(color("Press Enter to return to main menu...", "1;37"))

def main_menu():
    while True:
        print_banner()
        print(color("                         MAIN MENU\n", "1;37"))
        print(color("   [1] 🌟 Generate Password List", "1;34"))
        print(color("   [2] 🔐 Random Password Generator", "1;34"))
        print(color("   [3] 🔍 Password Strength Checker", "1;34"))
        print(color("   [4] 🔤 Leet Speak Converter", "1;34"))
        print(color("   [5] 📄 Merge Custom Wordlist", "1;34"))
        print(color("   [6] 📜 View Last List", "1;34"))
        print(color("   [7] 🗑️ Clean Old Lists", "1;34"))
        print(color("   [8] 🔗 Follow & Support", "1;34"))
        print(color("   [9] 📖 About Tool", "1;34"))
        print(color("   [10] 🚪 Exit\n", "1;34"))

        try:
            choice = int(input(color("Select option (1-10): ", "1;33")))
            if choice == 1:
                generate_wordlist()
            elif choice == 2:
                random_password_generator()
            elif choice == 3:
                strength_checker()
            elif choice == 4:
                leet_converter()
            elif choice == 5:
                merge_custom_wordlist()
            elif choice == 6:
                view_last_list()
            elif choice == 7:
                clean_old_lists()
            elif choice == 8:
                follow_us()
            elif choice == 9:
                about_tool()
            elif choice == 10:
                clear_screen()
                print(color("Thanks for using Ultimate Password List Generator!", "1;32"))
                print(color("Stay Ethical & Keep Hacking ❤️ @Mdnurnobirazz", "1;33"))
                break
            else:
                print(color("Invalid option!", "1;31"))
                input(color("Press Enter...", "1;37"))
        except ValueError:
            print(color("Please enter a number!", "1;31"))
            input(color("Press Enter...", "1;37"))

if __name__ == "__main__":
    main_menu()