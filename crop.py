from PIL import Image
import os

def image_crop(infilename, save_path):
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
            fname = "{}.jpg".format(name2+'_'+"{0:03d}".format(w)+'_'+"{0:03d}".format(h))
            savename = save_path + fname
            crop_img.save(savename)

if __name__ == '__main__':
    filename = input("filename")
    filepath = input("filepath")
    image_crop(filename, filepath)

    # 'test/test_A/90-1.png', 'test/test_A/90-1/'