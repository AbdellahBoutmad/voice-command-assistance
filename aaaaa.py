import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import os
import datetime
import subprocess
import time

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[2].id)

def speak(text):
    """Function to convert text to speech"""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Function to listen to user input"""
    with sr.Microphone() as source:
        speak("Abdellah, I am listening to your command...")
        print("Abdellah, I am listening to your command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

def write():
    """Function to listen to user input and write"""
    print("Listening to text...")
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                command_text = recognizer.recognize_google(audio, language="en-US")
                print(f"You said: {command_text}")
                if command_text.lower() == "text":
                    speak("Stopping text writing.")
                    break
                else:
                    pyautogui.write(str(command_text) + " ")
                    speak("Text written successfully.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")

def open_browser():
    webbrowser.open("https://www.google.com")
    speak("Opening the browser")

def open_facebook():
    webbrowser.open("https://www.facebook.com")
    speak("Opening Facebook")

def open_music():
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write('media player')
    time.sleep(1)
    pyautogui.press('enter')
    speak("Opening music")

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube")

def time_speak():
    local_time = datetime.datetime.now()
    return local_time.strftime("%A, %B %d, %Y")

def disable_defender():
    disable_defender_cmd = "powershell Set-MpPreference -DisableRealtimeMonitoring $true"
    os.system(disable_defender_cmd)
    speak("Disabling Windows Defender")

def enable_defender():
    enable_defender_cmd = "powershell Set-MpPreference -DisableRealtimeMonitoring $false"
    os.system(enable_defender_cmd)
    speak("Enabling Windows Defender")

def take_image():
    subprocess.run('start microsoft.windows.camera:', shell=True)
    speak("Opening camera")

def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
    speak("Opening camera")

def open_notepad():
    os.system("notepad.exe")
    speak("Opening Notepad")

def open_vscode():
    os.system("code")
    speak("Opening Visual Studio Code")

def open_calculator():
    os.system("calc")
    speak("Opening calculator")

def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com")
    speak("Opening WhatsApp")

import ctypes

def volume_up():
    for _ in range(5):
        pyautogui.press('volumeup')
    speak("Volume increased")

def volume_down():
    for _ in range(5):
        pyautogui.press('volumedown')
    speak("Volume decreased")

def mute_volume():
    pyautogui.press('volumemute')
    speak("Volume muted")

def open_task_manager():
    os.system("taskmgr")
    speak("Opening Task Manager")

def open_file():
    os.system("explorer")
    speak("Opening File Explorer")

def play_pause_media():
    pyautogui.press('playpause')
    speak("Toggling play/pause")

def next_track():
    pyautogui.press('nexttrack')
    speak("Skipping to next track")

def previous_track():
    pyautogui.press('prevtrack')
    speak("Going back to previous track")

def open_gmail():
    webbrowser.open("https://mail.google.com")
    speak("Opening Gmail")

def open_settings():
    os.system("start ms-settings:")
    speak("Opening Settings")

commands = {
    "hello": lambda: speak("Hello! How can I help you today?"),
    "open the browser": open_browser,
    "take a picture": lambda: (take_image(), pyautogui.press('space'), speak("Image saved")),
    "open the camera": open_camera,
    "write text": write,
    "open music": open_music,
    "open notepad": open_notepad,
    "open visual studio code": open_vscode,
    "open whatsapp": open_whatsapp,
    "open facebook": open_facebook,
    "open youtube": open_youtube,
    "disable windows defender": disable_defender,
    "enable windows defender": enable_defender,
    "open calculator": open_calculator,
    "what is your name": lambda: speak("I am the voice assistant. My developer is Abdellah Boutmad, a student at ISTA Guelmim."),
    "what is the date today": lambda: speak(time_speak()),
    "see you later": lambda: (speak("Alright, see you later!"), exit()),
    "4 space": lambda: pyautogui.hotkey('tab'),
    "enter": lambda: pyautogui.hotkey('enter'),
    "delete": lambda: pyautogui.hotkey('delete'),
    "down": lambda: pyautogui.hotkey('down'),
    "up": lambda: pyautogui.hotkey('up'),
    "increase volume": volume_up,
    "decrease volume": volume_down,
    "mute volume": mute_volume,
    "open task manager": open_task_manager,
    "open file explorer": open_file,
    "play pause media": play_pause_media,
    "next track": next_track,
    "previous track": previous_track,
    "open gmail": open_gmail,
    "open settings": open_settings
}

def execute_command(command):
    """Function to execute commands based on recognized voice input"""
    for i in commands:
        if i in command:
            commands[i]()
            return
    speak("Sorry, I didn't understand.")

speak("Hello Abdellah. How can I help you today?")
while True:
    command = listen()
    if command:
        execute_command(command)
