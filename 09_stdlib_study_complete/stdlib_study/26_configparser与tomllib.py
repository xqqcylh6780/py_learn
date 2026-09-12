# -*- coding: utf-8 -*-
"""26 configparser / tomllib：INI 与 TOML 配置"""
import configparser
import tomllib

print("=== configparser ===")
ini = "[server]\nhost = 127.0.0.1\nport = 8080\ndebug = yes\n"
cfg = configparser.ConfigParser()
cfg.read_string(ini)
print(cfg["server"]["host"])
print(cfg["server"].getint("port"))
print(cfg["server"].getboolean("debug"))

print("\n=== TOML ===")
toml_text = 'title = "demo"\n[server]\nhost = "127.0.0.1"\nport = 8080\nfeatures = ["a", "b"]\n'
data = tomllib.loads(toml_text)
print(data)

print("\n注意：tomllib 只负责读取 TOML，不负责写入。")
print("配置中的密码/Token 不应因为放进 INI/TOML 就变安全；秘密管理是另一个问题。")
