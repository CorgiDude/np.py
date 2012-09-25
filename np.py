#!/usr/bin/env python
import urllib2
import xml.dom.minidom as minidom

LASTFM_USERNAME = "CorgiDude"
NP_TEXT = "Now listening to"

last_sock = urllib2.urlopen("http://ws.audioscrobbler.com/1.0/user/{fm_user}/recenttracks.rss".format(fm_user = LASTFM_USERNAME))
last_xml = last_sock.read()
last_sock.close()
last_doc = minidom.parseString(last_xml)
titles = last_doc.getElementsByTagName("title")
if titles.count > 1:
  print u"{np_text}: {track} (via Last.fm)".format(np_text = NP_TEXT, track = titles[1].childNodes[0].data).replace(u'\u2022', '--')
else:
  print "Hasn't listened to anything on Last.fm recently"

