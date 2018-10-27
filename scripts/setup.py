import os, time , sys

print('System Setup. Press any key to continue')
input('>> ')

print('Installing system software')
time.sleep(3)
os.system('sudo pacman -S plasma xorg-xerver gwenview okular dolphin konsole lolcat')
os.system('for x in $(cat package_list.txt); do pacman -S $x; done')

print('Enabling services')
time.sleep(3)
os.system('sudo systemctl enable sddm --now')
os.system('sudo systemctl enable tlp --now')
os.system('sudo cp ../services/suspendfix.service /etc/systemd/system/ && sudo sudo systemctl enable suspendfix.service --now')

print('Installing YAY and SNAP for Software Installation')
time.sleep(3)
os.system('git clone https://aur.archlinux.org/yay.git')
os.system('cd yay && makepkg')

os.system('yay -S snapd')
os.system('systemctl enable snapd --now')
os.system('snap install bitwarden powershell slack spotify discord nextcloud-client mailspring')

time.sleep(3)
print('Installation Complete')
sys.exit(0)