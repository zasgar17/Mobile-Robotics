#!/usr/bin/env python3
import math
import time
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import SpeedPercent
# ============================================================
# ROBOT PARAMETERS
# ============================================================
# Replace these with YOUR experimentally measured values
WHEEL_RADIUS = 2.8       # cm
WHEEL_DISTANCE = 12.0    # cm
# Motors
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
# ============================================================
# FUNCTION 1: DRIVE STRAIGHT
# ============================================================
def drive_straight(distance_cm, speed=30):
    # Wheel circumference
    circumference = 2 * math.pi * WHEEL_RADIUS
    # Number of wheel rotations needed
    rotations = distance_cm / circumference
    # Convert rotations to degrees
    degrees = rotations * 360
    # Move both motors the same amount
    left_motor.on_for_degrees(
        SpeedPercent(speed),
        degrees,
        block=False
    )
    right_motor.on_for_degrees(
        SpeedPercent(speed),
        degrees
    )
# ============================================================
# FUNCTION 2: TURN
# ============================================================
def turn(angle, speed=20):
    distance = (
        math.pi *
        WHEEL_DISTANCE *
        abs(angle) /
        360
    )
    # Convert distance to wheel rotations
    rotations = distance / (
        2 * math.pi * WHEEL_RADIUS
    )
    # Convert rotations to degrees
    degrees = rotations * 360
    if angle > 0:
        # Turn LEFT
        left_motor.on_for_degrees(
            SpeedPercent(-speed),
            degrees,
            block=False
        )
        right_motor.on_for_degrees(
            SpeedPercent(speed),
            degrees
        )
    else:
        # Turn RIGHT
        left_motor.on_for_degrees(
            SpeedPercent(speed),
            degrees,
            block=False
        )
        right_motor.on_for_degrees(
            SpeedPercent(-speed),
            degrees
        )
# ============================================================
# TEST
# ============================================================
print("Starting in 3 seconds...")
time.sleep(2)
# ============================================================
# 50 cm SQUARE
# ============================================================
drive_straight(50)
turn(89)

drive_straight(50)
turn(89)

drive_straight(50)
turn(89)

drive_straight(50)
turn(89)
# Stop motors
left_motor.off()
right_motor.off()

print("Square completed!")