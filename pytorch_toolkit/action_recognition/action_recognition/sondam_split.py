import os

data_dir_path = '/home/sci2019/Downloads/200312_2d_recorder_(1)'
for name in os.listdir(data_dir_path):
    state = False
    for folderName in os.listdir(data_dir_path + '/' + name):
        # file_list_mp4 = [file for file in folderName if file.endswith(".mp4")]
        for fileName in os.listdir(data_dir_path + '/' + name + '/' + folderName):
        # for fileName in file_list_mp4:
            # fileName = folder2Name.split('_')[:-1]
            print(fileName)
            if state == False:
                f = open(fileName + '.txt', 'w')
                state = True

            f.write(fileName+' \n')

f.close()

