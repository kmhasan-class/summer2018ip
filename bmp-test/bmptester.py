import os

filename1 = "image1.bmp"
filename2 = "image2.bmp"

filesize1 = os.path.getsize(filename1)
filesize2 = os.path.getsize(filename2)

file1 = open(filename1, "rb")
file2 = open(filename2, "rb")

byte_array1 = bytearray(file1.read(filesize1))
byte_array2 = bytearray(file2.read(filesize2))

print("Size of image1 ", filesize1)
print("Size of image2 ", filesize2)

print("Image 1 Bytes [2, 5]:", list(byte_array1[2:6]))
print("Image 2 Bytes [2, 5]:", list(byte_array2[2:6]))

print("Image 1 Bytes [34, 37]:", list(byte_array1[34:38]))
print("Image 2 Bytes [34, 37]:", list(byte_array2[34:38]))

for i in range(0, 54):
    # if byte_array1[i] != byte_array2[i]:
        print(i, byte_array1[i], byte_array2[i])