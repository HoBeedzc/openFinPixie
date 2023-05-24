class BaseFundAPI:
    def __init__(self,*args,**kwargs):
        pass

    def get_fund_by_code(self, code: str):
        raise NotImplementedError
    