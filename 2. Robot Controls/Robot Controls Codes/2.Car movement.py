from pico_car import pico_car, SSD1306_I2C
from machine import Pin, I2C
import time

Motor = pico_car()

i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq = 100000)
oled = SSD1306_I2C(128, 32, i2c)

def show_on_display(text, x, y):
    print(f"{text}\n")
    oled.text(text, x, y)
    oled.show()
    oled.fill(0)
    
#Car forward，parameter(Left motor speed，Right motor speed),speed 0-255
oled.text("Car Forward", 0, 0)
oled.show()
show_on_display("Motor.Car_Run(255,255)", 0, 9)
Motor.Car_Run(255,255)
time.sleep(1)
#Car back
oled.text("Car Backward", 0, 0)
oled.show()
show_on_display("Motor.Car_Back(255,255)", 0, 9)
Motor.Car_Back(255,255)
time.sleep(1)
#left
oled.text("Car Left", 0, 0)
oled.show()
show_on_display("Motor.Car_Run(0,255)", 0, 9)
Motor.Car_Run(0,255)
time.sleep(1)
#right
oled.text("Car Right", 0, 0)
oled.show()
show_on_display("Motor.Car_Run(255,0)", 0, 9)
Motor.Car_Run(255,0)
time.sleep(1)
#Turn left
oled.text("Car Turn Left", 0, 0)
oled.show()
show_on_display("Motor.Car_Left(255,255)", 0, 9)
Motor.Car_Left(255,255)
time.sleep(1)
#Turn right
oled.text("Car Turn Right", 0, 0)
oled.show()
show_on_display("Motor.Car_Right(255,255)", 0, 9)
Motor.Car_Right(255,255)
time.sleep(1)
#Car stop
oled.text("Car Stop", 0, 0)
oled.show()
show_on_display("Motor.Car_Stop()", 0, 9)
Motor.Car_Stop()