LastFM Bio Scraper
==================
This is a simple artist biography scraper written in Python, designed to be used with Foobar2000 and the biography plugin.

Installation
------------
* Download and extract this script somewhere easy to find
* Install [Python 2.7](https://www.python.org/download/releases/2.7/)
* Install the [requests](http://docs.python-requests.org/en/latest/) library (easiest way is by using `pip`)
* In Foobar2000 go to Preferences -> Tools -> Biography Server (make sure you have the `foo_uie_biography` plugin installed)

![Screenshot showing the settings pane](http://i.imgur.com/SCCYexn.png)
* Make sure that "Run External Script" is at the top of the "Current source list"
* Go to the "Run External Script" under "Biography Server"
* As "Command line" enter `python C:/SCRIPT_LOCATION/script.py "%artist%"`, replacing `SCRIPT_LOCATION` with, well.. your script's location
* Set "Character code" to "UTF-8"

![Second screenshot showing the settings pane](http://i.imgur.com/iajXFT8.png)
* Click "Add New" to finish adding the script 

Now you should be able to see biographies again.

Why are you not using the Last.fm API?
--------------------------------------
The API does not always return the full biography and some of the useful 
formatting is gone and therefore a different solution is needed to retrieve it.

TODO
----
* Support for artist names with special characters


