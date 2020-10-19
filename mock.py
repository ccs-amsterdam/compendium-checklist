import csv
import logging
from collections import namedtuple
from jinja2 import Template

template = Template(open("mock_template.html").read())

PHASES = ["Getting Started", "Version Control for Your Program/Language", "Structure of Your Project Folders", "Checks Before Submitting Your Manuscript"]


class Question:
    def __init__(self, phase, q, followup, followup_if, title, explanation, yes_explanation,
    no_explanation, followup_box, info_box_header, info_box_content, yes_answer, show_me,**_):
        self.phase = PHASES[int(phase) - 1]
        self.q = q.replace(".", "_")
        self.followup = followup.replace(".", "_")
        self.followup_if = followup_if
        self.title = title
        self.explanation = explanation
        self.yes_explanation = yes_explanation
        self.no_explanation = no_explanation
        self.info_box_header = info_box_header
        self.info_box_content = info_box_content
        self.followup_box = followup_box
        self.yes_answer = yes_answer
        self.show_me = show_me

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
    if q.followup_box:
        when = {"Yes": "yes", "n": "no"}[q.yes_answer]


open("index.html", "w").write(template.render(**locals()))
