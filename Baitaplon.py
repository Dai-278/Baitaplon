import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ham thuc hien tra cuu phat nguoi
def run_tra_cuu():
    print("Đang mở trình duyệt và tải trang...")

    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    # Mở trang tra cứu
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    # Đợi trường nhập "Biển kiểm soát" xuất hiện
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "BienKiemSoat"))
        )
    except:
        print("Không thể tải được trang. Thử lại sau.")
        driver.quit()
        return

    # Ghi thông tin biển số
    input_bienso = driver.find_element(By.NAME, "BienKiemSoat")
    input_bienso.clear()
    input_bienso.send_keys("74D1-86868")

    # Chọn loại xe (gợi ý: có thể phải dùng Select nếu là dropdown <select>)
    try:
        input_loaixe = driver.find_element(By.NAME, "LoaiXe")
        input_loaixe.send_keys("Xe máy")
    except:
        print("Không tìm thấy trường 'Loại xe'.")

    # Đợi người dùng nhập captcha và bấm nút "Tra cứu"
    input("Vui lòng nhập captcha và bấm nút 'Tra cứu' trên trình duyệt, sau đó nhấn Enter tại đây để tiếp tục...")

    # Chờ kết quả hiển thị
    time.sleep(30)

    # Lấy kết quả nếu có
    results = driver.find_elements(By.CLASS_NAME, "btnTraCuu")
    if results:
        print("Kết quả phạt nguội:")
        for result in results:
            print(result.text.strip())
    else:
        print("Không có kết quả hoặc captcha sai.")

    # Đóng trình duyệt
    driver.quit()
# Hàm đợi đến đúng giờ
def wait_until(*target_hours):
    while True:
        now = datetime.datetime.now()
        if now.hour in target_hours and now.minute == 0:
            print(f"\n--- Bắt đầu tra cứu lúc {now.strftime('%H:%M')} ---")
            run_tra_cuu()
            time.sleep(60)  # Chờ qua phút hiện tại
        else:
            time.sleep(20)  # Kiểm tra lại sau 20 giây

# Chương trình chính
if __name__ == "__main__":
    print("Đang chạy... Tự động tra cứu lúc 6h và 12h hàng ngày.")
    wait_until(6)
    wait_until(12)