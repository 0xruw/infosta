import os 
import requests 
import instaloader 
from colorama import Fore, Style, init 
 
init(autoreset=True) 
 
def print_credits(): 
    os.system("pip install requests instaloader colorama ") 
    os.system("cls" if os.name == "nt" else "clear") 
    credits = r""" 
  ___                             _        __           _         
 / _ \__  ___ __ _   ___      __ (_)_ __  / _| ___  ___| |_ __ _  
| | | \ \/ / '__| | | \ \ /\ / / | | '_ \| |_ / _ \/ __| __/ _` | 
| |_| |>  <| |  | |_| |\ V  V /  | | | | |  _| (_) \__ \ || (_| | 
 \___//_/\_\_|   \__,_| \_/\_/   |_|_| |_|_|  \___/|___/\__\__,_| 
  
 Insta : 0xruw 
"""  
    print(Fore.GREEN + credits) 
 
def read_settings(): 
    settings = {} 
    try: 
        with open("settings.txt", "r") as file: 
            for line in file: 
                if "=" in line: 
                    key, value = line.strip().split("=", 1) 
                    settings[key] = value 
        return settings 
    except FileNotFoundError: 
        print(Fore.RED + "Settings file not found. Please create the file and try again.") 
        return None 
 
def fetch_high_quality_profile_pic(profile): 
    try: 
        return profile.get_hd_profile_pic_url() 
    except AttributeError: 
        return 'N/A' 
 
def fetch_details(loader, username, token, chat_id, proxy): 
    try: 
        profile = instaloader.Profile.from_username(loader.context, username) 
        profile_pic_url = fetch_high_quality_profile_pic(profile) 
        creation_date = date(profile.userid)   
 
        details = ( 
            f"Username: {profile.username}\n" 
            f"Full Name: {profile.full_name}\n" 
            f"Followers: {profile.followers}\n" 
            f"Following: {profile.followees}\n" 
            f"Posts: {profile.mediacount}\n" 
            f"Bio: {profile.biography}\n" 
            f"Profile Picture URL: {profile_pic_url}\n" 
            f"Account Creation Year: {creation_date}\n" 
            f"{'-'*40}\n" 
        ) 
 
        send_to_telegram(details, token, chat_id, proxy) 
 
    except instaloader.exceptions.ProfileNotExistsException: 
        error_message = f"The account {username} does not exist or has been banned." 
        send_to_telegram(error_message, token, chat_id, proxy)   
 
    except instaloader.exceptions.QueryReturnedBadRequestException: 
        pass  
 
    except Exception: 
        pass 
 
def send_to_telegram(message, token, chat_id, proxy): 
    proxies_dict = {"http": proxy, "https": proxy} if proxy else None 
    try: 
        response = requests.post( 
            f"https://api.telegram.org/bot{token}/sendMessage", 
            data={"chat_id": chat_id, "text": message}, 
            proxies=proxies_dict 
        ) 
        if response.status_code == 200: 
            print(Fore.GREEN + "Message sent to Telegram successfully.") 
 
    except Exception as e: 
        print(Fore.RED + f"Error sending message to Telegram: {e}") 
 
def date(hy): 
    try: 
        ranges = [ 
            (1279000, 2010), 
            (17750000, 2011), 
            (279760000, 2012), 
            (900990000, 2013), 
            (1629010000, 2014), 
            (2500000000, 2015), 
            (3713668786, 2016), 
            (5699785217, 2017), 
            (8597939245, 2018), 
            (21254029834, 2019) 
        ] 
 
        for upper, year in ranges: 
            if hy <= upper: 
                return year 
        return "2020-2025" 
    except Exception as e : 
        return str(e) 
 
def process_user_input(): 
    while True: 
        print(Fore.YELLOW + "\nSelect an option:") 
        print("1 - Search for a single user") 
        print("2 - Search using a list of usernames from a file") 
        print("99 - Exit") 
         
        choice = input("Enter your choice: ").strip() 
 
        if choice == '1': 
            username = input("Enter the Instagram username: ").strip() 
            fetch_details(loader, username, token, chat_id, None) 
        elif choice == '2': 
            file_path = input("Enter the file path containing usernames: ").strip() 
            if not os.path.exists(file_path): 
                print(Fore.RED + "The file was not found. Please check the path and try again.") 
                continue 
            with open(file_path, "r") as file: 
                usernames = [line.strip() for line in file] 
            for target_username in usernames: 
                fetch_details(loader, target_username, token, chat_id, None) 
        elif choice == '99': 
            print(Fore.GREEN + "Exiting...") 
            break 
        else: 
            print(Fore.RED + "Invalid choice. Please try again.") 
 
def main(): 
    print_credits() 
 
    settings = read_settings() 
    if not settings: 
        return 
     
    global token, chat_id, loader 
    token = settings.get("Bot_token") 
    chat_id = settings.get("User_id") 
    instagram_username = settings.get("Your_instagram_(fake)") 
    instagram_password = settings.get("Password") 
 
    if not all([token, chat_id, instagram_username, instagram_password]): 
        print(Fore.RED + "Some settings are missing in the settings.txt file.") 
        return 
 
    loader = instaloader.Instaloader() 
    session_dir = os.getenv("TEMP") or "/tmp"  # تحديد مسار افتراضي 
    session_path = os.path.join(session_dir, f".instaloader-{os.getlogin()}", f"session-{instagram_username}") 
 
    try: 
        if os.path.exists(session_path): 
            loader.load_session_from_file(instagram_username) 
            print(Fore.GREEN + "Session loaded successfully.") 
        else: 
            loader.login(instagram_username, instagram_password) 
            loader.save_session_to_file() 
            print(Fore.GREEN + "Login successful and session saved.") 
    except Exception as e: 
        print(Fore.RED + f"Login failed: {e}") 
        return 
 
    process_user_input() 
 
if __name__ == "__main__": 
    main()
