import configparser
config = configparser.RawConfigParser()
path = "Configurations/config.ini"
config.read(path)

class ReadConfig:
    @staticmethod
    def get_Application_url():
        url = config.get('common info', 'pageurl')
        return url

    @staticmethod
    def get_search_text():
        searchtext = config.get('common info', 'search_text')
        return searchtext

    @staticmethod
    def get_promo_code():
        promo_code = config.get('common info', 'promocode')
        return promo_code
