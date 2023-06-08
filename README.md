# Tài-Xỉu Assistant
Tài-Xỉu Assistant (TXA) là một phần mềm hỗ trợ dự đoán kết quả tài xỉu bằng các thuật toán học máy.
## Tính năng
- **Khởi tạo kết quả ngẫu nhiên**: Bạn không tin vào khả năng dự đoán của các thuật toán học máy? Không vấn đề, TXA hỗ trợ khởi tạo các kết quả ngẫu nhiên, giúp bạn phần nào trong việc đưa ra quyết định dựa vào may mắn của bản thân
- **Dự đoán kết quả**: Bằng cách sử dụng các thuật toán học máy, TXA tự tin thay bạn học các quy luật Tài Xỉu, đưa ra dự đoán lượt kế tiếp từ thông tin phiên hiện tại. Từ đây, cầu bệt, 1-1, 1-2 không còn là vấn đề đáng lo ngại nữa.
## Cài đặt
Clone thư mục github này về, đảm bảo bạn đã cài đặt đầy đủ các thư viện cần thiết bằng lệnh: 
```bash
pip install -r requirements.txt
```
## Huấn luyện
Bạn cần chuẩn bị dữ liệu huấn luyện cho các mô hình học máy, tuân theo các yêu cầu sau:
- Dữ liệu cần được chứa trong file .txt, lưu tại thư mục /assets
- Dữ liệu là kết quả của các phiên tài xỉu liên tiếp, được ngăn cách bởi dấu ",".
    - **Ví dụ**: 5, 9, 14, 14, 10, 3, 5,...
- Các phiên không kết nối với nhau, ví dụ như được thu thập tại các ngày riêng biệt, cần được đặt tại các dòng riêng biệt.
- Một phiên cần có độ dài lớn hơn config.input_length (mặc định là 8, có thể thay đổi bằng lệnh ilength).
- Độ lớn (và chính xác) của tệp dữ liệu huấn luyện tỉ lệ thuận với độ chính xác của các mô hình học máy trong việc dự đoán.
## Sử dụng
Để có thể sử dụng TXA vào việc dự đoán kết quả tài xỉu, bạn có thể tham khảo các bước sau đây:
1. Huấn luyện các mô hình học máy bằng lệnh /train
2. Kiểm tra độ chính xác của từng mô hình trong phiên chỉ định bằng lệnh test hoặc ktest
3. Sử dụng lệnh predict để các mô hình học máy đưa ra dự đoán

Từ kết quả dự đoán và độ chính xác của từng thuật toán, bạn có thể đưa ra quyết định đặt Tài hoặc Xỉu, thậm chí bỏ lượt đợi một phiên ổn định hơn.