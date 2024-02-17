import controls
import time


controls.start_up()

status = "ON"

while(status == "ON"):
    time.sleep(0.5)

controls.shut_down()