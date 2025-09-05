import os
import glob
import shutil

extensions = {
    "jpg": "images",
    "jpeg": "images",
    "png": "images",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "zip": "archive",
    "docx": "word",
    "doc": "word",
    "dmg": "sw installer",
    "txt": "text",
    "ipynb": "python",
    "py": "python",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
}

path = r"" # pass your directory name which you want to sort
verbose = 0

for extension, folder_name in extensions.items():
    # get all the files matching the extension
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Found {len(files)} files with {extension} extension")
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        # create the folder if it does not exist before
        print(f"[+] New {folder_name} folder")
        os.mkdir(os.path.join(path, folder_name))
    for file in files:
        # for each file in that extension, move it to the corresponding folder
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        if verbose:
            print(f"[*] Moving {file} to {dst}")
        shutil.move(file, dst)
