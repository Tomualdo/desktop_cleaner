#! /usr/bin/env python3

from pathlib import Path
from time import sleep
import logging

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from EventHandler import EventHandler

if __name__ == '__main__':
    logging.basicConfig(filename=Path.home() / 'cleaner.log',level=logging.DEBUG,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    watch_path = Path.home() / 'Desktop'
    # watch_path = Path.home() / 'Documents/test_clean'

    destination_root = Path.home() / 'Desktop/holder'
    # destination_root = Path.home() / 'Documents/test_clean/holder'

    loging_event_handler = LoggingEventHandler()
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.schedule(loging_event_handler, f'{watch_path}', recursive=True)
    observer.start()
    Path.home

    try:
        while True:
            sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

#nssm.exe install "clean_desk" "C:\Users\tkrajcoviech\Documents\desktop_cleaner\.cleaner_env\Scripts\python.exe" "C:\Users\tkrajcoviech\Documents\desktop_cleaner\cleandesk.py"
#SJSK\tkrajcoviech