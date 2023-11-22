import os
import time
from natsort import natsorted
from utils.config import *


def EXIT():
    """
    退出程序
    """
    os._exit(0)


def CWD():
    """
    返回当前目录绝对路径
    """
    return os.getcwd()


def ISABS(path: str):
    """
    判断是否为绝对路径
    """
    return os.path.isabs(path)


def EXISTS(path: str):
    """
    判断路径是否有效
    """
    return os.path.exists(path)


def XOPENED(dir: str, fname: str):
    """
    打开的表格文件会生成以~$为前缀的临时文件
    判断~$文件是否存在即可获悉原表格是否打开
    """
    # print(PJOIN(dir, f"~${fname}"))
    return EXISTS(PJOIN(dir, f"~${fname}"))


def ISDIR(path: str):
    """
    判断目标路径是否为文件夹
    """
    return os.path.isdir(path)


def ISFILE(path: str):
    """
    判断目标路径是否为文件
    """
    return os.path.isfile(path)


def ISTAR(files):
    """
    约束文件名，只取目标格式文件，并自然排序
    """
    if not files:
        return []
    files = [f for f in files if EXTENSION(f) in INEXT]
    files = natsorted(files)
    return files


def PTYPE(path: str):
    """
    返回路径类型
    """
    if ISFILE(path):
        return "file"
    elif ISDIR(path):
        return "dir"
    return "path"


def PSRCS(path: str, type: str):
    """
    解析目标路径，返回目标父级目录和目标文件名集合
    """
    if type == "file":
        return [PDIR(path), ISTAR([BASENAME(path)])]
    elif type == "dir":
        return [path, ISTAR(LISTDIR(path))]
    return [path, []]


def LISTDIR(path: str):
    """
    返回目标文件夹下所有元素名
    """
    return os.listdir(path)


def MAKEDIR(path: str):
    """
    创建文件夹
    """
    os.makedirs(path)


def REMOVE(path: str):
    """
    删除文件
    """
    os.remove(path)


def PJOIN(*parts: str):
    """
    返回拼接路径
    """
    return os.path.join(*parts)


def PDIR(path: str):
    """
    返回父级目录绝对路径
    """
    return os.path.dirname(path)


def EXTENSION(path: str):
    """
    返回目标路径文件格式名
    """
    # 分割文件路径和扩展名
    file_name, file_extension = os.path.splitext(path)
    return file_extension


def BASENAME(path: str):
    """
    返回目标路径文件基本名
    """
    return os.path.basename(path)


def CONTENT(path: str):
    """
    返回目标路径文件内容
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except Exception as e:
        print(str(e))
        return [""]


# 当前时间
def NOW():
    """
    返回当前时间戳
    """
    return time.perf_counter()


# 计时
def DUR(start: float):
    """
    返回时间差
    """
    return NOW() - start


def SLEEP(secs: float):
    """
    休眠
    """
    time.sleep(secs)


def DATETIME():
    """
    返回格式化日期时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def timestr(time: float):
    """
    返回格式化计时时间
    """
    return "{:.1f}s".format(time)


def numstr(num: float, precision=5):
    """
    返回格式化数字
    """
    int_num = int(num)
    if int_num == num:
        return "{:4d}".format(int_num)
    else:
        return "%.{}f".format(precision) % num


def zipstr(keys: tuple, values: tuple, separator=f"{COMA} ", connector=f"{EQL} "):
    """
    返回元组卷积文本，给定A、B，返回（*A=*B）
    """
    if len(keys) != len(values):
        return ""
    return separator.join(
        f"{START}{key}{END}{connector}{value}" for key, value in zip(keys, values)
    )


def isfull(c: str):
    """
    判定字符全半角
    """
    if len(c) > 1:
        return False
    _ord = ord(c)
    return _ord >= 0x2E80 and _ord <= 0xFFEF


def natlen(s: str):
    """
    返回字符串自然长度
    """
    if not s:
        return 0
    _len = 0
    for c in s:
        if isfull(c):
            _len += 2
        else:
            _len += 1
    return _len


def maxlen(arr):
    """
    返回数组元素最大长度
    """
    if not arr:
        return 0
    ml = len(arr[0])
    for f in arr:
        tl = len(f)
        if tl > ml:
            ml = tl
    return ml


def attach(main_str: str, attach_str=" ", count=1, left=False):
    """
    粘贴串，返回主串和副串的拼接串，可定义副串的值、重复数量和拼接方向，默认为空格、不重复、右拼接
    """
    if count <= 0:
        return main_str
    join_str = attach_str * count
    if left:
        join_str += main_str
    else:
        join_str = main_str + join_str
    return join_str


def align(str: str, width: int, right=False):
    """
    对齐文本，可定义方向，默认左对齐
    """
    if width <= len(str):
        return str
    form = "{:<{width}}"
    if right:
        form = "{:>{width}}"
    return form.format(str, width=width)


# _func格式名函数仅限本文件使用
def _genargs(key: str):
    """
    生成参数键
    """
    attc = "-"
    if len(key) == 1:
        return [attach(key, attc, left=True)]
    return [attach(key[0], attc, left=True), attach(key, attc, count=2, left=True)]


# def reset(*num):
#     num = 0


def _fronted(key):
    """
    生成头部文本，如‘文件’→‘文件：’
    """
    return attach(FRONT[key], COLON)


# 初始化常量数据
for parg in PARGS:  # 生成指令参数
    key = parg["key"]
    if "main" in parg:
        MAINKEY = key
        if parg["main"]:
            DEFAULT = parg["main"]
    parg["args"] = _genargs(key)

for key in FRONT:  # 生成对应头文
    FRONTED.update({key: _fronted(key)})

_key_file = "file"  # 内部变量
# 额外生成file_front等宽空文
FRONTED.update({f"={_key_file}": " " * natlen(FRONTED[_key_file])})
# print(FRONTED)

for key in STAT:  # 生成填充符
    stat = STAT[key]
    stat["filler"] = SYMB[stat["filler"]]
