import csv
import re
import sys

from lxml import html, etree
from lxml.html import Element

html_str = open("index.html").read()
tree = html.fromstring(html_str)


def cssselect(node: Element, selector: str) -> Element:
    result = node.cssselect(selector)
    if len(result) != 1:
        raise Exception(f"Selector {str} on node {inner_html(node)} gave {len(result)} results, needed one")
    return result[0]


def inner_html(node: Element) -> str:
    return ''.join([etree.tostring(child, encoding="utf-8").decode("utf-8") for child in node.iterdescendants()])


w = csv.writer(open("steps.csv", "w"))
w.writerow(["id", "title", "explanation", "icon", "answer", "long_answer", "next_step"])
for step in tree.cssselect(".step"):
    parent = step.getparent()
    if "branch" in parent.get("class", "").split():
        id = parent.get("id")
    else:
        id = step.get("id")
    state = step.get("data-state")
    global_next_step = None if state == "branchtype" else state
    title = cssselect(step, ".question_title > h3").text_content()
    explanation = cssselect(step, ".question_title > p").text_content()

    for answer in step.cssselect(".item"):
        value = cssselect(answer, "input").get("value")
        label = inner_html(cssselect(answer, "label"))
        m = re.match(r'<img [^>]*src="(.*?)"[^>]*>(?:<strong>(.*?)</strong>)?(.*)', label)
        if not m:
            print(repr(label))
            raise Exception("Moe")
        icon, answer, long_answer = m.groups()


        next_step = global_next_step if global_next_step is not None else value
        w.writerow([id, title, explanation, icon, answer, long_answer, next_step])
