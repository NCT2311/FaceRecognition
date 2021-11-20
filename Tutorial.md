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

## Calculate accuracy in Face-Recognition

### First Method
You should test your Face Recognition method on some dataset that also has ground truth. Then you can check how many are correctly recognized.\
You should read about True positive and True negative, false positve and negatives.\
With this formula of your accuracy=(TP+TN)/(Total).

More detail: [First-Method](https://www.researchgate.net/post/How_do_I_determine_the_accuracy_of_Face_Recognition)

### Second Method
More detail: [Second-Method](https://www.pnas.org/content/115/24/6171)
