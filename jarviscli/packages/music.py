# -*- coding: utf-8 -*-

import webbrowser
import os
from colorama import Fore
from packages.memory.memory import Memory
from utilities.GeneralUtilities import print_say
import six

def play(data, self):
    if len(data) == 0:
        print_say(Fore.BLUE + "Song name doesn't exist. (play '"'song name'"') " + Fore.RESET, self)

    else:
        wanted = data
        find = os.popen("ls | grep -i " + '"' + wanted + '"')
        music = str(find.readline())

        if not music:
            os.system("instantmusic -s " + wanted + " 2> /dev/null")
            find = os.popen("ls -tc --hide='__*' --hide='*.py'")
            music = str(find.readline()).replace("\n", "")
            os.system("XDG_CURRENT_DESKTOP= DESKTOP_SESSION= xdg-open " +
                      music.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)") +
                      " 2> /dev/null")

        else:
            os.system("XDG_CURRENT_DESKTOP= DESKTOP_SESSION= xdg-open " +
                      music.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)") +
                      " 2> /dev/null")

def radio(string, self, memory):
	self.c = Memory()
	if self.c.get_data('channel') is None:
	    print_say("Should I save " + string + " as your favourite channel?(Y/n)", self, Fore.RED)
	    if six.PY2:
		i = raw_input()
	    else:
		i = input()
	    if i == 'Y' or i =='Yes':
		memory.add_data('channel', string)
		url = "http://{}.radio.de".format(string.replace(" ",""))
		webbrowser.open(url)
		memory.save()
	    else:
		url = "http://{}.radio.de".format(string.replace(" ",""))
		webbrowser.open(url)
	else:
	    print_say("Do you want to hear your favourite channel sir?(Y/n)", self, Fore.RED)
	    if six.PY2:
		i = raw_input()
	    else:
		i = input()
	    if i == 'Y' or i == 'Yes':
		radio = memory.get_data('channel')
		url = "http://{}.radio.de".format(radio)
		webbrowser.open(url)
		memory.save()
	    else:
		print_say("Should I save " + string + " as your favourite channel sir?(Y/n)", self, Fore.RED)
		if six.PY2:
		    i = raw_input()
		else:
		    i = input()
		if i == 'Y' or i == 'Yes':
			memory.update_data('channel', string)
			memory.save()
		url = "http://{}.radio.de".format(string)
		webbrowser.open(url)

