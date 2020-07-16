import csv
from collections import namedtuple

r = csv.reader(open("steps.csv"))
next(r)  # skip header

Question = namedtuple("Question", ["id", "title", "explanation", "answers"])
Answer = namedtuple("Answer", ["icon", "answer", "long_answer", "next_step"])

seen_questions = set()

questions = {}

for row in r:
    id = row[0] or "root"
    if id not in questions:
        questions[id] = Question(id, *row[1:3], [])
    a = Answer(*row[3:])
    questions[id].answers.append(a)

print('digraph G {graph [rankdir="lr"];')
for i, q in enumerate(questions.values()):
    print(f"subgraph cluster0 {{")
    print(f'{q.id} [label="{q.title}"];')
    for i, a in enumerate(q.answers):
        print(f'{q.id}_{i} [label="{a.answer}"]; {q.id} -> {q.id}_{i} -> {a.next_step};')
    print(f"}}")

print("}")