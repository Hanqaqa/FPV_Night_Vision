# FPV Night Vision with Face Dectection
In this project I created a small script for a fast face detection system using a Raspberry Pi 3B+ reaching around 5 Frames Per Second using OpenCV and Python


I will be using a Raspberry Pi 3B+ with Raspbian installed and a original NoIR camera which will be stuck using double sided tape in the front of some FPV goggles.
The whole system will be powered by a portable 10000 mAh battery which has a current draw of around 0.8 Amps when the system is working, therefore one can expect around 10 hours of use.

I used OpenCV in conjunction with Python to create and try to get the best performance for this face detection script.
Most of the explanations are in the Jupyter Notebook OpenCVTests.ipynb, although the main script Raspberry_Night_Vision also has some small comments.
For the face detection algorithm I will be using a Haar Cascade algorithm due to its simplicty and availability. The best parameters were chosen so it could detect only small faces, saving some during the repetition of the algorithm and therefore getting a more fluid video.
The parameters chosen for the Haar Cascade were: 

| Parameter| Choice|
|-----------|-------|
| Resolution| 640*360 |
|Scale Factor| 1,2 |
|Minimum Neighbours| 5| 
|Max Size| 200*200| 
|Min Size| 30*30 |


There is a video in the Media folder showing its performance in real time as well as some photos of the device.