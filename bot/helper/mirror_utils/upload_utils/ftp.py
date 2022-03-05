from ftplib import FTP
import ftplib
import os,subprocess

LOGGER.info(f"FTP name: {up_name}")
ftp = FTP(FTP_SERVER)
ftp.login(FTP_USER,FTP_PASSWORD)
def files(path):
 for file in os.listdir(path):
  if os.path.isfile(os.path.join(path, file)):
    yield file
path ="downloads"
up_file = up_name
up_path = glob.glob(os.path.join(path, '*'))
total_files = len(up_path)
loop = 0
while not total_files == loop:
  file_name=up_path[loop]
  path2 = glob.glob(os.path.join(file_name, '*'))
  path2 = str(path2[0])
  loop = loop+1
  for file in files(file_name):
   if file == up_file:
   ftp.set_pasv(True)
   file = open(path2, 'rb')
   up = "Uploading to FTP Server 📤"
   x = bot.send_message(up, self.bot, self.update)
   ftp.storbinary(f"STOR {up_name}", file)
   up = f"{up_name} is Uploaded ✅"
   bot.edit_message_text(x, up, self.bot, self.update)

