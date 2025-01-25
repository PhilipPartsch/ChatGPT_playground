# from https://pypi.org/project/openai/ chapter usage

import os
import time
from openai import OpenAI
from datetime import datetime


class Ai_Interaction:
    """The class offers the communication with an AI model."""
    client: OpenAI = None
    last_used = []
    RPM = 3
    RPD = 200

    def __init__(self):
        try:
            openai_api_key = os.environ.get("OPENAI_API_KEY")
        except KeyError:
            openai_api_key = "Token not available!"
            # or raise an error if it's not available so that the workflow fails

        self.client = OpenAI(api_key=openai_api_key,)

    def _add_request_to_list(self):
        if len(self.last_used) > (RPD + 10): # if we are above day limit plus 10
            del self.last_used[0] # remove oldest entry
        self.last_used.append(datetime.now())
        print("request " + len(self.last_used) + ": at " + self.last_used[-1])

    def _get_amount_of_requests_in_last_minute(self):
        if len(self.last_used) == 0:
            return 0
        else:
            amount_within_last_minute = 0
            now = datetime.now()
            for i in self.last_used:
                duration = now - i
                if duration.total_seconds() < 61:
                    amount_within_last_minute = amount_within_last_minute + 1
            return amount_within_last_minute

    def _get_amount_of_requests_in_last_day(self):
        if len(self.last_used) == 0:
            return 0
        else:
            amount_within_last_day = 0
            now = datetime.now()
            for i in self.last_used:
                duration = now - i
                if duration.days < 1:
                    amount_within_last_day = amount_within_last_day + 1
            return amount_within_last_day

    def _wait_if_needed(self):
        while True:
            if self._get_amount_of_requests_in_last_minute() < self.RPM and \
               self._get_amount_of_requests_in_last_day() < self.RPD:
                break
            else:
                time.sleep(10)

    def request (self, task, request, ):
        """Create requests to the AI and collect feedback."""

        # Links:
        # Defintion of roles:
        # https://platform.openai.com/docs/guides/text-generation#messages-and-roles
        #
        # Basics:
        # https://platform.openai.com/docs/api-reference/introduction
        #
        # Howto chat with gpt:
        # https://platform.openai.com/docs/api-reference/chat/create
        #
        # Structered output (json data):
        # https://platform.openai.com/docs/guides/structured-outputs
        # Examples:
        #    https://cookbook.openai.com/examples/structured_outputs_intro

        self._wait_if_needed()

        chat_completion = self.client.chat.completions.create(
            messages= [
                {
                "role": "developer",
                "content": [ {"type": "text", "text": task} ]
                },
                {
                "role": "user",
                "content": [{"type": "text", "text": request} ]
                }
            ],

            model="gpt-4o-mini",
            store=False,
            #metadata
            # check howto use

            #response_format
            # check howto use:
            # https://platform.openai.com/docs/api-reference/chat/create#chat-create-response_format
        )

        print(chat_completion)

        self._add_request_to_list()

        return(chat_completion)


ai = Ai_Interaction()

task = "Du bist eine Kinderbuch Autor."
request = "Er stelle eine Liste von fünf Charakter für eine Weltraum-Piraten Geschichte. "

response = ai.request(task, request, )

print(response)
