# PhantomCV
PhantomCV is an open-source Computer Vision script for use with Titan Two and Gtuner. Phantom makes use of a YOLOv5s model to detect objects on screen and then calculates a trajectory for the right stick that it sends to a separate Gtuner script for interpretation. The project is no longer being actively developed, but contributions from the community are welcome.

## Preview
[![Preview](https://img.youtube.com/vi/lcsM_D6omaw/0.jpg)](https://www.youtube.com/watch?v=lcsM_D6omaw)

## Installation Requirements
 - [Python 3.8](https://www.python.org/downloads/release/python-380/) (MUST BE PYTHON 3.8)
 - [pip](https://bootstrap.pypa.io/get-pip.py)
 - [Visual Studio Community](https://visualstudio.microsoft.com/downloads/)
 - [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
 - [Gtuner](https://www.consoletuner.com/titan-two-downloads/)
 
### Installation
Assuming you have all the requirements listed above downloaded and installed, run the 'install-cv.bat' script on your machine to install all the required Python modules.
 
## How To Make Your Own Changes

### Compile phantomcv_helper.py with Nuitka
Nuitka is a Python package used to compile 'phantomcv_helper.py' as a '.pyd' file, which is installed along with the other modules when running 'install-cv.bat'. The conversion to C is more efficient and provides a performance boost. To compile with Nuitka, run 'helpermodule_maker.bat' and have 'phantomcv_helper.py' in the same directory.

### Dataset
Here is a link to the dataset used to train the 'warzone.pt' model. It is not perfect and there is plenty of room for improvement, but it is a large enough dataset to get good results with YOLOv5. Feel free to add or make improvements to the current model. The current model was trained on over 9,000 images for 6,000 generations at an image size of 416.

[Google Drive Link](https://drive.google.com/file/d/1F2vXIlsopzv8AQtsGaopYcSvoexcIcS6/view?usp=sharing)

## Disclaimer

Please do not use this tool to gain an advantage in online gameplay. However, feel free to enjoy its features in offline gameplay, and share your thoughts if you're interested in making the tool better for those who suffer from disabilities. This project is being released as a learning tool to help new programmers learn about object detection and OpenCV. Acquiring the knowledge to build this project took hundreds of hours, and there isn't an abundance of information available on this topic, so the goal is to help the community however possible. Thank you!

## Donate
I spent a lot of time on this so any donations would be greatly appreciated!

Bitcoin - 1Fwdk5fkhZ1Y3uyb2HKywHyHQuddiik6Xu

Ethereum - 0x794067Aa418A6bBe774eE313140cCDFd35C2a148

Dogecoin - DS8q14xNtRD3FZAzpmTrGfJ88Ain61wXor

Ripple - rMVLwS4A5onNvcCPYAeqS2fq3DQg6DRr7L

Cardano - addr1q8u9add5zjczkulmexmm4v3hwjqqra522544c046096l7qahx5a2eqnz26pu84yfs39j4rspz3xaqyjs2el0ldx3fxqqqsnsu0
