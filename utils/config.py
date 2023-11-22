# 配置 基量
CONFIG = {
    "PARGS": [
        {
            "main": "data",
            "key": "make",
            "args": [],
            "kwargs": {
                "nargs": "?",
                "metavar": "PATH",
                "help": "make excel file(s) from PATH",
            },
        },
        {
            "key": "force",
            "args": [],
            "kwargs": {
                "action": "store_true",
                "help": "force to make excel file(s)",
            },
        },
        {
            "key": "calc",
            "args": [],
            "kwargs": {
                "action": "store_true",
                "help": "compute data from excel file(s)",
            },
        },
    ],
    "STAT": {
        "make": {
            "len": 20,
            "filler": "rect",
        },
        "save": {
            "len": 3,
            "filler": "dot",
            "freq": 0.167,
        },
        "calc": {
            "len": 3,
            "filler": "dot",
            "freq": 0.167,
            "precs": 7,
            "var": ("Y_min", "Sg_max", "Sg_sum"),
        },
    },
    "ZH": {
        "front": {
            "path": "路径",
            "dir": "目录",
            "file": "文件",
            "make": "转化",
            "save": "保存",
            "calc": "运算",
        },
        "err": {
            "errupt": "中断",
            "not_exist": "不存在",
            "opened": "已被打开",
            "no": "没有",
            "not": "不是",
            "broken": "损坏",
            "removed": "已删除",
        },
    },
    "SYMB": {
        "left": "<",
        "right": ">",
        "start": "[",
        "end": "]",
        "pip": "|",
        "clon": ":",
        "clon_zh": "：",
        "yes": "[√]",
        "no": "[x]",
        "at": "@",
        "rect": "■",
        "dot": ".",
        "comma": ",",
        "udline": "_",
        "bar": "-",
        "any": "*",
        "equal": "=",
    },
    "EXT": {
        "input": [".dat", ".flow"],
        "output": ".xlsx",
    },
}


# 次量
PARGS = CONFIG["PARGS"]  # 自定义参数集
FRONT = CONFIG["ZH"]["front"]  # 关键中文词集
FRONTED = {}  # 头文集
ERR = CONFIG["ZH"]["err"]  # 报错中文集
STAT = CONFIG["STAT"]  # 进度集
SYMB = CONFIG["SYMB"]  # 符号集
EXT = CONFIG["EXT"]  # 尾缀集
MAINKEY = ""  # 参数主键
DEFAULT = ""  # 默认数据文件夹


# 再次量
OK = SYMB["yes"]
NOK = SYMB["no"]
COLON = SYMB["clon_zh"]
SEP = SYMB["pip"]
DOT = SYMB["dot"]
COMA = SYMB["comma"]
ANY = SYMB["any"]
EQL = SYMB["equal"]
START = SYMB["start"]
END = SYMB["end"]
INEXT = EXT["input"]  # 输入文件格式
OUTEXT = EXT["output"]  # 输出文件格式
MAKE = STAT["make"]  # 转换百分比加载
MAKE_LEN = MAKE["len"]
SAVE = STAT["save"]  # 动态点加载
SAVE_LEN = SAVE["len"]
SAVE_FREQ = SAVE["freq"]  # 刷新频率
CALC = STAT["calc"]
CALC_LEN = CALC["len"]
CALC_FREQ = CALC["freq"]
PRECS = CALC["precs"]
CVAR = CALC["var"]
