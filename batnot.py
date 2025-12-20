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

# Initialize notification
notify2.init("batnot")


def notify(percent, secs_left):

  hrs, mins, secs = expand_secs(secs_left)

  # Display notification on screen
  global n
  n = notify2.Notification(f"Low Battery",
                           f"You have {percent}% battery left \nEstimated time left {hrs}hrs {mins}mins {secs}secs"
                           )
  n.show()

  system("mpg123 lowbat.mp3")

def update_notification(notification, percent, secs_left):
  # Update notification
  """The notify function must always be called at least once before this function"""

  hrs, mins, secs = expand_secs(secs_left)

  #Update notification
  notification.update("Low battery",
                      f"You have {percent}% battery left \nEstimated time left {hrs}hrs {mins}mins {secs}secs"
                      )
  notification.show()


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

      while True:
        sleep_time = sleeptime(percent, secsleft)
        sleep(sleep_time)

        percent, secsleft, power_plugged = sensors_battery()
        percent = int(percent)

        if percent <= 30 and power_plugged == False:
          update_notification(n, percent, secsleft)

        else:
          break

    sleep_time = sleeptime(percent, secsleft)
    sleep(sleep_time)

main()

