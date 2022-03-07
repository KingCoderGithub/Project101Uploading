import os
import dropbox
from dropbox.files import WriteMode

class TransferData :
    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        for root, dirs, files in os.walk(file_from):
            
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path) 
            
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
    
def main () :
    access_token = 'sl.BDVDrA6OaLr2hc-WJckoQzZAJFO9ZSdaKxIG1wL9ESnIheaelfrx9dEUOdR3QZVxPxCLHArfRAjxnYBPOfWkxcsMRLvCIIyqnogqdfFfovhrfzmxFz1rmwO0V9T4t2B8d53Bh3k'
    transferData = TransferData(access_token)
    
    file_from = input("Enter th efile path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
