# -*- coding: utf-8 -*-
"""32 .pyi、py.typed 与类型检查工程实践

- .pyi：stub，只描述公开类型接口，不提供普通运行时实现。
- py.typed：PEP 561 标记，告诉类型检查器一个已安装包自带内联类型信息。
- mypy/pyright：第三方静态检查器；本课程不强依赖它们，但真实项目应在 CI 中运行一种。
"""
# 学习重点：类型信息要随包正确发布，使用者的检查器才能看到它。
# - 内联注解包应包含 py.typed；分离接口可通过同名 .pyi stub 描述。
# - stub 必须与运行时实现保持同步，并纳入 CI 检查。
# - 项目应固定一个主检查器、版本、严格度和增量采用规则。
# 常见误区：本地源码检查通过，就以为安装后的发行包也携带类型信息。
from pathlib import Path

print('推荐工程策略：')
print('1. 新代码尽量完整注解公开边界')
print('2. 严格度逐步提高，不要一上来全局 Any')
print('3. # type: ignore 要尽量带错误码并解释原因')
print('4. 库作者关注 .pyi / py.typed / 公共 API')
print('5. CI 固定检查器版本，避免团队结果不一致')
print('static_cases/ 中提供可交给 pyright/mypy 检查的样例。')
