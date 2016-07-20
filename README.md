# Introduction
ToshoParser is a small console application that automates fetching media from tokyotosho.info
# Usage
Install Python 3 and navigate to ToshoParser's directory, then type
```
pip install feedparser
python feeds.py
```

You will be greeted with a screen that looks similar to this.

```
Main Menu
    1 Run
    2 Edit Filters
    3 List All Filters And Conditions
    4 List All Downloaded Entries
    5 Open Feed
    0 Exit
```

Selecting Edit Filters will open a text file in your system's default editor.
Each line represents one query to Tokyo Toshokan and consists of the name of the query followed by a variable number of arguments.
For example,
```
Natsume +Natsume Yuujinchou +720p -HorribleSubs
```
will return all recent entries that match "Natsume Yuujinchou" and "720p" but do not have "HorribleSubs" in the title.
Currently only '+' and '-' is supported.
Afterwards, selecting Run from the main menu will open all links that were matched by your entries.
If you wish to run the query without bringing up the menu, you can pass "-run" to feeds.py
```
python feeds.py -run
```

