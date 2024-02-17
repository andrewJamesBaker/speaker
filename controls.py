import vlc

global __volume__
global __station__
global __current_atc__
global __atc_volume__


def start_up():
    media_player = vlc.MediaListPlayer()
    player = vlc.Instance()
    media_list = player.media_list_new()
    # Start up stub

def shut_down():
    print("Shutdown")
    # shutdown stub
    

def set_station(newStation):
    __station__ = newStation

def next_station(currentStation):
    set_station()

def prev_station(currentStation):
    set_station()

def get_station():
    return __station__

def set_volume(newVolume):
    __volume__ = newVolume
    

def volume_up(currentVolume):
    set_volume()

def volume_down(currentVolume):
    set_volume()

def get_volume():
    return __volume__

def atc_on():
    # airtrafficPlayer = vlc.MediaPlayer(planeUrl)
    # airtrafficPlayer.play()

def atc_off(player):
    player.stop()
    
def set_atc(player, currentFeed):

def next_atc(currrentAtc):
    set_atc()

def prev_atc(currrentAtc):
    set_atc()

def get_atc():
    return __current_atc__