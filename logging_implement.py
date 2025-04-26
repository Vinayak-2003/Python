import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

# least imp / critical
logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")
# most imp / critical

# logging the value of a variable
x = 2
logging.info(f'The value of x is {x}')


# logging exceptions
try:
    1/0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError", exc_info=True)
    logging.exception("test-ZeroDivisionError")
    # logging.exception("ZERRRRRRRRRRRRRRRROOOOOOOOOO")
    

# custom loggers - seprate in each file
logger = logging.getLogger()
logger.info("Test the custom logger")
logger.error("This is an errorr")   #level->error


# logging with exception handling
# try:
#     age = int(input("Enter your age: "))
# except Exception as e:
#     logging.error(e, exc_info=True)
    
    
# User defined errors
class accessDenied(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age<18:
        raise accessDenied("Access Denied!!")
    logging.info(f"A user with age {age} has entered...")
except Exception as e:
    logging.error("Exception occured", exc_info=True)