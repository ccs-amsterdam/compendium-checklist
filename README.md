# Compendium checklist

Code to reverse-engineer the original checklist html and create a bootstrap version.
The most important file to edit is probably [mock_template.html](mock_template.html) , which controls the template. 
To render, install the packages from requirements.txt and call [mock.py](mock.py), e.g. something like:

```
python3 -m venv env
env/bin/pip install -r requirements.txt
env/bin/python mock.py
firefox mock.html
```

## Files:

- [scrape.py](scrape.py) scrapes [index.html](index.html) to extract the steps into [steps.csv](steps.csv)
- [dichotomise.py](dichotomise.py) transforms the steps into yes/no follow ups stored in [steps_dichotomised.csv](steps_dichotomised.csv). IIRC, I manually changed the programming language question into three yes/no questions for each language. 
- [mock.py](mock.py) then uses the dichotomised steps and [mock_template.html](mock_template.html) to render the checkist in [mock.html](mock.html). [Rendered Preview](https://htmlpreview.github.io/?https://github.com/vanatteveldt/compendium-checklist/blob/master/mock.html)
- As a bonus, [graph.py](graph.py) visualizes the steps as a [DOT graph](https://raw.githubusercontent.com/vanatteveldt/compendium-checklist/master/graph.png)


