from os import system
from time import sleep

def installFedora():
    print("Coming Soon...")

def installArch():
    print("Coming Soon...")

def installDebian():
    system("cd ~/")
    system("mkdir files")
    system("cd ~/files")
    system("sudo add-apt-repository ppa:flatpak/stable")
    system("sudo apt update && sudo apt install wget gcc make curl snapd flatpak rpi-imager gparted gnome-software-plugin-flatpak")
    system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    system("wget https://flathub.org/repo/appstream/org.libretro.RetroArch.flatpakref")
    system("wget https://dl.flathub.org/repo/appstream/org.audacityteam.Audacity.flatpakref")
    system("wget https://dl.flathub.org/repo/appstream/org.shotcut.Shotcut.flatpakref")
    system("wget https://dl.flathub.org/repo/appstream/com.obsproject.Studio.flatpakref")
    system("wget https://dl.flathub.org/repo/appstream/com.discordapp.Discord.flatpakref")
    system("wget https://github.com/gbdk-2020/gbdk-2020/releases/download/4.0.6/gbdk-linux64.tar.gz")
    system("sudo tar -xzvf gbdk-linux64.tar.gz")
    system("sudo mv gbdk /")
    system("sudo snap install --classic code")
    system("code --install-extension ms-python.python")
    system("code --install-extension ms-vscode.cpptools")
    system("code --install-extension ms-vscode.notepadplusplus-keybindings")
    system("code --install-extension peaceshi.syntax-highlight")
    system("code --install-extension emulicious.emulicious-debugger")
    system("code --install-extension donaldhays.rgbds-z80")
    system("sudo snap install vlc")

def main():
    print("Select the distro you are using:")
    print("1 - Debian-Based")
    print("2 - Arch-Based")
    print("3 - Fedora-Based")
    print("4 - Exit")
    decision = input()
    if decision == str(1):
        print("Option", decision, "chosen...")
        sleep(3)
        system("clear")
        installDebian()
        print("End of multi-stage job.")
    if decision == str(2):
        installArch()
    if decision == str(3):
        installFedora()
    print("Program will exit...")

main()