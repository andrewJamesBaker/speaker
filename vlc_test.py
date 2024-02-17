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



lofiUrl = "https://www.lofiatc.com/assets/music/Casiio%20x%20Sleepermane%20%E2%80%93%20Maya.mp3"
# testUrl = "https://www.lofiatc.com/s1-bos.liveatc.net/ksea2_twr_e"
# testUrl = "http://listen.livestreamingservice.com/181-beatles_128k.mp3"
# planeUrl = "https://s1-lhr.liveatc.net/ksea2_twr_e?nocache=2024021602370176142"
planeUrl = "https://s1-lhr.liveatc.net/ksea2_twr_e"

lofiSiteResponse = requests.get(BASE_SITE + MADISON_AIRPORT, stream=True)


soup = BeautifulSoup(lofiSiteResponse.content, 'html.parser')

currentSong = soup.find("audio", id = "music-audio-player")

airtrafficPlayer = vlc.MediaPlayer(planeUrl)
lofiPlayer = vlc.MediaPlayer(lofiUrl)



# airtrafficPlayer.play()
lofiPlayer.play()

# --- Control Loop ---
while (True):
    time.sleep(5)
    lofiPlayer.pause()
    