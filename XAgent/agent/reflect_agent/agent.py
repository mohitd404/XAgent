from typing import List
from XAgent.agent.base_agent import BaseAgent
from XAgent.utils import RequiredAbilities
from XAgent.message_history import Message

class ReflectAgent(BaseAgent):
    abilities = set([RequiredAbilities.reflection])

    def parse(
        self,
        placeholders: dict = {},
        arguments:dict = None,
        functions=None,
        function_call=None,
        stop=None,
        additional_messages: List[Message] = [],
        *args,
        **kwargs
    ):
        prompt_messages = self.fill_in_placeholders(placeholders)
        messages = prompt_messages + additional_messages

        return self.generate(
            messages=messages,
            arguments=arguments,
            functions=functions,
            function_call=function_call,
            stop=stop,
            *args,**kwargs
        )
