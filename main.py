import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 1  # in seconds
start = Key.f1
pause = Key.f2
quit = Key.esc
#  ==========================

pause = True
running = True

def gui_controls():
    print("╔════════════════════════════════════════════╗")
    print("║         AutoClicker by Slothy              ║")
    print("║                - Settings -                ║")
    print(f"║  Delay: {delay} sec                              ║")
    print("║                                            ║")
    print("║                - Controls -                ║")
    print("║  F1 = Start                                ║")
    print("║  F2 = Pause                                ║")
    print("║  F3 = Quit                                 ║")
    print("║                                            ║")
    print("╚════════════════════════════════════════════╝")
    print("Press F1 to start ...")

def on_press(key):
    global running, pause

    if key == start:
        pause = False
        print("▶ Start ▶")
    elif key == pause:
        pause = True
        print("⏸ Pause ⏸")
    elif key == quit:
        running = False
        print("⛔ Quit ⛔")


def main():
    Listen = Listener(on_press=on_press)
    Listen.start()

    gui_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    Listen.stop()


if __name__ == "__main__":
    main()