from pytrends.request import TrendReq

class trends():
    def __init__(self, geo='GB', gprop='',cat=0, years=5):
        pytrend = TrendReq(hl='en-US', tz=360)
        self.params  = {'gprop': gprop, 'geo': geo, 'timeframe': 'today {}-y'.format(years)}
        
    def get_related(self, kw_list):
        time.sleep(2)
        pytrend.build_payload(kw_list,**self.params)
        related_json = pytrend.related_queries()
        related_dfs=[]
        for kw in related_json.keys():
            for cat in ['top','rising']:
                tmp = related_json[kw][cat]
                tmp['cat'] = cat
                tmp['kw'] = kw
                related_dfs+=[tmp]
        return pd.concat(dfs,axis=0).reset_index(drop=True)
    
    def get_trends(self, kw_list):
        time.sleep(2)
        pytrend.build_payload(kw_list,**self.params)
        return pytrend.interest_over_time().iloc[:,:-1]