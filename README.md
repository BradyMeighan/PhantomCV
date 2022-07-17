# PhantomCV
PhantomCV is an open source Computer Vision script for use with Titan Two and Gtuner. Phantom makes use of a yolov5s model to detect objects on screen and then calculate a trajectory for the right stick that it then sends to a seperate Gtuner script for interpretation. I would love to finish this project but I don't really have time to work on this anymore so i'm going to just release it to the public. Feel free to make your own changes to the code for your own personal use or make a pull request and I will incorporate it into the main branch.

## Preview
[![Preview](https://img.youtube.com/vi/lcsM_D6omaw/0.jpg)](https://www.youtube.com/watch?v=lcsM_D6omaw)

## Installation Requirements
 - [Python 3.8](https://www.python.org/downloads/release/python-380/) (MUST BE PYTHON 3.8)
 - [pip](https://bootstrap.pypa.io/get-pip.py)
 - [Visual Studio Community](https://visualstudio.microsoft.com/downloads/)
 - [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
 - [Gtuner](https://www.consoletuner.com/titan-two-downloads/)
 
### Installation
Assuming you have all the requirements listed above downloaded and installed, run the install-cv.bat script on your machine to install all the required Python modules.
 
## How To Make Your Own Changes

### Compile phantomcv_helper.py with Nuitka
I used a python package called Nuitka to compile phantomcv_helper.py as a pyd file (Nuitka is installed along with the other modules when running install-cv.bat). I've read that the conversion to C is more efficient and you get a couple more frames per second. To compile with Nutika run 'helpermodule_maker.bat' and have 'phantomcv_helper.py' in the same directory. After a short wait, you will have a a lot of extra files in your directory but what your looking for is 'phantomcv_helper.pyd'.

### Dataset
Here is a link to the dataset I used to train the 'warzone.pt' model. It is by no means perfect and there is plenty of improvement to be made but it is a large enough dataset to get a good result with yolov5. Feel free to add or make improvements on the current model. The current model was trained on over 9,000 images for 6000 generations at an image size of 416.

[Google Drive Link](https://drive.google.com/file/d/1F2vXIlsopzv8AQtsGaopYcSvoexcIcS6/view?usp=sharing)

## Disclaimer

I’d urge you to please not use the tool to gain an advantage in online gameplay. Though, please enjoy the features in offline gameplay, and share your thoughts if you’re also interested in making the tool better for those who suffer with disabilities. I'm only releasing this as a learning tool to help newer programmers like myself get a grasp on object detection and OpenCV. Just a couple months ago I was a complete beginner at Python and a lot of the knowledge I aquired while making this project took hundreds of hours to learn and implement correctly. There isn't exactly an abundance of information out there on this stuff so I want to help the community out however I can. Thank you!

## Donate
I spent a lot of time on this so any donations would be greatly appreciated!

Bitcoin - 1Fwdk5fkhZ1Y3uyb2HKywHyHQuddiik6Xu

Ethereum - 0x794067Aa418A6bBe774eE313140cCDFd35C2a148

Dogecoin - DS8q14xNtRD3FZAzpmTrGfJ88Ain61wXor

Ripple - rMVLwS4A5onNvcCPYAeqS2fq3DQg6DRr7L

Cardano - addr1q8u9add5zjczkulmexmm4v3hwjqqra522544c046096l7qahx5a2eqnz26pu84yfs39j4rspz3xaqyjs2el0ldx3fxqqqsnsu0
