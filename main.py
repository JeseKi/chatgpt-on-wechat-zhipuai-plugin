from common.log import logger
from bridge.context import ContextType
from bridge.reply import Reply , ReplyType
from plugins.plugin import Plugin
import plugins
from plugins.event import Event, EventAction, EventContext
from config import conf
from .config import config

from zhipuai import ZhipuAI

@plugins.register(name="zhipuai", desc="接入了智谱AI的API", version="1.0", author="JeseKi", desire_priority= 600)
class ZhiPuAIPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.text_gen
        logger.info("[ZhiPuAIPlugin] inited")
        self.config = super().load_config()
        self.api_key = config['api_key']
        self.client = ZhipuAI(api_key=self.api_key)
        
        self.prompt = config['prompt']
        self.model = config['model']
        self.temperature = config['temperature']
        self.top_p = config['top_p']
        
    def text_gen(self , e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return
        
        text = e_context["context"].content
        
        response = self.client.chat.completions.create(
            model=self.model,  # 填写需要调用的模型名称
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": text},
            ],
            temperature=self.temperature,
            top_p=self.top_p,
        )
        
        reply = Reply()
        reply.type = ReplyType.TEXT
        reply.content = response.choices[0].message.content
        
        e_context['reply'] = reply
        e_context.action = EventAction.BREAK_PASS