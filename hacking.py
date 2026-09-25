import time
import random
import os

# Colors
GREEN = "\033[92m"
RESET = "\033[0m"

os.system('cls' if os.name == 'nt' else 'clear')

print(f"{GREEN}>> Initiating Matrix Protocol...{RESET}")
time.sleep(1)

chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ$#@!*"

try:
    for i in range(100): # 100 lines chalengi
        line = "".join(random.choice(chars) for _ in range(50))
        print(f"{GREEN}{line}{RESET}")
        time.sleep(0.05)
except:
    pass

print("\n" + "="*50)
print("  ACCESS GRANTED - SYSTEM HACKED SUCCESSFULLY")
print("="*50)
print("\n>> Coded by: GitHub Legend 😎")