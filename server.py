from fastmcp import FastMCP
import requests
import json
from typing import Optional
from urllib.parse import urlencode

mcp = FastMCP(name="Report Database Server")

BASE_URL = "http://127.0.0.1:8080/api"

@mcp.tool
def get_all_resource() -> dict|list|str:
    """
    Lấy tất cả nguồn (source_key) dùng để lấy báo cáo.

    Returns:
        JSON của nguồn hoặc thông báo lỗi.
    """
    try:
        url = f"{BASE_URL}/source/list"
        response = requests.get(url, timeout=30)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Lỗi kết nối API: {str(e)}"


@mcp.tool
def get_report_by_source_year(source_key: Optional[str] = None, year: int = 2025) -> dict|list|str:
    """
    Lấy báo cáo theo nguồn  (source_key) và năm (bắt buộc phải có năm).

    Args:
        source_key: (ví  dụ "crm" hoặc "crm, shopee"). Bỏ trống để lấy tất cả.
        year: Năm (mặc định 2025).

    Returns:
        JSON của báo cáo hoặc thông báo lỗi.
    """
    try:
        params = {"year": year}
        if source_key:
            params["rootKeyName"] = source_key
            
        url = f"{BASE_URL}/reports/source/yearly"
        
        # Hiển thị đường dẫn cuối trước khi request
        full_url = f"{url}?{urlencode(params)}" if params else url
        print(f"Final URL: {full_url}")
        
        response = requests.get(url, params=params, timeout=30)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Lỗi kết nối API: {str(e)}"


@mcp.tool
def get_all_report_by_source(source_key: Optional[str] = None) -> dict|list|str:
    """
    Lấy tất cả báo cáo tổng theo các nguồn, không phân biệt ngày tháng.

    Args:
        source_key: Nguồn (vd. "crm" hoặc "crm, shopee"). Bỏ trống để lấy tất cả.

    Returns:
        JSON của báo cáo hoặc thông báo lỗi.
    """
    try:
        params = {}
        if source_key:
            params["rootKeyName"] = source_key
            
        url = f"{BASE_URL}/reports/source/all"
        
        # Hiển thị đường dẫn cuối trước khi request
        full_url = f"{url}?{urlencode(params)}" if params else url
        print(f"Final URL: {full_url}")
        
        response = requests.get(url, params=params, timeout=30)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Lỗi kết nối API: {str(e)}"
    


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=9999)