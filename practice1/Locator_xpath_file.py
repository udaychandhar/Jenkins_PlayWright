"""
XPath Locator is stroed in XML path
"""

import pytest
from playwright.sync_api import Page, expect

def test_xpathLocator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("//ul[@class='top-menu']//a[normalize-space()='Books']").click()
    # page.locator('//a[contains(text(),"Books")]')



    page.wait_for_timeout(2000)