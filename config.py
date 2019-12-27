import os 
class Config:
    
    BASE_URL ='https://newsapi.org/v2sources?&apiKey={}'
    NEWS_API_KEY='edd4b77a584a495da73d081cebc0bc7e'
    
    
    pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
     Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}