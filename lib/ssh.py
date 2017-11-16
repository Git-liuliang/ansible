

import paramiko


class M_ssh:
    '''封装自paramiko,实现自己的ssh命令'''

    def __init__(self,hostname,port,username,password):

        self.x = paramiko.SSHClient()
        self.x.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.x.connect(hostname=hostname,port=port,username=username,password=password)

    def cmd(self,cmd):

        stdin, stdout, stderr = self.x.exec_command(cmd)
        result = stdout.read()
        # print(result.decode('utf-8'))
        self.x.close()
        return result.decode('utf-8')

class M_sftp:

    def __init__(self,hostname,port,username,password):
        self.z = paramiko.Transport(hostname,port)
        self.z.connect(username=username,password=password)

    def mput(self,local_path,remote_path):

        sftp = paramiko.SFTPClient.from_transport(self.z)
        sftp.put(local_path,remote_path)
        return 'transinfer succesfully!'

    def mget(self,remote_path,local_path):

        sftp = paramiko.SFTPClient.from_transport(self.z)
        sftp.get(remote_path,local_path)



# p = M_ssh('172.18.3.188',22,'root','xinwei')
# p.cmd('ifconfig')
#
# x = M_sftp('192.168.88.128',22,'liuliang','python')
# x.mget('/home/liuliang/FTP_demo/ftp.png','C:\\Users\liuliang\Desktop\FTP\ggg')

# x = M_sftp('192.168.88.128',22,'liuliang','python')
# x.mput('C:\\Users\liuliang\Desktop\FTP\day8_homework.zip','/home/liuliang/fff')
