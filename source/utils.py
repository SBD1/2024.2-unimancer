DEBUG = True

def debug(*args):
    if DEBUG:
        print("DEBUG: ", *args)