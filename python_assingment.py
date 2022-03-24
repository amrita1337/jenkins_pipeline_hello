import shutil
total, used, free = shutil.disk_usage(__file__)
print( int(total/1024), int(used/1024), int(free/1024))
