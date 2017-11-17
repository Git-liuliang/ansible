
from  concurrent.futures import ProcessPoolExecutor
from lib.ssh import *
from lib.handler import *

import logging

logger = logging.getLogger(__name__)  # 生成logger实例


def magic():
    '''get ip informations'''
    arg_list = Put_opt().core()
    ipinfo = Get_host().ip_info(arg_list)
    return ipinfo

def get_putinfo():
    '''get put path infomation'''
    arg_list = Put_opt().core()
    # print('arg_list',arg_list)
    cmdinfo = Get_host().putinfo(arg_list)
    putinfo = cmdinfo.split(',')
    return putinfo

def fris(line, local_path,remote_path):
    '''as target function by processpool'''
    ip = line['ip']
    port = int(line['port'])
    username = line['username']
    password = line['password']
    p = M_sftp(ip, port, username, password)
    res = p.mput(local_path,remote_path)
    return res


def core():
    try:
        ipinfo = magic()
        putinfo = get_putinfo()
    except AttributeError:
        exit('请输入正确的参数，使用-h 或者 --help查看')

    # print(putinfo)
    res = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        for line in ipinfo:
            # print(line)
            future = executor.submit(fris, line, putinfo[0], putinfo[1])
            # print(future.result())
            re = [future,line]
            res.append(re)
    for i in res:
        logger.debug('from host:%s'%i[1]['ip'])
        logger.debug(i[0].result())
        # print(i.result())

if __name__ == '__main__':

    # x = M_sftp('172.18.3.188',22,'root','xinwei')
    # x.mput('C:\\Users\liuliangliang\Desktop\ss.txt','/home/ddd')
    # a = magic()
    # print(a)
    core()

