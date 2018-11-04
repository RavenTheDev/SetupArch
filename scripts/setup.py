# An interactive version of the install script

import os
import sys
import time


def header():

    print("-" * 50)
    print("Arch Installation and Management")
    notify_clear_or_not()
    print("-" * 50)


def notify_clear_or_not():
    global clear_input
    if clear_input == "yes":
        print("Clear on Input is On")
    if clear_input != "yes":
        print("Clear on Input is Off")


def clear_or_not():
    global clear_input
    if clear_input == "yes":
        clear()
    else:
        pass


def header_options():

    print("-" * 50)
    print("Arch Installation and Management - Options")
    notify_clear_or_not()
    print("-" * 50)


def header_devicemenu():
    print("-" * 50)
    print("Arch Installation and Management")
    print("DEVICE MANAGEMENT")
    notify_clear_or_not()
    print("-" * 50)


def clear():
    os.system("clear")


def intro():
    clear()
    global clear_input
    clear_input = "no"  # Set Clear on Input to DISABLED by Default
    header()
    print(
        "\nWelcome to RavenTheDev's ArchLInux installation and configuration script\n"
    )
    print(
        "This application will assist with setup of Archlinux (or Arch Bases Systems) on new systems.\n"
        "The application will allow you to install most recommended software (user customizable) and "
        "allow viewing of system resources and settings"
    )
    input("\n \nPress any key to continue ...")
    time.sleep(0.1)


def menu():
    time.sleep(0.1)
    clear()
    print("Loading Application . . . ")
    print("Memory Loaded . . . \n")
    header()
    print("Please choose an option \n")

    # The Menu Options
    print("1. Install Base System")
    print("2. Setup and Enable Services")
    print("3. Install YAY and SNAP")
    print("4. Install AUR Packages")
    print("5. Install SNAP Packages")
    print("6. Setup NBFC")
    print("7. Setup Oh-My-ZSH")
    print("\n" + "-" * 50 + "\n")
    print("8. Disk and Memory Management")
    print("\n" + "-" * 50)
    print("M. Options Menu")
    print("0. Exit Software")

    choice = input("\n Enter your choice: ")

    # Install Base System
    if choice == "1":
        clear_or_not()
        print("Installing system software . . . please wait")
        os.system(
            "for x in $(cat package_list.txt); do sudo pacman -S $x --noconfirm >/dev/null 2>&1; done;"
        )

    # Setup and Enable Services
    if choice == "2":
        clear_or_not()
        print("Enabling Services . . . please wait")
        os.system("sudo systemctl enable sddm")
        os.system("sudo systemctl enable tlp")
        os.system(
            "sudo cp ../services/suspendfix.service /etc/systemd/system/ && sudo sudo systemctl enable suspendfix.service --now"
        )

    # Install YAY and SNAP
    if choice == "3":
        print("Installing YAY and SNAP for Software Installation . . . please wait")
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.system("cd yay && makepkg")
        os.system("rm -r yay")
        os.system("yay -S snapd")

    # Install AUR Packages
    if choice == "4":
        clear_or_not()
        print("Installing AUR Packages . . . please wait")
        os.system("yay -S qownnotes")

    # Install SNAP Packages
    if choice == "5":
        clear_or_not()
        print("Installing SNAP Packages . . . please wait")
        os.system("systemctl enable snapd --now")
        os.system("snap install bitwarden spotify discord nextcloud-client mailspring")
        os.system("snap install powershell --classic")
        os.system("snap install slack --classic")

    # Setup NBFC
    if choice == "6":
        clear_or_not()
        print("Setup NBFC . . . please wait")
        os.system("yay -S nbfc")
        os.system("systemctl service nbfc enable --now")
        os.system(
            "sudo mv /opt/nbfc/Plugins/StagWare.Plugins.ECSysLinux.dll /opt/nbfc/Plugins/StagWare.Plugins.ECSysLinux.dll.old"
        )
        os.system('nbfc config -s "Asus Zenbook UX430UA"')
        os.system("systemctl restart nbfc")
        os.system("nbfc set -a")
        os.system("nbfc start")

    # Setup Oh-My-ZSH
    if choice == "7":
        clear_or_not()

        print("Setup ZSH. . . please wait")
        os.system(
            'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
        )

    if choice == "8":
        time.sleep(0.2)
        clear()
        menu_disk()

    if choice == "0":
        clear()
        sys.exit()

    if choice == "M" or "m":
        menu_options()

    else:
        clear()
        print("Invalid Option Chosen. Please try again")
        input("Press Enter to Continue")
        menu()

    clear()
    menu()


def menu_disk():
    time.sleep(0.1)
    header_devicemenu()
    print("Please choose an option \n")

    # The Menu Options
    print("1. List Current Disks")
    print("2. List Free Space")
    print("3. List Memory Usage")
    print("\n0. Return to Main Menu")

    choice = input("\n Enter your choice: ")

    if choice == "1":
        clear_or_not()
        header_devicemenu()
        print("Disks found:")
        os.system("lsblk")
        input("Press any key to return to menu\n")
        clear_or_not()
        menu_disk()

    if choice == "2":
        clear_or_not()
        header_devicemenu()
        print("Hard Drive Space:")
        os.system("df -h -t ext4")
        input("Press any key to return to menu\n")
        clear_or_not()
        menu_disk()

    if choice == "3":
        clear_or_not()
        header_devicemenu()
        print("Free memory:")
        os.system("free -h -l")
        input("Press any key to return to menu\n")
        clear_or_not()
        menu_disk()

    if choice == "0":
        menu()


def toggle_clear_or_not():
    global clear_input
    if clear_input == "yes":
        clear_input = "no"
    else:
        clear_input = "yes"


def menu_options():
    time.sleep(0.1)
    clear()
    header_options()
    print("Please choose an option \n")

    # The Menu Options
    print('1. Enable / Disable "Clear On Input"')
    print("\n0. Return to Main Menu")

    choice = input("\n Enter your choice: ")

    if choice == "1":
        toggle_clear_or_not()
        menu_options()


# Run the main program
intro()
menu()
