from collections import Counter
from datetime import datetime
import time

from flashtext import KeywordProcessor
import json
file = "/data/projects/undertheseanlp/word_tokenize/egs/vlsp2013_crf/data/train.txt"

kp = KeywordProcessor(case_sensitive=True)
rules = json.load(open("rules.json"))
kp.add_keywords_from_dict(rules)

# text = 'công ti vậy mà ty hoà nhã hoàn lương lí luận'
# new_sentence = kp.replace_keywords(text)
# print(new_sentence)
# keyword_found = kp.extract_keywords(text, span_info=True)
# print(keyword_found)
all_founds = []
start = time.time()
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
for i, line in enumerate(open(file)):
    text = line.strip()
    founds = kp.extract_keywords(text, span_info=True)
    if len(founds) > 0:
        all_founds.extend(founds)
        print("\n", founds)
        print(text)
        print(kp.replace_keywords(text))


print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("\nTotal sentences: ", i)
counter = Counter([item[0] for item in all_founds])
end = time.time()
duration = end - start
print(f"Duration:{duration:.2f}")
print(f"Speed: {i / duration:.2f} sentences/second")
print(f"\n{counter}")

