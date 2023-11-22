import argparse
from utils.config import PARGS
from utils.handle import handle_args


def main():
    # 定义
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    for parg in PARGS:
        parser.add_argument(*parg["args"], **parg["kwargs"])

    # 执行
    kwargs = vars(parser.parse_args())  # 获取参数
    handle_args(**kwargs)  # 处理参数命令


if __name__ == "__main__":
    main()
