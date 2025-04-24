# Báo cáo các bài tập

## Exercise 1

Sau khi `docker build --tag=exercise-1 .`, thêm code vào `main.py` và chạy `docker-compose up`.
Tải các file zip (trừ 1 link lỗi: `https://divvy tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip`).
File zip được lưu trong thư mục `downloads_url`.

![Exercise 1](https://i.imgur.com/cG7wOWb.jpeg)

![Exercise 1](https://i.imgur.com/xBjWCX8.png)


## Exercise 2
Sau khi `docker build --tag=exercise-2 .`, thêm code vào `main.py` và chạy `docker-compose up`.
Cào dữ liệu từ website và lưu vào file CSV.

![Exercise 2](https://i.imgur.com/44fA3zZ.png)

![Exercise 2](https://i.imgur.com/EABvYT2.png)

## Exercise 3
Sau khi thực hiện lệnh docker build --tag=exercise3 . để tạo Docker image cho dự án, ta có thể thêm đoạn mã cần thiết vào file main.py để xử lý việc tải và giải nén dữ liệu từ Common Crawl. Tiếp đó, khi chạy lệnh docker-compose up trong thư mục EXERCISE-3, chương trình sẽ được thực thi trong môi trường container, tự động tải tập tin wet.paths.gz từ S3 bucket của Common Crawl. Quá trình này tạo ra ba thư mục để lưu trữ dữ liệu: thư mục gzip_files chứa file .gz vừa tải về; thư mục path_files lưu trữ file .txt được giải nén từ .gz, trong đó có danh sách các đường dẫn WET file; và thư mục data_files là nơi chứa file .wet sau khi được giải nén hoàn chỉnh – đây là nội dung văn bản thô được thu thập từ các trang web.

![Exercise 3](https://i.imgur.com/LiJ7jKx.png)


## Exercise 4

Sau khi `docker build --tag=exercise4 .`, thêm code vào `main.py` và chạy `docker-compose up`.
Tìm tất cả file JSON trong thư mục `data` và các thư mục con, sau đó chuyển từng file sang CSV.

![Exercise 4](https://i.imgur.com/qtuSlPj.png)

![Exercise 4](https://i.imgur.com/NSlIYhx.png)

## Exercise 5

Sau khi `docker build --tag=exercise5 .`, thêm code vào `main.py` và chạy `docker-compose up`.
Kết nối PostgreSQL và pgAdmin4, tạo bảng cho 3 file CSV trong `data` và insert dữ liệu tương ứng.

![Exercise 5](https://i.imgur.com/np2VlRZ.png)


![Exercise 5](https://i.imgur.com/EhQSC0Y.png)


![Exercise 5](https://i.imgur.com/li4PsZV.png)


![Exercise 5](https://i.imgur.com/XHM614R.png)
