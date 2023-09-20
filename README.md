# Face Counter

This project provides a Python script for counting faces in an image and a web application to visualize the count and highlight the faces in the image.

## [Link to the Website](https://facecounter.onrender.com) (Hosted on Render)

## Project Flowchart

![ML and Web Dev Flowchat](./static/images/Flowchart%20SVG.svg)

## Example

### Input Image

![Input Image](./static/images/faces.png)

### Output Image

![Output Image](./static/output/output.png)

### Individual Faces Extracted

<div style="display: flex; flex-wrap: wrap; justify-content: space-evenly;">

![Face 1](./static/output/face_1.jpg)

![Face 2](./static/output/face_2.jpg)

![Face 3](./static/output/face_3.jpg)

![Face 4](./static/output/face_4.jpg)

![Face 5](./static/output/face_5.jpg)

</div>

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
