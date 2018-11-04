# SetupArch
This script is designed after ARCH has been installed to install the common setup for myself (using KDE) and configure the system accordingly.

The script is developed in python, since this is the system I know, but of course could be moved to Bash quite easily

## ToDo

1. Move Functions to another file for better readability
2. Include function for creation of package_list.txt
3. Test the script against a new installation of Arch
4. Figure out how to get Oh-My-ZSH to install, and set the default shell to ZSH, without stopping the Python Script
5. Add more options (asynchronous downloads with pacman, update MirrorList etc)
6. Add functionality to run the script on Arch Live media, and allow it to setup Partitions and Configuration First >> May need to find a way to check if the user is running a live session or not, and disable functions depending on results
7. Add option to read from JSON Settings File for Options such as "Clear on Input" etc