# -*- coding: utf-8 -*-

import re


def register_params_check(content):
    """
    TODO: 进行参数检查
    """
    if not content:
        return "username", False

    # check username
    try:
        username = content['username']
        username_len = len(username)
    except BaseException:
        return "username", False
    else:
        username_pattern = re.compile(r"^[a-zA-Z][a-zA-Z]*[0-9][0-9]*$", re.S)
        if username_len < 5 or username_len > 12 or not re.match(
                username_pattern, username):
            return "username", False

    # check password
    try:
        password = content['password']
    except BaseException:
        return "password", False
    else:
        password_pattern = re.compile(
            r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-_*^]).{8,15}$", re.S)
        if not re.match(password_pattern, password):
            return "password", False

    # check nickname
    try:
        nickname = content['nickname']
    except BaseException:
        return "nickname", False
    else:
        nickname_len = len(nickname)
        if nickname_len == 0:
            return "nickname", False

    # check url
    try:
        url = content['url']
    except BaseException:
        return "url", False
    else:
        if not isinstance(url, str):
            return 'url', False
        url_pattern = re.compile(
            r"^(https?:\/\/)(((([\da-zA-Z]+)|([\da-zA-Z][\da-zA-Z-]*[\da-zA-Z]))\.)+"
            r"(([\da-zA-Z]+)|([\da-zA-Z][\da-zA-Z-]*[\da-zA-Z])))$",
            re.S)
        if not re.match(url_pattern, url):
            return "url", False
        else:
            re_body = re.compile(
                r"(((([\da-zA-Z]+)|([\da-zA-Z][\da-zA-Z-]*[\da-zA-Z]))\.)+(([\da-zA-Z]+)"
                r"|([\da-zA-Z][\da-zA-Z-]*[\da-zA-Z])))$",
                re.S)
            body = re.search(re_body, url).group()
            if len(body) > 48:
                return "url", False
            re_url2 = re.compile(r"^.*\.[\d]+$", re.S)
            if re.match(re_url2, url):
                return "url", False

    # check mobile
    try:
        mobile = content['mobile']
    except BaseException:
        return "mobile", False
    else:
        mobile_pattern = re.compile(r"^[+][0-9]{2}[.][0-9]{12}$", re.S)
        if not re.match(mobile_pattern, mobile):
            return "mobile", False

    # check magic_number
    try:
        magic_number = content['magic_number']
    except BaseException:
        content['magic_number'] = 0
    else:
        if not isinstance(magic_number, int):
            return "magic_number", False
        elif int(magic_number) < 0:
            return "magic_number", False
    return "ok", True
