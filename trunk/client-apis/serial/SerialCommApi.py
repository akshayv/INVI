from threading import Thread
from time import sleep
from SerialQueueListener import SerialQueueListener
__author__ = 'akshay'


class SerialCommApi:

    @staticmethod
    def onSerialMessage(item):
        #TODO READ SERIAL DATA FROM PORT AND BATCH AND SEND
        SerialQueueListener.queue.put(item)

if __name__ == '__main__':
    api = SerialCommApi()
    for i in range(1):
        t = Thread(target=SerialQueueListener.listen)
        t.daemon = True
        t.start()
    sleep(5)
    for i in range(50):
        if i % 3 == 0:
            SerialQueueListener.queue.put("Hello!")
            print "Put Hello!"
        if i % 3 == 1:
            SerialQueueListener.queue.put("Here!")
            print "Put Here!"
        if i % 3 == 2:
            SerialQueueListener.queue.put("I am!")
            print "Put I am!"

    SerialQueueListener.queue.join()

