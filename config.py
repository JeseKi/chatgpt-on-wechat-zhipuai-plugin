import json
from config import Config , load_config , conf

with open('plugins/chatgpt-on-wechat-zhipuai-plugin/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
print(config)