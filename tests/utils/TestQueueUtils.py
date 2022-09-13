import threading
import time
from unittest import TestCase

from utils.LogUtils import LogUtils
from utils.QueueUtils import LoopQueue, PipeQueue

logger = LogUtils(__name__).getLogger()


def producer(name, queue, count, interval):
    """
    生产者
    :param name: 生产者名称
    :param queue: 产品队列
    :param count: 要产出的数量,负数为一直生产
    :param interval: 每次生产的间隔时间
    :return:
    """
    i = 0
    while count != 0:
        i += 1
        count -= 1
        queue.put(i)
        logger.info(f"Producer({name}) put({i}) {i} at {time.time()}")
        time.sleep(interval)


def consumer(name, queue, count, interval=1):
    """
    消费者
    :param name: 消费者名称
    :param queue: 产品队列
    :param count: 要消费的数量,负数为一直消费
    :param interval: 每次消费的间隔时间
    :return:
    """
    i = 0
    while count != 0:
        i += 1
        count -= 1
        start_time = time.time()
        item = queue.get()
        logger.info(f"Consumer({name}) get({i}) {item} wait({time.time() - start_time})")
        time.sleep(interval)


def test_producer_consumer(queue, producer_count, consumer_count):
    producers = []
    consumers = []

    for i in range(producer_count):
        producers.append(threading.Thread(target=producer, args=(f"P{i}", queue, -1, 0.2,)))
    for i in range(consumer_count):
        consumers.append(threading.Thread(target=consumer, args=(f"C{i}", queue, -1, 0.2)))

    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    for p in producers:
        p.join()
    for c in consumers:
        c.join()


class TestLoopQueue(TestCase):
    producer_count = 1
    consumer_count = 10

    @classmethod
    def setUpClass(cls) -> None:
        cls.lq = LoopQueue(5)
        cls.pq = PipeQueue(5)

    # def test_get(self):
    #     for i in range(100):
    #         self.lq.put(i)
    #
    #     def t1():
    #         while not self.lq.empty():
    #             print(f"{threading.currentThread().getName()}:{self.lq.get()}")
    #
    #     threading.Thread(target=t1).start()
    #     threading.Thread(target=t1).start()
    #     threading.Thread(target=t1).start()
    #     threading.Thread(target=t1).start()

    def test_loop_queue(self):
        test_producer_consumer(self.lq, self.producer_count, self.consumer_count)

    def test_pipe_queue(self):
        test_producer_consumer(self.pq, self.producer_count, self.consumer_count)
