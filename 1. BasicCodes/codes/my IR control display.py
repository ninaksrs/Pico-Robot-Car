
import time
from machine import Pin, I2C
from pico_car import SSD1306_I2C, ir

# Initialization ir
Ir = ir()

# Initialization oled
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

# Mapping of values to their corresponding text
value_to_text = {
    0: 'Power',
    1: 'Up',
    2: 'Light',
    4: 'Left',
    5: 'Sound',
    6: 'Right',
    8: 'Turn Left',
    9: 'Down',
    10: 'Turn Right',
    12: '+',
    13: '0',
    14: '-',
    16: '1',
    17: '2',
    18: '3',
    20: '4',
    21: '5',
    22: '6',
    24: '7',
    25: '8',
    26: '9'
}

while True:
    # Get value
    value = Ir.Getir()
    time.sleep(0.01)
    if value is not None:
        print(value)
        # Display press
        if value in value_to_text:
            while value in value_to_text:
                value = Ir.Getir()
            oled.text(f'Press:{value_to_text[value]}', 0, 0)
            oled.show()
            oled.fill(0)