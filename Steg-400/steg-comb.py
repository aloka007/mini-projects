from PIL import Image

width,height = 400,400

imA = Image.open("galaxy.bmp")
imB = Image.open("dog.bmp")

imC = Image.new("RGB", (width,height), "white")

pixA = imA.load()
pixB = imB.load()
pixC = imC.load()

#range compress function
def r_compress(tup):
    s = 64 #compress by this amount
    res = ((tup[0]/s)*s,(tup[1]/s)*s,(tup[2]/s)*s)
    return res

def compress(tup):
    s = 64 #compress by this amount
    res = ((tup[0]/s),(tup[1]/s),(tup[2]/s))
    return res

print imA.size #Get the width and hight of the image for iterating over
#print pix[399,399] #Get the RGBA Value of the a pixel of an image

#scanning loop
for i in range(0,width):
    print "processing...","(",i,"/",width,")"
    for j in range(0,height):
        #print i,j," - ",pixA[i,j]," - ",pixB[i,j]
        
        pixB[i,j] = compress(pixB[i,j])

        #pixA[i,j] = pixA[i,j]
        
        pixC[i,j] = (
            ((pixA[i,j])[0]+(pixB[i,j])[0])%255,
            ((pixA[i,j])[1]+(pixB[i,j])[1])%255,
            ((pixA[i,j])[2]+(pixB[i,j])[2])%255
            )

imB.save("comp.bmp")
imC.save("steg.bmp")
print "done"


    
