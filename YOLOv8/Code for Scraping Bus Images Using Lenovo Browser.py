import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# 创建存储图片的文件夹
if not os.path.exists("flood_bus_images"):
    os.makedirs("flood_bus_images")

# 设置联想浏览器的安装路径
lenovo_browser_path = r"C:\Program Files (x86)\Lenovo\SLBrowser\SLBrowser.exe"  # 请确保路径正确

# 设置 Selenium 使用的 Chrome 浏览器驱动
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = lenovo_browser_path

# 使用 ChromeDriverManager 安装 ChromeDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 百度图片搜索 URL
url = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwxLDMsMiw2LDQsNSw3LDgsOQ%3D%3D&word=%E6%B4%AA%E6%B0%B4%E4%B8%AD%E8%A1%8C%E9%A9%B6%E7%9A%84%E5%85%AC%E4%BA%A4%E8%BD%A6'
# 访问指定的百度图片搜索 URL
driver.get(url)

# 等待页面加载
time.sleep(5)

image_urls = set()
num_images_to_download = 3000

# 模拟滚动页面以加载更多图片，直到获取到所需数量的图片 URL
while len(image_urls) < num_images_to_download:
    # 向下滚动页面以加载更多图片
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)  # 等待页面加载

    # 解析网页内容
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # 更新选择器以确保获取正确的图片 URL
    image_tags = soup.find_all("img", class_="main_img")

    for img_tag in image_tags:
        img_url = img_tag.get("data-imgurl")
        if not img_url:
            img_url = img_tag.get("src")
        if img_url and img_url not in image_urls:
            image_urls.add(img_url)
            if len(image_urls) >= num_images_to_download:
                break

# 关闭浏览器
driver.quit()

def download_image(img_url, index):
    try:
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        image_path = os.path.join("flood_bus_images", f"image_{index+1}.jpg")
        with open(image_path, "wb") as image_file:
            image_file.write(img_response.content)
        print(f"第{index}张图片下载成功: {img_url}")
    except requests.RequestException as e:
        print(f"第{index}张图片下载失败: {img_url}, 错误: {e}")

# 使用多线程并行下载图片
with ThreadPoolExecutor(max_workers=10) as executor:
    for i, img_url in enumerate(image_urls):
        executor.submit(download_image, img_url, i)

print("图片下载完成")
