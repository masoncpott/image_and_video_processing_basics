import cv2

image = cv2.imread("galaxy.jpg", 0)

print(type(image)) # <class 'numpy.ndarray'>
print(image.shape) # (h, w) = (1485, 990)

height = int(image.shape[0] / 2)
width = int(image.shape[1] / 2
)
resized_image = cv2.resize(image, (width, height))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()