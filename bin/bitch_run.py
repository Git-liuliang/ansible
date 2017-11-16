import sys,os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import cmd

from conf import mylogging  # 导入自定义的logging配置





if __name__ == '__main__':


    mylogging.load_my_logging_cfg()
    cmd.core()