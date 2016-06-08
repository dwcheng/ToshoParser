# Introduction
ToshoParser is a small console application that automates fetching media from tokyotosho.info
# Usage
Install Python 3 and navigate to ToshoParser's directory, then run
```
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
Each line represents one query to Tokyo Toshokan.
A line consists of the name of the query and then a variable number of arguments proceeded by a "+" or a "-".
For example,
```
Natsume +Natsume Yuujinchou +720p -HorribleSubs
```
will return all recent entries that match "Natsume Yuujinchou" and "720p" but do not have "HorribleSubs" in the title.
Afterwards, selecting Run from the main menu will open all links that were matched by your entries.
A query can return multiple results.
