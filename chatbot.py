import random
import time
import os
import string
import sys
from datetime import datetime
import re

# ====================== OPTIONAL LIBRARIES ======================
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 0.9)
    VOICE_AVAILABLE = True
except Exception:
    VOICE_AVAILABLE = False
    engine = None

# ====================== CONFIG ======================
BOT_NAME = "Grokie"
VERSION = "6.0"
MODE = "message"          # "message" or "voice"
VOICE_ENABLED = False

# ====================== DATA ======================
user_name = None

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break... and it said 'No problem, I'll go to sleep.'",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call a fake noodle? An impasta!",
    "Why can't you give Elsa a balloon? Because she will let it go.",
    "Why did the tomato turn red? Because it saw the salad dressing!"
]

fun_facts = [
    "Honey never spoils. Archaeologists have found 3000-year-old honey that is still edible!",
    "Octopuses have three hearts and blue blood.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries are not.",
    "The human brain can store about 2.5 petabytes of information.",
    "There are more stars in the universe than grains of sand on all the beaches on Earth.",
    "A group of flamingos is called a flamboyance."
]

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It always seems impossible until it's done. – Nelson Mandela"
]

stories = [
    "Once upon a time, a little robot named Grokie learned to talk. One day it made a human smile, and that became its favorite thing to do forever.",
    "In a quiet village, a boy found a glowing stone. When he touched it, he could understand every animal. He spent his life helping lost pets find their way home.",
    "A lonely star wished to visit Earth. One night it fell as a shooting star and landed in a garden. A child made a wish upon it, and the star felt happy at last."
]

# ====================== VISUAL & VOICE HELPERS ======================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def speak(text):
    global VOICE_ENABLED
    if VOICE_AVAILABLE and VOICE_ENABLED and engine:
        try:
            clean = re.sub(r'[^\w\s\.,!?\-]', '', text)
            engine.say(clean)
            engine.runAndWait()
        except:
            pass

def type_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_banner():
    clear_screen()
    robot = f"""
{Fore.CYAN}{Style.BRIGHT}
     ╔══════════════════════════════════════════╗
     ║                                          ║
     ║           ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄               ║
     ║         ▄█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄             ║
     ║        █│  ●         ●   │█             ║
     ║        █│       ▄▄       │█             ║
     ║        █│      ▀▀▀▀      │█             ║
     ║         ▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀              ║
     ║            ██       ██                  ║
     ║         ▄▄███▄▄▄▄▄▄▄███▄▄               ║
     ║        █               █                ║
     ║        █   G R O K I E  █               ║
     ║         ▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀                ║
     ║                                          ║
     ╚══════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(robot)
    print(f"{Fore.YELLOW}{Style.BRIGHT}          ★  {BOT_NAME} AI Chatbot  v{VERSION}  ★{Style.RESET_ALL}")
    print(f"{Fore.GREEN}          ────────────────────────────────────{Style.RESET_ALL}\n")

def choose_mode():
    global MODE, VOICE_ENABLED
    print(f"{Fore.CYAN}{Style.BRIGHT}  Choose your mode:{Style.RESET_ALL}\n")
    print(f"  {Fore.GREEN}1.{Style.RESET_ALL} Message Mode   (Text only – no voice)")
    print(f"  {Fore.YELLOW}2.{Style.RESET_ALL} Voice Mode     (Bot will speak replies)")
    print()
    while True:
        choice = input(f"{Fore.GREEN}Enter 1 or 2: {Style.RESET_ALL}").strip()
        if choice == "1":
            MODE = "message"
            VOICE_ENABLED = False
            print(f"\n{Fore.GREEN}✓ Message Mode selected{Style.RESET_ALL}")
            print(f"{Fore.WHITE}  You will chat by typing only.{Style.RESET_ALL}\n")
            break
        elif choice == "2":
            if not VOICE_AVAILABLE:
                print(f"\n{Fore.RED}Voice library not installed!{Style.RESET_ALL}")
                print(f"Run this command first:")
                print(f"  {Fore.YELLOW}pip install pyttsx3 colorama{Style.RESET_ALL}\n")
                print(f"{Fore.CYAN}Switching to Message Mode...{Style.RESET_ALL}\n")
                MODE = "message"
                VOICE_ENABLED = False
            else:
                MODE = "voice"
                VOICE_ENABLED = True
                print(f"\n{Fore.YELLOW}✓ Voice Mode selected{Style.RESET_ALL}")
                print(f"{Fore.WHITE}  Bot will speak its replies.{Style.RESET_ALL}\n")
                speak(f"Hello! I am {BOT_NAME}. Voice mode is now active.")
            break
        else:
            print(f"{Fore.RED}Please enter only 1 or 2{Style.RESET_ALL}")
    time.sleep(0.6)
    print(f"{Fore.CYAN}Type {Fore.YELLOW}'help'{Fore.CYAN} to see all commands{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type {Fore.YELLOW}'mode'{Fore.CYAN}  to switch between Message / Voice{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type {Fore.YELLOW}'bye'{Fore.CYAN}   to exit{Style.RESET_ALL}\n")

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s\+\-\*\/\.\(\)]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def contains_any(text, keywords):
    return any(k in text for k in keywords)

def starts_with_any(text, prefixes):
    return any(text.startswith(p) for p in prefixes)

def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.now().strftime("%A, %d %B %Y")

def calculate(expression):
    try:
        expression = expression.replace(" ", "").replace("x", "*").replace("×", "*").replace("÷", "/")
        if not re.match(r'^[\d\+\-\*\/\.\(\)]+$', expression):
            return "Sorry, I can only calculate with numbers and + - * / ( )"
        if "__" in expression:
            return "Invalid expression."
        result = eval(expression, {"__builtins__": {}})
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except:
        return "Sorry, I couldn't calculate that. Example: calculate 25 * 4 + 10"

def generate_password(length=12):
    length = max(6, min(length, 50))
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(length))

def number_guessing_game():
    number = random.randint(1, 20)
    attempts = 0
    print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} I'm thinking of a number between 1 and 20.")
    print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Type 'quit' anytime to stop.")
    speak("I'm thinking of a number between 1 and 20. Can you guess it?")
    while True:
        try:
            guess = input(f"{Fore.GREEN}Your guess: {Style.RESET_ALL}").strip().lower()
            if guess in ["quit", "exit", "stop", "cancel"]:
                print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Game cancelled. The number was {number}.")
                speak(f"Game cancelled. The number was {number}.")
                return
            guess = int(guess)
            attempts += 1
            if guess < number:
                print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Too low! Try again.")
                speak("Too low")
            elif guess > number:
                print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Too high! Try again.")
                speak("Too high")
            else:
                msg = f"Correct! You got it in {attempts} attempt{'s' if attempts > 1 else ''}. Nice job!"
                print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} {msg}")
                speak(msg)
                return
        except ValueError:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Please enter a number between 1 and 20.")

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Let's play Rock-Paper-Scissors!")
    speak("Let's play Rock Paper Scissors!")
    print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Type rock, paper or scissors (or 'quit' to stop).")
    while True:
        user = input(f"{Fore.GREEN}Your choice: {Style.RESET_ALL}").strip().lower()
        if user in ["quit", "exit", "stop"]:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Okay, game over!")
            speak("Game over")
            return
        if user not in options:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Please choose: rock, paper or scissors.")
            continue
        bot = random.choice(options)
        print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} I chose → {bot}")
        speak(f"I chose {bot}")
        if user == bot:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} It's a tie!")
            speak("It's a tie")
        elif (user == "rock" and bot == "scissors") or (user == "paper" and bot == "rock") or (user == "scissors" and bot == "paper"):
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} You win!")
            speak("You win!")
        else:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} I win this round!")
            speak("I win this round")
        again = input(f"{Fore.YELLOW}Play again? (yes/no): {Style.RESET_ALL}").strip().lower()
        if again not in ["yes", "y"]:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Thanks for playing!")
            speak("Thanks for playing")
            return

def show_help():
    mode_text = f"{Fore.GREEN}Message Mode{Style.RESET_ALL}" if MODE == "message" else f"{Fore.YELLOW}Voice Mode{Style.RESET_ALL}"
    return f"""
{Fore.YELLOW}{'='*55}
{BOT_NAME} v{VERSION} — Command List
{'='*55}{Style.RESET_ALL}
{Fore.MAGENTA}CURRENT MODE: {mode_text}

{Fore.CYAN}MODE CONTROL{Style.RESET_ALL}
  mode / switch             → Switch between Message & Voice
  message                   → Switch to Message Mode (text only)
  voice                     → Switch to Voice Mode (bot speaks)

{Fore.CYAN}CHAT & INFO{Style.RESET_ALL}
  hello / hi / hey          → Greet
  how are you               → Ask mood
  my name is [name]         → Save your name
  what is my name           → Recall your name
  who are you / info        → About me
  help                      → This menu

{Fore.CYAN}TIME & DATE{Style.RESET_ALL}
  time                      → Current time
  date / today              → Today's date

{Fore.CYAN}TOOLS{Style.RESET_ALL}
  calculate [expression]    → Math (e.g. calculate 12*8)
  password [length]         → Generate password
  random                    → Random number 1-100
  flip / coin               → Flip a coin
  dice / roll               → Roll a dice
  upper [text]              → Convert to UPPERCASE
  lower [text]              → Convert to lowercase
  count [text]              → Count words & characters
  age [year]                → Calculate age (e.g. age 2000)

{Fore.CYAN}FUN & GAMES{Style.RESET_ALL}
  joke                      → Tell a joke
  fact                      → Fun fact
  quote                     → Motivational quote
  story                     → Short story
  game                      → Number guessing (1-20)
  rps                       → Rock-Paper-Scissors

{Fore.CYAN}OTHER{Style.RESET_ALL}
  clear                     → Clear screen
  weather                   → Weather note
  bye / exit / quit         → End chat
{Fore.YELLOW}{'='*55}{Style.RESET_ALL}
"""

def get_response(user_input):
    global user_name, MODE, VOICE_ENABLED
    original = user_input.strip()
    text = normalize(user_input)
    if not text:
        return "Please type something.", False
    if text in ["bye", "exit", "quit", "goodbye", "see you", "cya", "good bye"]:
        name_part = f", {user_name}" if user_name else ""
        return f"Goodbye{name_part}! Take care.", True
    if text in ["help", "commands", "menu", "what can you do", "options"]:
        return show_help(), False
    if text in ["clear", "cls", "clear screen"]:
        clear_screen()
        return "Screen cleared!", False
    if text in ["mode", "switch", "switch mode", "change mode"]:
        if MODE == "message":
            if VOICE_AVAILABLE:
                MODE = "voice"
                VOICE_ENABLED = True
                return "Switched to Voice Mode. I will now speak my replies.", False
            else:
                return "Voice library not available. Stay in Message Mode.\nInstall with: pip install pyttsx3", False
        else:
            MODE = "message"
            VOICE_ENABLED = False
            return "Switched to Message Mode. Text only now.", False
    if text in ["message", "text", "message mode", "text mode"]:
        MODE = "message"
        VOICE_ENABLED = False
        return "Message Mode activated. I will only reply in text.", False
    if text in ["voice", "voice mode", "speak"]:
        if VOICE_AVAILABLE:
            MODE = "voice"
            VOICE_ENABLED = True
            return "Voice Mode activated. I will speak my replies.", False
        return "Voice library not installed. Run: pip install pyttsx3", False
    if text in ["info", "about", "version", "who are you", "what are you", "your name", "what is your name"]:
        mode_name = "Message Mode" if MODE == "message" else "Voice Mode"
        return (f"I am {BOT_NAME} v{VERSION} — your intelligent terminal chatbot.\n"
                f"Current mode: {mode_name}\n"
                f"I can chat, calculate, play games, tell jokes and more.\n"
                f"Type 'help' to see all commands."), False
    if starts_with_any(text, ["my name is ", "i am ", "i'm ", "this is "]):
        for prefix in ["my name is ", "i am ", "i'm ", "this is "]:
            if text.startswith(prefix):
                name = original[len(prefix):].strip().title()
                name = re.sub(r'[^\w\s]', '', name).strip()
                if name and len(name) < 40:
                    user_name = name
                    return f"Nice to meet you, {user_name}! I'll remember your name.", False
        return "Please tell me your name clearly. Example: my name is Ali", False
    if text in ["what is my name", "whats my name", "what's my name", "do you know my name", "my name"]:
        if user_name:
            return f"Your name is {user_name}.", False
        return "I don't know your name yet. Say: my name is [Your Name]", False
    if text in ["time", "what time", "current time", "whats the time", "what's the time", "tell me the time"]:
        return f"The current time is {get_time()}.", False
    if text in ["date", "today", "what date", "whats the date", "what's the date", "what day", "what day is it", "today's date"]:
        return f"Today is {get_date()}.", False
    if starts_with_any(text, ["calculate ", "calc ", "compute ", "solve "]):
        for prefix in ["calculate ", "calc ", "compute ", "solve "]:
            if text.startswith(prefix):
                return calculate(text[len(prefix):]), False
    if re.fullmatch(r'[\d\+\-\*\/\.\(\)\s]+', text) and any(op in text for op in "+-*/"):
        return calculate(text), False
    if starts_with_any(text, ["password", "pass ", "generate password", "create password"]):
        try:
            numbers = re.findall(r'\d+', text)
            length = int(numbers[0]) if numbers else 12
            pwd = generate_password(length)
            return f"Here's a secure password ({len(pwd)} characters):\n{pwd}", False
        except:
            return f"Here's a password:\n{generate_password()}", False
    if text in ["random", "random number", "rand", "generate number", "give me a number"]:
        return f"Random number: {random.randint(1, 100)}", False
    if text in ["flip", "coin", "flip a coin", "toss", "toss a coin", "coin flip", "heads or tails"]:
        result = random.choice(["Heads", "Tails"])
        return f"Coin flip → {result}", False
    if text in ["dice", "roll", "roll a dice", "roll dice", "roll the dice", "throw dice"]:
        return f"You rolled a {random.randint(1, 6)}!", False
    if starts_with_any(text, ["upper ", "uppercase ", "to upper "]):
        content = original.split(" ", 1)[1] if " " in original else ""
        return content.upper() if content else "Please provide text. Example: upper hello world", False
    if starts_with_any(text, ["lower ", "lowercase ", "to lower "]):
        content = original.split(" ", 1)[1] if " " in original else ""
        return content.lower() if content else "Please provide text. Example: lower HELLO WORLD", False
    if starts_with_any(text, ["count ", "word count ", "count words "]):
        content = original.split(" ", 1)[1] if " " in original else ""
        if not content:
            return "Please provide text. Example: count I love coding", False
        words = len(content.split())
        chars = len(content)
        no_space = len(content.replace(" ", ""))
        return f"Words: {words}\nCharacters (with spaces): {chars}\nCharacters (without spaces): {no_space}", False
    if starts_with_any(text, ["age ", "how old if born ", "calculate age "]):
        try:
            year = int(re.findall(r'\d{4}', text)[0])
            current = datetime.now().year
            age = current - year
            if year < 1900 or year > current:
                return "Please enter a realistic birth year (e.g. age 1998).", False
            return f"If born in {year}, the age is {age} years.", False
        except:
            return "Please use: age [year]   Example: age 2005", False
    if text in ["joke", "tell joke", "tell me a joke", "say a joke", "funny", "make me laugh"]:
        return random.choice(jokes), False
    if text in ["fact", "fun fact", "tell me a fact", "interesting fact", "random fact"]:
        return random.choice(fun_facts), False
    if text in ["quote", "inspiration", "motivate me", "motivate", "motivational quote", "inspire me"]:
        return random.choice(quotes), False
    if text in ["story", "tell me a story", "short story", "tell a story"]:
        return random.choice(stories), False
    if text in ["game", "play", "guess", "number game", "guessing game", "play game"]:
        number_guessing_game()
        return "Good game! Type 'game' to play again.", False
    if text in ["rps", "rock paper scissors", "rock paper scissor", "play rps", "rockpaperscissors"]:
        rock_paper_scissors()
        return "Thanks for playing!", False
    if contains_any(text, ["weather", "temperature", "forecast", "is it raining", "is it sunny"]):
        return ("I don't have live weather data right now.\n"
                "Please check a weather app or website for accurate information."), False
    if contains_any(text, ["hello", "hi ", "hey", "salam", "assalam", "good morning",
                            "good evening", "good afternoon", "hi there", "hello there"]):
        if user_name:
            return f"Hello {user_name}! How are you doing today?", False
        return random.choice([
            "Hello! How are you?",
            "Hi there! What's up?",
            "Hey! Nice to chat with you.",
            "Hello! How can I help you today?"
        ]), False
    if contains_any(text, ["how are you", "how r you", "how r u", "how's it going",
                            "how do you do", "how are u", "you okay", "you good"]):
        return random.choice([
            "I'm doing great, thanks for asking! How about you?",
            "I'm fine, thank you! What about you?",
            "All systems running perfectly! How are you?"
        ]), False
    if contains_any(text, ["thank", "thanks", "thx", "shukriya", "thank you", "thanku"]):
        return random.choice([
            "You're welcome!",
            "Happy to help!",
            "Anytime!",
            "No problem at all!"
        ]), False
    if contains_any(text, ["how old are you", "your age", "are you old"]):
        return "I'm a chatbot, so I don't age... forever young!", False
    return random.choice([
        "I didn't understand that clearly. Type 'help' to see what I can do.",
        "Hmm, I'm not sure about that. Try 'help' for the full command list.",
        "Could you rephrase? Or type 'help' to see available commands.",
        "I can help with time, date, math, jokes, games and more. Type 'help'."
    ]), False

if __name__ == "__main__":
    show_banner()
    choose_mode()
    while True:
        try:
            mode_tag = f"{Fore.GREEN}[Message]{Style.RESET_ALL}" if MODE == "message" else f"{Fore.YELLOW}[Voice]{Style.RESET_ALL}"
            user = input(f"{mode_tag} {Fore.GREEN}You: {Style.RESET_ALL}").strip()
            if not user:
                continue
            reply, should_exit = get_response(user)
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} {reply}\n")
            if MODE == "voice" and VOICE_ENABLED and len(reply) < 280:
                speak(reply)
            if should_exit:
                break
        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Chat interrupted. Goodbye!")
            speak("Goodbye")
            break
        except Exception:
            print(f"{Fore.CYAN}{BOT_NAME}:{Style.RESET_ALL} Something went wrong, but we can continue chatting.")
