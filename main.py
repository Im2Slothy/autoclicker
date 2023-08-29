import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 0.11  # in seconds
start = Key.esc
pause_key = Key.space
#  ==========================

paused = True
running = True

def gui_controls():
    print("╔════════════════════════════════════════════╗")
    print("║         AutoClicker by Slothy              ║")
    print("║                - Settings -                ║")
    print(f"║  Delay: {delay} sec                            ║")
    print("║                                            ║")
    print("║                - Controls -                ║")
    print("║  space = Start                             ║")
    print("║  esc = Pause                               ║")
    print("║                                            ║")
    print("╚════════════════════════════════════════════╝")
    print("Press F1 to start ...")

def on_press(key):
    global running, paused  # Changed 'pause' to 'paused'

    if key == start:
        paused = False
        print("▶ Start ▶")
    elif key == pause_key:  # Use 'pause_key' here
        paused = True
        print("⏸ Pause ⏸")

def main():
    Listen = Listener(on_press=on_press)
    Listen.start()

    gui_controls()
    while running:
        if not paused:  # Changed 'pause' to 'paused'
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    Listen.stop()

if __name__ == "__main__":
    main()
