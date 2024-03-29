# Speaker project code

import spotipy
import tekore as tk

print("hello world")


client_id = "8c720eb661fe4e798186b79a382fc9dd"
client_secret="4a4de01f308e4745be4cd79d1a0be3ae"

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)

# album = spotify.album('3RBULTZJ97bvVzZLpxcB0j')
# for track in album.tracks.items:
#     print(track.track_number, track.name)

# print(album)
# print(album.artists[0])

redirect_uri = 'https://example.com/callback'

# security_file=open("tokens.txt","r+")

# user_token=security_file.read([0])

user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)

# if (user_token == ""):
    # security_file.write(user_token)

conf = (client_id, client_secret, redirect_uri, user_token.refresh_token)
tk.config_to_file('tekore.cfg', conf)

conf = tk.config_from_file('tekore.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])


spotify.token = user_token

tracks = spotify.current_user_top_tracks(limit=10)
# for track in tracks.items:
#     print(track.name)


# conf = (client_id, client_secret, redirect_uri)
# token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

# spotify = tk.Spotify(token)
# tracks = spotify.current_user_top_tracks(limit=10)
# spotify.playback_start_tracks([t.id for t in tracks.items])