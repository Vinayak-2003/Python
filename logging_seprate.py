import logging

#create logger for info
info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)

#create logger for error
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)

#create file handler for info logs
info_handler = logging.FileHandler('logging_info.log')
info_handler.setLevel(logging.INFO)

#create file handler for error logs
error_handler = logging.FileHandler('logging_error.log')
error_handler.setLevel(logging.ERROR)

#create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#add the formatter to the handlers
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

#add handlers to loggers
info_logger.addHandler(info_handler)
error_logger.addHandler(error_handler)

# use logger in your code
info_logger.info("This is an info message")
error_logger.error("this is an error message")


# ----------------------------------EXAMPLE---------------------------------

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
try:
    c = a/b
    info_logger.info('a/b: ' + str(c))
except Exception:
    error_logger.error("ZZZZZZZZZEEEEEEEEEEERRRRRRRRRROOOOOOOOOO")
    