#!/usr/bin/env python
import os
from multiprocessing import Process

from download_ckan import download as ckan
import portals

ROOT_DIR = 'portals'

def create():
    processes = {}

    for portal in portals.ckan:
        args = ("http://" + portal, os.path.join(ROOT_DIR, 'ckan', portal))
        processes[('ckan', portal)] = Process(target = ckan, args = args)

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
