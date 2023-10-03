#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os, subprocess
import time
import configparser
import argparse

from pathlib import Path 

def main(args):
    config = configparser.ConfigParser()
    config.read(args.kwinrc)
    nod = config["Desktops"]["Number"]

    while True:
        if subprocess.getoutput("qdbus org.kde.KWin /KWin currentDesktop") == nod:
            os.system("qdbus org.kde.KWin /KWin setCurrentDesktop 1")
        else:
            os.system("qdbus org.kde.KWin /KWin nextDesktop")
        time.sleep(args.delay)
    
if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog="desktopchanger",
        description="A simple script to automatically change the actual virtual desktop on KDE Plasma 5.",
        epilog="Written by Miklos Horvath <hmiki@blackpantheros.eu>",
    )
    parser.add_argument('-d','--delay', type=int, default=1200, help='Delay in seconds between desktop changing events.')
    parser.add_argument('-k','--kwinrc', type=str, default=f"{Path.home()}/.config/kwinrc", help='kwinrc config file path')
    args = parser.parse_args()
    main(args)
