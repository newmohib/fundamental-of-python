# Files and Directories

# Absolute Path

# C:\Program Files\Microsoft
# /usr/local/bin

# Relative Path
#

from pathlib import Path

path = Path("ecommerce")
# Return True/False if this path exists
print(path.exists())

# Create a Directory
# path = Path("emails")
# print(path.mkdir())

# Remove Directory
# print(path.rmdir())

# search all file and directory from current directory using glob() functions

path = Path()


# files are iterate return

# return only all files
files = path.glob("*.*")
# return only py extensions file
files = path.glob("*.py")
# all file and directory
files = path.glob("*")

for file in files:
    print(file)




