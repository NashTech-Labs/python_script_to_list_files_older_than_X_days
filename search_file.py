import os
import datetime

file_age_days=90
current_age=datetime.datetime.now()

for directory,dirpath,file_name in os.walk("/var/log"):
    for file in file_name:
        absolute_path=os.path.join(directory,file)
        file_creation_time=datetime.datetime.fromtimestamp(os.path.getctime(absolute_path))
        time_difference=(current_age-file_creation_time).days
        if time_difference> file_age_days:
            print(absolute_path, time_difference)