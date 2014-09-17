#!/usr/bin/python
# -*- coding: utf-8 -*-

# alarm.py

# Copyright 2014 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# CLI Alarm Clock

# https://github.com/dslackw/alarm

# Alarm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
import datetime
import calendar

__all__ = "alarm"
__author__ = "dslackw"
__version_info__ = (1, 2)
__version__ = "{0}.{1}".format(*__version_info__)
__license__ = "GNU General Public License v3 (GPLv3)"
__email__ = "d.zlatanidis@gmail.com"


class ALARM(object):
    '''
        CLI Alarm Clock
    '''    
    def __init__(self, alarm_day, alarm_time, song):
        self.alarm_day = alarm_day
        self.alarm_time = alarm_time.replace(":", " ").split() # split items
        self.song = song
        self.alarm_hour = self.alarm_time[0]
        self.alarm_minutes = self.alarm_time[1]
    def start(self):
        '''
            All the work going on here. To the Authority the 
            right time format and finding the correct path of 
            the file. The Application requires Mplayer to play
            the alarm sound. Please read which sounds are supported 
            in page : 
            http://web.njit.edu/all_topics/Prog_Lang_Docs/html/mplayer/formats.html
        '''
        RUN_ALARM = True
        try:
            now = datetime.datetime.now()
            if int(self.alarm_day) > calendar.monthrange(now.year, now.month)[1] or int(self.alarm_day) < 1:
                print("Error: day out of range")
                RUN_ALARM = False
            for item in self.alarm_time:
                if len(self.alarm_time) > 2 or len(item) > 2 or len(item) == 1:
                    print("Usage 'HH:MM'")
                    RUN_ALARM = False 
                    break
            if int(self.alarm_hour) in range(0, 24):
                pass
            else:
                print("Error: hour out of range")
                RUN_ALARM = False
            if int(self.alarm_minutes) in range(0, 60):
                pass
            else:
                print("Error: minutes out of range")
                RUN_ALARM = False
        except ValueError:
            print("Usage 'HH:MM'")
            RUN_ALARM = False
        if not os.path.isfile(self.song):
            print("Error: the file does not exist")
            RUN_ALARM = False
        alarm_day_name = calendar.day_name[calendar.weekday(now.year, now.month, int(self.alarm_day))]
        self.alarm_time.insert(0, self.alarm_day)
        self.alarm_time = ":".join(self.alarm_time) # reset begin format
        if RUN_ALARM:
            os.system("clear")
            print("+" + "=" * 78 + "+")
            print("|" + " " * 30 + "CLI Alarm Clock" + " " * 33 + "|")
            print("+" + "=" * 78 + "+")
            print("| Alarm set at : %s %s" % (
                  alarm_day_name, self.alarm_time[3:]) + " " * (
                  61-len(alarm_day_name + self.alarm_time[3:])) + "|")
            print("| Sound file : %s" % self.song + " " * (64-len(self.song)) + "|")
            print("| Time : " + " " * 70 + "|")
            print("+" + "=" * 78 + "+")
            while RUN_ALARM:
                try:
                    start_time = time.strftime("%d:%H:%M:%S")
                    self.position(6, 10, self.color(
                         "green") + start_time[3:] + self.color("endc"))
                    time.sleep(1)
                    if start_time[:-3] == self.alarm_time:
                        self.position(6, 10, self.color(
                             "red") + start_time[3:-3] + self.color("endc") + " Wake Up !")
                        os.system("mplayer '%s'" % self.song)
                        RUN_ALARM = False
                except KeyboardInterrupt:
                    print("\nAlarm canceled!")
                    RUN_ALARM = False

    def position(self, x, y, text):
        '''
            ANSI Escape sequences
            http://ascii-table.com/ansi-escape-sequences.php
        '''    
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()

    def color(self, color):
        '''
            Print foreground colors 
        '''
        paint = {
                "red" : "\x1b[31m",
                "green" : "\x1b[32m",
                "endc" : "\x1b[0m"
                }
        return paint[color] 

def main():
    args = sys.argv
    args.pop(0)
    if len(args) == 0:
        print("try alarm --help")
    elif len(args) == 1 and args[0] == "-h" or args[0] == "--help":
        print("usage: %s [-h] [-v]" % __all__)
        print("             [-s] <day> <alarm time> <song>\n")
        print("optional arguments")
        print("  -h, --help       show this help message and exit")
        print("  -v, --version    print version and exit")
        print("  -s, --set        set alarm day, time and sound")
        print("\nexample: alarm -s 21 06:00 /path/to/song.mp3") 
    elif len(args) == 1 and args[0] == "-v" or args[0] == "--version":
        print("Version : %s" % __version__)
    elif len(args) == 4 and args[0] == "-s" or len(args) == 4 and args[0] == "--set":
        ALARM(alarm_day=args[1], alarm_time=args[2], song=args[3]).start()
    else:
        print("try alarm --help")
        
if __name__ == "__main__":
    main()
