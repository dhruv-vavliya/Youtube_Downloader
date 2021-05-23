import sys

from cx_Freeze import setup, Executable

setup( name = "Youtube_Downloader",
       version = "3.1",
       description = "youtube_downloader",
       executables = [Executable("youtube_downloader.py",base = "Win32GUI")]
       )



