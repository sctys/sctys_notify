import time
import os
import logging


def retry(func, *params, checker, num_retry, sleep_time, logger):
    count = 0
    run_success = False
    while count < num_retry and not run_success:
        response = func(*params)
        if not checker(response)['status']:
            logger.error('Fail attempt {} for function {}: {}'.format(count + 1, func.__name__,
                                                                      checker(response)['message']))
            time.sleep(sleep_time)
            count += 1
        else:
            run_success = True
    return response


def set_logger(logger_path, logger_file_name, logger_level, logger_name):
    logger_file = os.path.join(logger_path, logger_file_name)
    logging.basicConfig(level=getattr(logging, logger_level),
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(filename=logger_file), logging.StreamHandler()])
    logger = logging.getLogger(logger_name)
    return logger

