from .api.eastmoney import EastMoneyFundAPI

class Crawler:
    def __init__(self) -> None:
        self._api = EastMoneyFundAPI()
    
    def crawler_fund_by_code(self, code):
        return self._api.get_fund_by_code(code)