import os
import re
import pickle
import sys
import webbrowser
import feedparser

from filter import Filter, Condition
from menu import Menu, Button

filters_list = []


def read_filters_from_textfile():
    del filters_list[:]
    f = open("save.txt", "r")
    for line in f:
        filter_name = re.match('[\w\s]*\w', line)
        conditions = re.findall('([+-][\w\s]*\w)', line)
        filt = Filter(filter_name.group(0))
        for condit in conditions:
            if condit[0] == "+":
                filt.add(Condition(condit[1:], "include"))
            elif condit[0] == "-":
                filt.add(Condition(condit[1:], "exclude"))
        filters_list.append(filt)

read_filters_from_textfile()

try:
    # noinspection PyArgumentList
    downloaded_items = pickle.load(open("down.p", "rb"))
except IOError:
    downloaded_items = []

feed_address = "http://tokyotosho.info/rss.php?filter=1&entries=450"
feed = feedparser.parse(feed_address)


def parse_feeds():
    read_filters_from_textfile()
    for entry in feed.entries:
        for filt in filters_list:
            if filt.check(entry.title) and not entry.title in downloaded_items:
                webbrowser.open(entry.link)
                downloaded_items.append(entry.title)
                filt.seen = True
    # noinspection PyArgumentList
    pickle.dump(downloaded_items, open("down.p", "wb"))
    sys.exit()


def list_all():
    for filt in filters_list:
        print(filt.name)
        for condition in filt.conditions:
            print("    ", condition.operation, condition.match_string)
    main_menu.display()


def list_downloaded():
    for downloaded in downloaded_items:
        print(downloaded)
    main_menu.display()


def filters_to_textfile():
    f = open("save.txt", "w")
    for filt in filters_list:
        line = ""
        line += filt.name
        for condit in filt.conditions:
            if condit.operation == "include":
                line += " +" + condit.match_string
            elif condit.operation == "exclude":
                line += " -" + condit.match_string
        line += "\n"
        f.write(line)
    f.close()
    os.startfile(os.path.dirname(os.path.realpath(__file__)) + "\\save.txt")
    main_menu.display()

def open_feed():
	webbrowser.open(feed_address)

# Main menu
main_menu_run = Button("Run", parse_feeds, 1)
main_menu_edit = Button("Edit Filters", filters_to_textfile, 2)
main_menu_all = Button("List All Filters And Conditions", list_all, 3)
main_menu_downloaded = Button("List All Downloaded Entries", list_downloaded, 4)
main_menu_feed = Button("Open Feed", open_feed, 5)
main_menu_exit = Button("Exit", sys.exit, 0)

main_menu_buttons = [main_menu_run, main_menu_edit, main_menu_all, main_menu_downloaded, main_menu_feed, main_menu_exit]

main_menu = Menu("Main Menu", main_menu_buttons)

try:
    if sys.argv[1] == "-run":
        parse_feeds()
except IndexError:
    pass

main_menu.display()
