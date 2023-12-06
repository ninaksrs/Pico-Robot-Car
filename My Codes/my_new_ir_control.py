import time
from machine import Pin, I2C
from pico_car import SSD1306_I2C, ir

# Initialization ir
Ir = ir()

# Initialization oled
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

# Mapping of values to their corresponding text
key_to_text = {
    1: 'Power',
    3: 'Up',
    5: 'Light',
    9: 'Left',
    11: 'Sound',
    13: 'Right',
    17: 'Turn Left',
    19: 'Down',
    21: 'Turn Right',
    25: '+',
    27: '0',
    29: '-',
    33: '1',
    35: '2',
    37: '3',
    41: '4',
    43: '5',
    45: '6',
    49: '7',
    51: '8',
    53: '9'
}

while True:
    value = Ir.Getir()
    time.sleep(0.01)
    if value in key_to_text:
        while value == Ir.Getir():
            pass  # Wait until the value changes
        print(f"IR Key: {value}, Remote Button: {key_to_text[value]}")
        oled.text(f'Pess: {key_to_text[value]}', 0, 0)
        oled.show()
        oled.fill(0)