import cv2
import numpy as np

image = cv2.imread("background.jpg")

grid_spacing = 50
grid_color = (0, 0, 255)
line_thickness = 1

for x in range(0, image.shape[1], grid_spacing):
    cv2.line(image, (x, 0), (x, image.shape[0]), grid_color, line_thickness)

for y in range(0, image.shape[0], grid_spacing):
    cv2.line(image, (0, y), (image.shape[1], y), grid_color, line_thickness)

cv2.imshow("Image with Grid", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("background_with_grid.jpg", image)
