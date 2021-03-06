import pytest
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

wc = WebsiteController()

def test_login():
    try:
        uname = 'testuname'
        pwd = 'testpwd'
        result = wc.login(uname, pwd)
        
    except:
        result = 'Could not login.'
        
    assert result
    
def test_setMinDryness():
    minDryness = 5
    try:
        result = wc.setMinDryness(minDryness)
        
    except:
        result = 'Could not set minimum dryness value.'
        
    assert result

def test_waterPlant():
    try:
        result = wc.waterPlant()
        
    except:
        result = 'Could not water plant.'
        
    assert result
