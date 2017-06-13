#!/usr/bin/env python

import git, argparse, sys, os.path, yaml 

parser = argparse.ArgumentParser(description = 'A simple utility for managing large numbers of git repos simultaneously')

verbosGroup = parser.add_mutually_exclusive_group()

verbosGroup.add_argument('-v', '--verbose', action = 'count', default = 0, dest = 'verbosity',
        help = 'Increase output verbosity')
verbosGroup.add_argument('-q', '--quiet', action = 'store_true', 
        help = 'Silences all output except for errors')

parser.add_argument('-p', '--pull', action = 'store_true',
        help = 'Pull lastest version of remote repo to local (If local copy exists)')
parser.add_argument('--fork', action = 'store_true', 
        help = 'Fork repos pulled')

# Is overridden by username specified in manifest, is used as fallback
parser.add_argument('-u', '--user', type = str, 
        help = 'Username/identity to use on the server')
parser.add_argument('-f', '--fetch', action = 'store_true', 
        help = '')

# Is overridden by host found in manifest, is used as fallback
parser.add_argument('-s', '--server', type = str, default = 'github.com',
        help = 'Location of the git server (Defaults to github.com)')
parser.add_argument('-m', '--manifest', type = str, default = 'manifest.yml', nargs = '*', dest = 'manifest',
        help = 'Location of the repo manifest(s)')

args = parser.parse_args()


if args.verbosity >= 2:
    print args
