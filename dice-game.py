#!/usr/bin/env python3

from gpiozero import LED, Button
from time import sleep
import random

# Set up LEDs
leds = [LED(i) for i in range(7)]

# Set up button
button = Button(14)

# Define LED patterns for dice numbers
dice_patterns = [
    [0, 0, 0, 1, 0, 0, 0],  # 1
    [1, 0, 0, 0, 0, 0, 1],  # 2
    [1, 0, 0, 1, 0, 0, 1],  # 3
    [1, 1, 0, 0, 0, 1, 1],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 1, 0, 1, 1, 1]   # 6
]

def roll_dice():
    # Simulate dice rolling animation
    for _ in range(10):
        for pattern in dice_patterns:
            display_pattern(pattern)
            sleep(0.1)
    
    # Generate random number and display result
    result = random.randint(1, 6)
    display_pattern(dice_patterns[result - 1])
    return result

def display_pattern(pattern):
    for led, value in zip(leds, pattern):
        if value:
            led.on()
        else:
            led.off()

print("Press the button to roll the dice!")

while True:
    button.wait_for_press()
    result = roll_dice()
    print(f"You rolled a {result}")
    sleep(0.5)  # Debounce delay


