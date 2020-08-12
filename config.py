
import os

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./TestCases/"

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "http://172.16.161.48:8089/echod_manager/index.html#/login"

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    # 项目目录配置
    # 项目目录配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    REPORT_DIR = BASE_DIR + "/TestResult/"
    NEW_REPORT = REPORT_DIR
