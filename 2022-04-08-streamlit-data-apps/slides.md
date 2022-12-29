---
theme: default
class:
  - lead
  - invert
paginate: true
# backgroundColor: #fff
marp: true
# header: Hello
footer: Alberto Cámara - Streamlit Data Apps - 2022-04-08
---

<!-- _class: -->
# **Building a Data App in Python with Streamlit**

![bg left:30% width:300](img/hybrid-theory.png)

**Alberto Cámara**
**Hybrid Theory Tech Talk**
2022-04-08

---

## Helping non-technical people make __data-driven decisions__

This is a painful, difficult and noble art

---

### Related __Data Analysis__ and __reporting__ disciplines

- __Data Visualization__. Representation of information in graphical form

- __Data Storytelling__. Effective communication of insights from a dataset using narratives and visualizations

---

![bg right:40% width:500](img/data-viz.png)

# Data Visualization

* **D3.js**
* **Matplotlib** / **Pyplot**
* **Seaborn**
* **Bokeh**
* **Plotly** / **Plotly Express**

<!-- D3.js: best choice for data visualization professionals -->
<!-- Matplotlib: comes from matlab, non-pythonic -->
<!-- Seaborn: good for statistical visualization -->
<!-- Bokeh: great for interactive plots on a browser -->
<!-- Plotly: really a javascript package with a python port -->

---

# Data Storytelling

* **Dashboards**
    - **Power BI**, Tableau, QlikView, **Apache Superset**, **Databricks**
* **Notebooks**
    - **Databricks**, Jupyter, SageMaker
* **Data Apps**
    - Plotly Dash, **Streamlit**


<!-- Dashboards: Good for multiple users, data drill-down -->
<!-- Notebooks: They enable code execution; good for combining code, explanations and viz -->
<!-- Data Apps: good for lightweight, backend-less, mock-ups -->
<!-- The choice of tool depends on the problem at hand -->

---

# Installing & running Streamlit

```bash
pip install streamlit
```

```python
#app.py
import streamlit as st

st.title("Hello world")
```

```bash
streamlit run app.py
```

Go to `http://localhost:8501`

---

# Meteobeguda

* **Narcís Batlle** from **La Beguda Alta** has a weather station

* We use its data in order to learn:
   - Amounts of rainfall
   - Whether it is freezing

* We are working on a project to predict **mildew attacks**:
   - Analysis and aggregation of historical data going back to 1990
   - Daily ETL of weather data 

---

# Idea: let's check the weather using a Data App

We need:

* Recent information from `https://meteobeguda.cat/`
* To digest and transform the data
* To visualize the data and report main values of KPIs

---

# Dependencies
<!-- _class: -->

```toml
[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.27.1"
pandas = "^1.4.1"
numpy = "^1.22.3"
streamlit = "^1.7.0"
typer = "^0.4.0"
plotly-express = "^0.4.1"
```
---
<!-- _class: -->

- Fetching data: via `requests.get`
- Parsing response (after defining a long dict of `COLUMNS` and their `dtypes`):

```python
import pandas as pd

def parse_response(raw: bytes) -> pd.DataFrame:
    return pd.read_csv(
        BytesIO(raw),
        sep=r"\s+",
        header=None,
        skiprows=3,
        encoding="latin1",
        names=COLUMNS.keys(),
        index_col=False,
        dtype=COLUMNS,
    )

def parse_timestamps(data: pd.DataFrame) -> None:
    data["timestamp"] = pd.to_datetime(data["date"] + " " + data["time"], dayfirst=True)
    data.drop(["date", "time"], axis=1, inplace=True)
```
---

A few Streamlit widgets:

* `st.text()`, `st.markdown()`: add text
* `st.metric()`: define a value with a label and a _delta_
* `st.plotly_chart()`: out of several plotting options
* `st.button()`, `st.text_input()`, `st.date_input()`... many more input widgets

---

# Code, test, run locally, deploy

---

# Streamlit use cases at Hybrid Theory

* Monitoring of files in S3 buckets

* Demo for the URL IAB Classifier
