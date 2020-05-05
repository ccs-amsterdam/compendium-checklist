import csv
import logging
from collections import namedtuple

r = csv.reader(open("steps.csv"))
Row = namedtuple("Row", next(r))
rows = [Row(*x) for x in r]
Answer = namedtuple("Answer", ["icon", "answer", "long_answer", "next_step"])


class Question:
    def __init__(self, id, title, explanation):
        self.id = id
        self.title = title
        self.explanation = explanation
        self.answers = []

questions = {}
for row in rows:
    if row.id not in questions:
        questions[row.id] = Question(*row[:3])
    questions[row.id].answers.append(Answer(*row[3:]))

w = csv.writer(open("steps_dichotomised.csv", "w"))
w.writerow(["id", "title", "explanation",
            "yes_answer", "yes_icon", "yes_explanation", "yes_next",
            "no_answer", "no_icon", "no_explanation", "no_next"])
for q in questions.values():
    if len(q.answers) != 2:
        logging.warning(f"Skipping {q.title}")
        continue
    row = [q.id, q.title, q.explanation]
    for a in q.answers:
        row += [a.answer, a.icon, a.long_answer, a.next_step]
    w.writerow(row)
