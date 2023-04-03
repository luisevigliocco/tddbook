#!/usr/bin/env python3
from selenium import webdriver
import unittest
import sys
import os


variable_name = "TEST_URL"

if len(sys.argv) == 2:
  SITE_URL = 'http://' + sys.argv[1]
elif variable_name in os.environ:
  SITE_URL = os.environ[variable_name]
else:
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

