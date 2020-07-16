import csv
import logging
from collections import namedtuple
from jinja2 import Template

template = Template(open("mock_template.html").read())

PHASES = ["Getting Started", "Version Control for Your Program/Langauge", "Structure of Your Project Folders", "Checks Before Submitting Your Manuscript"]


class Question:
    def __init__(self, phase, q, followup, followup_if, title, explanation, **_):
        self.phase = PHASES[int(phase) - 1]
        self.q = q.replace(".", "_")
        self.followup = followup.replace(".", "_")
        self.followup_if = followup_if
        self.title = title
        self.explanation = explanation

phases = {phase: [] for phase in PHASES}

questions = [Question(**row) for row in csv.DictReader(open("steps_dichotomised.csv"))]

dependencies = {} # {q: 'yes'/'no': [deps]}
qdict = {q.q: q for q in questions}
for q in questions:
    phases[q.phase].append(q)
    if q.followup:
        target = qdict[q.followup]
        when = {"y": "yes", "n": "no"}[q.followup_if]
        dependencies.setdefault(target.q, {}).setdefault(when, []).append(q.q)


open("mock.html", "w").write(template.render(**locals()))
