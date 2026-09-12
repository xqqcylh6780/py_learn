# -*- coding: utf-8 -*-
"""
13 argparse 设计 CLI
==================

CLI 应有清晰帮助、稳定错误码、子命令，并把解析入口设计成可测试的 main(argv)。

解析参数、执行业务和输出结果应分层，这样测试可以传入参数列表而不修改全局 `sys.argv`。
参数错误由解析器处理，业务失败则由入口边界转换为稳定消息和退出码。
命令名和选项一旦供脚本调用就是接口，重命名时也要考虑兼容性。
"""

import argparse

def make_parser():
    p=argparse.ArgumentParser(prog='demo')
    sub=p.add_subparsers(dest='command', required=True)
    hello=sub.add_parser('hello')
    hello.add_argument('name')
    hello.add_argument('--upper', action='store_true')
    return p

def main(argv=None):
    args=make_parser().parse_args(argv)
    text=f'hello {args.name}'
    print(text.upper() if args.upper else text)
    return 0

print('模拟运行:')
print('exit =', main(['hello','Alice','--upper']))
