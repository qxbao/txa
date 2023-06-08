TÀI XỈU ASSISTANT - Trợ lý thông minh đút tiền cho bạn
(Orca)

TXA được viết bằng Python, cung cấp nhiều lựa chọn, từ ngẫu nhiên hoàn toàn cho đến các dự đoán dựa theo khả năng học quy luật (soi cầu) của Machine Learning. Trước khi chạy lần đầu, hãy chắc chắn rằng thiết bị của bạn đã có sẵn môi trường Python và cài đặt đầy đủ các thư viện cần thiết trong file requirements.txt. Nếu chưa, sử dụng lệnh "pip install -r requirements.txt" để cài đặt chúng.

Độ chính xác của khả năng dự đoán phụ thuộc vào độ dài tệp dữ liệu huấn luyện được cung cấp. Bạn cần lưu file dữ liệu huấn luyện dưới dạng file .txt trong thư mục "assets/", với format là các phiên Tài - Xỉu được sắp xếp theo thứ tự, ngăn cách bởi dấu ",".
Với các phiên không liên kết với nhau, bạn cần phân tách chúng bằng phím [Enter] để phần mềm có thể phân biệt.

Để có thể sử dụng tính năng dự đoán, bạn cần làm theo những bước sau:
1. Huấn luyện AI bằng lệnh "train" theo file huấn luyện có sẵn
2. Kiểm tra độ chính xác của từng AI bằng lệnh "test", sử dụng dữ liệu kiểm thử từ phiên tài xỉu hiện tại
3. Dùng lệnh "predict" để dự đoán từ kết quả phiên theo thời gian thực
Lưu ý: AI được huấn luyện với độ dài mảng đầu vào = input_length trong config. Bạn có thể sử dụng lệnh "config" để kiểm tra. Chắc chắn rằng độ dài mẫu kiểm thử dài hơn input_length ít nhất là 2, càng dài càng có kết quả chính xác. Ngoài ra, độ dài mảng sử dụng cho lệnh "predict" cần bằng chính xác input_length.

Hiện tại, phần mềm hỗ trợ 3 thuật toán ML để dự đoán:
+ Support Vector Regression (svr)
+ Random Forest (rf)
+ Neural Network (nn)

Các thông tin khác như cú pháp lệnh, kiểu dữ liệu tham số, mô tả từng lệnh sẽ được hiển thị bằng lệnh "help".