# Import libraries
import RPi.GPIO as GPIO
import time


# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)


# Set pin as an output, and define as servo as PWM pin
# Servo 1
GPIO.setup(8,GPIO.OUT)
servo1 = GPIO.PWM(8,50)

# Servo 2
GPIO.setup(10,GPIO.OUT)
servo2 = GPIO.PWM(10,50)

# Servo 3
GPIO.setup(12,GPIO.OUT)
servo3 = GPIO.PWM(12,50)


# Start PWM running, with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)
servo3.start(0)


# Start app
try:
    while True:
        num_servo = int(input('Pls write num of servo which u want move: '))

        if num_servo == 1:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo1 angle between 0 & 180: '))
            servo1.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)


        elif num_servo == 2:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo2 angle between 0 & 180: '))
            servo2.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo2.ChangeDutyCycle(0)


        elif num_servo == 3:
            #Ask user for angle and turn servo to it
            angle = float(input('Enter for servo3 angle between 0 & 180: '))
            servo3.ChangeDutyCycle(2+(angle/18))
            time.sleep(0.5)
            servo3.ChangeDutyCycle(0)



finally:
    #Clean things up at the end
    servo1.stop()
    servo2.stop()
    servo3.stop()
    GPIO.cleanup()
    print("Servo Stop")
