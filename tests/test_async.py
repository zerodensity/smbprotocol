import os

import pytest
import threading

from smbclient import (
    register_session,
    open_file
)


def read_in_chunks(file_object, chunk_size=10 * 1024 * 1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def write_to_file(local_dir, remote_dir):
    f = open(local_dir, "wb")
    with open_file(remote_dir, mode="rb") as fd:
        for chunk in read_in_chunks(fd):
            print(local_dir, "is being copied.")
            f.write(chunk)


def test_async_download_two_files():
    register_session("ZDHQ-HUB", username="reality", password="reality")
    thread1 = threading.Thread(target=write_to_file, args=("example1.dmp", r"\\ZDHQ-HUB\RealityWorkspace\example.dmp"))
    thread2 = threading.Thread(target=write_to_file, args=("example2.dmp", r"\\ZDHQ-HUB\RealityWorkspace\example2.dmp"))

    thread1.daemon = False
    thread2.daemon = False

    thread1.start()
    thread2.start()


def test_show_cur_dir():
    print(os.getcwd())
