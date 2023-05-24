from .api.base import BaseFundAPI

class Crawler:
    def __init__(self, fund_api: BaseFundAPI) -> None:
        self._api: BaseFundAPI = fund_api
    
    def crawler_fund_by_code(self, code: str):
        return self._api.get_fund_by_code(code)
    
def get_crawler(fund_api: BaseFundAPI) -> Crawler:
    return Crawler(fund_api)