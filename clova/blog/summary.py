# -*- coding: utf-8 -*-

import requests
import json

class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }

        response_lines = []

        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-002',
                        headers=headers, json=completion_request, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    response_lines.append(line.decode("utf-8"))

        # 마지막에서 4번째 줄 출력
        if len(response_lines) >= 4:
            data= str(response_lines[-4][5:])
        return data


def summary():
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiYzjAYq2uZZtr0ns8xJeNqCKU/rGkBcGakeU20ADskchYewPuItf/Sn86Dm7+JHaw/Z9wJ1q5s/OBcQA6TInMGT43Gvu7IhbvW1NhDDTzV5AsNlaa6OJOxGL2KqO3Pr7RHWjJEwoC+ITSczC8NIaYHBzBvL3JYMmZOcoxLl4Ad9YNvQhFw1eX9N3R6YyyEx2MkHwB6JFlf/r9KMwXAcbvTW8=',
        api_key_primary_val='UIuIUdFAlwVtaHf1JnG8qmttirh33waDWvVa7b7m',
        request_id='bb815f90035e4825ad9e68ebc21de95e'
    )

    preset_text = [{"role":"system","content":"회의 내용 : 태형: 안녕하세요, 모두! 오늘은 동민님이 제안해주신 사용자 경험과 디자인 아이디어에 대해 논의해보려고 합니다. 동민님, 어떤 아이디어를 갖고 계신가요?\r\n동민: 네, 먼저 시각장애인들을 위한 웹사이트이기 때문에 화면 낭독기를 활용한 기능이 중요하다고 생각합니다. 사용자가 웹 페이지에서 어떤 내용이 있는지 손쉽게 파악할 수 있도록 음성 안내가 필요할 것 같아요.\r\n원국: 그런 아이디어는 좋네요. 화면 낭독기를 통해 정보를 전달하는 것은 시각적으로 정보를 얻기 어려운 사용자들에게 큰 도움이 될 것 같습니다.\r\n기호: 또한, 웹사이트 내에서 콘텐츠를 찾아가는 과정이 간편해야 할 것 같아요. 메뉴 구성이나 검색 기능을 효과적으로 활용하여 사용자가 원하는 정보에 빠르게 접근할 수 있도록 해야 합니다. \r\n태형: 동민님의 의견을 반영해서 UI와 UX 디자인에 이러한 기능을 포함하는 것이 중요하겠네요. 더불어, 사용자 피드백을 수시로 받아 개선하는 체계도 필요할 것 같습니다. 기호님이 진행 중인 업무를 정리해주세요\r\n동민: 맞아요. 사용자들의 피드백을 통해 우리 서비스를 지속적으로 개선해 나가는 것이 중요하겠죠.\r\n원국: 그리고 특수한 Bed-to-Bed 서비스에 대해서도 어떤 추가 기능이 필요한지 생각해봐야 할 것 같아요. 기호님이 해주실 수 있나요?\r\n기호: 네. 제가 처리할게요. 또한 추가 기능을 계속해서 생각해봐야 할 거 같아요.\r\n동민: 맞아요. 예를 들면, 예약된 서비스에 대한 상태를 실시간으로 확인할 수 있는 기능이 있으면 좋을 것 같습니다.\r\n태형: 좋은 아이디어네요. 다음 회의 때에는 이런 세부 기능에 대해 더 깊이 논의해보도록 하겠습니다. 동민님, 계속해서 소중한 의견 주셔서 감사합니다.\r\n동민: 감사합니다. 다음 회의에서 더 많은 아이디어를 나눠보도록 하겠습니다. 모두 수고하세요!\n\r\n\n"},{"role":"user","content":"회의 내용을 기반으로 회의록으로 작성해줘 "},{"role":"assistant","content":"회의록\n\n일시: 2023년 7월 5일 오후 2시\n\n참석자: 태형, 동민, 원국, 기호\n\n회의 주제: 시각장애인용 웹사이트 개발 관련 회의\n\n회의 내용\n\n- 동민 님이자 경험과 디자인 아이디어에 대해 논의함\n- 화면 낭독기를 활용한 기능이 중요하다는 의견 제시됨\n- 메뉴 구성이나 검색 기능을 효과적으로 활용하여 사용자가 원하는 정보에 빠르게 접근할 수 있도록 해야 한다는 의견 제시됨\n- 사용자 피드백을 수시로 받아 개선하는 체계가 필요하다는 의견 제시됨\n- 특수한 Bed-to-Bed 서비스에 대해 추가 기능이 필요하다는 의견 제시됨\n- 예약된 서비스에 대한 상태를 실시간으로 확인할 수 있으면 좋겠다는 의견 제시됨\n\n다음 회의 일정\n\n- 일시: 2023년 7월 12일 오후 2시\n- 장소: 온라인 회의 플랫폼 Zoom\n- 안건: 이번 회의에서 나온 아이디어를 구체화하고, 세부 기능에 대해 논의하기로 함"},
                   {"role":"user","content":"회의 내용을 기반으로 회의록으로 작성해줘 "}]

    request_data = {
        'messages': preset_text,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.5,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True
    }

    result = completion_executor.execute(request_data)
    parsed_data = json.loads(result)
    output_data = parsed_data['message']['content']
  
    # 회의록 데이터를 줄 단위로 분리
    lines = output_data.split('\n')

    # 회의록을 HTML 형식으로 재구성
    formatted_meeting = "<div class='meeting-summary'>\n"
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("일시:") or line.startswith("참석자:") or line.startswith("회의 주제:"):
            formatted_meeting += f"<h2>{line}</h2>\n"
        elif line == "회의 내용" or line == "다음 회의 일정":
            formatted_meeting += f"<h2 class='important-section'>{line}</h2>\n"
        elif line.startswith("- "):  # 회의 내용의 항목 처리
            formatted_meeting += f"<li>{line[2:]}</li>\n"
        else:  # 기타 텍스트 처리
            formatted_meeting += f"<p>{line}</p>\n"

    formatted_meeting += "</div>"
    return formatted_meeting