import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
# Dictionary is mainly key value pair
try:
    student = {'name': 'John','age': 25, 'courses': ['math','computers']}
    logger.info("Dictionary created = {}".format(student))
    logger.info("Print value of key courses : {}".format(student['courses']))
#     if want to pass the key which is not present and provide none value or customise value
    logger.info("Key not present in dictionary and displaying custom value : {}".format(student.get('phone','Not found')))
#     add a key to dictionary with value
    student['phone'] = 2567989
    logger.info("Update dictionary after adding key : {}".format(student))
#     update values of multiple keys
    student.update({'name': 'Sam','age': 30})
    logger.info("Updated dictionary after updating multiple keys value : {}".format(student))

#     delete key from dictionary
#     first method using del
#     del student['phone']
#     logger.info("student dictionary after deleting phone key : {}".format(student))
#     Second method through pop
#     popped_key = student.pop('age')
#     logger.info("popped key's value from dictionary = {}".format(popped_key))
#     logger.info("Dictionary after popping key = {}".format(student))

#     length of dictionary or number of keys
    logger.info("Length of Dictionary/number of keys= {}".format(len(student)))
    logger.info(" Keys of student Dictionary = {}".format(student.keys()))
    logger.info(" Values of student Dictionary = {}".format(student.values()))
#     print key and values
    logger.info("key value pair = {}".format(student.items()))
#     to iterate
    for k,v in student.items():
        logger.info("Keys: {} --> Values: {}".format(k,v))


except KeyError as e:
    logger.exception(e)

except Exception as e:
    logger.exception(e)