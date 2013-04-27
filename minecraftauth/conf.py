from django.conf import settings
from appconf import AppConf

class MinecraftAuthConf(AppConf):
    LOGIN_URL = 'https://login.minecraft.net/'

