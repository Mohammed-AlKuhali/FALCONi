# download.py
from SoccerNet.Downloader import SoccerNetDownloader as SNdl

# Change this to a folder on your computer where you want to save the data.
mySNdl = SNdl(LocalDirectory="C:/Users/Asus/Desktop/SoccerNetData")

# Replace "your_password" with the password you got from the NDA.
mySNdl.downloadDataTask(task="mvfouls", split=["train", "valid", "test", "challenge"], password="s0cc3rn3t")
