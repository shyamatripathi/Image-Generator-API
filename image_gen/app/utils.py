# app/utils.py
import os, time

def cleanup_old_images(directory='outputs/images', age=3600):
    now = time.time()
    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        if os.path.isfile(path) and os.stat(path).st_mtime < now - age:
            os.remove(path)
