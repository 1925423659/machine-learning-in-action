import bayes
import feedparser

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
vocab_list, p_sf, p_ny = bayes.local_words(ny, sf)
vocab_list, p_sf, p_ny = bayes.local_words(ny, sf)