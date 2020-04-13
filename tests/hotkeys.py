from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.Key.right},
    {keyboard.Key.ctrl, keyboard.Key.left},
    {keyboard.Key.ctrl, keyboard.Key.down}
]

# The currently active modifiers
current = set()

def next_song():
    print ("Soundkey next song!")

def old_song():
    print ("Soundkey old_song!")

def pause_play():
    print ("Soundkey pause_play!")

def on_press(key):
    for COMBO in COMBINATIONS:
        if key in COMBO:
            current.add(key)
            if all(k in current for k in COMBO):
                if keyboard.Key.right in COMBO:
                    next_song()
                
                if keyboard.Key.left in COMBO:
                    old_song()

                if keyboard.Key.down in COMBO:
                    pause_play()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
