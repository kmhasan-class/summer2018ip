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


def basicGlobalThresholding(image):
    frequency = np.zeros(256, int)
#    print(frequency)

    # calculate the frequency
    for r in range(0, image.shape[0]):
        for c in range(0, image.shape[1]):
            intensity = image[r][c]
            frequency[intensity] = frequency[intensity] + 1

    cumulativeFrequency = np.zeros(256, int)
    cumulativeFrequency[0] = frequency[0]
    for i in range(1, 256):
        cumulativeFrequency[i] = frequency[i] + cumulativeFrequency[i - 1]

    product = np.zeros(256, int)
    for i in range(0, 256):
        product[i] = frequency[i] * i

    cumulativeProduct = np.zeros(256, int)
    cumulativeProduct[0] = product[0]
    for i in range(1, 256):
        cumulativeProduct[i] = product[i] + cumulativeProduct[i - 1]

    iteration = 1
    T = int(cumulativeProduct[255] / cumulativeFrequency[255])
    while True:
        m1 = cumulativeProduct[T] / cumulativeFrequency[T]
        m2 = (cumulativeProduct[255] - cumulativeProduct[T]) / (cumulativeFrequency[255] - cumulativeFrequency[T])
        m = (m1 + m2) / 2
        print("Iteration: ", iteration, "T", T, "m1", m1, "m2", m2, "m", m)
        if T == int(m):
            break
        T = int(m)
        iteration = iteration + 1


    return T


def applyThreshold(image, T):
    output = np.zeros((image.shape), image.dtype)
    for r in range(0, image.shape[0]):
        for c in range(0, image.shape[1]):
            if image[r, c] <= T:
                output[r, c] = 0
            else:
                output[r, c] = 255
    return output


print("Hello, World!")
image = cv2.imread("spider.jpeg")
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
canny = cv2.Canny(image, 70, 90)
cv2.imwrite("canny.jpg", canny)
print("Dimension of Canny: ", canny.shape)
print("Dimension of Image: ", image.shape)
print("Dtype of Canny: ", canny.dtype)
print("Dtype of Image: ", image.dtype)
print("Pixel [0, 0] of Canny: ", canny[0, 0])
print("Pixel [0, 0] of Image: ", image[0, 0])

thresholdedImage = applyThreshold(image, basicGlobalThresholding(image))
cv2.imwrite("threshold1.jpg", thresholdedImage)
thresholdedImage = applyThreshold(image, 127)
cv2.imwrite("threshold2.jpg", thresholdedImage)

#cv2.imshow("Test", canny);

#HW3: try out the other kernels: Prewitt, Robert, etc.
#HW4: try to find out how we can profile functions in Python -- calculate how much
#time it takes to run a function or some piece of code
#kernel = [[-1, 0, +1], [-2, 0, +2], [-1, 0, +1]]
#print(kernel)
# this is the output of gx
#output = convolve(image, kernel)
#HW1: compute gy
#HW2: combine gx and gy to produce the final output M(x, y) page 706 of your textbook
#cv2.imwrite("beetroot1.jpg", output)
