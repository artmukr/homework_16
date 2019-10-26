# Write a context manager Logger that provides an object for logging data and
# writing it to a file.
# Logger must have log method that takes any value and writes it into a file
# A filename must be specified when calling context manager.
# You must provide a timestamp (just use time.time()) for every new line
# in file.
import time


class Logger:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __repr__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# example:


with Logger("log1.txt", 'w') as logger:
    logger.write(f'{time.time()} {12 + 14}\n')
    logger.write(f'{time.time()} Hello World\n')
    logger.write(f'{time.time()} {True}\n')

# this code must create log1.txt file with the following structure:
# [timestamp] 26
# [timestamp] Hello World
# [timestamp] True
#
# where timestamp is the result of time.time() call
