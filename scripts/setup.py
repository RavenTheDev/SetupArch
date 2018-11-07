# An interactive version of the install script

import os
import time
import sys

def setup_app():
    """
    This module sets up the app with the require settings are boot time
    """
    global clear_input
    clear_input = "yes"  # Set Clear on Input to ENABLED by Default

    header_main()

    print(
        "\nWelcome to RavenTheDev's ArchLInux installation and configuration script\n"
    )

    print(
        "This application will assist with setup of Archlinux (or Arch Based Systems) on new systems.\n \n"
        "The application will allow you to install most recommended software (user customizable) and "
        "allow viewing of system resources and settings\n \n \n"
    )

    print("|---------------------- IMPORTANT ---------------------- |\n")

    print("Before running this application, please ensure you have Arch-Chroot")
    print("(or equivalent) into the OS environment, so that the script can run against the new install.")
    print("I take no responsibility for any damage done to your system\n")


    print("|---------------------- IMPORTANT ---------------------- |")

    input("\n Press any key to continue ...")
    
    time.sleep(0.1)

# Methods for the Display of Different Headers
def header_main():
    """
    This method prints the pre-defined Header on each menu page
    """
    clear_screen()
    print("-" * 50)
    print("Arch Installation and Management")
    disp_clear_screen()
    print("-" * 50)

def header_options():
    """
    Print the Header for the Options Page
    """
    clear_screen()
    print("-" * 50)
    print("Arch Installation and Management - Options")
    disp_clear_screen()
    print("-" * 50)

def header_devicemenu():
    """
    Print the header for the Device Management page
    """
    clear_screen()
    print("-" * 50)
    print("Arch Installation and Management")
    print("DEVICE MANAGEMENT")
    disp_clear_screen()
    print("-" * 50)

# Methods fo the "Clear Screen" options
def disp_clear_screen():
    """
    Display the "Clear on Input" status
    """
    global clear_input
    if clear_input == "yes":
        print("Clear Screen is On")
    if clear_input != "yes":
        print("Clear Screen is Off")

def clear_screen():
    """
    Clear the Screen if "Clear on Input" is turned ON
    """
    global clear_input
    if clear_input == "yes":
        os.system('clear')
    else:
        pass

def toggle_clear_on_input():
    """
    Toggle the "Clear on Input" option
    """
    global clear_input
    if clear_input == "yes":
        clear_input = "no"
    else:
        clear_input = "yes"

# Methods for displaying the different Menu choices
def main_menu():
    """
    Launch the Main Menu
    """
    header_main()
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
        disp_clear_screen()
        print("Installing system software . . . please wait")
        os.system(
            "for x in $(cat package_list.txt); do sudo pacman -S $x --noconfirm >/dev/null 2>&1; done;"
        )

    # Setup and Enable Services
    if choice == "2":
        disp_clear_screen()
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
        disp_clear_screen()
        print("Installing AUR Packages . . . please wait")
        os.system("yay -S qownnotes")

    # Install SNAP Packages
    if choice == "5":
        disp_clear_screen()
        print("Installing SNAP Packages . . . please wait")
        os.system("systemctl enable snapd --now")
        os.system("snap install bitwarden spotify discord nextcloud-client mailspring")
        os.system("snap install powershell --classic")
        os.system("snap install slack --classic")

    # Setup NBFC
    if choice == "6":
        disp_clear_screen()
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
        disp_clear_screen()

        print("Setup ZSH. . . please wait")
        os.system(
            'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
        )

    if choice == "8":
        time.sleep(0.2)
        menu_disk()

    if choice == "0":
        os.system('clear')
        sys.exit()

    if choice == "M" or "m":
        menu_options()

    if choice == "":
        clear_screen()
        print("Invalid Option Chosen. Please try again")
        input("Press Enter to Continue")
        main_menu()

    else:
        clear_screen()
        print("Invalid Option Chosen. Please try again")
        input("Press Enter to Continue")
        main_menu()

    main_menu()

def menu_disk():
    """
    Launch the Disk Management Menu
    """
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
        header_devicemenu()
        print("Disks found:\n")
        os.system("lsblk")
        input("\nPress any key to return to menu\n")
        disp_clear_screen()
        menu_disk()

    if choice == "2":
        header_devicemenu()
        print("Hard Drive Space:\n")
        os.system("df -h -t ext4")
        input("\nPress any key to return to menu\n")
        menu_disk()

    if choice == "3":
        header_devicemenu()
        print("Free memory:\n")
        os.system("free -h -l")
        input("\nPress any key to return to menu\n")
        menu_disk()

    if choice == "0":
        main_menu()

def menu_options():
    time.sleep(0.1)
    header_options()
    print("Please choose an option \n")

    # The Menu Options
    print('1. Enable / Disable "Clear On Input"')
    print("\n0. Return to Main Menu")

    choice = input("\n Enter your choice: ")

    if choice == "1":
        toggle_clear_on_input()
        menu_options()

# ------------------------------------------------------------------- #
# Run the Main Application under this line
setup_app()
main_menu()
