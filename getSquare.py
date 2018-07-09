from PIL import Image
import math

# Return an Image loaded from the specified file.
#  * filename: string, name of file to load
def load_img(filename):
  im = Image.open(filename)
  return im

# Display Image to the user (for debugging purposes).
#   * im: Image to display
def show_img(im):
  im.show()

# Save the Image to a file with the specified filename,
#  then show the Image to the user.
#  * im: Image to be saved
#  * filename: string, name to save file as
def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

# Return a new Image, with Obamicon filter applied.
#  * im: Image to be filtered
def squareImage(im):

    # load the pixel data from im.
    pixels = im.getdata()

    # get the width and height of the current image
    width, height = im.size

    # will be set to the shortest dimension later on
    newSize = 0

    # create a list to hold the new image pixel data.
    new_pixels = []

    # if image is horizontal
    if(width > height):

        newSize = height
        dif = (width - height) // 2

        row = 0
        while (row * width) < len(pixels):
            rowIndex = row * width

            for col in range(height):
                i = row * width + dif + col
                new_pixels.append(pixels[i])

            row += 1

    # if image is vertical
    else:

        newSize = width
        dif = (height - width)//2

        # moves past the first dif rows
        i = width * dif

        # copies over the next width rows
        widthSqaured = width * width
        for j in range(widthSqaured):
            new_pixels.append(pixels[i])
            i += 1

    # save the new image
    newim = Image.new("RGB", (newSize, newSize))
    newim.putdata(new_pixels)
    return newim
