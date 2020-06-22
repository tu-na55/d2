# データベースへの接続設定を変更
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',
        'USER': 'root',
        'PASSWORD': 'rpass',
        'PORT': '3306',
        'HOST': 'db',
        # 'HOST': '127.0.0.1',
    }
}

# DisallowedHost対策
# ALLOWED_HOSTS = ['192.168.64.8',]

# Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = '/static/' # 追加します
