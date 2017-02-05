def mkImg():
    img = open("pic.ppm",'w')
    img.write("P3 500 500 255\n")
    for x in range(0,250):
        for y in range(0,500):
            img.write("%d %d %d " % ((y%250),(x%250),(255)))
            img.write("%d %d %d " % ((y%250),(x%250),(255)))
        img.write("\n")

mkImg()
