# -*- coding: utf-8 -*-
"""
05 依赖可复现与锁定策略
=============

版本范围和部署锁定是不同层次；库与应用的依赖策略也不同。

库需要与下游解析器协作，通常声明经过验证的兼容范围；应用控制最终环境，适合锁定解析结果。
可复现还取决于 Python 版本、平台标记、包索引和系统依赖，只有版本号列表并不充分。
锁文件应由声明重新生成并在干净环境验证，而不是持续手改间接依赖。
"""

print('库: 在项目元数据里声明兼容范围。')
print('应用: 通常还要锁定完整解析结果并从干净环境重建。')
print('\n不要把 pip freeze 当成所有项目唯一的依赖设计。')
print('freeze 更像当前环境快照，可能包含临时安装、间接依赖和平台特定项。')

def choose_policy(project_kind):
    return 'compatible-range' if project_kind == 'library' else 'resolved-lock'

for kind in ['library', 'application']:
    print(kind, '=>', choose_policy(kind))
print('验证锁定结果时还要固定 Python/平台条件，并在空环境重新解析和安装。')
