window.getUTC=function() {
  var now = new Date();
  return now.getUTCHours()*3600+now.getUTCMinutes()*60;
}
window.get420offset = function() {
  var offset = 16*3600+20*60-getUTC();
  if (offset<0) {
    offset += 24*3600;
  }
  return offset;
}
window.next420 = function() {
  var offs = get420offset();
  for (var i=0; i<timezones.length; i++) {
    if (timezones[i][0]<=offs) {
      return {
        minutes: (offs-timezones[i][0])/60,
        places: timezones[i][1]
      }
    }
  }
  return {
    minutes: 666,
    places: ["Snafu (Yes. It's a bug)"]
  }
}
window.flickrplace = function(p) {
  return window.flickrplaces[p] || '/'+escape(p);
}
