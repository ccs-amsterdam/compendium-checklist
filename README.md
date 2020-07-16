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

- [mock.py](mock.py) uses the dichotomised list of steps ([steps_dichotomised.csv](steps_dichotomised.csv)) and the [mock_template.html](mock_template.html) to render the checkist in [mock.html](mock.html).
- The folder [scrape_first_version](scrape_first_version) contains the code to extract the steps from the original versoin:
  - [scrape.py](scrape_first_version/scrape.py) scrapes [index.html](scrape_first_version/index.html) to extract the steps into [steps.csv](scrape_first_version/steps.csv)
  - [dichotomise.py](scrape_first_version/dichotomise.py) transforms the steps into yes/no follow ups in ([steps_dichotomised.csv](steps_dichotomised.csv)). IIRC, I manually changed the programming language question into three yes/no questions for each language. 
  - As a bonus, [graph.py](scrape_first_version/graph.py) visualizes the steps as a [DOT graph](https://raw.githubusercontent.com/vanatteveldt/compendium-checklist/master/scrape_first_version/graph.png)


