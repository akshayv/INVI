from business.deadreckoning.SerialQueueListener import SerialQueueListener

__author__ = 'akshay'


class SerialCommApi:

    @staticmethod
    def onSerialMessage(item):
        #TODO READ SERIAL DATA FROM PORT AND BATCH AND SEND
        SerialQueueListener.queue.put(item)
