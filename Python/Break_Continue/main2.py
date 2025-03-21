import time
counter = 0
while counter < 20:
    print(counter)
    time.sleep(0.6)
    counter += 1
    if counter == 7:
        counter +=1
        continue
    if counter == 19:
        break
    # print("This is the end of loop")