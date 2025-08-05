# Project-Week-5
Project: Applied Data Analysis: Wrangling, Exploration &amp; BI Dashboards

# Formula One
**Hypothesis / Insights / Business Questions:**


**1. Qualifying Position/Start of Race Position vs. Final Position**
Is there a strong correlation between starting grid position and race finishing position, and does it differ by track?
General and by the track, e.g. which tracks allow the drivers to overtake and win regardless of what position they start? (Reference the Monaco street circuit, which is renown for being difficult to overtake - but where else?)

**2. Pit Stop Strategy and Constructor position in the table Hypothesis:**
On average the duration of the pit stop is faster for the top 3 constructors compared to the rest of the group.

**3. Constructor / Driver Performance Trends Question:**
Which constructor(s) have shown the most consistent performance over multiple seasons, and is there a correlation between the winning driver and winning constructor?

**Plan for the week:**

**Day One (Monday):** 
Choose Datasets and Questions.
  
**Day Two (Tuesday):** 
Begin working on data wrangling and develop a plan for cleaning and transforming the data.

**Day 3 (Wednesday):** 
- Finalize all cleaning, analysis and transformation tasks.
- Finish doing basic EDA and use the insights gained from it to answer the proposed business questions.
- Refine code according to best practices e.g. functions.py.

**Day 4 (Thursday):**
- Create a dashboard in Tableau that can help gain insights necessary to answer the relevant business questions proposed (and beyond)
- Prepare a visually appealing presentation with minimal text to effectively communicate the insights and conclusions to stakeholders.

**Extra Info:**

**1. Qualifying Position vs. Final Position Question:**
- Use `qualifying.csv` and `results.csv`.
- Calculate correlations and create visual heatmaps.
- Can be split into street vs. permanent circuits (`circuits.csv`).
- General and by the track (e.g. which tracks allow the drivers to overtake and win e.g. opposite of Monaco)
 
**2. Pit Stop Strategy and Constructor position in the table Hypothesis:**
- Use `pit_stops.csv`, `results.csv`, and `races.csv`.
- Joining datasets and clean time formats.
- Scatter plots and regression in Python, and dashboards in Tableau?

**3. Constructor / Driver Performance Trends Question:**
- Use `constructor_standings.csv`, `constructor_results.csv`, `races.csv`, and 'driver_standings.csv'.
- Aggregate by constructor, season and driver.
- Visualised as line charts in Tableau for storytelling.

 The [Dataset](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
