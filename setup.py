import sys
from cx_Freeze import setup, Executable

copyDependentFiles = True
silent = True
base = None
packages = []
includes = []
excludes = ['PyQt4', 'PyQt5']

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = '稼働分析用ストップウォッチ',
    version = '0.0.0.2',
    options = {'build_exe': {'includes': includes, 'excludes': excludes, 'packages': packages}},
    executables = [Executable('kadou_bunseki.py', base=base)]
)
