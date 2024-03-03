import threading
import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    print(f"Square root of {number} is: {result}")

number = float(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))

thread = threading.Thread(target=delayed_square_root, args=(number, delay))
thread.start()

thread.join()
