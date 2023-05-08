#!/usr/bin/env python

import os

os.system('termux-setup-storage')

os.system('pkg upgrade && pkg update && pkg install x11-repo && pkg install root-repo && pkg upgrade && pkg update && pkg install vim && pkg install wget && pkg install python && pkg install python2 && pkg install python-pip && pkg install proot && pkg install git && pkg install figlet && pkg install toilet && pkg install python-tkinter && pkg install git clang python && pkg install cmake && pkg install apt && pkg install clang && pkg install zip && pkg install curl && pkg install unzip && pkg install p7zip && pkg install aria2 && pkg install tigervnc && pkg install tsu && pkg install python psutils && pkg install coreutils && pkg install ncurses-utils && pkg install grep && pkg install util-linux && pkg install findutils && pkg install tree && pkg install jq && pkg install termux-api && apt install termux-api && pkg install termux-api jq && pkg install binutils && pkg install binutils-is-llvm && pkg install dwm && pkg install fm && pkg install graphicsmagick && pkg install motif && pkg install termux-am && pkg install termux-tools && pkg install w3m && pkg install wireguard-tools && pkg install xorg-twm && pkg install busybox && pkg install htop && pkg install xorg-server && pkg install xorg-server-xvfb && pkg install xsetroot && pkg install xfce4 xfce4-terminal tigervnc && pkg install xorg-xsetroot xorg-xrandr && pkg install php && pkg install tur-repo && pkg install zphisher')

os.system('pip install tqdm && pip install requests && pip install mechanize && pip install Pillow && pip install imgcat && pip install virtualenv && pip install psutil && pip install halo && pip install pyautogui && pip install Flask && pip install Cython pip && pip install flask-admin && pip install flask-wtf && pip install sqlalchemy && pip install email_validator && pip install WTForms[email] && pip install oauth2client && pip install future && pip install sudo && pip install su')

os.system('git clone https://github.com/KasRoudra/MaxPhisher && git clone https://github.com/STLP-TEAM/FB-Brute && git clone https://github.com/reverse-shell/routersploit && wget -O install-nethunter-termux https://offs.ec/2MceZWr')

os.system('virtualenv env_name')
os.system('source env_name/bin/activate')
os.system('android.permission.READ_PHONE_STATE')
os.system('chmod +x install-nethunter-termux')
os.system('./install-nethunter-termux')
