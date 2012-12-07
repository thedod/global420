This [web page](http://zzzen.com/global420) answers 2 simple questions:

* Where is it going to be 4:20 PM next?
* How soon?

Feel free to fork this if you prefer some other hour :)

### Generating tz.js

The standard [time zone db](http://timezonedb.com/) needs to
be pre-processed in order to easily answer these seemingly simple questions.

For that, you should generate `tz.js` by running `python mk420tz.py` on the latest csv files (available [here](http://timezonedb.com/download)).

This should be done each time a time zone goes in or out of daylight saving time (DST). Best is to run this as a daily cron task.

Once in a while, the TZ database changes and you need to load fresh csv files. To be notified when this happens, you can follow [@timezonedb](https://twitter.com/timezonedb) on twitter, or use the [atom feed](http://feeds.feedburner.com/timezonedb).

### Quick start for the lazy

For your convenience, if you want to start running this right away, `tz-example.js` contains _some_ version of `tz.js`.
Not necessarily the freshest, but no harm in running a slightly inaccurate version of this ;)

### generating flickrplaces.js

Nomally, you _don't_ have to do this, unless a future version of the timezone db introduces new places,
or you want to change the format of the place names in `tz.js` (by tweaking `mk420tz.py`).
If you're into it, here's how:

1. Get a flickr [API key](https://secure.flickr.com/services/api/keys/).
1. Copy `conf-example.py` to `conf.py` and edit it.
1. Run `python mkflickrplaces.py`. Note that it takes about 15 minutes to run, because it waits 2 seconds
   between API requests, to avoid flooding the good folks at flickr.
1. Edit `flickrplaces.js` and fix the following known bugs

   * `"Costa Rica, CR": "/Italy/Lombardy"` should be `"/Costa+Rica"`
   * `"Malta, MT": "/United+States/Montana/Malta"` should be `"/Malta"`
   * If you find other bugs there, please leave an issue here.

### Thanks

* To [Timezonedb](http://timezonedb.com) for maintaining the data
* To [Twitter](http://twitter.github.com) for [Bootstrap](http://twitter.github.com/bootstrap)
* To [Bootswatch](http://bootswatch.com/) for the themes
* To [DuckDuckGo](http://duckduckgo.com/), [Open Street Map](http://www.openstreetmap.org/) and [flickriver](http://flickriver.com) for giving us stuff to link to
* To my wife for discovering the need for such an app. This is her birthday present.

### Frequently Asked question
Seattle doesn't appear because it isn't on [the timezone list](http://timezonedb.com/time-zones) :(

----------------------------

*<p align="right">Deadlines are either dead or dying. Procrastination is for life.</p>*
<a href="http://flattr.com/thing/942995/Global-420-countdown" target="_blank">
<img src="http://api.flattr.com/button/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0" /></a>
