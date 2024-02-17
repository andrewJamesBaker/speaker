import vlc
import time
import urllib.request 
import requests
from bs4 import BeautifulSoup 

# --- Base Settings ---
MADISON_AIRPORT = "KMSN"
BASE_SITE = "https://www.lofiatc.com/?icao="

# --- User Settings ---
__master_volume__ = 1
__station__ = "KMSN"
__live_setting__ = 1

radioPlaylist = "./lofiRadio.m3u"

# lofiUrl = "https://www.lofiatc.com/assets/music/Casiio%20x%20Sleepermane%20%E2%80%93%20Maya.mp3"
# testUrl = "https://www.lofiatc.com/s1-bos.liveatc.net/ksea2_twr_e"
# testUrl = "http://listen.livestreamingservice.com/181-beatles_128k.mp3"
# planeUrl = "https://s1-lhr.liveatc.net/ksea2_twr_e?nocache=2024021602370176142"
# planeUrl = "https://s1-lhr.liveatc.net/ksea2_twr_e"

# lofiSiteResponse = requests.get(BASE_SITE + MADISON_AIRPORT, stream=True)


# soup = BeautifulSoup(lofiSiteResponse.content, 'html.parser')

# currentSong = soup.find("audio", id = "music-audio-player")

# airtrafficPlayer = vlc.MediaPlayer(planeUrl)
# lofiPlayer = vlc.MediaPlayer(lofiUrl)

media_player = vlc.MediaListPlayer()
player = vlc.Instance()
media_list = player.media_list_new()
media = player.media_new("./lofiRadio.m3u")
media_list.add_media(media)
media_player.set_media_list(media_list)
media_player.play()

# testPlayer.play()

# airtrafficPlayer.play()
# lofiPlayer.play()

# --- Control Loop ---
while (True):
    time.sleep(5)
    # lofiPlayer.pause()
    