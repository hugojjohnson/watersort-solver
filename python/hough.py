import cv2
import numpy as np

def detect_and_plot_vertical_lines(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error: Unable to load the image.")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection (optional but can enhance line detection)
    edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

    # Detect lines using Hough Line Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=1, minLineLength=100, maxLineGap=1)

    # Extract start and end points of vertical lines
    vertical_lines = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(x2 - x1) < 5:  # Check if the line is approximately vertical
            vertical_lines.append((x1, y1, x2, y2))
            
            # Draw the line on the image (optional)
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Display the image with lines (optional)
    # cv2.imshow("Detected Vertical Lines", image)
    cv2.imwrite("GPT.jpg", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return vertical_lines

# Example usage
image_path = "lines.jpg"
vertical_lines = detect_and_plot_vertical_lines(image_path)
for line in vertical_lines:
    x1, y1, x2, y2 = line
    print(f"Start point: ({x1}, {y1}), End point: ({x2}, {y2})")
