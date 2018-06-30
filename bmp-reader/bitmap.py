import os

class Bitmap:
    def read_file(self, filename):
        file = open(filename, "rb")
        try:
            filesize = os.path.getsize(filename)
            print("Reading from", filename)
            print("File size", filesize)
            self.byte_array = bytearray(file.read(filesize))
            self.width = self.convertToInteger(reversed(self.byte_array[18:22]))
            print("Width", self.width)
            self.height = self.convertToInteger(reversed(self.byte_array[22:26]))
            print("Height", self.height)
            self.data_offset = self.convertToInteger(reversed(self.byte_array[10:14]))
        finally:
            file.close()


    def convertToInteger(self, array):
    #input 0 2 191 154
    #output 180122
        sum = 0
        for value in array:
            sum = sum * 256
            sum = sum + value
        return sum


    def get_pixel(self, row, col):
        offset = self.data_offset + (row * self.width + col) * 3
        red = self.byte_array[offset + 2]
        green = self.byte_array[offset + 1]
        blue = self.byte_array[offset + 0]
        return red, green, blue


    def get_offset(self, row, col):
        offset = self.data_offset + (row * self.width + col) * 3
        return offset


    #H/W #1
    def set_pixel(self, row, col, red, green, blue):
        offset = self.get_offset(row, col)
        self.byte_array[offset + 2] = red
        self.byte_array[offset + 1] = green
        self.byte_array[offset + 0] = blue


    #H/W #2
    #Write a method to flip an image horizontally
    #and another one to flip the image vertically
    def flip_horizontal(self):
        half_width = int(self.width / 2)
        for r in range(0, self.height):
            for c in range(0, half_width):
                pixel1 = self.get_pixel(r, c)
                pixel2 = self.get_pixel(r, self.width - 1 - c)
                self.set_pixel(r, c, pixel2[0], pixel2[1], pixel2[2])
                self.set_pixel(r, self.width - 1 - c, pixel1[0], pixel1[1], pixel1[2])


    #Task for class
    #Write a method to flip an image vertically
    def flip_vertical(self):
        half_height = int(self.height / 2)
        for r in range(0, half_height):
            for c in range(0, self.width):
                pixel1 = self.get_pixel(r, c)
                pixel2 = self.get_pixel(self.height - 1 - r, c)
                self.set_pixel(r, c, pixel2[0], pixel2[1], pixel2[2])
                self.set_pixel(self.height - 1 - r, c, pixel1[0], pixel1[1], pixel1[2])


    #H/W #3
    #Write a method to increase the brightness of an
    #image by 25%
    def increase_brightness(self, factor):
        brightness_factor = 1 + factor
        for r in range(0, self.height):
            for c in range(0, self.width):
                red, green, blue = self.get_pixel(r, c)
                red, green, blue = red * brightness_factor, green * brightness_factor, blue * brightness_factor
                if red > 255:
                    red = 255
                if green > 255:
                    green = 255
                if blue > 255:
                    blue = 255
                self.set_pixel(r, c, int(red), int(green), int(blue))


    def write_file(self, filename):
        file = open(filename, "wb")
        try:
            file.write(self.byte_array)
        finally:
            file.close()


    def convert_to_grayscale_average_method(self):
        for r in range(0, self.height):
            for c in range(0, self.width):
                red, green, blue = self.get_pixel(r, c)
                average = int((red + green + blue) / 3)
                self.set_pixel(r, c, average, average, average)


    def extract_red_channel(self):
        for r in range(0, self.height):
            for c in range(0, self.width):
                red, green, blue = self.get_pixel(r, c)
                #average = int((red + red + red) / 3)
                self.set_pixel(r, c, red, red, red)


    # C/W #1
    # do the extraction for G and B. And also for C, M, Y and K.

    # C/W #2
    # implement the other two grayscale conversion methods

    # C/W #3
    # write a method that blurs the image (3x3 radius)



                # H/W #4
    # rotate the image clockwise by 90 degrees
    #def rotate_clockwise_90(self):

    # H/W #5
    # rotate the image counter clockwise by 90 degrees
    #def rotate_counter_clockwise_90(self):


    # H/W #6
    # create a cropped version of the current image
    #def crop(self, start_row, start_col, end_row, end_col):


    # H/W #7
    # create a blank bitmap based on the dimension given
    #def create_bitmap(self, width, height):


    # H/W #8
    # have a look at HIPR (Worksheet - Image Arithmetic, in particular)

#write a method in this class that writes the output to a file

def convert_to(number_in_decimal, base):
    number = number_in_decimal
    digits = []
    while number > 0:
        digit = number % base
        number = int(number / base)
        digits.append(digit)
    #H/W: make sure you return the reversed result
    return digits


print("Hello IP...")
print(convert_to(180122, 256))
bitmap = Bitmap()
bitmap.read_file("beetroot1.bmp")
#bitmap.read_file("test1.bmp")
print("Pixel 0, 0", bitmap.get_pixel(0, 199))
#
# for c in range(0, 50):
#     bitmap.set_pixel(3, c, 255, 255, 0)
# bitmap.flip_vertical()
#bitmap.rotate_clockwise_90()
#bitmap.increase_brightness(0.25)
#bitmap.convert_to_grayscale_average_method()
bitmap.extract_red_channel()
bitmap.write_file("beetroot2.bmp")
#bitmap.write_file("test2.bmp")
