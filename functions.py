import logging
# logging.basicConfig(level=logging.INFO,format='%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s')

# file_handler = logging.FileHandler('functions.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)



stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

#
# logger.addHandler()

tom_expenses_monthly = [2500,2330,5080,6000]
sam_expenses_monthly = [3000,5050,4900,2880]

def calculate_total_expenses(expenses):
    # print("hello")
    total = 0
    try:
        for i in range(len(tom_expenses_monthly)):
            # print("Month : ", i+1,"Expenses:", expenses[i])
            logger.info("Month : {} Expenses: {}" .format(i+1,expenses[i]))
            total = total + expenses[i]
        return total
    except IndexError:
        logger.exception("Error")

    # tom_expenses_monthly_total = calculate_total_expenses(tom_expenses_monthly)
logger.info("Tom's total monthly expenses = {}".format(calculate_total_expenses(tom_expenses_monthly)))

sam_expenses_monthly_total = calculate_total_expenses(sam_expenses_monthly)
logger.info("Sam's total monthly expenses = {}".format(sam_expenses_monthly_total))


