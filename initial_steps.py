import sys
import pprint
import spotipy
import spotipy.util as util

# we need 'playlist-modify-public', 'user-top-read' scopes
username = '12167117255'
scope = 'user-top-read'
client_id = '832a7bc6d77345daade6d437ab7ecc35'
client_secret = 'd853a5f3ca714d28bcc0ab8ccf818cbf'
redirect_uri = 'http://localhost:8888/callback/'

token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)

if token:
  pp = pprint.PrettyPrinter(indent=4)
  sp = spotipy.Spotify(auth=token)
  top_tracks = sp.current_user_top_tracks(limit=1, time_range='short_term')
  item = top_tracks['items']
  pp.pprint(item[0]['name'])
  id = item[0]['id']
