import time
from plyer import notification
while True:
    notification.notify(
    title="Please Drink Water Now",
     message="You drink atleast 10 litres of water a day", #Your message here
    timeout=2  #timeout for the display
    )
    time.sleep(6) #sleep time

