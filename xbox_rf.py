import RPi.GPIO as GPIO
import time

data_pin = 5  # data line (pin 6 on the module)
clock_pin = 6  # clock line (pin 7 on module)

cmdlist = {
    "led_cmd": "0010000100",
    "anim_cmd": "0010000101",
    "green_ul": "0010100001",
    "green_ur": "0010100010",
    "green_dr": "0010101000",
    "green_dl": "0010100100",
    "red_ul": "0010110001",
    "red_ur": "0010110010",
    "red_dr": "0010111000",
    "red_dl": "0010110100",
    "ctl_sync": "0000000100",
    "ctl_shutdown": "0000001001"
}

cmdlist_reversed = {v: k for k, v in cmdlist.items()}

GPIO.setmode(GPIO.BCM)
GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)

def send_data(command, delay=0):
    GPIO.output(data_pin, 0)

    for bit in command:
        while GPIO.input(clock_pin) == 1:
            pass

        GPIO.output(data_pin, int(bit))

        while GPIO.input(clock_pin) == 0:
            pass

    GPIO.output(data_pin, 1)
    GPIO.setup(data_pin, GPIO.IN)
    time.sleep(delay / 1000.0)

def init():
    GPIO.setup(data_pin, GPIO.IN)
    GPIO.setup(clock_pin, GPIO.IN)
    send_data(cmdlist["led_cmd"])
    time.sleep(0.05)

def boot_animation():
    send_data(cmdlist["anim_cmd"])
    time.sleep(7)

def send_command(name, delay=0):
    send_data(cmdlist[name], delay)

def delay(ms):
    time.sleep(ms / 1000.0)

def bruteforce(begin=0, end=255, ignore_known=True):
    while begin <= end:
        binstr = "00" + format(begin, '08b')[5:]
        if binstr not in cmdlist.values() or not ignore_known:
            send_data(binstr)
            print(binstr + " : " + str(begin))
        else:
            print(binstr + " : " + cmdlist_reversed[binstr])
        time.sleep(1)
        begin += 1

if __name__ == "__main__":
    try:
        init()
        boot_animation()
        # You can add more function calls or modify as needed
    finally:
        GPIO.cleanup()
