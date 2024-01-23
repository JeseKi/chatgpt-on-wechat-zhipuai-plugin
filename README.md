# chatgpt-on-wechat-zhipuai-plugin

## 1. 用途
此插件旨在接入智谱AI的API，不过值得注意的是这将覆盖原本的ChatGPT且会覆盖一部分插件，可以选择将`plugins.json`中zhipuai的`priority`调低来选择避免覆盖一部分插件。

## 2. 环境
插件兼容Python 3.10。

## 3. 安装方法
要安装此插件，请按照[插件安装说明](https://github.com/zhayujie/chatgpt-on-wechat/blob/master/plugins/README.md#%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95)中的步骤进行。

## 4. 启动方法
要启动此插件，请导航到此插件的目录，复制`config.json.template`，然后将其重命名为`config.json`。在其中填入你的数据，格式如下：

```python
{
    "model" : "glm-3-turbo", # 模型名称
    "api_key": "", # 你的智谱API Key，可在智谱AI官网申请，假如没有则会出现报错
    "prompt" : "", # 你的智谱AI对模型的角色定义
    "temperature" : 0.7, # 温度
    "top_p" : 0.7 # 核取样
}
```

完成这些步骤后，即可正常使用插件。