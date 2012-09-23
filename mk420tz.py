# Generates tz.js from time zone csv files
# get latest files from http://timezonedb.com/download
import csv,json,time,os
countries = {}
for r in csv.reader(file("country.csv")):
  countries[r[0]] = r[1]
zones = {}
for r in csv.reader(file("zone.csv")):
  parts = r[2].replace('_',' ').split('/')
  city = parts[-1]
  if len(parts)>2: # e.g. America/North_Dakota/New_Salem
    country = parts[1] # e.g. North Dakota
  else: # e.g. America/Denver
    country = countries[r[1]] # e.g. United States
  if country==city: # Avoid awkward searches like "Anguilla, Anguilla"
    country = parts[0] # Use continent instead
  zones[int(r[0])] = {"name":', '.join((city,country))}
  # zones[int(r[0])] = {"name":r[2].replace('_',' ')}
now = int(time.time())
for r in csv.reader(file("timezone.csv")):
  code = int(r[0])
  if not zones.has_key(code):
    continue
  starttime = int(r[2])
  offs = int(r[3])
  if offs < 0:
    offs += 60*60*24
  d = zones[code]
  if starttime<now and (not d.has_key("starttime") or d["starttime"]<starttime):
    d["starttime"] = starttime
    d["offs"] = offs
offsdict = {}
for k in zones:
  d = zones[k]
  if d["offs"]%3600: # One a dem funkey time zones
    continue # Let's not confuse the user :)
  offsdict[d["offs"]] = offsdict.get(d["offs"],[])+[d["name"]]
res = sorted([[k,sorted(offsdict[k])] for k in offsdict],key=lambda x:-x[0])
js = file("tz.js","w")
js.write("// Generated by mk420tz.py - see https://github.com/thedod/global420\n")
js.write("// Data source: http://timezonedb.com/files/timezonedb.csv.zip\n")
js.write("//              (version: {0})\n".format(time.ctime(os.stat("zone.csv").st_mtime)))
js.write("window.timezones = ")
json.dump(res,js,indent=1)
js.close()
