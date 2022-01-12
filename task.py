import json
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


rule_list = ['WRS005','WRS006']

x = open("/home/h/PycharmProjects/book.txt","r")
a = x.read()
# y = []

def demo(myList = [], *args):
    try:
        for i in range(len(myList)):
            b = json.loads(a)
            d = []
            c = b.copy()
            # print(c)
            d = d.append(c)
            print(d)
        return d
    except UnboundLocalError as e:
        logging.error(e)

z = demo(rule_list)
print("test= ",z)


