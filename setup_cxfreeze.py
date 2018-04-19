from cx_Freeze import setup, Executable
import sys

base = None
path = sys.path
executables = [Executable("main.py", base=base)]
includeFiles = ['multichaind.exe', 'config.cfg']
includes = []
packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': includeFiles,
        'includes': includes,
        'path': path
    },
}

setup(
    name = "Hardis-Blockchain",
    options = options,
    version = "1",
    description = 'Programme de management du mobilier chez Hardis',
    executables = executables
)