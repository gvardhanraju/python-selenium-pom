import inspect
import logging

class Logger:

    def custom_logger(loglevel = logging.DEBUG, logger_name = None):
        if logger_name is None:
            logger_name = inspect.stack()[1][3]
        else:
            logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        fh = logging.FileHandler("C:\\Data\\Python Selenium\\SeleniumCaseStudy\\Registration\\logs\\logfile.log", mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt= "%d-%m-%Y %I:%M:%S %p")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger