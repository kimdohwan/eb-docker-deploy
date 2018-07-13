#!/usr/bin/env python
import argparse
import sys

import os
import subprocess

MODES = ['base', 'local', 'dev', 'production']


def mode_function(mode):
    if mode in MODES:
        cur_module = sys.modules[__name__]
        getattr(cur_module, f'build_{mode}')()
    else:
        raise ValueError(f'{MODES}에 속하는 모드만 가능합니다')


def build_base():
    try:
        # pipenv lock으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
        # doker build
        subprocess.call('docker build -t eb-docker:base -f Dockerfile.base .', shell=True)
    finally:
        # 끝난 후 reqirements.txt 삭제
        os.remove('requirements.txt')


def build_local():
    try:
        # pipenv lock으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
        # doker build
        subprocess.call('docker build -t eb-docker:local -f Dockerfile.local .', shell=True)
    finally:
        # 끝난 후 reqirements.txt 삭제
        os.remove('requirements.txt')


def build_dev():
    try:
        # pipenv lock으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements --dev > requirements.txt', shell=True)
        # doker build
        subprocess.call('docker build -t eb-docker:dev -f Dockerfile.dev .', shell=True)
    finally:
        # 끝난 후 reqirements.txt 삭제
        os.remove('requirements.txt')


def build_production():
    try:
        # pipenv lock으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
        # doker build
        subprocess.call('docker build -t eb-docker:production -f Dockerfile.production .', shell=True)
    finally:
        # 끝난 후 reqirements.txt 삭제
        os.remove('requirements.txt')


parser = argparse.ArgumentParser()
parser.add_argument(
    "-m", "--mode",
    help=f'select docker mode {MODES}'
)
args = parser.parse_args()

if args.mode:
    mode = args.mode.strip().lower()
else:
    while True:
        for index, mode_name in enumerate(MODES, start=1):
            print(f'{index}. {mode_name}')
        selected_mode = input('Choice: ')
        try:
            mode_index = int(selected_mode) - 1
            mode = MODES[mode_index]
            break
        except IndexError:
            print(f'1~{len(MODES)}번을 입력하세요')

# __name__ == '__main__' 은 python build.py를 실행할 때를 의미
# 만약 다른 곳에서 이 파일을 import 시킬 경우는 실행하지 않는다는 의미
if __name__ == '__main__':
    mode_function(mode)

# if args.mode:
#     mode = args.mode.strip().lower()
# else:
#     while True:
#         print('Select mode')
#         print('1. base')
#         print('2. local')
#         selected_mode = input('Choice: ')
#
#         try:
#             mode_index = int(selected_mode) - 1
#             mode = MODES[mode_index]
#             break
#         except IndexError:
#             print('1,2번을 입력하세요')
# if mode == 'base':
#     build_base()
# elif mode == 'local':
#     raise NotImplementedError('build_local not implemented')
# else:
#     raise ValueError(f'{MODES}에 속하는 모드만 가능합니다')


# if args.m == 'local':
#     mode = 'local'
# elif args.m == 'base':
#     mode = 'base'
# else:
#     while 1:
#         mode_num = input('1. local\n2. base\n3. exit\n')
#         if mode_num == '1':
#             mode = 'local'
#             break
#         elif mode_num == '2':
#             mode = 'base'
#             break
#         else:
#             print('plz select mode')
#             break
# build_mode()
