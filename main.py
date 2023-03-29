import datetime
import os
import string
import dropbox

PARENT_DIR = os.path.expanduser("~")
DROPBOX_FOLDER_DIR = os.path.join(PARENT_DIR, "Dropbox")
SCRINTAL_DIR = os.path.join(DROPBOX_FOLDER_DIR, "Scrintal")
SCRINTAL_EVERYDAY_DIR = os.path.join(SCRINTAL_DIR, "每日卡片")


def create_daily_card_folder(scrintal_dir: string):
    today = datetime.date.today().strftime("%Y%m%d")

    if not os.path.isdir(scrintal_dir):
        print("{} don't exist".format(scrintal_dir))

    scrintal_everyday_dir = os.path.join(scrintal_dir, "每日卡片")
    if not os.path.isdir(scrintal_everyday_dir):
        os.mkdir(scrintal_everyday_dir)
        print("create folder: ", scrintal_everyday_dir)

    today_dir_in_dropbox = os.path.join(scrintal_everyday_dir, today)
    if not os.path.isdir(today_dir_in_dropbox):
        os.mkdir(today_dir_in_dropbox)
        print("create folder: ", today_dir_in_dropbox)


def startup_dropbox():
    dropbox.start_dropbox()


if __name__ == '__main__':
    startup_dropbox()
    create_daily_card_folder(SCRINTAL_DIR)
