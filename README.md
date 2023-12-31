# Face Counter

Welcome to Face Counter, a Python project that simplifies face counting in images and provides an intuitive web application for visualizing the results with highlighted faces. Whether you're curious about the number of faces in a group photo or need to analyze facial data, Face Counter has got you covered.

## [Link to the Website](https://facecounter.onrender.com) (Hosted on Render)

## Project Flowchart

![ML and Web Dev Flowchat](./static/images/ML%20and%20Web%20Dev%20Flowchat.png)

## Example

### Input Image

![Input Image](./static/images/faces.png)

### Output Image

![Output Image](./static/output/output.jpg)

### Individual Faces Extracted

![Face 1](./static/output/face_1.jpg) ![Face 2](./static/output/face_2.jpg) ![Face 3](./static/output/face_3.jpg) ![Face 4](./static/output/face_4.jpg) ![Face 5](./static/output/face_5.jpg)

## Installation

1. Clone the repo

   ```bash
   git clone https://github.com/Hardvan/FaceCounter
   ```

2. Navigate to the folder

   ```bash
   cd FaceCounter
   ```

3. Create a virtual python environment by typing the following in the terminal

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment

   Windows:

   ```bash
   .\.venv\Scripts\activate
   ```

   Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies by typing the following in the terminal

   ```bash
   pip install -r requirements.txt
   ```

6. Run the app

   ```bash
   python app.py
   ```

7. Click on the link in the terminal to open the website

   It will look something like this:

   ```bash
   Running on http://127.0.0.1:5000
   ```

### Testing the CountFaces.py script

If you want to test the script, you can run the following command in the terminal:

```bash
python CountFaces.py
```

This will run the script on the image in the `images` folder and print the number of faces found in the image along with storing the image with the faces highlighted in the `output` folder.
