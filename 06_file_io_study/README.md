# 06_file_io_study

Python 文件与 I/O 完整学习包。目标不是只会 `open()`，而是能够安全、可靠、可维护地处理真实项目中的文件。

## 课程目录

| # | 文件 | 主题 |
|---|---|---|
| 01 | `01_open与文件对象.py` | open、模式、文件对象、with |
| 02 | `02_文本模式与encoding.py` | Unicode、encoding、errors、newline、BOM |
| 03 | `03_pathlib路径模型.py` | pathlib、PurePath、resolve、路径语义 |
| 04 | `04_二进制文件与bytes.py` | bytes、bytearray、struct、二进制文件 |
| 05 | `05_文件指针seek_tell与随机访问.py` | seek/tell、随机访问 |
| 06 | `06_上下文管理与资源清理.py` | 多文件、ExitStack |
| 07 | `07_大文件与流式处理.py` | 逐行、分块、增量处理 |
| 08 | `08_目录遍历glob与walk.py` | iterdir、glob、rglob、walk |
| 09 | `09_创建删除移动复制.py` | mkdir、unlink、shutil |
| 10 | `10_CSV可靠读写.py` | csv、DictReader、newline |
| 11 | `11_JSON可靠读写.py` | json、Unicode、Decimal、自定义对象 |
| 12 | `12_Pickle与反序列化安全.py` | pickle 与安全边界 |
| 13 | `13_临时文件与临时目录.py` | tempfile |
| 14 | `14_文件元数据stat与时间.py` | stat、mtime、ctime、权限 |
| 15 | `15_权限符号链接与硬链接.py` | symlink、lstat、权限模型 |
| 16 | `16_原子写入与安全替换.py` | 临时文件、fsync、os.replace |
| 17 | `17_备份轮换与安全覆盖.py` | 覆盖前备份、版本策略 |
| 18 | `18_压缩流gzip_bz2_lzma.py` | gzip、bz2、lzma |
| 19 | `19_ZIP与TAR归档.py` | zip/tar、Zip Slip |
| 20 | `20_StringIO与BytesIO.py` | 内存文件、测试 |
| 21 | `21_mmap内存映射文件.py` | mmap、随机访问 |
| 22 | `22_文件锁与并发访问.py` | fcntl/msvcrt、advisory lock |
| 23 | `23_哈希校验与文件完整性.py` | hashlib、流式哈希、HMAC 边界 |
| 24 | `24_安全路径与目录穿越.py` | path traversal、resolve/relative_to |
| 25 | `25_文件I_O异常与竞态.py` | OSError 子类、TOCTOU、重试 |
| 26 | `26_文件格式选型与工程实践.py` | CSV/JSON/pickle/SQLite 选型与检查表 |
| 99 | `99_exercises.py` | 56 道自动判分练习 |

## 推荐学习方式

```powershell
cd 06_file_io_study
python 01_open与文件对象.py
python 99_exercises.py
```

每节教程大致对应两道练习。练习初始应为 `0/56`，完成 TODO 后逐渐增加。

## 学完应具备的能力

你应该能够独立解释和实现：

- 文本与二进制 I/O 的真正区别
- UTF-8、BOM、newline 和错误解码策略
- pathlib 路径组合、规范化与跨平台差异
- 大文件逐行/分块流式处理
- CSV/JSON 的正确读写及其格式限制
- 为什么绝不能反序列化不可信 pickle
- 临时文件、备份、原子替换与崩溃一致性
- ZIP/TAR 解压路径穿越风险
- symlink、stat/lstat 与路径安全边界
- 文件锁为什么具有平台与协作协议限制
- mmap 适合什么，不适合什么
- SHA-256 完整性校验与 HMAC/密码哈希的区别
- TOCTOU 文件竞态和精确 OSError 处理
- 什么时候该从 JSON 文件升级到 SQLite/数据库

## 环境

- 推荐 Python 3.11+
- 仅标准库
- Windows / macOS / Linux 均可学习；涉及权限、符号链接、文件锁的行为存在平台差异，课程中明确说明。
