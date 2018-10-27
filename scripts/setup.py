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

print('Setup NBFC')
os.system('yay -S nbfc')
os.system('systemctl service nbfc enable --now')
os.system('nbfc config -s Asus Zenbook UX430UA')
os.system('sudo mv /opt/nbfc/Plugins/StagWare.Plugins.ECSysLinux.dll /opt/nbfc/Plugins/StagWare.Plugins.ECSysLinux.dll.old')
os.system('systemctl restart nbfc')
os.system('nbfc set -a')
os.system('nbfc start')

print('Setup ZSH')
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
os.system('mv .zshrc ~/.zshrc')

time.sleep(3)
print('Installation Complete')
sys.exit(0)