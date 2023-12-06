from pico_car import SSD1306_I2C, ultrasonic, ds
from machine import Pin, ADC, I2C
import time

#initialization oled
i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq=100000)
oled = SSD1306_I2C(128,32, i2c)

#Onboard Temperature Sensor on RP2040 chip
sensor_temp = ADC(4) # 16 bits ADC GPIO 26, 27, 28, 29
conversion_factor = 3.3 / (65535) # 2^16 = 0 ~ 65535

# Light Sensors
light_sensor_1 = ADC(26)
light_sensor_2 = ADC(27)

#Bettery
battery = ADC(28)

#Ultrasonic
ultrasonic = ultrasonic()
distance = ultrasonic.Distance_accurate()

while True:
    
    #Get Value Temperature
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print("temperature is %f\n" %(temperature))
    
    print("Distance is %d cm\n" %(distance))
    
    #Get Value Light sensors
    l1 = light_sensor_1.read_u16()
    l2 = light_sensor_2.read_u16()
    print("Light sensor 1 is %d\n" %(l1))
    print("Light sensor 2 is %d\n" %(l2))
    
    print("Bettery is %d\n" %(battery.read_u16()))
    
    #Display on OLED
    oled.text('Temp: ', 0, 0)
    oled.text(str(temperature)[:2], 40, 0)
    
    oled.text('Dist: ', 60, 0)
    oled.text(str(distance), 104, 0)
    oled.text('L1: ', 0, 9)
    oled.text(str(l1), 23, 9)
    oled.text('L2: ', 65, 9)
    oled.text(str(l2), 88, 9)
    oled.text('Bettery: ', 0, 18)
    oled.text(str(battery.read_u16()), 64, 18)
    oled.show()
    oled.fill(0)
    time.sleep(0.5)
