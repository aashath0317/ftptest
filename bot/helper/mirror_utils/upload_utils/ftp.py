from ftplib import FTP
import ftplib
import os,subprocess

FTP_SERVER = "ftp.c2ptech.com"
FTP_USER = "Aashath@c2ptech.com"
FTP_PASSWORD = "Aashath0317@"
ftp = FTP(FTP_SERVER)
ftp.login(FTP_USER,FTP_PASSWORD)
m_path= 
path=m_path+".zip" 
subprocess.run(["7z","a","-mx=0", path, m_path])
import os.path
ftp.set_pasv(True)
totalSize = os.path.getsize(path)
print('Total file size : ' + str(round(totalSize / 1024 / 1024 ,1)) + ' Mb')
file = open(path, 'rb')
ftp.storbinary(f"STOR {path}", file)
