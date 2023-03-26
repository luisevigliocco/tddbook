from selenium import webdriver
import unittest

SITE_URL='http://localhost:8000'

class NewVisitorTest(unittest.TestCase):
  
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_start_list(self):
    self.browser.get(SITE_URL)
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')

