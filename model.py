import os
path = "/Users/cheng_louebrf/Desktop/python/class99/abc.txt"
root_ext=os.path.splitext(path)
print("root part",root_ext[0])
print("ext part",root_ext[1],"\n")