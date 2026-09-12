# 推荐项目模板

```text
my_project/
├─ .gitignore
├─ README.md
├─ pyproject.toml
├─ src/
│  └─ my_project/
│     ├─ __init__.py
│     ├─ __main__.py
│     ├─ cli.py
│     ├─ config.py
│     └─ service.py
├─ tests/
│  ├─ test_cli.py
│  └─ test_service.py
├─ scripts/
└─ docs/
```

不是每个项目都需要所有目录。原则是：**先满足真实需求，再扩展结构。**

应用还应明确：运行时数据目录、配置来源与优先级、日志位置、secret 来源、支持 Python 版本、本地开发命令、CI 门禁、构建命令、发布和回滚方式。
