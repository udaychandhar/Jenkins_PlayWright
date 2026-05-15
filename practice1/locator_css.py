"""
css_selector are taken elements in four different ways:
tag id
tag class
tag attribute
tag class attribute
"""

import pytest
from playwright.sync_api import Page,expect

def test_cssselect_locator(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    #tag id
    # page.locator("input#small-searchterms").fill("Books")
    # page.locator("#small-searchterms").fill("Books")
    # page.wait_for_timeout(3000)


    #tag class
    # page.locator("input.search-box-text").fill("Shoes")
    # page.locator(".search-box-text").fill("Shoes")
    # page.wait_for_timeout(3000)

    #tag attribute
    # page.locator("input[name=q]").fill("cell phones")
    # page.locator("[placeholder='Search store']").fill("cell phones")
    # page.wait_for_timeout(3000)


    #tag class attribute
    # page.locator("input.search-box-text[name=q]").fill("Bolls")
    # page.locator(".search-box-text[name=q]").fill("Bolls")
    # page.wait_for_timeout(3000)

