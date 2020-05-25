import time
from plyer import notification
while True:
    notification.notify(
    title="Please Drink Water Now",
    message="You drink atleast 10 litres of water a day",
    timeout=2
    )
    time.sleep(6)

