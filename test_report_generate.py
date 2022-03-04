import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    # execute test cases, and report in HTML
    # use unittest default test loader to find test cases end wit ".py" in /testcase
    suit = unittest.defaultTestLoader.discover("./testcase", "*.py")

    # generate html report
    report_file = open("./report/reports.html", "wb")

    #generate a HTMLTestRunner object (need to download a file"HTMLTestRunner.py, to .....")
    runner = HTMLTestRunner(stream=report_file, title="Selenium_easy_test_report", description="Details are below")

    # run
    runner.run(suit)
