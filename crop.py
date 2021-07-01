from posixpath import split
from PIL import Image
import os
import os.path

def image_crop_A(infilename, save_path, stride, patch_x_size, patch_y_size, A):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = (int)(stride) #10
    grid_h = (int)(stride) #10
    range_w = (int)(patch_y_size) #48
    range_h = (int)(patch_x_size) #64
    ran_w = range_w/10
    ran_h = range_h/10
    num1 = ((img_h-range_h)//grid_w)+1 #58
    num2 = ((img_w-range_w)//grid_w)+1 #44
    for w in range(0,num2):
        for h in range(0,num1):
            a = h*grid_h
            b = w*grid_w
            c = (h+ran_h)*(grid_h)
            d = (w+ran_w)*(grid_w)
            bbox = (a, b, c, d)
            crop_img = img.crop(bbox)
            z = str(grid_h)
            n = str(range_h)
            m = str(range_w)
            wi = str(w)
            he = str(h)
            fname = "{}.jpg".format(name2+'_'+z+'_'+n+'_'+m+'_'+wi+'_'+he+'_'+A)
            savename = save_path + fname
            crop_img.save(savename)

def image_crop_C(infilename, save_path, stride, patch_x_size, patch_y_size, B):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = (int)(stride) #10
    grid_h = (int)(stride) #10
    range_w = (int)(patch_y_size) #48
    range_h = (int)(patch_x_size) #64
    ran_w = range_w/10
    ran_h = range_h/10
    num1 = ((img_h-range_h)//grid_w)+1 #58
    num2 = ((img_w-range_w)//grid_w)+1 #44
    for w in range(0,num2):
        for h in range(0,num1):
            a = h*grid_h
            b = w*grid_w
            c = (h+ran_h)*(grid_h)
            d = (w+ran_w)*(grid_w)
            bbox = (a, b, c, d)
            crop_img = img.crop(bbox)
            z = str(grid_h)
            n = str(range_h)
            m = str(range_w)
            wi = str(w)
            he = str(h)
            fname = "{}.jpg".format(name2+'_'+z+'_'+n+'_'+m+'_'+wi+'_'+he+'_'+C)
            savename = save_path + fname
            crop_img.save(savename)

def image_crop_B(infilename, save_path, stride, patch_x_size, patch_y_size, B):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = (int)(stride)
    grid_h = (int)(stride)
    range_w = (int)(patch_y_size)
    range_h = (int)(patch_x_size)
    ran_w = range_w/10
    ran_h = range_h/10
    num1 = ((img_h-range_h)//grid_w)+1 #58
    num2 = ((img_w-range_w)//grid_w)+1 #44
    for w in range(num2):
        for h in range(num1):
            a = h*grid_h
            b = w*grid_w
            c = (h+ran_h)*(grid_h)
            d = (w+ran_w)*(grid_w)
            bbox = (a, b, c, d)
            crop_img = img.crop(bbox)
            z = str(grid_h)
            n = str(range_h)
            m = str(range_w)
            wi = str(w)
            he = str(h)
            fname = "{}.jpg".format(name2+'_'+z+'_'+n+'_'+m+'_'+wi+'_'+he+'_'+B+'_')
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
            wh = str(white)
            os.rename(save_path+name2+'_'+z+'_'+n+'_'+m+'_'+wi+'_'+he+'_'+B+'_.jpg', save_path+name2+'_'+z+'_'+n+'_'+m+'_'+wi+'_'+he+'_'+B+'_'+wh+'.jpg')
            black = 0

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
    tarA = split[11]
    tarB = split[14]
    tarC = split[17]
    A = tarA[-1]
    B = tarB[-1]
    C = tarC[-1]
    # print(A,B,C)
    
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
        createFolder(split[20]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+A)

    for i in range(len(arr_A)):
        createFolder(split[20]+'/'+arr_B[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+B)

    for i in range(len(arr_A)):
        createFolder(split[20]+'/'+arr_C[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+arr_A[i]+'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+C)

    for n in arr_A:
        filename = split[11]+'/' + n + '.png'
        filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+A+'/'
        image_crop_A(filename, filepath, split[8], split[2], split[5], A)
    
    for n in arr_B:
        filename = split[14]+'/' + n + '.png'
        filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+B+'/'
        image_crop_B(filename, filepath, split[8], split[2], split[5], B)
    
    for n in arr_C:
        filename = split[17]+'/' + n + '.png'
        filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+C+'/'
        image_crop_C(filename, filepath, split[8], split[2], split[5], C)

    # # test
    # type_model = ['1-1','2-1']
    # for n in type_model:
    #     filename = split[11]+'/' + n + '.png'
    #     filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+A+'/'
    #     image_crop_A(filename, filepath, split[8], split[2], split[5], A)

    # for n in type_model:
    #     filename = split[14]+'/' + n + '.png'
    #     filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+B+'/'
    #     image_crop_B(filename, filepath, split[8], split[2], split[5], B)
    
    # for n in type_model:
    #     filename = split[17]+'/' + n + '.png'
    #     filepath = split[20]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'/'+ n +'_'+split[8]+'_'+split[2]+'_'+split[5]+'_'+C+'/'
    #     image_crop_C(filename, filepath, split[8], split[2], split[5], C)