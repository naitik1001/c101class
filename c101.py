
import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BBMDvbyWl2upKXirDUTwua3g_m7OwUrOPFxNFZODxwWmVbAzWOJeqnnrtKuNUIFL1jF1pqcntgLdpx7QDu-oPCvX2nU2SyoBm2zNNpYFm4alKvai58ePRwAzQBW1xVXBbiNmTNc'
    transferData = TransferData(access_token)

    file_from = input("enter the full path of the file to transfer")
    file_to = input("enter the full path to upload to dropbox")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()
        

