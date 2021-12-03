[Setup]

    - Setup python for win10: https://www.python.org/downloads/release/python-397/ => Windows installer 64bits (recommend)
    - OpenCV for python: https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/
    - OpenCV version 4.5.3; Python version 3.9.7

- Mongodb
  pip install pymongo
  pip install "pymongo[srv]"

[How-to-setup-package]

1. Copy Haar Cascades:
   - In terminal:
     python
     import cv2
     print(cv2.\_\_file\_\_) //Delete '\' character
     => Get directory cv2 => Copy folder data to src/cascades
2. Haar Cascades Classifier
   - Cho phép chụp hình khung ảnh mặt cuối cùng khi ta press 'q'
3. Draw a rectangle around face
4. Recognize
   - Training image into a numpy array
     pip install pillow --upgrade

[NOTE]

Chức năng trên Web Đồ án:

1. Xử lý yêu cầu người lạ

- Flow data: từ webcam gửi 1 hình hoặc 1 video (như này thì sẽ có delay) lên server, web lấy data đso hiển thị ra, có 2 nút accept và decline,
  nhấn nút thì phản hồi lại data lên server. Bơ code py léo data đso về để show ra completed or not

2. Xử lý người quen thì có sẵn trong database rồi, so sánh rồi xuất output luôn
3. Suy nghĩ cách thông báo cho admin (gửi mail, ....)
4. History lượt mở cửa, thống kê

status: Người lạ/quen (True: quen/ fa

[Requirements]

- [DONE] Setup khuôn mặt lần đầu tiên của admin => Được rồi nhưng nó phải chậm lại để bắt nhiều góc
- [DONE] Push data lên server
- [DONE] 2/11: Quét mặt (5s đứng yên mới quét), screen shot vào folder response
  => Done
  Có 3 cách:
  C1: Nhấn nút thì chụp hình lúc đó => Phi thực tế
  C2: Delay trong while => Khung hình bị khựng lại, không quét được liên tục
  C3: Cho count_shot rồi khoảng 2 giây nó tự chụp 1 lần, chuyển động chậm là được
- 6/11: Quét vừa người quen, vừa người lạ thì tùy mình quyết định mở hay không? Vẫn gửi request như người lạ, nhưng giờ gửi nhiều thông tin người hơn
- Gửi mail thì gửi luôn thông tin + Đường link web

  - Thống kê: Vũ đang làm
  - [DONE] Bắt mặt chính xác hơn
  - Xử lý case vừa lạ vừa quen => Cho vào + Gửi turn
  - Người lạ => Gửi turn + Person
  - 1 quen, nhiều quen, 1 lạ, nhiều lạ, quen với lạ
