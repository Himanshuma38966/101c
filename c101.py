import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_folder(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(local_path, 'rb')
        dbx.files_upload(f.read(), dropbox_path , mode=Writmode('overwrite'))

def main():
    access_token = 'sWtnBh50g_cAAAAAAAAAAVzZP37YH13il3tDQy0_ynKIfwQuwx28p-xqes6q9IyH'
    transferData = TransferData(access_token)

    folder_from = input("Enter the Folder path to transfer : -")
     
    folder_to = input("enter the full path to upload to dropbox:- ")
    # API v2
    transferData.upload_folder(folder_from, folder_to)
    print("Folder has been moved !!!")


main()