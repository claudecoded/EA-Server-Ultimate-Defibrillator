#!/usr/bin/env python3
import os
import sys
import time
import random
import threading

# ==============================================================================
# EA SERVER ULTIMATE DEFIBRILLATOR (OVERDRIVE CLI)
# A Hollywood-style satirical hacking dashboard to keep EA servers online.
# ==============================================================================

# --- Terminal ANSI Color Palettes ---
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
WHITE = '\033[1;37m'
RESET = '\033[0m'
CLEAR_SCREEN = '\033[2J\033[H'

def boot_sequence():
    """Renders a cinematic Hollywood hacking initialization sequence."""
    os.system('') # Initialize ANSI coloring windows overrides
    print(CLEAR_SCREEN)
    
    logs = [
        "Connecting to secure routing node: 127.0.0.99...",
        "Bypassing EA Origin Core Security Framework... [SUCCESS]",
        "Injecting dynamic memory patches into Frostbite Engine...",
        "WARNING: Found 42,912 memory leaks in FIFA Matchmaking module.",
        "Locating primary hardware cluster...",
        "CRITICAL: Primary hardware identified as 'Russet Potato Mk.IV'.",
        "Bootstrapping Overdrive Dashboard Environment..."
    ]
    
    for log in logs:
        sys.stdout.write(f"{GREEN}[+] {log}{RESET}\n")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.8))
        
    print(f"\n{YELLOW}[!] ACCESS GRANTED. PRESS ENTER TO OVERCLOCK THE POTATO...{RESET}")
    input()

# Global state trackers for the multi-threaded simulation loops
server_health = 100
active_players = 450000
potato_voltage = 1.2
active_crisis = "NONE"
game_running = True
def crisis_orchestrator():
    """Background engine loop generating automated server degradation and crisis."""
    global server_health, active_players, potato_voltage, active_crisis, game_running
    
    crises_pool = [
        "VOLTAGE_DROP: The potato is running out of starch! Boost current immediately.",
        "SERVERS_MELTING: Apex Legends tournament just launched. Fans are dead.",
        "PACKET_FLOOD: Ultimate Team pack opening frenzy detected. Bandwidth choked.",
        "DDOS_ATTACK: Angered gamers are attacking the routing mainframe.",
        "GREMLIN_ALARM: Someone spilled energy drink on the master server rack."
    ]
    
    while game_running:
        time.sleep(random.uniform(4.0, 7.0))
        if active_crisis == "NONE" and server_health > 0:
            active_crisis = random.choice(crises_pool)
            # Escalating the baseline drain speed during ongoing crisis loops
            server_health -= random.randint(10, 20)
        else:
            server_health -= random.randint(2, 6)
            
        active_players += random.randint(-20000, 50000)
        if server_health <= 0:
            server_health = 0
            game_running = False
def refresh_dashboard():
    """Prints the actual real-time status matrix viewport panel layout."""
    print(CLEAR_SCREEN)
    print(f"{CYAN}======================================================================{RESET}")
    print(f"{WHITE}       EA SERVER OVERDRIVE CORE TERMINAL v4.2.0 - LIVE SYSTEM         {RESET}")
    print(f"{CYAN}======================================================================{RESET}")
    
    # Dynamic health indicator coloring
    health_color = GREEN if server_health > 50 else (YELLOW if server_health > 20 else RED)
    
    print(f" [+] SERVER HEALTH  : {health_color}{server_health}%{RESET}")
    print(f" [+] ACTIVE PLAYERS  : {BLUE}{active_players:,} connections{RESET}")
    print(f" [+] POTATO VOLTAGE : {YELLOW}{potato_voltage:.2f}V (Target: 1.50V){RESET}")
    
    print(f"{CYAN}----------------------------------------------------------------------{RESET}")
    crisis_color = RED if active_crisis != "NONE" else GREEN
    print(f" [!] CURRENT STATUS : {crisis_color}{active_crisis}{RESET}")
    print(f"{CYAN}======================================================================{RESET}")
    print(f"{WHITE} COMMANDS AVAILABLE:{RESET}")
    print(f"  {GREEN}'boost'{RESET}  -> Inject starch electrolytes (Fixes VOLTAGE_DROP)")
    print(f"  {GREEN}'cool'{RESET}   -> Pour liquid nitrogen on the potato (Fixes MELTING)")
    print(f"  {GREEN}'route'{RESET}  -> Re-route network packets to empty server (Fixes FLOOD/DDOS)")
    print(f"  {GREEN}'patch'{RESET}  -> Hot-patch memory leaks directly into production")
    print(f"{CYAN}======================================================================{RESET}")

def main():
    global server_health, active_crisis, potato_voltage, game_running
    
    boot_sequence()
    
    # Threading setup to decouple interface rendering from background health calculations
    bg_thread = threading.Thread(target=crisis_orchestrator, daemon=True)
    bg_thread.start()
    
    while game_running:
        refresh_dashboard()
        # Prompt interceptor loop
        cmd = input(f"{WHITE}ea-root@mainframe:~# {RESET}").strip().lower()
        
        if not game_running:
            break
            
        if cmd == 'boost':
            potato_voltage = min(potato_voltage + 0.15, 1.8)
            if "VOLTAGE_DROP" in active_crisis:
                active_crisis = "NONE"
                server_health = min(server_health + 30, 100)
        elif cmd == 'cool':
            if "MELTING" in active_crisis:
                active_crisis = "NONE"
                server_health = min(server_health + 40, 100)
        elif cmd == 'route':
            if "FLOOD" in active_crisis or "DDOS" in active_crisis:
                active_crisis = "NONE"
                server_health = min(server_health + 35, 100)
        elif cmd == 'patch':
            server_health = min(server_health + 15, 100)
            if active_crisis == "NONE":
                print(f"{GREEN}[+] Micro-patch deployed safely.{RESET}")
                time.sleep(0.5)
                
    # Server Death/Crash sequence trigger
    print(CLEAR_SCREEN)
    print(f"{RED}######################################################################{RESET}")
    print(f"{RED}💥 [CRITICAL FAILURE] EA SERVER HAS EXPLOITED / CRASHED 💥{RESET}")
    print(f"{RED}######################################################################{RESET}")
    print(f"{WHITE}Final Report:{RESET}")
    print(f" - Peak concurrent traffic unhandled: {active_players:,} clients.")
    print(f" - Core hardware status: Carbonized / Roasted Potato.")
    print(f"\n{YELLOW}Result: FIFA servers are down again. Millions of gamers are crying.{RESET}\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting EA Core Mainframe Control Room Panel. System offline.")
