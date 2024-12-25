from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=45),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     
    'ROTATE_REFRESH_TOKENS': False,                  
    'BLACKLIST_AFTER_ROTATION': True,                 
    'ALGORITHM': 'HS256',                            
    'SIGNING_KEY': 'your_secret_key_here',            
    'VERIFYING_KEY': None,                       
    'AUTH_HEADER_TYPES': ('Bearer',),                
    'USER_ID_FIELD': 'id',                            
    'USER_ID_CLAIM': 'user_id',
}