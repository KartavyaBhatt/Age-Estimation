import os

folder = "/home/joker/Downloads/00"
temp = "/home/joker/Downloads/00_1"
for filename in os.listdir(folder):
    start = '_'
    end = '-'
    birth = (filename.split(start))[1].split(end)[0]

    today = filename[-8:-4]

    age = int(today) - int(birth)
    age = str(age)

    directory = temp+'/'+age
    if not os.path.exists(directory):
        os.makedirs(directory)

    os.rename(folder+'/'+filename, temp+'/'+age+'/'+filename[0:-5]+'('+age+')'+filename[-4:])