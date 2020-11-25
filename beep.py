import time
import RPi.GPIO as pi
import argparse

def beepDuration(pin=12,duration=1):
    pi.setwarnings(False)
    pi.setmode(pi.BCM)
    pi.setup(pin,pi.OUT)
    pi.output(pin,pi.HIGH)
    time.sleep(duration)
    pi.output(pin,pi.LOW)
    pi.cleanup()

def pulseBeep(pin=12,freq=4,duration=1):
    pi.setwarnings(False)
    pi.setmode(pi.BCM)
    pi.setup(pin,pi.OUT)
    for i in range(int(freq*duration/2)):
        pi.output(pin,pi.HIGH)
        time.sleep(1/freq)
        pi.output(pin,pi.LOW)
        time.sleep(1/freq)
    pi.output(pin,pi.LOW)
    pi.cleanup()

def warning(pin):
    pulseBeep(pin,freq=8,duration=1.5)

def confirmed(pin):
    pulseBeep(pin,freq=16,duration=.5)

def brr(pin):
    pulseBeep(pin,freq=50,duration=.5)

def shortBeep(pin):
    beepDuration(pin,.05)

def mediumBeep(pin):
    beepDuration(pin,.25)

def longBeep(pin):
    beepDuration(pin,.5)

    
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Variety of beeps')
    subparsers = parser.add_subparsers(help='Choose a prompt.')
    
    short = subparsers.add_parser('short', help='Make a short beep.')
    short.add_argument('--pin',type=int, help='The GPIO pin number the beeper is on.',default=12)
    short.set_defaults(func=pulseBeep)
    
    warning = subparsers.add_parser('warning', help='Make a warning sound.')
    warning.add_argument('--pin',type=int, help='The GPIO pin number the beeper is on.',default=12)
    warning.set_defaults(func=warning)
    
    args = parser.parse_args()
    args.func(args)
    
