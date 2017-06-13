#!/usr/bin/env python

import git, argparse, sys, os.path, yaml 

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--verbose', action = 'count', default = 0, 
        help = 'Increase output verbosity')
parser.add_argument('-p', '--pull', 
        help = 'Pull lastest version of remote repo to local (If local copy exists)')
parser.add_argument('--fork', 
        help = 'Fork repos pulled')
parser.add_argument('-u', '--user', type = str, 
        help = 'Username/identity to use on the server')
parser.add_argument('-f', '--fetch', 
        help = '')
parser.add_argument('-c', '--clone', 
        help = 'Specifies whether to clone missing repos') 
parser.add_argument('-s', '--server', type = str, default = 'github.com',
        help = 'Location of the git server (Defaults to github.com)')
parser.add_argument('-m', '--manifest', type = str, default = 'manifest.yml',
        help = 'Location of the repo manifest')

args = parser.parse_args()

def clone():
    print 'test' 
