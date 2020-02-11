import os

video_path = r"E:\数据分析与机器学习"

all_file = os.listdir(video_path)

file_list = [os.path.join(video_path, file) for file in all_file]

for file in file_list:
    if os.path.splitext(file)[-1] in [".flv", ".swf"]:
        if "[www.zxit8.com 自学IT吧论坛]" in file:
            new_file_name = file.replace("[www.zxit8.com 自学IT吧论坛]", "")
            os.rename(file, new_file_name)
            print("{}->{}".format(file, new_file_name))
