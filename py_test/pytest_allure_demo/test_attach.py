#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure

def test_attach_text():
    allure.attach("这是一个纯文本", name="这是测试文本附件", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段html块</body>", name="这是测试html附件", attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("C:\\Users\\Administrator.USER-20150816GZ\\Desktop\\test.jpg", name="这是测试图片附件", attachment_type=allure.attachment_type.JPG)

