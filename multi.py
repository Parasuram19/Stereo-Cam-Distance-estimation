import cv2

image = cv2.imread('frame.png', 0)
heatmap = cv2.applyColorMap(image, cv2.COLORMAP_HOT)

cv2.imshow('heatmap', heatmap)
cv2.waitKey()