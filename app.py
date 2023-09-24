from flask import Flask, render_template, request, redirect
import os
import cv2
import time


# Custom modules
import CountFaces


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure the UPLOAD_FOLDER exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def clear_upload_folder():

    folder = app.config['UPLOAD_FOLDER']

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)  # Delete the file

        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Clear the upload folder before saving the new image
        clear_upload_folder()

        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Save the uploaded image to the UPLOAD_FOLDER
            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg')
            file.save(image_path)

            # Measure the time taken to process the image
            start_time = time.time()

            # Call the face detection function
            output_image_path = os.path.join(
                app.config['UPLOAD_FOLDER'], 'output_image.jpg')
            face_count, faces = CountFaces.count_and_highlight_faces(
                image_path, output_image_path)

            # Calculate the processing time
            processing_time = round(time.time() - start_time, 2)

            # Get additional information
            image_resolution = get_image_resolution(image_path)
            file_size = get_file_size(image_path)
            confidence_score = calculate_confidence_score(faces)

            # Render the template with additional information
            return render_template('index.html',
                                   uploaded=True,
                                   face_count=face_count,
                                   processing_time=processing_time,
                                   image_resolution=image_resolution,
                                   file_size=file_size,
                                   confidence_score=confidence_score)

    return render_template('index.html', uploaded=False)


def get_image_resolution(image_path):

    img = cv2.imread(image_path)
    height, width, channels = img.shape

    return f"{width} x {height}"


def get_file_size(image_path):

    file_size = os.path.getsize(image_path)
    file_size = round(file_size / (1024 * 1024), 2)  # Convert to MB

    return f"{file_size} MB"


def calculate_confidence_score(faces):

    # No faces detected
    if len(faces) == 0:
        return 0.0

    total_aspect_ratio = 0.0

    for (x, y, w, h) in faces:
        aspect_ratio = float(w) / h
        total_aspect_ratio += aspect_ratio

    average_aspect_ratio = total_aspect_ratio / len(faces)

    # Define a threshold for aspect ratio
    threshold = 1.0  # You can adjust this threshold as needed

    # Calculate the confidence score based on the threshold
    confidence_score = min(1.0, average_aspect_ratio / threshold)

    return round(confidence_score, 2)


if __name__ == "__main__":
    app.run(debug=True)
