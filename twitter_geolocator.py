import twitter
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import datetime
import json
import descartes
import pdb
import sys
from os import environ

if len(sys.argv) <= 1:
    raise ValueError('Keyword arguments must be provided.')

CONSUMER_KEY        = environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET     = environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN_KEY    = environ.get('TWITTER_ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_TOKEN_SECRET')

keywords       = ''
api_connection = twitter.Api(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET
)

for keyword in sys.argv[1:]:
    keywords += (keyword + ' ')

date_of_today 	   = datetime.date.today()
date_of_last_month = date_of_today - datetime.timedelta(days=30)
date_param 	   = date_of_last_month.strftime('%Y-%m-%d')
keywords_as_params = urllib.parse.quote(keywords)
query_string       = 'q=' + keywords_as_params + '&result_type=recent&' \
                     'since=' + date_param + '&count=100'

# Pending app verification:
# results = api_connection.GetSearch(raw_query=query_string)

pdb.set_trace()

