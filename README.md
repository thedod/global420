This [web page](http://zzzen.com/global420) answers 2 simple questions:

* Where is it going to be 4:20 PM next?
* How soon?

Feel free to fork this if you prefer some other hour :)

The standard [time zone db](http://timezonedb.com/) needs to
be pre-processed in order to easily answer these seemingly simple questions.

Fo that, you should generate `tz.js` by running `mk420tz.py` on the latest csv files (available [here](http://timezonedb.com/download)).

This should be done each time a time zone goes in or out of daylight saving time (DST). Best is to run this as a daily cron task.

Once in a while, the TZ database changes and you need to load fresh csv files. To be notified when this happens, you can follow [@timezonedb](https://twitter.com/timezonedb) on twitter, or use the [atom feed](http://feeds.feedburner.com/timezonedb).

For your convenience, if you want to start running this right away, _some_ version of `tz.js` comes with the repository.
Not necessarily the freshest, but no harm in running a slightly inaccurate version of this page ;)

### Thanks

* To [Timezonedb](http://timezonedb.com) for maintaining the data
* To [Twitter](http://twitter.github.com) for [Bootstrap](http://twitter.github.com/bootstrap)
* To [Bootswatch](http://bootswatch.com/) for the themes
* To [DuckDuckGo](http://duckduckgo.com/), [Open Street Map](http://www.openstreetmap.org/) and [flickriver](http://flickriver.com) for giving us stuff to link to
* To my wife for discovering the need for such an app. This is her birthday present.

----------------------------

*<p align="right">Deadlines are either dead or dying. Procrastination is for life.</p>*
