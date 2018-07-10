import getSquare    # where the sqaure function is
import os

def main():

    # indir is the directory where your images are found
    indir = '/Users/Ilyav 1/Desktop/BabaBirthday2018/TestPhotoBank/all'
    outdir = '/Users/Ilyav 1/Desktop/BabaBirthday2018/TestPhotoBank/cropped'
    # used to name the images
    i = 0

    # goes through the files in the directory and checks if they are .jpg
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if f[-4:] != '.mov' and f[-4:] != '.MOV' and f[0] != '.':
               # print(indir + '/' + f)

                print('cropping .... ' + f)
                
                
                # new name for the new image
                newPhotoName = outdir + '/' + 'IM_' + format(i,'04d') + "_cropped.jpg"
                
                #create output directory
                if not os.path.exists(outdir):
                    print("output path doesn't exist. trying to make")
                    os.makedirs(outdir)
                
                
                i += 1

                imPath = indir + '/' + f
                img = getSquare.load_img(imPath)

                # Apply filters!
                newimg = getSquare.squareImage(img)
                
                print('saving to .... ' + newPhotoName) 
                getSquare.save_img(newimg, newPhotoName)

if __name__ == '__main__':
    main()
