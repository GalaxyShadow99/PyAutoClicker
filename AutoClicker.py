import pyautogui
import time
import threading
import keyboard
import json
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os
import platform
import subprocess
import sys

console = Console()

def is_root():
    """Vérifie si le script est exécuté avec les privilèges administrateur."""
    return os.geteuid() == 0

def request_admin_privileges():
    """Demande les privilèges administrateur en utilisant osascript."""
    script_path = os.path.abspath(__file__)
    command = f"""
    osascript -e 'do shell script "python3 {script_path}" with administrator privileges'
    """
    try:
        subprocess.check_call(command, shell=True)
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("Échec de l'obtention des privilèges administrateur.")
        sys.exit(1)

if not is_root():
    request_admin_privileges()
    
def clear_console():
    """
    Efface le contenu de la console en fonction du système d'exploitation.
    """
    if platform.system() == "Windows":
        os.system("cls")  # Commande pour effacer la console sur Windows
    else:
        os.system("clear")  # Commande pour effacer la console sur macOS et Linux

# Fonction pour charger les paramètres depuis un fichier JSON
def LoadSettings():
    try:
        with open("datas.json", "r") as SettingFile:
            return json.load(SettingFile)
    except FileNotFoundError:
        # Crée un fichier de paramètres par défaut si inexistant
        default_settings = {
            "key": "left",  # Touche par défaut
            "intervMin": 1000,  # Intervalles par défaut (en millisecondes)
            "intervMax": 3000
        }
        with open("datas.json", "w") as SettingFile:
            json.dump(default_settings, SettingFile, indent=4)
        return default_settings

# Fonction pour sauvegarder les paramètres dans un fichier JSON
def SaveSettings(settings):
    with open("datas.json", "w") as SettingFile:
        json.dump(settings, SettingFile, indent=4)

# Fonction pour lancer l'autoclicker avec les paramètres actuels
def AutoClicker(settings):
    console.print("L'autoclicker a été lancé ! Appuyez sur 'q' pour arrêter.")
    
    # Frames ASCII pour montrer que l'auto-clicker tourne
    frames = [
        r"""
        [bold green]⠋⠉⠉⠉⠙⠛⠻⠶⠦⠤⢤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠠⡡⢔⡬⢕⢗⢧⢺⠽⢿⣿⣿⡾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⡁⠊⡉⠉⠋⠉⠉[/bold green]
        """,
        r"""
        [bold green]⠀⠋⠉⠉⠙⠛⠻⠶⠦⠤⢤⣤⣄⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⡠⡡⢔⡬⢕⢗⢧⢺⠽⢿⣿⣿⡾⡆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⡁⠊⡉⠉⠋⠉⠉⠉[/bold green]
        """,
        r"""
        [bold green]⠀⠀⠙⠛⠻⠶⠦⠤⢤⣤⣄⡀⡀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢀⡡⢔⡬⢕⢗⢧⢺⠽⢿⣿⣿⡾⡆⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠈⠊⡉⠉⠋⠉⠉⠉[/bold green]
        """,
        r"""
        [bold green]⠀⠀⠀⠶⠦⠤⢤⣤⣄⡀⡀⡀⡀⡀⡀⡀⠀⠀⠀⠀⠀⠀⠀
        ⣠⡡⢔⡬⢕⢗⢧⢺⠽⢿⣿⣿⡾⡆⡇⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠉⠋⠉⠉⠉⠉[/bold green]
        """,
        r"""
        [bold green]⠀⠀⠀⠀⠤⢤⣤⣄⡀⡀⡀⡀⡀⡀⡀⡀⡀⠀⠀⠀⠀⠀⠀
        ⢠⡡⢔⡬⢕⢗⢧⢺⠽⢿⣿⣿⡾⡆⡇⡇⡇⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠉⠋⠉⠉⠉[/bold green]
        """
    ]
    
    idx = 0
    while not keyboard.is_pressed('q'):
        console.print(frames[idx % len(frames)])
        pyautogui.press(settings["key"])
        interv = random.randint(settings["intervMin"], settings["intervMax"])
        IntervMS = interv / 1000
        time.sleep(IntervMS)
        idx += 1
    
    console.print("Arrêt de l'autoclicker en cours...")
    time.sleep(2)

# Fonction pour configurer les paramètres
def Settings():
    settings = LoadSettings()

    autoclickable_keys = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', 
        '6', '7', '8', '9', 'enter', 'esc', 'shift', 'tab', 'backspace', 'ctrl', 'alt', 
        'space', 'capslock', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 
        'f11', 'f12', 'left', 'up', 'right', 'down', 'insert', 'delete', 'home', 'end', 
        'pageup', 'pagedown', 'printscreen', 'scrolllock', 'pause', 'numlock', 'numpad0', 
        'numpad1', 'numpad2', 'numpad3', 'numpad4', 'numpad5', 'numpad6', 'numpad7', 
        'numpad8', 'numpad9', 'numpadenter', 'add', 'subtract', 'multiply', 'divide', 
        'decimal', 'clear', 'left shift', 'right shift', 'left ctrl', 'right ctrl', 
        'left alt', 'right alt', 'left windows', 'right windows', 'apps', 'browser back', 
        'browser forward', 'browser refresh', 'browser stop', 'browser search', 
        'browser favorites', 'browser home', 'volume mute', 'volume down', 'volume up', 
        'media next', 'media prev', 'media stop', 'media play/pause', 'launch mail', 
        'launch media', 'launch app1', 'launch app2', '`', '-', '=', '[', ']', '\\', 
        ';', "'", ',', '.', '/', 'num lock', 'scroll lock', 'pause break'
    ]

    while True:
    
        clear_console()
        
        
        console.print("Configuration des paramètres :")
        console.print("---------------------------------------------------")
        console.print(f"Touche d'autoclick actuelle : [bold cyan]{settings['key']}[/bold cyan]")
        console.print(f"Intervalle minimum : [bold cyan]{settings['intervMin']}[/bold cyan] millisecondes")
        console.print(f"Intervalle maximum : [bold cyan]{settings['intervMax']}[/bold cyan] millisecondes")
        console.print("---------------------------------------------------")

        ValidInput1 = False
        while not ValidInput1:
            Key = input("Entrez la nouvelle touche d'autoclick : ").lower()
            if Key in autoclickable_keys:
                ValidInput1 = True
            else:
                console.print("La touche n'est pas valide. Assurez-vous qu'elle soit dans la liste des touches autoclickables.")

        ValidInput2 = False
        while not ValidInput2:
            IntervMin = input("Entrez la borne minimale pour l'intervalle (en millisecondes) : ")
            try:
                IntervMin = int(IntervMin)
                if IntervMin > 0:
                    ValidInput2 = True
                else:
                    console.print("La borne minimale doit être un nombre entier supérieur à 0.")
            except ValueError:
                console.print("Veuillez entrer un nombre entier valide pour la borne minimale.")

        ValidInput3 = False
        while not ValidInput3:
            IntervMax = input("Entrez la borne maximale pour l'intervalle (en millisecondes) : ")
            try:
                IntervMax = int(IntervMax)
                if IntervMax > 0 and IntervMax > IntervMin:
                    ValidInput3 = True
                else:
                    console.print("La borne maximale doit être un nombre entier supérieur à 0 et supérieur à la borne minimale.")
            except ValueError:
                console.print("Veuillez entrer un nombre entier valide pour la borne maximale.")

        # Mise à jour des paramètres
        settings["key"] = Key
        settings["intervMin"] = IntervMin
        settings["intervMax"] = IntervMax
        SaveSettings(settings)

        console.print("[bold yellow] Les paramètres ont été mis à jour avec succès ! [/bold yellow]")
        time.sleep(1)
        break

# Fonction pour afficher le menu principal
def Menu():
    while True:
        time.sleep(2)
        clear_console()

        table = Table(title="Menu Principal", box=box.DOUBLE_EDGE)

        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Description", justify="left", style="magenta")

        table.add_row("1", "Configurer les paramètres")
        table.add_row("2", "Lancer l'autoclicker")
        table.add_row("3", "Quitter l'application")

        panel = Panel(table, title="Choisissez une option", border_style="bright_yellow")
        console.print(panel)

        choice = console.input("\n[bold green]Entrez votre choix : [/bold green]")

        if choice == "1":
            Settings()
        elif choice == "2":
            settings = LoadSettings()
            AutoClicker(settings)
        elif choice == "3":
            console.print("Merci d'avoir utilisé l'auto-clicker ! Au revoir.")
            break
        else:
            console.print(f"[bold red] L'option {choice} est invalide. Veuillez choisir une option valide ! [/bold red]")

# Point d'entrée du programme
if __name__ == "__main__":
    Menu()
