[Setup]

    - Setup python for win10: https://www.python.org/downloads/release/python-397/ => Windows installer 64bits (recommend)
    - OpenCV for python: https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/
    - OpenCV version 4.5.3; Python version 3.9.7

[How-to-setup-package]

1. Copy Haar Cascades:
    - In terminal:
      python
      import cv2
      print(cv2.\_\_file\_\_) //Delete '\' character
      => Get directory cv2 => Copy folder data to src/cascades
