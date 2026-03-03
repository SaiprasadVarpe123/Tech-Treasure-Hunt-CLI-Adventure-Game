from colorama import init, Fore, Style
import os
import time
import sys

# Initialize colorama for cross-platform color support
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    banner = f"""
{Fore.YELLOW}════════════════════════════════════════════════════════════════════
             🎮  TECH TREASURE HUNT ADVENTURE  🎯
════════════════════════════════════════════════════════════════════
    
     🔍  Decode the Riddles  |  Find the Secrets  |  Win the Game
{Style.RESET_ALL}"""
    print(banner)

def print_treasure_box():
    treasure_chest = f"""
{Fore.BLACK}*******************************************************************************
          |                   |                  |                     |
 _________|________________{Fore.YELLOW}.=""_;=.{Fore.BLACK}______________|_____________________|_______
|                   |  {Fore.YELLOW},-"_,=""     `\"=.{Fore.BLACK}|                  |
|___________________|__{Fore.YELLOW}"=._o`"-._        `\"=.{Fore.BLACK}______________|___________________
          |                {Fore.YELLOW}`\"=._o`\"=._      _`\"=.{Fore.BLACK}_                     |
 _________|_____________________{Fore.YELLOW}:=._o `\"=._."_.-=\"'"=.{Fore.BLACK}__________________|_______
|                   |    {Fore.YELLOW}__.--" , ; `\"=._o." ,-\"\"\"-._ ".{Fore.BLACK}   |
|___________________|{Fore.YELLOW}_._"  ,. .` ` `` ,  `"-._"-._   ". ;{Fore.BLACK}___________________
          |           {Fore.YELLOW}|o`\"=._` , "` `; .". ,  "-._"-._; ;{Fore.BLACK}              |
 _________|___________{Fore.YELLOW}| ;`-.o`\"=._; ." ` '`.\"` . "-._ /{Fore.BLACK}_______________|_______
|                   |{Fore.YELLOW} |o;    `"-.o`\"=._``  '` " ,__.--o;{Fore.BLACK}   |
|___________________|_{Fore.YELLOW}| ;     (#) `-.o `\"=. `_.--"_o.-; ;{Fore.BLACK}___|___________________
____/______/______/___{Fore.YELLOW}|o;._    "      `\".o|o_.--"    ;o;{Fore.BLACK}____/______/______/____
/______/______/______/_{Fore.YELLOW}"=._o--._        ; | ;        ; ;{Fore.BLACK}/______/______/______/_ 
____/______/______/______/__{Fore.YELLOW}"=._o--._   ;o|o;     _._;o;{Fore.BLACK}____/______/______/____
/______/______/______/______/____{Fore.YELLOW}"=._o._; | ;_.--"o.--"{Fore.BLACK}_/______/______/______/_ 
____/______/______/______/______/_____{Fore.YELLOW}"=.o|o_.--""{Fore.BLACK}___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/{Fore.BLUE}[TIC Club]{Fore.BLACK}
*******************************************************************************
"""
    print(treasure_chest)

def check_answer(case_number, answer):
    answers = {
        1: "SOFTWARE",
        2: "BOOKS",
        3: "RESISTOR",
        4: "WHITEBOARD",
        5: "PLANT"
    }
    return answer.upper() == answers[case_number]

def print_case_header(case_number):
    header = f"""
{Fore.CYAN}╔{'═' * 58}╗
║{' ' * 24}TASK {case_number}{' ' * 28}║
╚{'═' * 58}╝{Style.RESET_ALL}"""
    print(header)

def run_case(case_number):
    riddles = {
        1: (
            f"{Fore.GREEN}In the realm where ideas take flight",
            "Where innovation shines bright.",
            "Seek the space where projects bright",
            f"Enter the password hidden in this sight.{Style.RESET_ALL}"
        ),
        2: (
            f"{Fore.GREEN}Amidst the shelves where knowledge hides",
            "Where stories bloom and thought resides.",
            "Find the haven where readers muse.",
            f"Discover the word where books are produced!{Style.RESET_ALL}"
        ),
        3: (
            f"{Fore.GREEN}Where circuits hum and wires entwine",
            "In a room where technology defines.",
            "Seek the place where innovation thrives",
            f"Find the word to unlock what your heart desires.{Style.RESET_ALL}"
        ),
        4: (
            f"{Fore.GREEN}Convert me to find your next Location",
            f" ‘ 0011 0001 0001 0011’{Style.RESET_ALL}"
        ),
        5: (
            f"{Fore.GREEN}Amongst the petals where beauty resides",
            "Where fragrance blooms and colors collide.",
            "One hole is big, the other are small,",
            "In a garden, I might stand tall.",
            f"Seek the place where nature reigns.{Style.RESET_ALL}"
        )
    }
    
    while True:
        clear_screen()
        print_banner()
        print_case_header(case_number)
        
        for line in riddles[case_number]:
            print_slow(line)
        
        print(f"\n{Fore.YELLOW}╭{'─' * 58}╮")
        answer = input(f"│ Your answer: ").strip()
        print(f"╰{'─' * 58}╯{Style.RESET_ALL}")
        
        if check_answer(case_number, answer):
            print(f"\n{Fore.GREEN}🌟 Excellent! You've solved TASK {case_number}! 🌟{Style.RESET_ALL}")
            time.sleep(2)
            return True
        else:
            print(f"\n{Fore.RED}❌ That's not quite right. Keep searching!{Style.RESET_ALL}")
            retry = input(f"\n{Fore.YELLOW}Press Enter to try again or 'quit' to exit: {Style.RESET_ALL}")
            if retry.lower() == 'quit':
                return False

def run_treasure_hunt():
    clear_screen()
    print_banner()
    print_treasure_box()
    print_slow(f"\n{Fore.CYAN}Welcome brave explorer! Your adventure awaits...{Style.RESET_ALL}", 0.05)
    time.sleep(2)
    
    current_case = 1
    while current_case <= 5:
        if not run_case(current_case):
            print(f"\n{Fore.YELLOW}Game ended. You solved {current_case - 1} cases.{Style.RESET_ALL}")
            break
        
        if current_case < 5:
            print(f"\n{Fore.MAGENTA}🎉 Preparing next challenge... 🎉{Style.RESET_ALL}")
            time.sleep(2)
        current_case += 1
    
    if current_case > 5:
        clear_screen()
        print_banner()
        print_treasure_box()
        victory_message = f"""
{Fore.GREEN}🎉 CONGRATULATIONS! 🎉

You've mastered all the challenges and completed the Tech Treasure Hunt!
You're truly a master of puzzles and exploration!

      {Fore.YELLOW} HERE IS YOUR TREASURE's LOCATION

{Fore.GREEN} A place for dreams to hatch and take flight,
Helping young minds soar into the light.
Ideas are fostered, and plans take shape,
This is the place where projects escape,
I am your TREASURE,
Hidden there.
Where am I?

{Fore.YELLOW}     🏆 GO AND COMPLETED YOUR GAME 🏆{Style.RESET_ALL}
"""
        print_slow(victory_message, 0.03)

if __name__ == "__main__":
    try:
        run_treasure_hunt()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Game terminated. Thanks for playing!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
    finally:
        print(f"\n{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}")
        input()
