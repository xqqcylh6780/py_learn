# -*- coding: utf-8 -*-
"""06_file_io_study 练习册：56 题。运行 `python 99_exercises.py`。"""
from pathlib import Path
from tempfile import TemporaryDirectory
from io import StringIO, BytesIO
import csv, json, hashlib, shutil, gzip, os, copy, zipfile

_TESTS=[]
def check(fn): _TESTS.append(fn); return fn

@check
def ex1_write_text_file():
    with TemporaryDirectory() as d:
        p=Path(d)/'a.txt'
        # TODO: 用 UTF-8 写入 hello\n
        assert p.read_text(encoding='utf-8') == 'hello\n'

@check
def ex2_exclusive_create():
    with TemporaryDirectory() as d:
        p=Path(d)/'x.txt'
        # TODO: 用 x 模式创建并写入 first
        assert p.read_text(encoding='utf-8') == 'first'
        try:
            with p.open('x', encoding='utf-8'): pass
        except FileExistsError: pass
        else: raise AssertionError('x 模式应在文件已存在时抛 FileExistsError')

@check
def ex3_utf8_roundtrip():
    text='中文🙂'
    raw=None  # TODO: encode utf-8
    restored=None  # TODO: decode utf-8
    assert isinstance(raw, bytes) and restored == text

@check
def ex4_utf8_sig():
    raw=b'\xef\xbb\xbfhello'
    text=None  # TODO: 解码且去掉 BOM
    assert text == 'hello'

@check
def ex5_path_join():
    base=Path('data')
    p=None  # TODO: data/images/a.png，不手写完整字符串
    assert p == Path('data')/'images'/'a.png'

@check
def ex6_change_suffix():
    p=Path('report.old.txt')
    result=None  # TODO: 改最后一个后缀为 .md
    assert result == Path('report.old.md')

@check
def ex7_binary_roundtrip():
    with TemporaryDirectory() as d:
        p=Path(d)/'x.bin'; raw=b'\x00\xffabc'
        # TODO: 写入 raw
        out=None  # TODO: 再读回来
        assert out == raw

@check
def ex8_mutable_bytes():
    b=None  # TODO: 创建 bytearray(b'ABC') 并把首字节改成 Z
    assert b == bytearray(b'ZBC')

@check
def ex9_seek_read():
    f=BytesIO(b'0123456789')
    # TODO: 移到位置 5
    result=f.read(2)
    assert result == b'56'

@check
def ex10_tail_bytes():
    f=BytesIO(b'abcdefgh')
    # TODO: 从末尾向前 3 字节定位
    result=f.read()
    assert result == b'fgh'

@check
def ex11_copy_upper():
    src=StringIO('hello')
    dst=StringIO()
    # TODO: 把 src 内容大写写入 dst
    assert dst.getvalue() == 'HELLO'

@check
def ex12_close_via_with():
    with TemporaryDirectory() as d:
        p=Path(d)/'x.txt'
        # TODO: with 打开并写入 x，退出后文件对象变量 f 应关闭
        f=None
        assert f is not None and f.closed and p.read_text(encoding='utf-8')=='x'

@check
def ex13_chunk_reader():
    f=BytesIO(b'abcdefghij')
    chunks=[]
    # TODO: 每次 read(4) 直到 b''
    assert chunks == [b'abcd', b'efgh', b'ij']

@check
def ex14_count_lines_streaming():
    f=StringIO('a\nb\nc\n')
    count=None  # TODO: 不调用 read()，迭代文件对象计数
    assert count == 3

@check
def ex15_rglob_txt():
    with TemporaryDirectory() as d:
        root=Path(d); (root/'a').mkdir(); (root/'a'/'x.txt').write_text('x'); (root/'y.py').write_text('y')
        names=None  # TODO: 所有 .txt 文件名排序列表
        assert names == ['x.txt']

@check
def ex16_stable_sort_paths():
    paths=[Path('b.txt'),Path('a.txt'),Path('c.txt')]
    result=None  # TODO: 按 name 排序
    assert [p.name for p in result] == ['a.txt','b.txt','c.txt']

@check
def ex17_mkdir_parents():
    with TemporaryDirectory() as d:
        p=Path(d)/'a'/'b'/'c'
        # TODO: 一次创建完整目录
        assert p.is_dir()

@check
def ex18_copy_metadata():
    with TemporaryDirectory() as d:
        a=Path(d)/'a'; b=Path(d)/'b'; a.write_text('x')
        # TODO: 用 shutil.copy2(a,b)
        assert b.read_text() == 'x'

@check
def ex19_csv_writer():
    buf=StringIO(newline='')
    # TODO: writerow ['A','hello, world']
    buf.seek(0)
    assert next(csv.reader(buf)) == ['A','hello, world']

@check
def ex20_csv_dictreader():
    buf=StringIO('name,age\nAlice,20\n', newline='')
    row=None  # TODO: 读第一条 DictReader 数据
    assert row == {'name':'Alice','age':'20'}

@check
def ex21_json_unicode():
    obj={'name':'中文'}
    s=None  # TODO: dumps，输出中保留中文而不是 \uXXXX
    assert '中文' in s and json.loads(s)==obj

@check
def ex22_json_roundtrip():
    s='{"items":[1,2],"ok":true}'
    obj=None  # TODO
    assert obj == {'items':[1,2],'ok':True}

@check
def ex23_pickle_security_knowledge():
    unsafe_source='network'
    should_unpickle=None  # TODO: 外部不可信来源必须为 False
    assert should_unpickle is False

@check
def ex24_choose_interchange_format():
    need_cross_language=True
    fmt=None  # TODO: 在 'json'/'pickle' 中选择
    assert fmt == 'json'

@check
def ex25_tempdir_cleanup():
    from tempfile import TemporaryDirectory
    holder=[]
    # TODO: with TemporaryDirectory() as d，把 Path(d) 放进 holder
    assert len(holder)==1 and not holder[0].exists()

@check
def ex26_named_tempfile():
    from tempfile import NamedTemporaryFile
    name=None
    # TODO: 创建 NamedTemporaryFile，并在 with 内把文件名赋给 name
    assert name is not None

@check
def ex27_file_size():
    with TemporaryDirectory() as d:
        p=Path(d)/'x'; p.write_bytes(b'12345')
        size=None  # TODO: stat
        assert size == 5

@check
def ex28_is_regular_file():
    with TemporaryDirectory() as d:
        p=Path(d)/'x'; p.write_text('x')
        result=None  # TODO
        assert result is True

@check
def ex29_detect_symlink_api():
    p=Path('whatever')
    method=None  # TODO: 取出 Path.is_symlink 方法本身
    assert method is Path.is_symlink

@check
def ex30_lstat_api():
    p=Path('.')
    st=None  # TODO: 调用 lstat()
    assert hasattr(st,'st_mode')

@check
def ex31_atomic_replace():
    with TemporaryDirectory() as d:
        root=Path(d); dst=root/'x.txt'; dst.write_text('old')
        tmp=root/'tmp.txt'; tmp.write_text('new')
        # TODO: 使用 os.replace(tmp,dst)
        assert dst.read_text()=='new' and not tmp.exists()

@check
def ex32_same_dir_temp_reason():
    reason=None  # TODO: 填字符串 'same-filesystem'
    assert reason == 'same-filesystem'

@check
def ex33_backup_copy():
    with TemporaryDirectory() as d:
        p=Path(d)/'a.txt'; p.write_text('v1')
        backup=p.with_suffix('.txt.bak')
        # TODO: copy2
        p.write_text('v2')
        assert backup.read_text()=='v1'

@check
def ex34_missing_backup():
    with TemporaryDirectory() as d:
        p=Path(d)/'missing.txt'
        should_create_backup=None  # TODO: 文件不存在时应为 False
        assert should_create_backup is False and not (Path(d)/'missing.txt.bak').exists()

@check
def ex35_gzip_text():
    with TemporaryDirectory() as d:
        p=Path(d)/'x.gz'
        # TODO: gzip.open wt 写入 hello
        text=None  # TODO: gzip.open rt 读回
        assert text=='hello'

@check
def ex36_compression_choice():
    compatibility_priority=True
    choice=None  # TODO: 本题课程默认选 gzip
    assert choice=='gzip'

@check
def ex37_zip_arcname():
    with TemporaryDirectory() as d:
        root=Path(d); f=root/'a.txt'; f.write_text('A'); zpath=root/'x.zip'
        # TODO: 把 f 归档为 docs/a.txt
        with zipfile.ZipFile(zpath) as z:
            assert z.namelist()==['docs/a.txt']

@check
def ex38_zip_slip_detect():
    names=['docs/a.txt','../../evil.txt']
    unsafe=None  # TODO: 找出含 .. 路径段的名称列表
    assert unsafe == ['../../evil.txt']

@check
def ex39_stringio():
    buf=StringIO()
    # TODO: 写 abc，然后取 getvalue
    result=None
    assert result=='abc'

@check
def ex40_bytesio():
    buf=BytesIO()
    # TODO: 写 b'xyz'
    assert buf.getvalue()==b'xyz'

@check
def ex41_mmap_use_case():
    use_case=None  # TODO: 'random-access'
    assert use_case=='random-access'

@check
def ex42_empty_mmap_guard():
    size=0
    should_map=None  # TODO: size > 0 才映射
    assert should_map is False

@check
def ex43_platform_lock_module():
    expected='msvcrt' if os.name=='nt' else 'fcntl'
    module_name=None  # TODO
    assert module_name==expected

@check
def ex44_lock_protocol():
    all_processes_obey=False
    safe=None  # TODO: advisory lock 是否足以保护不遵守锁协议的进程？
    assert safe is False

@check
def ex45_sha256():
    raw=b'abc'
    digest=None  # TODO: hexdigest
    assert digest == hashlib.sha256(raw).hexdigest()

@check
def ex46_stream_hash():
    f=BytesIO(b'a'*10000); h=hashlib.sha256()
    # TODO: 每 1024 字节更新 h
    assert h.hexdigest()==hashlib.sha256(b'a'*10000).hexdigest()

@check
def ex47_safe_relative():
    with TemporaryDirectory() as d:
        base=Path(d).resolve(); cand=(base/'a'/'b.txt').resolve()
        rel=None  # TODO: cand.relative_to(base)
        assert rel == Path('a')/'b.txt'

@check
def ex48_reject_escape():
    with TemporaryDirectory() as d:
        base=Path(d).resolve(); cand=(base/'..'/'evil.txt').resolve()
        escaped=False
        # TODO: relative_to(base)，ValueError 时 escaped=True
        assert escaped is True

@check
def ex49_missing_ok():
    with TemporaryDirectory() as d:
        p=Path(d)/'none'
        done=None
        # TODO: 调用 p.unlink(missing_ok=True)，然后 done=True
        assert done is True and not p.exists()

@check
def ex50_specific_exception():
    exc_type=None  # TODO: 文件不存在最精确异常类
    assert exc_type is FileNotFoundError

@check
def ex51_format_for_table():
    requirement='simple-2d-table'
    fmt=None  # TODO: csv
    assert fmt=='csv'

@check
def ex52_format_for_cross_language_nested():
    fmt=None  # TODO: json
    assert fmt=='json'

@check
def ex53_database_when_transactions():
    need_transactions=True
    choice=None  # TODO: sqlite
    assert choice=='sqlite'

@check
def ex54_text_encoding_policy():
    policy=None  # TODO: 'explicit-utf8'
    assert policy=='explicit-utf8'

@check
def ex55_large_file_policy():
    policy=None  # TODO: 'stream'
    assert policy=='stream'

@check
def ex56_untrusted_archive_policy():
    policy=None  # TODO: 'validate-paths'
    assert policy=='validate-paths'


def run_all():
    print('='*70); print('06_file_io_study 练习册'); print('='*70)
    passed=0
    for fn in _TESTS:
        try:
            fn()
        except AssertionError as e:
            print(f'[FAIL] {fn.__name__:<36} {e or "TODO/断言未通过"}')
        except Exception as e:
            print(f'[ERR ] {fn.__name__:<36} {type(e).__name__}: {e}')
        else:
            passed+=1; print(f'[ OK ] {fn.__name__}')
    print('-'*70); print(f'通过 {passed}/{len(_TESTS)}')

if __name__=='__main__': run_all()

# ================================================================
# 参考答案（建议先自己完成）
# ================================================================
ANSWERS = r"""
ex1: p.write_text('hello\\n', encoding='utf-8')
ex2: with p.open('x', encoding='utf-8') as f: f.write('first')
ex3: raw=text.encode('utf-8'); restored=raw.decode('utf-8')
ex4: text=raw.decode('utf-8-sig')
ex5: p=base/'images'/'a.png'
ex6: result=p.with_suffix('.md')
ex7: p.write_bytes(raw); out=p.read_bytes()
ex8: b=bytearray(b'ABC'); b[0]=ord('Z')
ex9: f.seek(5)
ex10: f.seek(-3, 2)
ex11: dst.write(src.read().upper())
ex12: with p.open('w',encoding='utf-8') as f: f.write('x')
ex13: while chunk:=f.read(4): chunks.append(chunk)
ex14: count=sum(1 for _ in f)
ex15: names=sorted(p.name for p in root.rglob('*.txt'))
ex16: result=sorted(paths,key=lambda p:p.name)
ex17: p.mkdir(parents=True)
ex18: shutil.copy2(a,b)
ex19: csv.writer(buf).writerow(['A','hello, world'])
ex20: row=next(csv.DictReader(buf))
ex21: s=json.dumps(obj,ensure_ascii=False)
ex22: obj=json.loads(s)
ex23: should_unpickle=False
ex24: fmt='json'
ex25: with TemporaryDirectory() as d: holder.append(Path(d))
ex26: with NamedTemporaryFile() as f: name=f.name
ex27: size=p.stat().st_size
ex28: result=p.is_file()
ex29: method=Path.is_symlink
ex30: st=p.lstat()
ex31: os.replace(tmp,dst)
ex32: reason='same-filesystem'
ex33: shutil.copy2(p,backup)
ex34: should_create_backup=False
ex35: with gzip.open(p,'wt',encoding='utf-8') as f:f.write('hello'); with gzip.open(p,'rt',encoding='utf-8') as f:text=f.read()
ex36: choice='gzip'
ex37: with zipfile.ZipFile(zpath,'w') as z:z.write(f,arcname='docs/a.txt')
ex38: unsafe=[n for n in names if '..' in Path(n).parts]
ex39: buf.write('abc'); result=buf.getvalue()
ex40: buf.write(b'xyz')
ex41: use_case='random-access'
ex42: should_map=size>0
ex43: module_name='msvcrt' if os.name=='nt' else 'fcntl'
ex44: safe=False
ex45: digest=hashlib.sha256(raw).hexdigest()
ex46: while chunk:=f.read(1024): h.update(chunk)
ex47: rel=cand.relative_to(base)
ex48: try:cand.relative_to(base)\nexcept ValueError:escaped=True
ex49: p.unlink(missing_ok=True); done=True
ex50: exc_type=FileNotFoundError
ex51: fmt='csv'
ex52: fmt='json'
ex53: choice='sqlite'
ex54: policy='explicit-utf8'
ex55: policy='stream'
ex56: policy='validate-paths'
"""
