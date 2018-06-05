from PyInstaller.utils.hooks import copy_metadata, collect_data_files

datas = copy_metadata('filters')
datas += collect_data_files('filters')

#datas += copy_metadata('iota')
#datas += collect_data_files('iota')