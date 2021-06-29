from PIL import Image
import os
import os.path

def image_crop_A(infilename, save_path):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = 10
    grid_h = 10
    range_w = (int)(img_w/grid_w)
    range_h = (int)(img_h/grid_h)
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

def image_crop_C(infilename, save_path):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = 10
    grid_h = 10
    range_w = (int)(img_w/grid_w)
    range_h = (int)(img_h/grid_h)
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

def image_crop_B(infilename, save_path):
    name = os.path.basename(infilename)
    name2 = os.path.splitext(name)[0]
    img = Image.open( infilename )
    (img_h, img_w) = img.size
    grid_w = 10
    grid_h = 10
    range_w = (int)(img_w/grid_w)
    range_h = (int)(img_h/grid_h)
    im = Image.open(infilename)
    black = 0
    white = 0
    for i in im.getdata():
        if i == 0:
            black += 1
        else:
            white += 1
    total = black + white
    per = total/white
    tage = str(per)
    Percentage = tage[0:5]
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
            fname = "{}.jpg".format(name2+'_'+a+'_'+b+'_'+c+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h)+'_B_'+Percentage)
            savename = save_path + fname
            crop_img.save(savename)

# 전체 이미지의 white 화소 수 Percentage 계산 함수
def Pixel(infilename):
    im = Image.open(infilename)
    black = 0
    white = 0
    for i in im.getdata():
        if i == 0:
            black += 1
        else:
            white += 1
    total = black + white
    per = total/white
    return per

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == '__main__':
    arr_A = []
    arr_B = []
    arr_C = []
    targerdir_A = r"train/train_A"
    targerdir_B = r"train/train_B"
    targerdir_C = r"train/train_C"

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
        createFolder('OutputImage/'+arr_A[i]+'_10_64_48')

    for i in range(len(arr_A)):
        createFolder('OutputImage/'+arr_A[i]+'_10_64_48/'+arr_A[i]+'_10_64_48_A')

    for i in range(len(arr_A)):
        createFolder('OutputImage/'+arr_B[i]+'_10_64_48/'+arr_B[i]+'_10_64_48_B')

    for i in range(len(arr_A)):
        createFolder('OutputImage/'+arr_C[i]+'_10_64_48/'+arr_C[i]+'_10_64_48_C')

    for n in arr_A:
        filename = 'train/train_A/' + n + '.png'
        filepath = 'OutputImage/'+ n +'_10_64_48/'+ n +'_10_64_48_A/'
        image_crop_A(filename, filepath)

    for n in arr_B:
        filename = 'train/train_B/' + n + '.png'
        filepath = 'OutputImage/'+ n +'_10_64_48/'+ n +'_10_64_48_B/'
        image_crop_B(filename, filepath)

    for n in arr_C:
        filename = 'train/train_C/' + n + '.png'
        filepath = 'OutputImage/'+ n +'_10_64_48/'+ n +'_10_64_48_C/'
        image_crop_C(filename, filepath)
