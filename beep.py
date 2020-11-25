import time
import RPi.GPIO as pi

def beepDuration(pin=12,duration=1):
    pi.setwarnings(False)
    pi.setmode(pi.BCM)
    pi.setup(pin,pi.OUT)
    pi.output(pin,pi.HIGH)
    time.sleep(duration)
    pi.output(pin,pi.LOW)
    pi.cleanup()
shortBeep = lambda pin=12: beepDuration(pin,.05)
mediumBeep = lambda pin=12: beepDuration(pin,.25)
longBeep = lambda pin=12: beepDuration(pin,.5)
def pulseBeep(pin=12,freq=4,duration=1):
    pi.setwarnings(False)
    pi.setmode(pi.BCM)
    pi.setup(pin,pi.OUT)
    for i in range(int(freq/duration)):
        pi.output(pin,pi.HIGH)
        time.sleep(duration/freq/2)
        pi.output(pin,pi.LOW)
        time.sleep(duration/freq/2)
    pi.output(pin,pi.LOW)
    pi.cleanup()

if __name__=="__main__":
    shortBeep()
        
