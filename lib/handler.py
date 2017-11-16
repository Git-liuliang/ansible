from lib.common import *

class Get_host:
    @classmethod
    def ip_info(cls,p):

        host_dic = p.host.split(',')
        group_dic = p.group.split(',')
        for u in group_dic:
            a = Config_hander.get_dic(u)
            for i in a:
                host_dic.append(i[1])
        r = set(host_dic)
        res = []
        for j in r:
            w = dict(Config_hander.get_dic(j))
            # print(w)
            res.append(w)

        return res

    @classmethod
    def cmd(cls,p):
        return p.cmd

    @classmethod
    def putinfo(cls,p):
        return p.put

    @classmethod
    def getinfo(cls,p):
        return p.get

# p = {1:'323',2:'4343'}
# a = p.items()
# print(a)