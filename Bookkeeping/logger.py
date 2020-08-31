from datetime import datetime

# логгер по первому заданию
"""
    def func_logger(some_func):
        def actual_logger(*args, **kwargs):

            log_entry = {}

            log_date_time = str(datetime.today())
            log_entry['datetime'] = log_date_time

            log_func_name = some_func.__name__
            log_entry['called function'] = log_func_name

            log_args = str(*args)
            log_entry['args'] = log_args

            log_kwargs = str(*kwargs)
            log_entry['kwargs'] = log_kwargs

            result = some_func(*args, **kwargs)
            log_entry['result'] = result

            with open(file_path, 'a', encoding = 'utf-8') as file:
                file.write(str(log_entry) + '\n')

            return result

        return actual_logger
"""

# окончательный логгер

def func_logger_w_path(file_path):
    def func_logger(some_func):
        def actual_logger(*args, **kwargs):

            log_entry = {}

            log_date_time = str(datetime.today())
            log_entry['datetime'] = log_date_time

            log_func_name = some_func.__name__
            log_entry['called function'] = log_func_name

            log_args = str(*args)
            log_entry['args'] = log_args

            log_kwargs = str(*kwargs)
            log_entry['kwargs'] = log_kwargs

            result = some_func(*args, **kwargs)
            log_entry['result'] = result

            with open(file_path, 'a', encoding = 'utf-8') as file:
                file.write(str(log_entry) + '\n')

            return result

        return actual_logger
    return func_logger