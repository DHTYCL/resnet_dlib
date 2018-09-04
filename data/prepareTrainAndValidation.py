import os
import cv2
import shutil
def makeValiddationSet(pictureRootPath,validationTextFilePath):
    resultTxt=open(validationTextFilePath,'w')
    labelnames = os.listdir(pictureRootPath+'/trains')
    labelnames.sort(reverse = False)
    for filename in labelnames:
        pictureFiles=os.listdir(pictureRootPath+'/trains/'+filename)
        for i in range(0,1000):
            src=pictureRootPath+'/trains/'+filename+'/'+pictureFiles[i]
            dst=pictureRootPath+'/'+'vals'
            shutil.move(src,dst)
            content=filename+' '+pictureFiles[i]+'\n'
            resultTxt.write(content)







def resize_train_image(path,min_size):
    pics=os.listdir(path)
    for pic in pics:
        src=cv2.imread(path+'/'+pic)
        # if (src.shape[0]<min_size or src.shape[1]<min_size):
        #     size=min(src.shape[0:2])
        #     size=max(size,min_size)
        #     print ("%s resize from %d*%d to %d*%d"%(pic,src.shape[0],src.shape[1],size,size))
        #     dst=cv2.resize(src,(size,size))
        #     cv2.imwrite(path+'/'+pic,dst)

        print ("%s resize from %d*%d to %d*%d"%(pic,src.shape[0],src.shape[1],min_size,min_size))
        dst=cv2.resize(src,(min_size,min_size))
        cv2.imwrite(path+'/'+pic,dst)

makeValiddationSet('/home/aitian/QtProject/dlib_resnet/data','/home/aitian/QtProject/dlib_resnet/data/validation.txt')
# path='/home/aitian/QtProject/dlib_resnet/data/train'
# resize_train_image(path,250)
#
# with open('/home/aitian/QtProject/dlib_resnet/data/labels.csv') as f:
#     lines = f.readlines()
#     label_names = []
#     num = 0
#     for line in lines:
#         num += 1
#         if num == 1:
#             continue
#         list = line.split(',')
#         pathDst = '/home/aitian/QtProject/dlib_resnet/data/trains/' + list[1]
#         if list[1] not in label_names:
#             label_names.append(list[1])
#             isExists = os.path.exists(pathDst)
#             if not isExists:
#                 os.makedirs(pathDst)
#         picSrcPath = '/home/aitian/QtProject/dlib_resnet/data/train/' + list[0] + '.jpg'
#         isExisPicFile = os.path.exists(picSrcPath)
#         if isExisPicFile and not os.path.exists(pathDst + list[0] + '.jpg'):
#             shutil.copy2(picSrcPath, pathDst)
#         else:
#             print('not exist!')
#
#     print(num)