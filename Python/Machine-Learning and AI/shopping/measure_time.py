from datetime import datetime

START = None


def start():
    global START
    START = datetime.now()


def end():
    if not START:
        print("starting point was not set")
    else:
        print(f"Completed with {datetime.now() -  START}")
