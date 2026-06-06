import os
import time

responses = {
    "hello": "Hello! I am J.A.R.V.I.S, your terminal AI. How can I assist?",
    "hi": "Hey! J.A.R.V.I.S online. What do you need?",
    "how are you": "All systems operational. Running at 100% efficiency.",
    "what can you do": "I can monitor systems, fetch data, run scripts and assist you with anything.",
    "time": f"Current time: {time.strftime('%H:%M:%S')}",
    "date": f"Today is: {time.strftime('%A, %B %d %Y')}",
    "who are you": "I am J.A.R.V.I.S — Just A Rather Very Intelligent System, built by Jatin.",
    "bye": "Goodbye. J.A.R.V.I.S going offline...",
    "shutdown": "Initiating shutdown sequence... just kidding 😄",
    "help": "Commands: hello, time, date, who are you, what can you do, bye",
}

os.system('clear')
print("\033[92m" + "="*55)
print("   🤖 J.A.R.V.I.S - Terminal AI Assistant v1.0")
print("   Built by Jatin | Type 'help' for commands")
print("="*55 + "\033[0m\n")

time.sleep(1)
print("\033[93mJ.A.R.V.I.S:\033[0m Booting up... ██████████ 100%")
time.sleep(1)
print("\033[93mJ.A.R.V.I.S:\033[0m All systems online. Hello Jatin.\n")

while True:
    try:
        user = input("\033[96mYou: \033[0m").lower().strip()
        if not user:
            continue
        
        response = responses.get(user, "I don't have data on that yet. Try 'help' for commands.")
        time.sleep(0.5)
        print(f"\033[93mJ.A.R.V.I.S:\033[0m {response}\n")
        
        if user == "bye":
            break
    except KeyboardInterrupt:
        print("\n\033[91mJ.A.R.V.I.S:\033[0m Emergency shutdown activated.")
        break
