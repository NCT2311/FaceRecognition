Chức năng trên Web Đồ án:
1. Xử lý yêu cầu người lạ
- Flow data: từ webcam gửi 1 hình hoặc 1 video (như này thì sẽ có delay) lên server, web lấy data đso hiển thị ra, có 2 nút accept và decline,
 nhấn nút thì phản hồi lại data lên server. Bơ code py léo data đso về để show ra completed or not
2. Xử lý người quen thì có sẵn trong database rồi, so sánh rồi xuất output luôn
3. Suy nghĩ cách thông báo cho admin (gửi mail, ....)
4. History lượt mở cửa, thống kê


status: Người lạ/quen (True: quen/ false: Lạ)
flag: Xử lý ở DB chưa (true: Chưa/ false: Rồi)
response: Mở cửa hay không (True: Accept/ False: Decline)
B1: Tạo data người quen local
B2: Push data người quen, tạo personid trên database
B3: Thực hiện quét mặt; nếu là người lạ => Tạo 1 person người lạ (trường status = false để phân biêt với người quen là status = true) và tạo 1 turn cho người lại trên DB; nếu là người quen => Chỉ cần tạo turn trên db
(flag ở 1 thực thể mới)