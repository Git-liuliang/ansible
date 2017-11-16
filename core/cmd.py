
from  concurrent.futures import ProcessPoolExecutor
from lib.ssh import *
from lib.handler import *
import logging

logger = logging.getLogger(__name__)  # 生成logger实例

def get_cmd():
    '''get cmd informaiton'''
    arg_list = Cmd_opt().core()
    cmdinfo = Get_host().cmd(arg_list)
    return cmdinfo

def magic():
    '''get ip information'''
    arg_list = Cmd_opt().core()
    ipinfo = Get_host().ip_info(arg_list)
    return ipinfo


def fris(line,cmd):

        '''as function by processpoll'''
        ip = line['ip']
        port = int(line['port'])
        username = line['username']
        password = line['password']
        p = M_ssh(ip,port,username,password)
        res = p.cmd(cmd)
        return res

def core():
    ipinfo = magic()
    cmdinfo = get_cmd()
    res = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        for line in ipinfo:
            # print(line)
            future = executor.submit(fris, line, cmdinfo)
            # print(future.result())
            re = [future,line]
            res.append(re)
    for i in res:

        logger.debug('from host:%s'%i[1]['ip'])
        logger.debug(i[0].result())



if __name__ == '__main__':

    core()

    # q = Cmd_opt().core()
    # print(q)
    # x = Get_host().inr(q)
    # print(x)
    # z = Get_host.cmd(q)
    # print(z)
    # for dic in x:
    #     p = M_ssh(dic['ip'], int(dic['port']), dic['username'], dic['password'])
    #     print(p.cmd(z))

    # ew = fuc()
    # obj = []
    # for dic in ew:
    #     excute = ProcessPoolExecutor(max_workers=4)
    #     future = excute.submit(dic, 'ifconfig')
    #     obj = obj.append(future)
    # excute.shutdown()

    # for fu in future:
    #     print(fu.result())

    # ew = fuc()
    # for i in ew:
    #     with ProcessPoolExecutor(max_workers=4) as executor:
    #             future = executor.submit(i, 'ifconfig')
    #             print(future.result())


    # result = []
    # for i in fuc():
    #     res = i.cmd
    #     result.append(res)
    # print(result)
    # objs = []
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     for i in result:
    #         obj = executor.submit(i, 'ifconfig')
    #         objs.append(obj)
    # for obj in objs:
    #     print(obj.result())


    # objs = []
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     for i in range(5):
    #             # print(i.cmd)
    #             obj = executor.submit(pow, 12,i)
    #             objs.append(obj)
    # print('zhu')
    # for obj in objs:
    #         print(obj.result())

    # ipinfo = magic()
    # cmdinfo = get_cmd()
    # res = []
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #         for line in ipinfo:
    #             print(line)
    #             future = executor.submit(fris, line,cmdinfo)
    #             # print(future.result())
    #             res.append(future)
    # for i in res:
    #     print(i.result())


