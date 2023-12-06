import time
from machine import Pin, I2C, PWM, Timer
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

Motor = pico_car()
Motor.Car_Stop()
num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
# Set all led off
pixels.fill(0,0,0)
pixels.show()
# set buzzer pin
BZ = PWM(Pin(22))
BZ.freq(1000)
#initialization ir
Ir = ir()
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#define Timer
tim = Timer()
times_ = 0
def tick(timer):
    global times_
    times_ = times_ + 1
    if times_ > 100:
        times_ = 0
#set timer frequency 20
tim.init(freq = 20,mode = Timer.PERIODIC,callback = tick)


def change_color(color, r, g, b):
    for i in range(num_leds):
        pixels.set_pixel(i,r,g,b)
    pixels.show()
    oled.text('Red', 0, 0)
    oled.show()
    oled.fill(0)

while True:
    #get value
    value = Ir.Getir()
    time.sleep(0.01)
    if value != None:
        print(value)

        #display press
        if value == 3:
            i = 0
            while value == 3:
                value = Ir.Getir()
                Motor.Car_Run(255,255)
                if times_ > 1:
                    times_ = 0
                    if i == 0:
                        pixels.set_pixel(2,150,0,150)
                        pixels.set_pixel(3,150,0,150)
                        i = 1
                    elif i == 1:
                        pixels.set_pixel(2,0,0,0)
                        pixels.set_pixel(3,0,0,0)
                        pixels.set_pixel(1,150,0,150)
                        pixels.set_pixel(4,150,0,150)
                        i = 2
                    elif i == 2:
                        pixels.set_pixel(1,0,0,0)
                        pixels.set_pixel(4,0,0,0)
                        pixels.set_pixel(0,150,0,150)
                        pixels.set_pixel(5,150,0,150)
                        i = 3
                    elif i == 3:
                        pixels.set_pixel(0,0,0,0)
                        pixels.set_pixel(5,0,0,0)
                        pixels.set_pixel(6,150,0,150)
                        pixels.set_pixel(7,150,0,150)
                        i = 4
                    elif i == 4:
                        pixels.set_pixel(0,0,0,0)
                        pixels.set_pixel(5,0,0,0)
                        pixels.set_pixel(6,150,0,150)
                        pixels.set_pixel(7,150,0,150)
                        i = 5
                    elif i == 5:
                        pixels.set_pixel(6,0,0,0)
                        pixels.set_pixel(7,0,0,0)
                        i = 0
                    pixels.show()

            Motor.Car_Stop()
            oled.text('Run', 0, 0)
            oled.show()
            oled.fill(0)


        elif value == 9:
            i = 0
            while value == 9:
                value = Ir.Getir()
                Motor.Car_Left(130,130)
                if times_ > 1:
                    times_ = 0
                    if i == 0:
                        pixels.set_pixel(7,0,0,0)
                        pixels.set_pixel(0,150,0,150)
                        i = i + 1
                    else:
                        pixels.set_pixel(i-1,0,0,0)
                        pixels.set_pixel(i,150,0,150)
                        i = i + 1
                        if i == 8:
                            i = 0
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Left', 0, 0)
            oled.show()
            oled.fill(0)


        elif value == 13:
            i = 8
            while value == 13:
                value = Ir.Getir()
                Motor.Car_Right(130,130)
                if times_ > 1:
                    times_ = 0
                    if i == 8:
                        pixels.set_pixel(7,150,0,150)
                        pixels.set_pixel(0,0,0,0)
                        i = i - 1
                    else:
                        pixels.set_pixel(i-1,150,0,150)
                        pixels.set_pixel(i,0,0,0)
                        i = i - 1
                        if i == 0:
                            i = 8
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Right', 0, 0)
            oled.show()
            oled.fill(0)


        elif value == 11:
            while value == 11:
                value = Ir.Getir()
                BZ.duty_u16(500)
                BZ.freq(624)
            BZ.duty_u16(0)
            oled.text('Buzzer', 0, 0)
            oled.show()
            oled.fill(0)


        elif value == 19:
            i = 0
            while value == 19:
                value = Ir.Getir()
                Motor.Car_Back(255,255)
                if times_ > 1:
                    times_ = 0
                    if i == 0:
                        pixels.set_pixel(6,150,0,150)
                        pixels.set_pixel(7,150,0,150)
                        i = 1
                    elif i == 1:
                        pixels.set_pixel(6,0,0,0)
                        pixels.set_pixel(7,0,0,0)
                        pixels.set_pixel(0,150,0,150)
                        pixels.set_pixel(5,150,0,150)
                        i = 2
                    elif i == 2:
                        pixels.set_pixel(0,0,0,0)
                        pixels.set_pixel(5,0,0,0)
                        pixels.set_pixel(1,150,0,150)
                        pixels.set_pixel(4,150,0,150)
                        i = 3
                    elif i == 3:
                        pixels.set_pixel(1,0,0,0)
                        pixels.set_pixel(4,0,0,0)
                        pixels.set_pixel(2,150,0,150)
                        pixels.set_pixel(3,150,0,150)
                        i = 4
                    elif i == 4:
                        pixels.set_pixel(1,0,0,0)
                        pixels.set_pixel(4,0,0,0)
                        pixels.set_pixel(2,150,0,150)
                        pixels.set_pixel(3,150,0,150)
                        i = 5
                    elif i == 5:
                        pixels.set_pixel(2,0,0,0)
                        pixels.set_pixel(3,0,0,0)
                        i = 0
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Back', 0, 0)
            oled.show()
            oled.fill(0)

        # Car LED Colors
        elif value == 33:
            while value == 33:
                value = Ir.Getir()
            change_color('Red', 255,0,0)

        elif value == 35:
            while value == 35:
                value = Ir.Getir()
            change_color('Green', 0,255,0)

        elif value == 37:
            while value == 37:
                value = Ir.Getir()
            change_color('Blue', 0,0,255)

        elif value == 41:
            while value == 41:
                value = Ir.Getir()
            change_color('Yellow', 255,255,0)

        elif value == 43:
            while value == 43:
                value = Ir.Getir()
            change_color('Cyan',0,255,255)

        elif value == 45:
            while value == 45:
                value = Ir.Getir()
            change_color('Purple',255,0,255)

        elif value == 49:
            while value == 49:
                value = Ir.Getir()
            change_color('White',255,255,255)

        elif value == 51:
            while value == 51:
                value = Ir.Getir()
            change_color('White',100,100,100)

        elif value == 53:
            while value == 53:
                value = Ir.Getir()
            change_color('Black',0,0,0)
            
        value = None


