# print a list
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
try:
    course = ['History','Math','Physics','Science']
    logger.debug("List = {} ".format(course))
    logger.debug("length of list = {}".format(len(course)))
    logger.debug("Value of element in list = {}".format(course[1]))
    logger.debug("Fetch last element of list = {}".format(course[-1]))
    logger.debug("first 2 elements of list = {}".format(course[0:2]))
    # course.append('Art')
    # logger.debug("Add element at the end of the list = {}".format(course))
    # course.insert(0,'Art')
    # logger.debug("Add element at the beginning element of the list = {}".format(course))
#     Add elements of any other list
    course_2 = ['Art','Computers']
#     want to add complete 2nd list to 1st list inn beginning and the end
#     course.insert(0,course_2)
#     logger.debug("First list with 2nd list at the beggining = {}".format(course))
#     course.append(course_2)
#     logger.debug("First list with 2nd list at the end = {}".format(course))
#     course.extend(course_2)
#     logger.debug("Add elements of list 2nd to list 1st = {}".format(course))

# remove element from list
#     first method
#     course.remove('Math')
#     logger.debug("List after removing of one element = {}".format(course))

#     Second method
#     popped_element = course.pop() # pop method removed last element from list
#     logger.debug("Popped element from list = {}".format(popped_element))
#     logger.debug("List after using pop method = {}".format(course))

# reverse the list
#     course.reverse()
#     logger.debug("Reversed list = {}".format(course))

# sort the list
#     course.sort() # in ascending order
#     logger.debug("Print list in ascending order = {}".format(course))
#     course.sort(reverse=True) # descending order
#     logger.debug("Print list in descending order = {}".format(course))
    nums =[1,6,2,9,0,1]
    # nums.sort()
    # logger.debug("Ascending order list = {}".format(nums))
#     Descending order
#     nums.sort(reverse=True)
#     logger.debug("Descending order list = {}".format(nums))

#     sorting list without altering the original list
    sorted_list = sorted(nums)
    logger.debug("Sorted list without altering original list ={}".format(sorted_list))

#     index of the element
    logger.debug("Index value of element in the list = {}".format(course.index('Math')))
    logger.debug("Check whether asked element present in the list = {}".format("art" in course))

# want to print index and value same time while iterating
    for index,items in enumerate(course):
        logger.debug("Index : {} , Value : {} ".format(index,items))

# want to convert list to string comma separated
    course_str = ', '.join(course)
    logger.debug("List conversion to comma separated string : {}".format(course_str))

# converting string to list
    l = list(course_str.split(','))
    logger.debug("string to List = {}".format(l))

# Tuples are immutable
    tuple1= ('History','Math','physics','science')
    print(tuple1)
    tuple2 = tuple1
    print(tuple2)
    # tuple1[0] = 'Art'
    # print(tuple1)

# Sets are unordered (order changes every execution) and have no duplicates
    sets1 = {'History','Math','physics','science'}
    sets2={'History','Math','art','science'}
    logger.debug(" Sets = {}".format(sets1))

#     Check what is common between 2 sets
    c = sets1.intersection(sets2)
    logger.debug("Common elements in both the sets = {}".format(c))
    # check which elements are different in both the sets
    d = sets1.difference(sets2)
    logger.debug("Different elements in both the sets = {}".format(d))
#     combine 2 sets
    x = sets1.union(sets2)
    logger.debug("combined elements of both the sets = {}".format(x))

except IndexError as e:
    logger.exception(e)

except ValueError as e:
    logger.exception(e)

except TypeError as e:
    logger.exception(e)

except Exception as e:
    logger.exception(e)