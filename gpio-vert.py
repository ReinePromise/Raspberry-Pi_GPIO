import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
 
try:
        GPIO.output(40,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(40,GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:    # 异常处理，如果Ctrl+C退出程序
    GPIO.output(40,GPIO.LOW)
    GPIO.cleanup()
