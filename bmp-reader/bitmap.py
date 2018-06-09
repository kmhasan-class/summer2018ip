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
            for c in range(0, half_width, 3):
                r1, c1 = r, c
                offset1 = self.get_offset(r1, c1)
                r2, c2 = r, self.width - c - 3
                # print(r1, c1, " <---> ", r2, c2)
                offset2 = self.get_offset(r2, c2)
                #self.byte_array[offset1 + 0], self.byte_array[offset2 + 0] = self.byte_array[offset2 + 0], self.byte_array[offset1 + 0]
                self.byte_array[offset1 + 1], self.byte_array[offset2 + 1] = self.byte_array[offset2 + 1], self.byte_array[offset1 + 1]
                # self.byte_array[offset1 + 2], self.byte_array[offset2 + 2] = self.byte_array[offset2 + 2], self.byte_array[offset1 + 2]



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


#write a method in this class that writes the output to a file


print("Hello IP...")
bitmap = Bitmap()
bitmap.read_file("beetroot1.bmp")
# bitmap.read_file("test1.bmp")
print("Pixel 0, 0", bitmap.get_pixel(0, 199))
#
# for c in range(0, 50):
#     bitmap.set_pixel(3, c, 255, 255, 0)
#bitmap.flip_horizontal()
bitmap.increase_brightness(0.25)
bitmap.write_file("beetroot2.bmp")
# bitmap.write_file("test2.bmp")
