#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import numpy as np

def one_click_build():
    browser.find_element_by_id('buttonBuild').click()
    time.sleep(0.01)

def lvl_up_building(document, loc, start_level, final_level):
    #print("Building:")
    document.get('http://x10000000.aspidanetwork.com/dorf2.php')
    time.sleep(0.01)
    for i in range(final_level-start_level):
        plots = document.find_elements_by_tag_name('area')
        plots[int(loc)-19].click()
        while plots[int(loc)-19] is None:
            time.sleep(0.01)
        plots = document.find_elements_by_tag_name('area')

def build_res(document):
    document.get('http://x10000000.aspidanetwork.com/dorf1.php')
    time.sleep(0.01)
    print("Building res")
    for i in range(18):
        lvl_up_building(document, i, 0, 10)

def find_uid(document):
    print("Reloading inside Find_UID1()...")
    document.get('http://x10000000.aspidanetwork.com/dorf2.php')
    document.find_elements_by_tag_name('area')[26-19].click()
    time.sleep(0.01)
    l = browser.find_elements_by_class_name("section1")[1].find_element_by_class_name("green").get_attribute("onclick")[41:44]
    time.sleep(0.01)
    print("Reloading inside Find_UID2()...")
    document.get('http://x10000000.aspidanetwork.com/dorf2.php')
    time.sleep(0.01)
    #print(str("UID: "+l))
    return l

def build_villa(document):
    print("Reloading inside Build_villa()...")
    document.get('http://x10000000.aspidanetwork.com/dorf2.php')
    time.sleep(0.01)
    print("Building vill")
    build_loc = np.array([['23', '25', '29', '33'], ['36'], ['31', '30', '39', '32', '19', '27', '22', '40', '37']], dtype=object)
    build_bid = np.array([['05', '06', '07', '08'], ['09'], ['10', '11', '16', '17', '25', '27', '37', '32', '19']], dtype=object)

    #lvl_up_building(document, 26, 1, 19)
    for a in range(len(build_loc)):
        print("Loop a: "+str(a))
        one_click_build()
        for b in range(len(build_loc[a])):
            print("Loop b1: "+str(b))
            uid = find_uid(document)
            build_building(document, build_loc[a][b], build_bid[a][b], uid)
        final_level = 20
        if a == 0 or a == 1:
            final_level = 5
        #Turn one_click_build ON
        one_click_build()
        document.get('http://x10000000.aspidanetwork.com/dorf2.php')
        time.sleep(0.01)
        for b in range(len(build_loc[a])):
            print("Loop b2: "+str(b))
            lvl_up_building(document, build_loc[a][b], 1, final_level)

def build_building(document, loc, bid, uid):
    print('http://x10000000.aspidanetwork.com/dorf2.php?'+u'\u0430'+'='+bid+'&id='+str(loc)+'&c='+str(uid))
    document.get('http://x10000000.aspidanetwork.com/dorf2.php?'+u'\u0430'+'='+bid+'&id='+str(loc)+'&c='+str(uid))
    time.sleep(0.01)

def build_vill(browser):
    browser.get('http://x10000000.aspidanetwork.com/dorf2.php')
    time.sleep(0.01)
    print("Building vill")
    #MB 20
    # for i in range(19):
    #     plots = browser.find_elements_by_tag_name('area')
    #     plots[26-19].click()
    #     while plots[26-19] is None:
    #         time.sleep(0.01)
    #     plots = browser.find_elements_by_tag_name('area')

    #Check num of buildings
    num_builds = 1
    i = 0
    category = 1
    while num_builds > 0 and 19+i < 39 and category <= 3:
        if 19+i == 26:
            i += 1
        browser.get('http://x10000000.aspidanetwork.com/build.php?id='+str(19+i)+'&category='+str(category))
        time.sleep(0.01)
        body = browser.find_element_by_id('content')
        sub_body = body.find_elements_by_class_name('contractWrapper')
        building = []
        for j in range(len(sub_body)):
            sub_body[j] = sub_body[j].find_element_by_class_name('contractLink')
            try:
                temp = sub_body[j].find_element_by_tag_name('button')
                cranny_check = temp.get_attribute("onclick")
                if 'dorf2.php?a=23&' not in cranny_check:
                    building.append(temp)
            except:
                break
        num_builds = len(building)-1
        if num_builds >= 0:
            building[0].click()
            time.sleep(0.01)
        if num_builds == 0:
            category += 1
            num_builds = 1
        i+=1

    res_list = [27, 28, 29, 30]
    for a in range(i-1):
        if 19+a == 26:
            continue
        if 19+a not in res_list:
            for j in range(19):
                plots = browser.find_elements_by_tag_name('area')
                plots[19+a-19].click()
                while plots[19+a-19] is None:
                    time.sleep(0.01)
                plots = browser.find_elements_by_tag_name('area')
        else:
            for j in range(4):
                plots = browser.find_elements_by_tag_name('area')
                plots[19+a-19].click()
                while plots[19+a-19] is None:
                    time.sleep(0.01)
                plots = browser.find_elements_by_tag_name('area')

#BROWSER SETUP
browser = webdriver.Chrome('./chromedriver')
browser.get('http://x10000000.aspidanetwork.com/login.php')
time.sleep(0.01)

#LOGIN
login = browser.find_element_by_class_name('loginTable')
text = login.find_elements_by_class_name('text')
text[0].send_keys('raja')
text[1].send_keys('1lT&HTML')
btn = login.find_element_by_class_name('green')
btn.submit()
time.sleep(0.01)

one_click_build()

#VIEW BUILD LEVEL
browser.get('http://x10000000.aspidanetwork.com/dorf2.php')
time.sleep(0.01)
browser.find_element_by_id('lswitch').click()
plots = browser.find_elements_by_tag_name('area')

#BUILD ALL RES to 10
browser.get('http://x10000000.aspidanetwork.com/dorf1.php?newdid='+str(604)+'&')
time.sleep(0.01)
#build_res(browser)
build_villa(browser)
time.sleep(120)

#19 - 39
#26 = MB
