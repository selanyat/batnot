#!./batnot/bin/python

from time import sleep
from psutil import sensors_battery
import notify2
from os import system

def expand_secs(secs_left):
  # Convert seconds into hours minutes and seconds
  hrs = secs_left // 3600
  secs_left -= hrs * 3600
  mins = secs_left //60
  secs_left -= mins*60

  return (hrs, mins, secs_left)



def notify(percent, secs_left):

  hrs, mins, secs = expand_secs(secs_left)

  # Display notification on screen
  notify2.init("batnot")
  n = notify2.Notification(f"Low Battery",
                           f"You have {percent}% battery left \nEstimated time left {hrs}hrs {mins}mins {secs}secs"
                           )
  n.show()

  system("mpg123 lowbat.mp3")



def sleeptime(percent, secs_left):
  sleep_time = (secs_left // 10) * (percent / 100)

  return int(sleep_time) + 1


def main():

  while True:
    percent, secsleft, power_plugged = sensors_battery()
    percent = int(percent)


    if percent <= 30 and power_plugged == False:
      notify(percent, secsleft)

    sleep_time = sleeptime(percent, secsleft)
    sleep(sleep_time)

main()

