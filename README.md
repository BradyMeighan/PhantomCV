# PhantomCV
PhantomCV is an open source OpenCV script for use with Titan Two and Gtuner. Phantom makes use of a yolov5s model to detect objects on screen and then calculate a trajectory that it then sends back to the controller through Gtuner.

##Preview
[![Preview](https://img.youtube.com/vi/lcsM_D6omaw/0.jpg)](https://www.youtube.com/watch?v=lcsM_D6omaw)

## Installation Requirements
 - [Python 3.8](https://www.python.org/downloads/release/python-380/) (MUST BE PYTHON 3.8)
 - [pip](https://bootstrap.pypa.io/get-pip.py)
 - [Visual Studio Community](https://visualstudio.microsoft.com/downloads/)
 - [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
 
### Installation
Assuming you have all the requirements listed above downloaded and installed, run the install-cv.bat script on your machine to install all the required Python modules.
 
## Compile phantomcv_helper.py with Nutika
I used a python package called Nutika to compile phantomcv_helper.py as a pyd file. I've read that the conversion to c is more efficient and you get a couple more frames per second. To compile with Nutika run 'helpermodule_maker.bat' and 

## Dataset
Here is a link to the dataset I used to train the 'warzone.pt' model. It is by no means perfect and there is plenty of improvement to be made but it is a large enough dataset to get a good result with yolov5.

[Google Drive Link](https://drive.google.com/file/d/1F2vXIlsopzv8AQtsGaopYcSvoexcIcS6/view?usp=sharing)

