#=======================================================================
# Description:
# Publisher module to publish downloaded posters to Google Drive
# Use ChatGPT to figure out how to enable the Google Drive API,
# create and get credentials json and to setup a folder id
# Use Prompt:
# can i get details on how to set up google drive api credentials
#
# The mandatory methods to implement are 
# publishDatabase()
# publishDat()
#=======================================================================

import os
import shutil

from utils.metahelper              import get_app_config
from googleapiclient.http          import MediaFileUpload
from googleapiclient.discovery     import build
from google.oauth2.service_account import Credentials

#=======================================================================
SERVICE_ACCOUNT_FILE = 'templates/publish/key.json'
SCOPES               = ['https://www.googleapis.com/auth/drive.file']
UPLOAD_FOLDER_ID     = '1S5E0vJnggpckQXtCO6F8VmMMuvDzUEaX'
CREDENTIALS          = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SERVICE              = build('drive', 'v3', credentials=CREDENTIALS)

SOURCE_DIRECTORY     = get_app_config('DEFAULT_POSTER_PATH')
BACKUP_FILENAME      = 'pmm_poster_backup.zip'
BACKUP_PATH          = os.path.join('templates', 'publish', 'temp', BACKUP_FILENAME)

#=======================================================================
def generateContent() -> None:
    """
    Create a backup file (e.g., zip file)
    """
    if os.path.exists(BACKUP_PATH):
        os.remove(BACKUP_PATH)

    shutil.make_archive(
        os.path.splitext(BACKUP_PATH)[0],
        'zip',
        SOURCE_DIRECTORY
    )


def publishContent() -> bool:
    """
    Upload a file to Google Drive.
    
    :param file_path: Path to the file to be uploaded.
    :param file_name: Desired name of the file on Google Drive.
    :param folder_id: Optional Google Drive folder ID to upload the file into.
    :return: ID of the uploaded file.
    """
    file_metadata            = {'name': os.path.basename(BACKUP_PATH)}
    file_metadata['parents'] = [UPLOAD_FOLDER_ID]

    media = MediaFileUpload(BACKUP_PATH, resumable=True)
    
    SERVICE.files().create(body=file_metadata, media_body=media, fields='id').execute()
    
    return True

#=======================================================================