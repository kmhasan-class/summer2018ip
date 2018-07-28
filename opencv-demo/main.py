import cv2
import numpy as np

def convolve(image, kernel):
    output = np.zeros((image.shape), image.dtype)
    for r in range(1, image.shape[0] - 1):
        for c in range(1, image.shape[1] - 1):
            value = 0
            for a in range(0, 3):
                for b in range(0, 3):
                    value = int(int(value) + int(kernel[a][b]) * int(image[r + a - 1, c + b - 1]))
            value = int(value / 8)
            if value < 0:
                value = 0
            if value > 255:
                value = 255
            output[r, c] = value
    return output

print("Hello, World!")
image = cv2.imread("beetroot.jpg")
print("Size", image.size)
print("Dtype", image.dtype)
shape = image.shape
# red = image[row, col][2]
# print(image[100, 100])
# print(red)

#scalar20 = np.array([20, 20, 20])
#image = cv2.add(image, 20)

#CW: turn half the image (column wise) to be grayscale
# for r in range(0, shape[0]):
#     for c in range(0, int(shape[1] / 2)):
#         gray = int((int(image[r, c][0]) + int(image[r, c][1]) + int(image[r, c][2])) / 3)
#         image[r, c] = [gray, gray, gray]

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#HW3: try out the other kernels: Prewitt, Robert, etc.
#HW4: try to find out how we can profile functions in Python -- calculate how much
#time it takes to run a function or some piece of code
kernel = [[-1, 0, +1], [-2, 0, +2], [-1, 0, +1]]
print(kernel)
# this is the output of gx
output = convolve(image, kernel)
#HW1: compute gy
#HW2: combine gx and gy to produce the final output M(x, y) page 706 of your textbook
cv2.imwrite("beetroot1.jpg", output)