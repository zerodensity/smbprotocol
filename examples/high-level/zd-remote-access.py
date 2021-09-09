import sys

from smbclient import (
    listdir,
    mkdir,
    register_session,
    rmdir,
    scandir,
    stat_volume,
    open_file
)

from smbclient.path import (
    isdir,
)

# Optional - register the server with explicit credentials
register_session("ZDHQ-HUB", username="reality", password="reality")

# # List the files/directories inside a dir
# for filename in listdir(r"\\ZDHQ-HUB\RealityWorkspace"):
#     print(filename)

# Use scandir as a more efficient directory listing as it already contains info like stat and attributes.
# for file_info in scandir(r"\\ZDHQ-HUB\RealityWorkspace"):
#     file_inode = file_info.inode()
#     if file_info.is_file():
#         print("File: %s %d" % (file_info.name, file_inode))
#     elif file_info.is_dir():
#         print("Dir: %s %d" % (file_info.name, file_inode))
#     else:
#         print("Symlink: %s %d" % (file_info.name, file_inode))

print(stat_volume(r"\\ZDHQ-HUB/RealityWorkspace/example.dmp"))


# def read_in_chunks(file_object, chunk_size=4096):
#     while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data
#
#
# import time
#
# start_time = time.time()
# size_of_file = 0
# # Read an existing file as bytes
# with open_file(r"\\ZDHQ-HUB\RealityWorkspace\example.dmp", mode="rb", username="reality", password="reality") as fd:
#     for chunk in read_in_chunks(fd):
#         size_of_file += len(chunk)
#         # print(chunk, end="")
#         sys.stdout.buffer.write(chunk)
#
# print(size_of_file)
# print("--- %s seconds ---" % (time.time() - start_time))
