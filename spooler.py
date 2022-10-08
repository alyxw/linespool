from flask import Flask
from flask import request
import threading
import time
from datetime import datetime

app = Flask(__name__)
queue = []


def processQueue():
    while True:
        now = datetime.now()
        timeprefix = "[" + now.strftime("%Y-%m-%d %H:%M:%S.%f") + "] "
        if (len(queue) == 0):
            time.sleep(1)
            now = datetime.now()
            timeprefix = "[" + now.strftime("%Y-%m-%d %H:%M:%S.%f") + "] "
            print(timeprefix + "no messages, checking in 1 seconds")
        else:
            with open('/dev/usb/lp0', 'w') as printer:
                printer.write(timeprefix + queue[0] + '\n')
                print(timeprefix + queue[0])
            queue.pop(0)


@app.route('/msg', methods=['POST'])
def postmsg():
    queue.append(request.form.get('message'))
    return "posted!\n"


def server():
    app.run(host='0.0.0.0')


threading.Thread(target=processQueue).start()
threading.Thread(target=server).start()
