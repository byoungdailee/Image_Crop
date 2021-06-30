from posixpath import split
from PIL import Image
import os
import os.path

def image_crop_A(infilename, save_path, stride, patch_x_size, patch_y_size):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = (int)(stride)
    grid_h = (int)(stride)
    range_w = (int)(patch_y_size) #64
    range_h = (int)(patch_x_size) #48
    for w in range(range_w):
        for h in range(range_h):
            a = h*grid_h
            b = w*grid_w
            c = (h+10)*(grid_h)
            d = (w+10)*(grid_w)

            if a+range_h > img_h:
                break
            if b+range_w > img_w:
                break
            if c+range_h > img_h:
                break
            if d+range_w > img_w:
                break
            
            bbox = (a, b, c, d)
            crop_img = img.crop(bbox)
            a = str(grid_h)
            b = str(range_h)
            c = str(range_w)
            fname = "{}.jpg".format(name2+'_'+a+'_'+b+'_'+c+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h)+'_A')
            savename = save_path + fname
            crop_img.save(savename)

def image_crop_C(infilename, save_path, stride, patch_x_size, patch_y_size):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = (int)(stride)
    grid_h = (int)(stride)
    range_w = (int)(patch_y_size)
    range_h = (int)(patch_x_size)
    for w in range(range_w):
        for h in range(range_h):
            a = h*grid_h
            b = w*grid_w
            c = (h+10)*(grid_h)
            d = (w+10)*(grid_w)

            if a+range_h > img_h:
                break
            if b+range_w > img_w:
                break
            if c+range_h > img_h:
                break
            if d+range_w > img_w:
                break
            
            bbox = (a, b, c, d)
            crop_img = img.crop(bbox)
            a = str(grid_h)
            b = str(range_h)
            c = str(range_w)
            fname = "{}.jpg".format(name2+'_'+a+'_'+b+'_'+c+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h)+'_C')
            savename = save_path + fname
            crop_img.save(savename)

def image_crop_B(infilename, save_path, stride, patch_x_size, patch_y_size):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = (int)(stride)
    grid_h = (int)(stride)
    range_w = (int)(patch_y_size)
    range_h = (int)(patch_x_size)
    
    for w in range(range_w):
        for h in range(range_h):
            a = h*grid_h
            b = w*grid_w
            c = (h+10)*(grid_h)
            d = (w+10)*(grid_w)

            if a+range_h > img_h:
                break
            if b+range_w > img_w:
                break
            if c+range_h > img_h:
                break
            if d+range_w > img_w:
                break

            bbox = (a, b, c, d)
            crop_img = img.crop(bbox)
            a = str(grid_h)
            b = str(range_h)
            c = str(range_w)
            fname = "{}.jpg".format(name2+'_'+a+'_'+b+'_'+c+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h)+'_B_')
            savename = save_path + fname
            crop_img.save(savename)

            im = Image.open(savename)
            black = 0
            white = 0
            for i in im.getdata():
                if i == 0:
                    black += 1
                else:
                    white += 1
            total = black + white
            try:
                per = total//white
            except ZeroDivisionError:
                per = 0
            tage = str(per)
            Percentage = tage[0:5]
            print(Percentage)
            os.rename(save_path+name2+'_'+a+'_'+b+'_'+c+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h)+'_B_.jpg', save_path+name2+'_'+a+'_'+b+'_'+c+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h)+'_B_'+Percentage+'.jpg')
            
# 전체 이미지의 white 화소 수 Percentage 계산 함수
def Pixel(save_path, fname):
    im = Image.open(save_path + fname)
    print(im)
    black = 0
    white = 0
    for i in im.getdata():
        if i == 0:
            black += 1
        else:
            white += 1
    total = black + white
    try:
        per = total/white
    except ZeroDivisionError:
        print("ZeroDivision")
    tage = str(per)
    Percentage = tage[0:3]
    return Percentage

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == '__main__':
    f = open('Parameter.txt', 'r', encoding='UTF-8')
    rd = f.read()
    split = rd.split()
    # split[2] patch_x_size
    # split[5] patch_y_size
    # split[8] stride
    # split[11] input_A_directory
    # split[14] input_B_directory
    # split[17] input_C_directory
    # split[20] output_directory

    arr_A = []
    arr_B = []
    arr_C = []
    targerdir_A = split[11] # input_A_directory
    targerdir_B = split[14] # input_B_directory
    targerdir_C = split[17] # input_C_directory
    grid_w = split[8]
    grid_h = split[8]

    files_A = os.listdir(targerdir_A)
    for i in files_A:
        if os.path.isdir(targerdir_A + r"\\" + i):
            pass
        else :
            if i.count(".") == 1 :
                V = i.split(".")
                arr_A.append(V[0])
            else :
                for k in range(len(i)-1,0,-1):
                    if i[k] == ".":
                        break
    
    files_B = os.listdir(targerdir_B)
    for i in files_B:
        if os.path.isdir(targerdir_B + r"\\" + i):
            pass
        else :
            if i.count(".") == 1 :
                V = i.split(".")
                arr_B.append(V[0])
            else :
                for k in range(len(i)-1,0,-1):
                    if i[k] == ".":
                        break
    
    files_C = os.listdir(targerdir_C)
    for i in files_C:
        if os.path.isdir(targerdir_C + r"\\" + i):
            pass
        else :
            if i.count(".") == 1 :
                V = i.split(".")
                arr_C.append(V[0])
            else :
                for k in range(len(i)-1,0,-1):
                    if i[k] == ".":
                        break

    for i in range(len(arr_A)):
        createFolder(split[20]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5])

    for i in range(len(arr_A)):
        createFolder(split[20]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'_A')

    for i in range(len(arr_A)):
        createFolder(split[20]+'/'+arr_B[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'_B')

    for i in range(len(arr_A)):
        createFolder(split[20]+'/'+arr_C[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'_C')

    # for n in arr_A:
    #     filename = split[11]+'/' + n + '.png'
    #     filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_A/'
    #     image_crop_A(filename, filepath, split[8], split[2], split[5])
    
    # for n in arr_B:
    #     filename = split[14]+'/' + n + '.png'
    #     filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_B/'
    #     image_crop_B(filename, filepath, split[8], split[2], split[5])
    
    # for n in arr_C:
    #     filename = split[17]+'/' + n + '.png'
    #     filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_C/'
    #     image_crop_C(filename, filepath, split[8], split[2], split[5])

    # test
    type_model = ['1-1','2-1']
    for n in type_model:
        filename = split[11]+'/' + n + '.png'
        filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_A/'
        image_crop_A(filename, filepath, split[8], split[2], split[5])

    for n in type_model:
        filename = split[14]+'/' + n + '.png'
        filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_B/'
        image_crop_B(filename, filepath, split[8], split[2], split[5])
    
    for n in type_model:
        filename = split[17]+'/' + n + '.png'
        filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_C/'
        image_crop_C(filename, filepath, split[8], split[2], split[5])

    # B 이미지 별로 화소 구하기