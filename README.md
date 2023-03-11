# Memory Backup
This tool can be used to backup your pictures to a safe place. You may scan your entire disk or a portion of your disk, and it will avoid duplication of pictures using the SHA-512 Algorithm.

## Screenshot
!["Screenshot"](https://i.ibb.co/qkZYYGz/Screenshot-9.png "Screenshot of 'start.py'")

## Working
- You give it the path of the directory where all your pictures live as the first argument.
- It scans the entire directory including all the sub-directories for given file formats (default are PNG, GIF, JPG and JPEG).
- Whenever it finds the matching file, it generates the SHA-512 hash of that file.
- Then, it checks if the hash is already present in a 'MAP File' in the destination.
- If so, it avoids saving that file as it's already saved in the destination directory.
- If the hash seems new, it copies that file to the 'saved' folder in the destination directory. On success, it adds the hash of that file to the 'MAP File' to avoid duplication in the future.

This way, if you scan your disk regularly, all your pictures will get backed up to the destination directory without backing up the files again it had already backed up in the past.

## How to use
Let's say you want to backup all the pictures inside your 'C:' Drive to an external storage device labelled 'D:'.
1. Replace content inside the `destination.txt` file with your destination path. Let's say `D:\Backup Files`.
2. Run this command to start the backup process: `python start.py [SOURCE-PATH]`
`[SOURCE-PATH]`  is the path from where all your pictures will get backed up. For example: `python start.py C:\Users\john`.

## Follow Me
**Twitter:** [@inosMooon](https://twitter.com/inosMooon)
**GitHub:** [@MoonStorage](https://github.com/MoonStorage)