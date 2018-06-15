import os
import time
import urllib

from FunctionTest.func_script.func_lib import AppiumInit
from FunctionTest.func_script.func_lib import AppOperation


class AppiumServerCheck(object):
    appium = AppiumInit()
    ap_opr = AppOperation()

    def check_appium_server(self):
        if 'node.exe' in os.popen('tasklist | findstr "node.exe"').read():
            # while True:
            #     try:
            #         self.appium.appium_init()
            #         break
            #     except ConnectionRefusedError:
            #         time.sleep(3)
            #     except urllib.error.URLError:
            #         time.sleep(3)
            self.ap_opr.force_stop('com.excelliance.dualaid')
            print('调试结束，开始执行测试...\n')
        else:
            os.popen("start appium")
            print("正在启动appium服务程序，请稍后...\n")
            while True:
                if 'node.exe' in os.popen('tasklist | findstr "node.exe"').read():
                    while True:
                        try:
                            self.appium.appium_init()
                            break
                        except ConnectionRefusedError:
                            time.sleep(3)
                        except urllib.error.URLError:
                            time.sleep(3)
                    self.ap_opr.force_stop('com.excelliance.dualaid')
                    print('调试结束，开始执行测试...\n')
                    break
                else:
                    time.sleep(3)

    def stop_appium_server(self):
        pid = os.popen('tasklist | findstr "node.exe"').read().split()[1]
        os.popen('taskkill /f /pid ' + pid)


# ap_ser_che = AppiumServerCheck()
# ap_ser_che.check_appium_server()
# ap_ser_che.stop_appium_server()
