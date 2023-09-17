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


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
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

            return render_template('index.html',
                                   uploaded=True,
                                   face_count=face_count,
                                   processing_time=processing_time)

    return render_template('index.html', uploaded=False)


if __name__ == "__main__":
    app.run(debug=True)
