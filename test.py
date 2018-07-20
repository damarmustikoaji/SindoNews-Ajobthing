"""
Example script to run one test against the SindoNews app using Appium
The test will:
- launch the app
-
"""

import os
import unittest
import time
from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from appium.webdriver.common.touch_action import TouchAction

class AndroidTests(unittest.TestCase):
    "Class to run tests against the SindoNews app"
    def setUp(cls):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'Nexus_5'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apk/SINDOnews com_v1.2.3_apkpure.com.apk'))
        desired_caps['appPackage'] = 'com.sindonews.android'
        desired_caps['appActivity'] = 'com.sindonews.android.home.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(cls):
        "Tear down the test"
        cls.driver.quit()

    def test_1_latest(self):
        "SindoNews Apps - LATEST"
        try:
            latesttab = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='LATEST']")))
            latesttab.click()
            title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/b_title")))
            channel = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/b_channel")))
            date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/b_date")))
            print title.text
            print channel.text
            print date.text
            time.sleep(5)
        except Exception as e:
            raise

    def test_2_popular(self):
        "SindoNews Apps - POPULAR"
        try:
            populartab = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='POPULAR']")))
            populartab.click()
            time.sleep(5)
            topfirst = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/pop_title")))
            topfirst.click()
            title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/ctn_title")))
            reporter = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/ctn_reporter")))
            date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.sindonews.android:id/ctn_date")))
            print title.text
            print reporter.text
            print date.text
            time.sleep(5)
        except Exception as e:
            raise

    def _3_sidebarmenu(self):
        "SindoNews Apps - Sidebar Menu"
        try:
            time.sleep(5)
            button = self.driver.find_element_by_accessibility_id('open')
            button.click()
            time.sleep(5)
            action = TouchAction(self.driver)
            el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "Soccer")))
            action.press(el).move_to(x=10, y=-500).release().perform()
            time.sleep(5)
        except Exception as e:
            raise

    def test_4_search(self):
        "SindoNews Apps - Search"
        try:
            search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.sindonews.android:id/search_button')))
            search.click()
            searchfield = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.sindonews.android:id/search_src_text')))
            searchfield.send_keys('viral')
            self.driver.press_keycode(66)
            time.sleep(5)
            title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.sindonews.android:id/src_title')))
            channel = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.sindonews.android:id/src_channel')))
            date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'com.sindonews.android:id/src_date')))
            print title.text
            print channel.text
            print date.text
            time.sleep(5)
        except Exception as e:
            raise

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
