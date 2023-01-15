import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

PIN = 31

GPIO.setup(PIN,GPIO.IN)

count = 0

bit_list = []

while True:
  count = 0
  while GPIO.input(PIN):
    count += 1
    if count > 100000:
      count = 0
      if bit_list:
        print(bit_list)
        bit_list = []
  bit_list.append(count)
  count = 0
  while not GPIO.input(PIN):
    count += 1
  bit_list.append(count)
