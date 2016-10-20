import unittest
import os
from appium import webdriver

class ContactAppTestAppium(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': "Android", 'deviceName': "HQ588YL07922",
                        'app':os.path.abspath("./Apps/app-debug.apk")}
        self.driver = webdriver.Remote(
            "http://localhost:4723/wd/hub", desired_caps)

    def test_ClickRefreshLink(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.marketlytics.calabashtest:id/editText1']") \
            .send_keys("Besm ellah")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)
