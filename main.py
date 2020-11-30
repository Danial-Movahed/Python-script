#!/usr/bin/env python
import os
import subprocess
from time import sleep
def envi():
    DE_STOP=os.system('xmessage -buttons Xfce4,Mate,Gnome,Lxde,Pantheon,Budgie,Next "$@" "Which desktop do you want to install?"')
    if DE_STOP==25856:
        os.system('xmessage Installing Xfce4')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "apt install xfce4 xfce4-goodies"')
    elif DE_STOP==26112:
        os.system('xmessage Installing Mate')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "apt install mate-desktop-environment"')
    elif DE_STOP==26368:
        os.system('xmessage Installing Gnome')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "apt install gnome-shell gnome gdm3"')
    elif DE_STOP==26624:
        os.system('xmessage Installing LXDE')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "apt install lxde"')
    elif DE_STOP==26880:
        os.system('xmessage "Installing pantheon (Please note that it is going to add a ppa!)"')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "add-apt-repository ppa: elementary-os/stable ; apt update ; apt install elementary-desktop"')
    elif DE_STOP==27136:
        os.system('xmessage "Installing pantheon (Please note that it is going to use tasksel!)"')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "apt install tasksel ; tasksel install ubuntu-budgie-desktop"')
    elif DE_STOP==27392:
        return 1
    return 0
def effect():
    effect_stop=os.system('xmessage -buttons Yes,No "$@" "Do you want to enable awesome cinnamon effects?"')
    if effect_stop==26112:
        return 1
    elif effect_stop==25856:
        sleep(1)
        os.system('xdotool key super')
        sleep(2)
        os.system('xdotool type Effects')
        sleep (1)
        os.system('xdotool key Return')
        sleep (6)
        sub = subprocess.Popen("xdotool getactivewindow getwindowname", shell=True, stdout=subprocess.PIPE)
        sub_ret = sub.stdout.read()
        if sub_ret==b'Effects\n':
            os.system('xdotool getactivewindow windowmove 10 20')
            os.system('xdotool mousemove 439 62')
            sleep (0.5)
            os.system('xdotool click 1')
            os.system('xdotool mousemove 696 115')
            sleep (2)
            os.system('xdotool click 1')
            ##############################
            sleep (0.5)
            os.system('xdotool mousemove 311 205')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 752 313')
            os.system('xdotool click 1')
            ###
            sleep (0.5)
            os.system('xdotool mousemove 774 211')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 553 222')
            os.system('xdotool click 1')
            os.system('xdotool click 1')
            sleep (0.5)
            os.system('xdotool type 50')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 318 270')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 764 375')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 466 276')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 728 230')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 564 263')
            os.system('xdotool click 1')
            os.system('xdotool click 1')
            sleep (0.5)
            os.system('xdotool type 120')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 350 312')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 654 407')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 444 321')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 764 896')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 569 318')
            os.system('xdotool click 1')
            os.system('xdotool click 1')
            sleep (0.5)
            os.system('xdotool type 460')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 342 366')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 536 384')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 459 365')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 608 618')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 573 368')
            os.system('xdotool click 1')
            os.system('xdotool click 1')
            sleep (0.5)
            os.system('xdotool type 250')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 354 421')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 541 452')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 481 419')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 725 313')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 568 422')
            os.system('xdotool click 1')
            os.system('xdotool click 1')
            sleep (0.5)
            os.system('xdotool type 300')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 328 484')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 556 502')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 496 492')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 642 209')
            os.system('xdotool click 1')
            ##
            sleep (0.5)
            os.system('xdotool mousemove 562 490')
            os.system('xdotool click 1')
            os.system('xdotool click 1')
            sleep (0.5)
            os.system('xdotool type 150')
            os.system('notify-send "Hmm" "It looks Nice!"')
            sleep (1)
            os.system('xdotool mousemove 792 30')
            os.system('xdotool click 1')
            os.system('notify-send "Hmm" "Effectation complete :P !"')
        return 0
            
def cam():
    cam_stop=os.system('xmessage -buttons Yes,No "$@" "Do you want to enable Face unlock?"')
    if cam_stop==25856:
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "add-apt-repository ppa:boltgolt/howdy ; apt update ; apt install howdy"')
        camadd=os.system('xmessage -buttons Yes,No "$@" "Do you want to add your face now?"')
        if camadd==25856:
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "howdy add"')
        camconf=os.system('xmessage -buttons Yes,No "$@" "Do you want to open howdy config?"')
        if camconf==25856:
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e "howdy config"')
            
def arashk():
    arra=os.system('xmessage -buttons Minimal,Full,"Not now" "$@" "Installing some goodies!"')
    if arra==25856:
        os.system('xmessage "Minimal Installation!"')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e \' wget --continue https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; apt install zsh codeblocks playonlinux skypeforlinux adobe-flashplugin adobe-flashplugin-properties-gtk boot-repair vim gromit-mpx ; add-apt-repository ppa:lutris-team/lutris ; apt update ; apt install lutris ; dpkg -i google-chrome-stable_current_amd64.deb\'')
        subprocess.Popen(['xterm', '-e','zsh'])
        sleep (2)
        os.system('xdotool type 1')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 1')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 0')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 2')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 1')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 0')
        os.system('xdotool key Return')
        sleep (2)
        os.system('notify-send "Hmm" "Minimal installation completed!"')
    elif arra==26112:
        os.system('xmessage "Full Installation!"')
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e \'add-apt-repository ppa:apandada1/xournalpp-stable ; apt update ; apt install xournalpp ; wget --continue https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; wget --continue http://www.geogebra.net/linux/pool/main/g/geogebra-classic/geogebra-classic_6.0.609.0-202010060653_amd64.deb ; wget --continue https://dl.discordapp.net/apps/linux/0.0.12/discord-0.0.12.deb ; apt install zsh codeblocks playonlinux skypeforlinux adobe-flashplugin tuxmath boot-repair vim gromit-mpx bb dolphin-emu cmatrix gnujump supertux supertuxkart thonny compiz dconf-editor grub-customizer anbox python3-pip ; add-apt-repository ppa:lutris-team/lutris ; apt update ; apt install lutris ; dpkg -i google-chrome-stable_current_amd64.deb geogebra-classic_6.0.609.0-202010060653_amd64.deb ; dpkg -i discord-0.0.12.deb ; python3 -m pip install legendary-gl\'')
        subprocess.Popen(['xterm', '-e','zsh'])
        sleep (2)
        os.system('xdotool type 1')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 1')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 0')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 2')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 1')
        os.system('xdotool key Return')
        sleep (2)
        os.system('xdotool type 0')
        os.system('xdotool key Return')
        sleep (2)
        os.system('notify-send "Hmm" "Full installation completed!"')   
def snap():
    snst=os.system('xmessage -buttons Yes,No "$@" "Do you like to install snap?"')
    if snst==25856:
        os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e \'mv /etc/apt/preferences.d/nosnap.pref /etc/apt/preferences.d/nosnap.pref.bak ; apt update ; apt install snap\'')
        os.system('notify-send "Achievment Unlocked!" "Canonical time!"')
def cortana():
    cortst=os.system('xmessage -buttons Yes,No "$@" "Do you like to install cortana (mycroft)? (Danial recommendation)"')
    if cortst==25856:
        sub = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE)
        pw = sub.stdout.read()
        subprocess.call(['xmessage', 'Installing cortana (mycroft) on', pw])
        os.system('xterm -e "git clone https://github.com/MycroftAI/mycroft-core.git;cd mycroft-core; bash dev_setup.sh"')
        os.system('notify-send "Achievment Unlocked!" "Wait thats illegal!"')
        
def atom():
    atst=os.system('xmessage -buttons Yes,No "$@" "Do you like to install atom?"')
    if atst==25856:
        atst2=os.system('xmessage -buttons Apt,Snap "$@" "Do you like to install atom from snap or apt?"')
        if atst2==25856:
            os.system('xmessage "Make sure you have enabled shecan!"')
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e \'wget -q https://packagecloud.io/AtomEditor/atom/gpgkey -O- |  apt-key add - ; add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" ; apt update ;apt install atom\'')
            os.system('notify-send "Achievment Unlocked!" "Mmmm Coding Time!"')
        elif atst2==26112:
            os.system('snap install atom')
            os.system('notify-send "Achievment Unlocked!" "Mmmm Coding Time!"')
            
def wine_stag():
    wnst=os.system('xmessage -buttons Yes,No "$@" "Do you like to install wine?"')
    if wnst==25856:
        wnst2=os.system('xmessage -buttons Yes,No "$@" "Do you like to install wine-staging?"')
        if wnst2==25856:
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e \'wget -nc https://dl.winehq.org/wine-builds/winehq.key ; apt-key add winehq.key ; add-apt-repository "deb https://dl.winehq.org/wine-builds/ubuntu/ focal main" ; apt update ; apt install --install-recommends winehq-staging\'')
            subprocess.Popen(['notify-send', 'Achievment Unlocked!', 'Ooooooooooooooooooo. Time for hackers!'])
            subprocess.Popen(['aplay','ooh.mp3'])
            subprocess.Popen(['sleep','5',';','notify-send', 'Achievment Unlocked!', 'Time for Micorrupt Office!'])
        elif wnst2==26112:
            os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xterm -e \'wget -nc https://dl.winehq.org/wine-builds/winehq.key ; apt-key add winehq.key ; add-apt-repository "deb https://dl.winehq.org/wine-builds/ubuntu/ focal main" ; apt update ; apt install --install-recommends winehq-stable\'')
            subprocess.Popen(['notify-send', 'Achievment Unlocked!', 'Time for Micorrupt Office!'])
            
depd=os.system('xmessage -buttons Yes,No "$@" "Are the dependencies installed?"')
if depd==25856:
    envi()
    effect()
    cam()
    arashk()
    wine_stag()
    snap()
    cortana()
    atom()
    os.system('xmessage "Finished! Enjoy your linux mint!"')
else:
    os.system('xmessage "Instaling dependencies!"')
    os.system('notify-send "Achievment Unlocked!" "Is it very old? :P"')
    os.system('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY gnome-terminal -- apt install xterm xdotool')
    envi()
    effect()
    cam()
    arashk()
    wine_stag()
    snap()
    cortana()
    atom()
    os.system('xmessage "Finished! Enjoy your linux mint!"')
