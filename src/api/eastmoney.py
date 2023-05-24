import requests as rs 

from .base import BaseFundAPI

class EastMoneyFundAPI(BaseFundAPI):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._base_url = "http://fundgz.1234567.com.cn/js/{}.js"
    
    def get_fund_by_code(self, code):
        r = rs.get(self._base_url.format(code))
        if 'html' in r.text:
            return None
        return r.text