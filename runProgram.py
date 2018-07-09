import getSquare    # where the sqaure function is
import os

def main():

    # indir is the directory where your images are found
    indir = '/Users/daryaverzhbinsky/CODE/FUN/Projects/PhotoMadeUpOfPhotos'

    # used to name the images
    i = 0

    # goes through the files in the directory and checks if they are .jpg
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if f[-4] == '.' and f[-3] == 'j' and f[-2] == 'p':

                # new name for the new image
                newPhotoName = "newPhotos/newImage" + str(i) + ".jpg"
                i += 1
                img = getSquare.load_img(f)

                # Apply filters!
                newimg = getSquare.squareImage(img)

                getSquare.save_img(newimg, newPhotoName)

if __name__ == '__main__':
    main()
