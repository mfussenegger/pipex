#!/usr/bin/env python3

import sys
import os
import venv
from subprocess import run
from hashlib import sha1


def parse_pkgs(line):
    line = line[len('# pipex'):]
    return [x.strip() for x in line.split('--pkg ') if x.strip()]


def extract_packages(path):
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            if line.startswith('# pipex'):
                yield from parse_pkgs(line)


def main():
    _, path = sys.argv
    packages = list(extract_packages(os.path.abspath(path)))
    fingerprint = sha1('|'.join(packages).encode('utf-8')).hexdigest()
    target = os.path.join(os.path.expanduser(f'~/.cache/pipex/{fingerprint}'))
    os.makedirs(target, exist_ok=True)
    venv.create(target, with_pip=True)
    vpython = os.path.join(target, 'bin', 'python')
    pip_install = [vpython, '-m', 'pip', 'install', '--upgrade']
    run(pip_install + packages)
    run([vpython, path])


if __name__ == "__main__":
    main()
