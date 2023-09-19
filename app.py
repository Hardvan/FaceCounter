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
            face_count = CountFaces.count_and_highlight_faces(
                image_path, output_image_path)

            # Calculate the processing time
            processing_time = time.time() - start_time
            processing_time = round(processing_time, 2)

            # Delay for 5 seconds on purpose (for testing Loading... animation)
            # time.sleep(5)

            return render_template('index.html',
                                   uploaded=True,
                                   face_count=face_count,
                                   processing_time=processing_time)

    return render_template('index.html', uploaded=False)


if __name__ == "__main__":
    app.run(debug=True)
