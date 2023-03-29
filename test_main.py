import os
import datetime
import shutil

import main


def test_create_daily_card_folder():
    scrintal_folder: str = "scrintal"
    if not os.path.isdir(scrintal_folder):
        os.mkdir(scrintal_folder)
        print("create folder: {}", scrintal_folder)

    main.create_daily_card_folder(scrintal_folder)

    today = datetime.date.today().strftime("%Y%m%d")
    today_dir = os.path.join(scrintal_folder, today)

    assert not os.path.isdir(today_dir)

    shutil.rmtree(scrintal_folder, ignore_errors=True)
