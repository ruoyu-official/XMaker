from utils.config import FRONTED, NOK, STAT, OK, SEP
from utils.lib import DUR, attach, natlen, timestr


def LOADING(stat: str, progress: int):
    """
    返回进度文本
    """
    loaded = STAT[stat]["filler"] * progress
    width = STAT[stat]["len"]
    if stat == "make":
        percent = (progress / width) * 100  # 百分比
        return "[{:<{width}}]{:>4.0f}%".format(loaded, percent, width=width)
    elif stat == "save" or stat == "calc":
        return "{:<{width}}".format(loaded, width=width)
    return ""


def PROGRESS(stat: str, start: float, progress=0, ok=False):
    """
    返回状态栏文本
    """
    front = f"{FRONTED[stat]}"
    rear = f"({timestr(DUR(start))})"
    progress = progress
    if ok:
        progress = STAT[stat]["len"]
    loading = LOADING(stat, progress)
    return "".join([front, loading, rear])


def LINE(*parts, separator=""):
    """
    返回拼接文本，可设置间隔符（\\r开头）
    """
    return f"\r{separator.join(parts)}"


def PRINT(*parts: str, err="", res="", ok=False, cover=0):
    """
    打印进度状态，不换行且从起始位置输出，并返回该行位长
    """
    sep = f" {SEP} "
    end = " "
    _cover = ""
    if ok or err:
        end = "\n"
        _ork = f"{OK} {res}" if ok else f"{NOK} {err}"
        _cover = LINE(parts[0], _ork, separator=sep)
        parts += (attach(_ork, count=cover - natlen(_cover)),)
    line = LINE(*parts, separator=sep)
    print(line, end=end)
    return line
