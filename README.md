# MCP Report Database Server

MCP Server để truy xuất dữ liệu báo cáo từ database thông qua REST API.

## Tính năng

### Tools có sẵn:

1. **get_report_by_source_year** - Lấy báo cáo theo nguồn và năm
   - `source`: Nguồn dữ liệu (crm, shopee, tiktok, etc.) - tùy chọn
   - `year`: Năm cần lấy báo cáo (mặc định 2024)

2. **get_available_sources** - Lấy danh sách các nguồn dữ liệu có sẵn

3. **get_report_summary** - Lấy tổng quan báo cáo theo năm
   - `year`: Năm cần lấy tổng quan (mặc định 2024)

4. **get_monthly_report** - Lấy báo cáo theo tháng
   - `source`: Nguồn dữ liệu - tùy chọn
   - `year`: Năm (mặc định 2024) 
   - `month`: Tháng (1-12, mặc định tháng 1)

## Cài đặt

```bash
pip install -e .
```

## Chạy server

```bash
python server.py
```

Server sẽ chạy trên port 9999 và kết nối đến API backend tại `http://127.0.0.1:8080/api`.

## Cấu hình

Có thể thay đổi `BASE_URL` trong file `server.py` để kết nối đến API backend khác.