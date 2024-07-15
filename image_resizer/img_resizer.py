import cv2

image = 'transformer.jpg'
final_image = 'transformer_rs.png'

# Read the image
src = cv2.imread(image, cv2.IMREAD_UNCHANGED)

# Check if the image was loaded properly
if src is None:
    print("Error: Could not load image")
    exit()

# Show the original image
# cv2.imshow('Original Image', src)

# Percent by which the image is resized
scale_percent = 70

# Calculate the scale percent of the total dimensions
height = int(src.shape[0] * scale_percent / 100)
width = int(src.shape[1] * scale_percent / 100)
dim = (width, height)

# Resize the image
output = cv2.resize(src, dim)

# Show the resized image
cv2.imshow('Resized Image', output)

# Save the resized image
cv2.imwrite(final_image, output)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
