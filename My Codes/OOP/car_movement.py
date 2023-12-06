from pico_car import pico_car, SSD1306_I2C
from machine import Pin, I2C
import time

class CarMovement:
    def __init__(self):
        self.Motor = pico_car()
        self.i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq = 100000)
        self.oled = SSD1306_I2C(128, 32, self.i2c)

    def show_on_display(self, text, x, y):
        print(f"{text}\n")
        self.oled.text(text, x, y)
        self.oled.show()
        self.oled.fill(0)

    def car_forward(self, sec):
        self.show_on_display("Car Forward", 0, 0)
        self.Motor.Car_Run(255,255)
        time.sleep(sec)

    def car_backward(self, sec):
        self.show_on_display("Car Backward", 0, 0)
        self.Motor.Car_Back(255,255)
        time.sleep(sec)

    def car_left(self, sec):
        self.show_on_display("Car Left", 0, 0)
        self.Motor.Car_Run(0,255)
        time.sleep(sec)

    def car_right(self, sec):
        self.show_on_display("Car Right", 0, 0)
        self.Motor.Car_Run(255,0)
        time.sleep(sec)

    def car_turn_left(self, sec):
        self.show_on_display("Car Turn Left", 0, 0)
        self.Motor.Car_Left(255,255)
        time.sleep(sec)

    def car_turn_right(self, sec):
        self.show_on_display("Car Turn Right", 0, 0)
        self.Motor.Car_Right(255,255)
        time.sleep(sec)

    def car_stop(self, sec = None):
        self.show_on_display("Car Stop", 0, 0)
        self.Motor.Car_Stop()
        time.sleep(sec)
   