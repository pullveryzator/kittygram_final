import os


def debug_flag():
    debug_flag = os.getenv('DEBUG')
    if debug_flag == 'True':
        return True
    else:
        return False
