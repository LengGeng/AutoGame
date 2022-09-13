import os.path
from datetime import date, datetime

DATE = date.today()
DATETIME = datetime.today()

LOG_PATH = os.path.join(os.path.dirname(__file__), "logs")  # 日志目录
LIBS_PATH = os.path.join(os.path.dirname(__file__), "libs")  # 库目录
TEMPLATE_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images")  # 模板图片目录
SCREEN_PATH = os.path.join(os.path.dirname(__file__), "images/screen")  # 截图目录
