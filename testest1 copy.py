import re

a = ["어깨를 으쓱함"]
b = ["손을 흔들고 있음"]
c = ["모자를 쓰고 있음"]


def _handle_speech_act(sentence_text: str):
    p = re.compile(r'\(([^)]+)')
    m = p.findall(sentence_text)
    if len(m) > 0:
        return m[0]
    return None

source = '(생각하는 표정을 지으며) "인세셔션"은 스토리가 흥미롭고 생각할 거리를 던져주는 영화입니다.'

action = _handle_speech_act(source)

print(source.replace("(" + action + ") ", ''))
print('here is copy')
print(source)

