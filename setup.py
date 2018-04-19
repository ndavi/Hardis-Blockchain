from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]
includeFiles = ['multichaind.exe', 'config.cfg']

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': includeFiles,
    },
}

setup(
    name = "Hardis-Blockchain",
    options = options,
    version = "1",
    description = 'Programme de management du mobilier chez Hardis',
    executables = executables
)