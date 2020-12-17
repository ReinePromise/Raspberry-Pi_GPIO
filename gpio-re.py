import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
 
try:
        GPIO.output(12,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(12,GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:    # 异常处理，如果Ctrl+C退出程序
    GPIO.output(12,GPIO.LOW)
    GPIO.cleanup()
