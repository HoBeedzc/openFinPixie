import requests as rs


def unit_test():
    # url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=000001&page=1&per=20&sdate=&edate='
    url = 'http://fundgz.1234567.com.cn/js/001186.js?rt=1463558676006'
    r = rs.get(url)
    print(r.text)
    print("unit test passed!")


if __name__ == "__main__":
    unit_test()
