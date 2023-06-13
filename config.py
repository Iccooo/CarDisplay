
import RPi.GPIO as GPIO
import time
from smbus import SMBus
import spidev
import ctypes

# Pin definition
RST_PIN         = 27
DC_PIN          = 25
CS_PIN          = 8

Device_SPI = 1
Device_I2C = 0

if(Device_SPI == 1):
    Device = Device_SPI
    spi = spidev.SpiDev(0, 0)
else :
    Device = Device_I2C
    address = 0x3c
    bus = SMBus(1)

def delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_writebyte(data):
    spi.writebytes([data[0]])

def i2c_writebyte(reg, value):
    bus.write_byte_data(address, reg, value)
   
def module_init():
    #print("module_init")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RST_PIN, GPIO.OUT)
    GPIO.setup(DC_PIN, GPIO.OUT)
    GPIO.setup(CS_PIN, GPIO.OUT)  
    GPIO.output(RST_PIN, 0)
    if(Device == Device_SPI):
        spi.max_speed_hz = 10000000
        spi.mode = 0b11  
    GPIO.output(CS_PIN, 0)
    GPIO.output(DC_PIN, 0)
    return 0

def module_exit():
    if(Device == Device_SPI):
        spi.close()
    else :
        bus.close()
    GPIO.output(RST_PIN, 0)
    GPIO.output(DC_PIN, 0)
