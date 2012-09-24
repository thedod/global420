This [web page](http://zzzen.com/global420) answers 2 simple questions:

* Where is it going to be 4:20 PM next?
* How soon?

Feel free to fork this if you prefer some other hour :)

Well, data is a bitch, and the standard [time zone db](http://timezonedb.com/) needs to
be pre-processed in order to easily answer these seemingly simple questions.
Not only that - the database keeps changing according to local decisions regarding
daylight saving time.

This means that whenver this happens, you need to generate `tz.js` by running
`mk420tz.py` on the latest csv files (available [here](http://timezonedb.com/download)).

To be notified when the database is changed, you can follow [@timezonedb](https://twitter.com/timezonedb) on twitter, or use the [atom feed](http://feeds.feedburner.com/timezonedb).

### Notes:

* If you want to start running this right away, _some_ version of `tz.js` comes with the repository.
  Not necessarily the freshest, but no harm in running a slightly inaccurate version of this page ;)
* If you want to check whether `tz.js` is up to date, the modification date of the source csv files
  appears as a comment inside it.

### Thanks

* To [Timezonedb](http://timezonedb.com) for maintaining the data
* To [Twitter](http://twitter.github.com) for [Bootstrap](http://twitter.github.com/bootstrap)
* To [Bootswatch](http://bootswatch.com/) for the themes
* To [DuckDuckGo](http://duckduckgo.com/) and [Open Street Map](http://www.openstreetmap.org/) for giving us stuff to link to

----------------------------

*<p align="right">Deadlines are either dead or dying. Procrastination is for life.</p>*
