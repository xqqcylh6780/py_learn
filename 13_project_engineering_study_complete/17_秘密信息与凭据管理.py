# -*- coding: utf-8 -*-
"""
17 秘密信息与凭据管理
============

API key、密码、token 不应进入源码、Git、日志、异常页面或构建产物。

秘密的安全性包含存储、注入、使用、轮换和撤销整个生命周期。
环境变量只是常见注入通道，在部分平台仍可能被进程检查或诊断工具读取。
脱敏日志也应尽量记录凭据标识或状态，而不是依赖截断真实秘密来排错。
"""

def masked(value):
    if not value:
        return '<missing>'
    if len(value) <= 6:
        return '***'
    return value[:2] + '***' + value[-2:]

fake='sk-example-secret'
print('日志里只显示:', masked(fake))
print('\n原则:')
for x in [
    '本地开发从环境变量或未提交本地配置读取',
    '生产环境使用平台 Secret 管理能力',
    '.env 仍是明文文件，不等于秘密管理系统',
    '真实 secret 不进入示例、快照和 crash dump',
]: print('-',x)
