# this file contains some common code snipets to help us develop faster.

# ----------------------------------------------------------------------------------------
# files
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()

# 'r' 	Open for reading (default)
# 'w' 	Open for writing, truncating (overwriting) the file first
# 'rb' or 'wb' 	Open in binary mode (read/write using byte data)
with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here

# more info on reading a writing files: https://realpython.com/read-write-files-python/
# ----------------------------------------------------------------------------------------


# test commit