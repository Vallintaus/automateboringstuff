#! python3
import time

# Display instructions
print("Press ENTER to begin. Afterwards, press ENTER or 'click' the stopwatch. Press Ctrl-C to quit.")
input() #Press enter to begin
print('Started')
startTime = time.time()
lastTime = startTime  # get the first laps starttime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap #{lapNum}: {totalTime} ({lapTime})")
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C
    print('\nDone')