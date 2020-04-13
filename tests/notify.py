import time 
import notify2 
  
# path to notification window icon 
ICON_PATH = None
  
# initialise the d-bus connection 
notify2.init("Soundkey Notifier") 
  
# create Notification object 
n = notify2.Notification('Soundkey', 'test', icon = ICON_PATH) 
  
# set urgency level 
n.set_urgency(notify2.URGENCY_NORMAL) 
  
# set timeout for a notification 
n.set_timeout(10000) 
    
# show notification on screen 
n.show() 

# short delay between notifications 
time.sleep(15)
