# -*- coding: utf-8 -*-
"""
16 配置分层与环境变量
============

默认值、配置文件、环境变量、CLI 参数应有明确优先级。

每个来源还需要统一解析和校验，例如字符串环境变量不能直接当作布尔值使用。
覆盖规则应写入文档并在启动时一次性解析，避免业务代码到处读取环境变量。
缺失必填配置要尽早失败，同时错误信息只指出配置名，不能泄露敏感值。
"""

def resolve(default, file_value=None, env_value=None, cli_value=None):
    value=default
    if file_value is not None: value=file_value
    if env_value is not None: value=env_value
    if cli_value is not None: value=cli_value
    return value

print(resolve(8000, file_value=8080, env_value=9000))
print(resolve(8000, file_value=8080, env_value=9000, cli_value=7000))
print('示例优先级: 默认 < 文件 < 环境变量 < CLI')
