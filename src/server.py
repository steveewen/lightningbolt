__author__ = 'manishankargoswami'

import os
import sys
import inspect
import argparse
from config.serverconfig import config

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from src.serverlib import run_in_cp_tree
from src.engine.controller import app

parser = argparse.ArgumentParser(description="Lightningbolt Micro service")
parser.add_argument('--pidfile', help='process id file', type=str)
args = parser.parse_args()

run_in_cp_tree(app, config['server.socket_host'], config['server.port'], args.pidfile)
