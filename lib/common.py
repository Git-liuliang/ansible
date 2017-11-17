import configparser
from conf import settings
from optparse import OptionParser


class Config_hander:

    @classmethod
    def getConfig(self,section,key):
        config = configparser.ConfigParser()
        path = settings.IP_DIR
        config.read(path)
        return config.get(section,key)

    @classmethod
    def get_dic(self,section):
        config = configparser.ConfigParser()
        path = settings.IP_DIR
        config.read(path)
        return config.items(section)



    @classmethod
    def modConfig(self,section,key,value):
        config = configparser.ConfigParser()
        path = settings.IP_DIR
        config.read(path)
        config.set(section,key,value)
        config.write(open(path, "w"))


# qq = Config_hander.getConfig('h2','port')
# dd = Config_hander.get_dic('h1')
# ss = Config_hander.get_dic('groups')
# print(qq)
# print(dd)
# print(dd[0][0])
# print(ss)
# aa = dict(Config_hander.get_dic('h1'))
# print(aa)


class M_optparse:

    def __init__(self):
        self.parser = OptionParser(usage="bitch_run [-i] h1,h2 [-g] g1,g2 [-c] 'your cmd'  \n bitch_scp [-i] h1,h2 [-g] g1,g2 [-p] local_path,remote_path", version="1.0")
        self.parser.add_option("-i", "--ip", action="store", dest="host" ,help="input your host ,like h1,h2,h3....")
        self.parser.add_option("-g", "--group", action="store", dest="group",help="input your hostgroup ,like g1,g2,g3.....")

    def core(self):
        (self.options, self.args) = self.parser.parse_args()
        return self.options


class Cmd_opt(M_optparse):

    def __init__(self):
        super().__init__()
        self.parser.add_option("-c", "--cmd", action="store", dest="cmd",help="input your command,like 'df -h'")
    def core(self):
        (self.options, self.args) = self.parser.parse_args()
        return self.options


class Put_opt(M_optparse):

    def __init__(self):

        super().__init__()
        self.parser.add_option("-p", "--put", action="store", dest="put",help="input the local_path and remote_path,like  C:/Users/liuliangliang/Desktop/ansible/core/scp.py,/home/scp.py")

    def core(self):
        (self.options, self.args) = self.parser.parse_args()
        return self.options

class Get_opt(M_optparse):

    def __init__(self):

        super().__init__()
        self.parser.add_option("-d", "--get", action="store", dest="get",help="input your remote_path and local_path like /home/scp.py,C:/Users/liuliangliang/Desktop/ansible/core/scp.py ")


    def core(self):

        (self.options, self.args) = self.parser.parse_args()
        return self.options







