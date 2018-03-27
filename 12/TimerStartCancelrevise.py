import threading

count = 0

def on_timer():
    global count
    count += 1
    print(count)
    timer = threading.Timer(1, on_timer)
    
    
    
    if count < 10:
        #timer = threading.Timer(1, on_timer)
        #여기에서 선언을 하나 위에서 선언을 하나 동일하게 작동한다.
        timer.start()    
    
print("Starting timer...")
on_timer()

