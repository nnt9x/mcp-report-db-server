from fastmcp import FastMCP
import requests
import json
from typing import Optional
from urllib.parse import urlencode

mcp = FastMCP(name="Report Database Server")

BASE_URL = "http://127.0.0.1:8080/api"

@mcp.tool
def get_report_by_source_year(source: Optional[str] = None, year: int = 2025) -> dict|list|str:
    """
    Lấy báo cáo theo nguồn và năm (bắt buộc phải có năm).

    Args:
        source: Nguồn (vd. "crm" hoặc "crm, shopee"). Bỏ trống để lấy tất cả.
        year: Năm.

    Returns:
        JSON của báo cáo hoặc thông báo lỗi.
    """
    try:
        params = {"year": year}
        if source:
            params["rootKeyName"] = source
            
        url = f"{BASE_URL}/reports/by-source/yearly"
        
        # Hiển thị đường dẫn cuối trước khi request
        full_url = f"{url}?{urlencode(params)}" if params else url
        print(f"Final URL: {full_url}")
        
        response = requests.get(url, params=params, timeout=30)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Lỗi kết nối API: {str(e)}"


@mcp.tool
def get_all_report_by_source(source: Optional[str] = None) -> dict|list|str:
    """
    Lấy tất cả báo cáo theo nguồn từ lúc bắt đầu đến nay, không phân biệt năm tháng.

    Args:
        source: Nguồn (vd. "crm" hoặc "crm, shopee"). Bỏ trống để lấy tất cả.

    Returns:
        JSON của báo cáo hoặc thông báo lỗi.
    """
    try:
        params = {}
        if source:
            params["rootKeyName"] = source
            
        url = f"{BASE_URL}/reports/by-source/all"
        
        # Hiển thị đường dẫn cuối trước khi request
        full_url = f"{url}?{urlencode(params)}" if params else url
        print(f"Final URL: {full_url}")
        
        response = requests.get(url, params=params, timeout=30)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Lỗi kết nối API: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=9999)