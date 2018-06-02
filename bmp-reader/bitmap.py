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

    #H/W #1
    def set_pixel(self, row, col, red, green, blue):
        print("Do something!")
        self.byte_array[124] = red
        self.byte_array[123] = green
        self.byte_array[122] = blue


    #H/W #2
    #Write a method to flip an image horizontally
    #and another one to flip the image vertically

    #H/W #3
    #Write a method to increase the brightness of an
    #image by 25%


    def write_file(self, filename):
        file = open(filename, "wb")
        try:
            file.write(self.byte_array)
        finally:
            file.close()


#write a method in this class that writes the output to a file


print("Hello IP...")
bitmap = Bitmap()
bitmap.read_file("test.bmp")
print("Pixel 0, 0", bitmap.get_pixel(0, 199))
bitmap.set_pixel(0, 0, 255, 255, 0)
bitmap.write_file("output.bmp")
