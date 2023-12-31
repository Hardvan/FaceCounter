import cv2
import os


def count_and_highlight_faces(input_image_path, output_image_path):

    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input image
    image = cv2.imread(input_image_path)
    original_image = image.copy()

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Sort the faces based on X-coordinate (left to right)
    faces = sorted(faces, key=lambda x: x[0])

    # Draw rectangles around detected faces and label them
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'Face {i + 1}', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save each face to a separate image file
        face = original_image[y:y+h, x:x+w]
        face_filename = os.path.join('static/uploads/', f'face_{i+1}.jpg')
        cv2.imwrite(face_filename, face)

    # Save the output image with faces highlighted
    cv2.imwrite(output_image_path, image)

    # Return the count of detected faces and the individual faces
    return len(faces), faces


# Example usage:
if __name__ == '__main__':

    # Replace with your input image path
    input_image_path = './static/images/faces.png'
    # Replace with your desired output image path
    output_image_path = './static/output/output.png'
    face_count = count_and_highlight_faces(input_image_path, output_image_path)
    print(f'Total Faces Detected: {face_count}')
