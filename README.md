# Sound Control With Gestures 
#####
[![Opencv](data:image/png;base64,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)](https://opencv.org/)[
![Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)](https://www.python.org/)
[![Numpy](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeXkEA3c2hxTcrZWwVnniXAFiqai51196osD9FWL0_D_Ca7fOT)](https://www.numpy.org/)
[![mediapipe](https://google.github.io/mediapipe/images/logo_horizontal_color.png)](https://google.github.io/mediapipe/)
&nbsp;

# Description

Control system volume using hand gestures with MediaPipe on python 3.

**Python** forms the language on which this program is built. **OpenCV** is employed to work with live video feed as set of frames.
**MediaPipe** Hands is adopted for hand and finger, detection and tracking. It utilizes machine learning to infer 21 3D landmarks of a hand from just a single frame. 
**Numpy** is used for Interpolation of data received from MediaPipe, which is then fed to the **Pycaw** library for System Sound Control.

### Technologies
1.  [Python] 
The python is one of the most accessible programming languages available because **it has simplified syntaxes, which gives more emphasis on natural language**. Due to its ease of learning and usage, python codes can be easily written and executed much faster than other programming languages.

2. [MediaPipe]  
MediaPipe offers open source cross-platform, customizable ML solutions for live and streaming media. MediaPipe offers ready-to-use yet customizable Python solutions as a prebuilt Python package.

3. [Opencv]
OpenCV is an open-source library that includes several hundreds of computer vision algorithms.

4. [Numpy]
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
5. [Pycaw]
It is a Python Core Audio Windows Library for working with both Python2 and Python3.

## Setup
##### This was build on Windows 10.
### Download
##### Ensure that you have downloaded Python on your system.
Click the python thumbnail to go to Python Download Page
[
![Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)](https://www.python.org/downloads/)

###  Installations
##### Install [OpenCV] with pip
```sh
pip install opencv-python
```
##### Install [Numpy] with pip
```sh
pip install numpy
```
##### Install [Pycaw] with pip
```sh
pip install pycaw
```
##### Install [MediaPipe] with pip
```sh
pip install mediapipe
```
## Download Repository
```sh
git clone https://github.com/Alpha-github/Sound_Control_With_Gesture.git
```

[Opencv]: <https://opencv.org/>
[Python]: <https://www.python.org/>
[Numpy]: <https://www.numpy.org/>
[MediaPipe]:<https://google.github.io/mediapipe/>
[Pycaw]:<https://github.com/AndreMiras/pycaw>

