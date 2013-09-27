#!/usr/bin/env python2
from download_ckan import main as ckan
from download_socrata import main as socrata

ROOT_DIR = 'portals'

def create_ckan():
    processes = {}

    for portal in portals.ckan:
        args = ("http://" + portal, os.path.join(ROOT_DIR, 'ckan', portal))
        processes[('ckan', portal)] = Process(target = download, args = args)

    return processes

def start(processes):
    'Start all of the processes.'
    for process in processes.values():
        process.start()

def join(processes):
    'Wait for all of the processes to end.'
    for process in processes.values():
        process.join()

def kill(processes):
    'Kill all of the processes.'
    for process in processes.values():
        process.terminate()

def main():
    import signal
    import sys

    p = create_ckan()

    def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        kill(p)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    start(p)
    join(p)

