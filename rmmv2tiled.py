# RMMV convert to Tiled
import os
from PIL import Image

path = './png/'
savepath = './convert/'
tilesize = 16

if not(os.path.exists(path) or os.path.exists(savepath)):
    print('pngpath or savepath no exist.')
    exit(1)

tw = 16*4
th = 16*6
filelist = os.listdir(path)
for item in filelist:
    im = Image.open(path + item)
    width, height = im.size[:2]
    saveim = Image.new("RGBA",(int(width*2),int(height/3*2)))
    print('image:%s (width:%d, height:%d) convert to (width:%d, height:%d)'%(item,width,height,saveim.size[0],saveim.size[1]))


    bx = by = nbx = nby = 0
    for h in range(int(height / th)):
        for w in range(int(width / tw)):
            bx = int(w*tw)
            by = int(h*th)
            nbx = int(w*(tw*2))
            nby = int(h*(th/3*2))

            # copy row 3 - 6
            for y in range(tw):
                for x in range(tw):
                    r, g, b, a = im.getpixel((bx + x, by + tilesize * 2 + y))
                    saveim.putpixel((nbx + tilesize*4 + x, nby + y),(r,g,b,a))

            # copy 8
            left = bx + tilesize*3
            top = by + tilesize
            right = left + tilesize
            bottom = top + tilesize
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize):
                for x in range(tilesize):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x, nby + y),(r,g,b,a))

            # copy 7
            left = bx + tilesize*2
            top = by + tilesize
            right = left + tilesize
            bottom = top + tilesize
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize):
                for x in range(tilesize):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x + tilesize*3, nby + y),(r,g,b,a))

            # copy 4
            left = bx + tilesize*3
            top = by
            right = left + tilesize
            bottom = top + tilesize
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize):
                for x in range(tilesize):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x, nby + y + tilesize*3),(r,g,b,a))

            # copy 3
            left = bx + tilesize*2
            top = by
            right = left + tilesize
            bottom = top + tilesize
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize):
                for x in range(tilesize):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x + tilesize*3, nby + y + tilesize*3),(r,g,b,a))

            # copy 10 11
            left = bx + tilesize
            top = by + tilesize*2
            right = left + tilesize*2
            bottom = top + tilesize
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize):
                for x in range(tilesize*2):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x + tilesize, nby + y + tilesize*3),(r,g,b,a))

            # copy 16 20
            left = bx + tilesize*3
            top = by + tilesize*3
            right = left + tilesize
            bottom = top + tilesize*2
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize*2):
                for x in range(tilesize):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x, nby + y + tilesize),(r,g,b,a))

            # copy 22 23
            left = bx + tilesize
            top = by + tilesize*5
            right = left + tilesize*2
            bottom = top + tilesize
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize):
                for x in range(tilesize*2):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x + tilesize, nby + y),(r,g,b,a))

            # copy 13 17
            left = bx
            top = by + tilesize*3
            right = left + tilesize
            bottom = top + tilesize*2
            tmpimg = im.crop((left,top,right,bottom))
            for y in range(tilesize*2):
                for x in range(tilesize):
                    r, g, b, a = tmpimg.getpixel((x,y))
                    saveim.putpixel((nbx + x + tilesize*3, nby + y + tilesize),(r,g,b,a))

    saveim.save(savepath + item)
    print('image of %s is converted.'%(item))


