---
title: "Project 2: Climate Change - Temperatures and Precipitation"
assignment: project2
semester: sp26
source: semester_assignments/sp26/project/project2/autograder/project2.ipynb
version: solution (autograder) with student scaffolds
student_source: semester_assignments/sp26/project/project2/student/project2.ipynb
total_points: 60.0
language: python
---

![The Data 8 course logo: the words DATA 8 on overlapping translucent colored circles.](project2_assets/data8logo.png)

# Project 2: Climate Change - Temperatures and Precipitation

In this project, you will investigate data on climate change, or the long-term shifts in temperatures and weather patterns!


### Logistics

**Deadline.**  This project is due at **5:00pm PT on Friday, 4/17**. You can receive 5 bonus points for submitting the project by **5:00pm PT on Thursday, 4/16.** Projects submitted fewer than 24 hours after the deadline will receive 80% credit. Any submissions later than 24 hours after the deadline will not be accepted. It's **much** better to be early than late, so start working now.

**Checkpoint.**  For full credit on the checkpoint, you must complete the questions up to the checkpoint, **pass all _public_ autograder tests** for those sections, and submit to the Pensieve Project 2 Checkpoint assignment by **5:00pm PT on Friday, 4/10**. <span style="color: #BC412B">**The checkpoint is worth 1 lab score**</span>. After you've submitted the checkpoint, you may still change your project answers before the final project deadline - **only your final submission, to the "Project 2 Autograder" assignment, will be graded for correctness** (including questions from before the checkpoint). You will have some lab time to work on these questions, but we recommend that you start the project before lab and leave time to finish the checkpoint afterward.

**Partners.** You may work with one other partner; your partner must be from your assigned lab section. **<span style="color: #BC412B">Only one partner should submit the project notebook to Pensieve.</span> If both partners submit, you will be docked 10% of your project grade. On Pensieve, the person who submits should also designate their partner so that both of you receive credit.** Once you submit, click into your submission, and there will be an option to Add Group Member in the top right corner. You may also reference [this walkthrough video](https://drive.google.com/file/d/1bs1l_f44tUeF1yKY_iljZMTE1X0dYKLl/view?usp=sharing) on how to add partners on Pensieve.

**Rules.** Don't share your code with anybody but your partner. You are welcome to discuss questions with other students, but don't share the answers. The experience of solving the problems in this project will prepare you for exams (and life). If someone asks you for the answer, resist! Instead, you can demonstrate how you would solve a similar problem.

**Support.** You are not alone! Come to office hours, post on Ed, and talk to your classmates. If you want to ask about the details of your solution to a problem, make a private Ed post and the staff will respond. If you're ever feeling overwhelmed or don't know how to make progress, email your TA or tutor for help. You can find contact information for the staff on the [course website](https://www.data8.org/su26/staff).

**Tests.** <span style="color: #BC412B">The tests that are given are **not comprehensive** and passing the tests for a question **does not** mean that you answered the question correctly.</span> For table manipulation questions, tests usually only check that your table has the correct column labels. Similarly, on multiple choice / select all that apply questions, tests are only checking that your response in the right format, not that it is correct. However, more tests will be applied to verify the correctness of your submission in order to assign your final score, so be careful and check your work! You might want to create your own checks along the way to see if your answers make sense. Additionally, before you submit, make sure that none of your cells take a very long time to run (several minutes).

**Free Response Questions:** Make sure that you put the answers to the written questions in the indicated cell we provide. **Every free response question should include an explanation** that adequately answers the question. 

**Advice.** Develop your answers incrementally. To perform a complicated task, break it up into steps, perform each step on a different line, give a new name to each result, and check that each intermediate result is what you expect. You can add any additional names or functions you want to the provided cells. Make sure that you are using distinct and meaningful variable names throughout the notebook. Along that line, **DO NOT** reuse the variable names that we use when we grade your answers. 

You **never** have to use just one line in this project or any others. Use intermediate variables and multiple lines as much as you would like!

All of the concepts necessary for this project are found in the textbook. If you are stuck on a particular problem, reading through the relevant textbook section will often help to clarify concepts.

---

The point breakdown for this assignment is given in the table below:
| Category | Points |
| --- | --- |
| Autograder (Coding questions) | 60 |
| Written | 40 |
| **Total** | 100 |

---

To get started, load `datascience`, `numpy`, and `matplotlib`. Make sure to also run the first cell of this notebook to load `otter`.

**Code:**

```python
# Run this cell to set up the notebook, but please don't change it.
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
np.set_printoptions(legacy='1.13')

import warnings
warnings.simplefilter('ignore')

import plotly.graph_objects as go
```

---
## Part 1: Temperatures

In the following analysis, we will investigate one of the 21st century's most prominent issues: climate change. While the details of climate science are beyond the scope of this course, we can start to learn about climate change just by analyzing public records of different cities' temperature and precipitation over time.

We will analyze a collection of historical daily temperature and precipitation measurements from weather stations in 210 U.S. cities. The dataset was compiled by Yuchuan Lai and David Dzombak [1]; a description of the data from the original authors and the data itself is available [here](https://kilthub.cmu.edu/articles/dataset/Compiled_daily_temperature_and_precipitation_data_for_the_U_S_cities/7890488). 

[1] Lai, Yuchuan; Dzombak, David (2019): Compiled historical daily temperature and precipitation data for selected 210 U.S. cities. Carnegie Mellon University. Dataset.

### Part 1, Section 1: Cities

Run the following cell to load information about the `cities` and preview the first few rows.

**Code:**

```python
cities = Table.read_table('city_info.csv', index_col=0)
cities.show(3)
```

*Output:*

| Name | ID | Lat | Lon | Stn.Name | Stn.stDate | Stn.edDate |
| --- | --- | --- | --- | --- | --- | --- |
| Lander | USW00024021 | 42.8153 | -108.726 | LANDER WBO | 1892-01-01 | 1946-05-28 |
| Lander | USW00024021 | 42.8153 | -108.726 | LANDER HUNT FIELD | 1946-05-29 | 2021-12-31 |
| Cheyenne | USW00024018 | 41.1519 | -104.806 | CHEYENNE WBO | 1871-01-01 | 1935-08-31 |

The `cities` table has one row per weather station and the following columns:

1. `"Name"`: The name of the US city
2. `"ID"`: The unique identifier for the US city
3. `"Lat"`: The latitude of the US city (measured in degrees of latitude)
4. `"Lon"`: The longitude of the US city (measured in degrees of longitude)
4. `"Stn.Name"`: The name of the weather station in which the data was collected
5. `"Stn.stDate"`: A string representing the date of the first recording at that particular station
6. `"Stn.edDate"`: A string representing the date of the last recording at that particular station

The data lists the weather stations at which temperature and precipitation data were collected. Note that although some cities have multiple weather stations, only one station records data for a city at any given time. Thus, we are able to just focus on the cities themselves.

---

**Question 1.1.1:** In the cell below, produce a scatter plot that plots the latitude and longitude of every city in the `cities` table so that the result places northern cities at the top and western cities at the left.

*Note*: It's okay to plot the same point multiple times!

*Hint*: A latitude is the set of horizontal lines that measures distances *north or south* of the equator. A longitude is the set of vertical lines that measures distances *east or west* of the prime meridian.

**Student scaffold:**

```python
...
```

**Solution:**

```python
cities.scatter("Lon", "Lat") # SOLUTION
```

![Plot output from cell 11 — see preceding code](project2_assets/cell011_out0.png)

These cities are all within the contiguous U.S., and so the general shape of the U.S. should be visible in your plot. The shape will appear distorted compared to most maps for two reasons: the scatter plot is square even though the U.S. is wider than it is tall, and this scatter plot is an [equirectangular projection](https://en.wikipedia.org/wiki/Equirectangular_projection) of the spherical Earth. A geographical map of the same data uses the common [Pseudo-Mercator projection](https://en.wikipedia.org/wiki/Web_Mercator_projection).

> *Note:* If this visualization doesn't load for you, please view a version of it online [here](https://github.jonathanferrari.com/static/city_map.html).

**Code:**

```python
# Just run this cell
fig = go.Figure(data=go.Scattergeo(
        lon = cities.column('Lon'),
        lat = cities.column('Lat'),
        text = cities.column('Name'),
        mode = 'markers'))

fig.update_layout(geo_scope='usa', width=800, height=500, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
fig.show()
```

*Output: interactive Plotly figure (not captured).*

---

**Question 1.1.2** Does it appear that these city locations are sampled uniformly at random from all land in the continental U.S.? Why or why not?

**SOLUTION:** No. The cities are very concentrated around the coasts; a uniform random sample would include more cities in the central regions.

---

**Question 1.1.3:** Assign `num_unique_cities` to the number of unique cities that appear in the `cities` table.

**Student scaffold:**

```python
num_unique_cities = ...

# Do not change this line
print(f"There are {num_unique_cities} unique cities that appear within our dataset.")
```

**Solution:**

```python
num_unique_cities = cities.group("Name").num_rows # SOLUTION

# Do not change this line
print(f"There are {num_unique_cities} unique cities that appear within our dataset.")
```

*Output (stdout):*

```text
There are 210 unique cities that appear within our dataset.
```

**Test — `q1_1_3` (4 points)**

```python
>>> bool(type(num_unique_cities) in set([int, np.int32, np.int64]))
True

>>> bool(num_unique_cities > 0)
True

# hidden test
>>> bool(num_unique_cities == 210)
True
```

In order to investigate further, it will be helpful to determine what region of the United States each city was located in: Northeast, Northwest, Southeast, or Southwest. For our purposes, we will be using the following geographical boundaries:

![USA Coordinate Map](project2_assets/usa_coordinates.png)

1. A station is located in the `"Northeast"` region if its latitude is above or equal to 40 degrees and its longitude is greater than or equal to -100 degrees.
2. A station is located in the `"Northwest"` region if its latitude is above or equal to 40 degrees and its longitude is less than -100 degrees.
3. A station is located in the `"Southeast"` region if its latitude is below 40 degrees and its longitude is greater than or equal to -100 degrees.
4. A station is located in the `"Southwest"` region if its latitude is below 40 degrees and its longitude is less than -100 degrees.

---

**Question 1.1.4**: Define the `coordinates_to_region` function below. It should take in two arguments, a city's latitude (`lat`) and longitude (`lon`) coordinates, and output a string representing the region it is located in.

**Student scaffold:**

```python
def coordinates_to_region(...):
    ...
```

**Solution:**

```python
""" # BEGIN PROMPT
def coordinates_to_region(...):
    ...
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
def coordinates_to_region(lat, lon):
    """Returns a string representing the geographical region corresponding to the lat and lon"""
    if lat < 40:
        if lon < -100:
            return "Southwest"
        elif lon >= -100:
            return "Southeast"
    elif lat >= 40:
        if lon <-100:
            return "Northwest"
        elif lon >= -100:
            return "Northeast"
# END SOLUTION
```

**Test — `q1_1_4` (4.0 points)**

```python
>>> bool(type(coordinates_to_region(50, 100)) == str)
True

# hidden test
>>> bool(coordinates_to_region(41, 10) == 'Northeast')
True

# hidden test
>>> bool(coordinates_to_region(40, -100) == 'Northeast')
True

# hidden test
>>> bool(coordinates_to_region(41, -110) == 'Northwest')
True

# hidden test
>>> bool(coordinates_to_region(10, -110) == 'Southwest')
True

# hidden test
>>> bool(coordinates_to_region(10, 15) == 'Southeast')
True

# hidden test
>>> bool(coordinates_to_region(39, -100) == 'Southeast')
True
```

---

**Question 1.1.5**: Add a new column in `cities` labeled `Region` that contains the region in which the city is located. For full credit, you must use the `coordinates_to_region` function you defined rather than reimplementing its logic.

**Student scaffold:**

```python
regions_array = ...
cities = ...
cities.show(5)
```

**Solution:**

```python
regions_array = cities.apply(coordinates_to_region, "Lat", "Lon") # SOLUTION
cities = cities.with_column("Region", regions_array) # SOLUTION
cities.show(5)
```

*Output:*

| Name | ID | Lat | Lon | Stn.Name | Stn.stDate | Stn.edDate | Region |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lander | USW00024021 | 42.8153 | -108.726 | LANDER WBO | 1892-01-01 | 1946-05-28 | Northwest |
| Lander | USW00024021 | 42.8153 | -108.726 | LANDER HUNT FIELD | 1946-05-29 | 2021-12-31 | Northwest |
| Cheyenne | USW00024018 | 41.1519 | -104.806 | CHEYENNE WBO | 1871-01-01 | 1935-08-31 | Northwest |
| Cheyenne | USW00024018 | 41.1519 | -104.806 | CHEYENNE MUNICIPAL ARPT | 1935-09-01 | 2021-12-31 | Northwest |
| Wausau | USW00014897 | 44.9258 | -89.6256 | Wausau Record Herald | 1896-01-01 | 1941-12-31 | Northeast |

**Test — `q1_1_5` (4 points)**

```python
>>> bool(len(cities.labels) == 8)
True

>>> bool(cities.labels[-1] == 'Region')
True

>>> bool(cities.row(0).item('Region') == 'Northwest')
True

# hidden test
>>> bool(np.all(np.sort(cities.group('Region').column('Region')) == make_array('Northeast', 'Northwest', 'Southeast', 'Southwest')))
True

# hidden test
>>> bool(np.all(cities.group('Region').column('count') == make_array(149, 62, 203, 47)))
True
```

To confirm that you've defined your `coordinates_to_region` function correctly and successfully added the `Region` column to the `cities` table, run the following cell. Each region should have a different color in the result.

**Code:**

```python
# Just run this cell
cities.scatter("Lon", "Lat", group="Region")
```

![Plot output from cell 28 — see preceding code](project2_assets/cell028_out0.png)

---

**Challenge Question 1.1.6 <span style="color:#BC412B">(OPTIONAL, ungraded)</span>**: Create a new table called `cities_nearest`. It should contain the same columns as the `cities` table and an additional column called `"Nearest"` that contains the **name of the nearest city** that is in a different region from the city described by the row.

To approximate the distance between two cities, take the square root of the sum of the squared difference between their latitudes and the square difference between their longitudes. **Don't use a `for` statement; instead, use the `apply` method and array arithmetic.**

*Hint*: We have defined a `distance` function for you, which can be called on numbers `lat0` and `lon0` and arrays `lat1` and `lon1`.

**Student scaffold:**

```python
def distance(lat0, lon0, lat1, lon1):
    "Approximate the distance between point (lat0, lon0) and (lat1, lon1) pairs in the arrays."
    return np.sqrt((lat0 - lat1) * (lat0 - lat1) + (lon0 - lon1) * (lon0 - lon1))

...

cities_nearest = ...
# Note: remove the comment(#) on the next line if you choose to do this question
#cities_nearest.show(5)
```

**Solution:**

```python
def distance(lat0, lon0, lat1, lon1):
    "Approximate the distance between point (lat0, lon0) and (lat1, lon1) pairs in the arrays."
    return np.sqrt((lat0 - lat1) * (lat0 - lat1) + (lon0 - lon1) * (lon0 - lon1))

# BEGIN SOLUTION
def nearest(name):
    row = cities.where('Name', name).row(0)
    others = cities.where('Region', are.not_equal_to(row.item('Region')))
    distances = distance(row.item('Lat'), row.item('Lon'), 
                         others.column('Lat'), others.column('Lon'))
    return others.with_column('dist', distances).sort('dist').row(0).item('Name')

nearest_array = cities.apply(nearest, "Name")
# END SOLUTION

cities_nearest = cities.with_column("Nearest", nearest_array) # SOLUTION
# Note: remove the comment(#) on the next line if you choose to do this question
#cities_nearest.show(5)
```

### Part 1, Section 2: Welcome to Phoenix, Arizona

Each city has a different CSV file full of daily temperature and precipitation measurements. The file for Phoenix, Arizona is included with this project as `phoenix.csv`. The files for other cities can be downloaded [here](https://kilthub.cmu.edu/articles/dataset/Compiled_daily_temperature_and_precipitation_data_for_the_U_S_cities/7890488) by matching them to the ID of the city in the `cities` table.

Since Phoenix is located on the upper edge of the Sonoran Desert, it has some impressive temperatures.

Run the following cell to load in the `phoenix` table. It has one row per day and the following columns:

1. `"Date"`: The date (a string) representing the date of the recording in **YYYY-MM-DD** format
2. `"tmax"`: The maximum temperature for the  day (°F)
3. `"tmin"`: The minimum temperature for the day (°F)
4. `"prcp"`: The recorded precipitation for the day (inches)

**Code:**

```python
phoenix = Table.read_table("phoenix.csv", index_col=0)
phoenix.show(3)
```

*Output:*

| Date | tmax | tmin | prcp |
| --- | --- | --- | --- |
| 1896-01-01 | 66 | 30 | 0 |
| 1896-01-02 | 64 | 30 | 0 |
| 1896-01-03 | 68 | 30 | 0 |

---

**Question 1.2.1:** Assign the variable `largest_2010_range_date` to the date of the **largest temperature range** in Phoenix, Arizona for any day between January 1st, 2010 and December 31st, 2010. To get started, use the variable `phoenix_with_ranges_2010` to filter the phoenix table to days in 2010 with an additional column corresponding to the temperature range for that day. 

**Your answer should be a string in the "YYYY-MM-DD" format.** Feel free to use as many lines as you need. A temperature range is calculated as the difference between the max and min temperatures for the day.

*Hint*: To limit the values in a column to only those that *contain* a certain string, pick the right `are.` predicate from the [Python Reference Sheet](https://www.data8.org/su26/reference/#table-filtering-predicates).

*Note:* Do **not** re-assign the `phoenix` variable; please use the `phoenix_with_ranges_2010` variable instead.

**Student scaffold:**

```python
...
phoenix_with_ranges_2010 = ...
largest_2010_range_date = ...
largest_2010_range_date
```

**Solution:**

```python
""" # BEGIN PROMPT
...
phoenix_with_ranges_2010 = ...
largest_2010_range_date = ...
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
ranges_array = phoenix.column("tmax") - phoenix.column("tmin")
phoenix_with_ranges = phoenix.with_column("ranges", ranges_array)
phoenix_with_ranges_2010 = phoenix_with_ranges.where("Date", are.containing("2010"))
largest_2010_range_date = phoenix_with_ranges_2010.sort("ranges", descending=True).column("Date").item(0)
# END SOLUTION
largest_2010_range_date
```

*Output:*

```text
'2010-06-24'
```

**Test — `q1_2_1` (4 points)**

```python
>>> bool(isinstance(largest_2010_range_date, str) or isinstance(largest_2010_range_date, np.str_))
True

# hidden test
>>> bool(str(largest_2010_range_date) == '2010-06-24')
True
```

We can look back to our `phoenix` table to check the temperature readings for our `largest_2010_range_date` to see if anything special is going on. Run the cell below to find the row of the `phoenix` table that corresponds to the date we found above.

**Code:**

```python
# Just run this cell
phoenix.where("Date", largest_2010_range_date)
```

*Output:*

| Date | tmax | tmin | prcp |
| --- | --- | --- | --- |
| 2010-06-24 | 113 | 79 | 0 |

ZOO WEE MAMA! Look at the maximum temperature for that day. That's hot.

The function `extract_year_from_date` takes a date string in the **YYYY-MM-DD** format and returns an integer representing the **year**. The function `extract_month_from_date` takes a date string and returns a string describing the month. Run this cell, but you do not need to understand how this code works or edit it.

**Code:**

```python
# Just run this cell
import calendar

def extract_year_from_date(date):
    """Returns an integer corresponding to the year of the input string's date."""
    return int(date[:4])

def extract_month_from_date(date):
    "Return an abbreviation of the name of the month for a string's date."
    month = date[5:7]
    return f'{month} ({calendar.month_abbr[int(date[5:7])]})'


# Example
print('2022-04-01 has year', extract_year_from_date('2022-04-01'),
      'and month', extract_month_from_date('2022-04-01'))
```

*Output (stdout):*

```text
2022-04-01 has year 2022 and month 04 (Apr)
```

---

**Question 1.2.2:** Add two new columns called `"Year"` and `"Month"` to the `phoenix` table that contain, for each day, the year as an integer and the month as a string (such as `"04 (Apr)"`).

*Note*: The functions above may be helpful!

**Student scaffold:**

```python
years_array = ...
months_array = ...
...
phoenix.show(5)
```

**Solution:**

```python
years_array = phoenix.apply(extract_year_from_date, 'Date') # SOLUTION
months_array = phoenix.apply(extract_month_from_date, 'Date') # SOLUTION
# BEGIN SOLUTION
phoenix = phoenix.with_column('Year', years_array).with_column('Month', months_array)
# END SOLUTION
phoenix.show(5)
```

*Output:*

| Date | tmax | tmin | prcp | Year | Month |
| --- | --- | --- | --- | --- | --- |
| 1896-01-01 | 66 | 30 | 0 | 1896 | 01 (Jan) |
| 1896-01-02 | 64 | 30 | 0 | 1896 | 01 (Jan) |
| 1896-01-03 | 68 | 30 | 0 | 1896 | 01 (Jan) |
| 1896-01-04 | 69 | 34 | 0 | 1896 | 01 (Jan) |
| 1896-01-05 | 70 | 46 | 0 | 1896 | 01 (Jan) |

**Test — `q1_2_2` (4 points)**

```python
>>> bool(phoenix.num_rows == 46021)
True

>>> bool(len(phoenix.labels) == 6)
True

>>> bool(phoenix.labels == ('Date', 'tmax', 'tmin', 'prcp', 'Year', 'Month'))
True

# hidden test
>>> bool(phoenix.group('Year').column(1).item(0) == 366)
True

# hidden test
>>> bool(phoenix.group('Year').column(1).item(110) == 365)
True

# hidden test
>>> bool(list(phoenix.group('Month').row(1)) == ['02 (Feb)', 3559])
True
```

---

**Question 1.2.3:** Using the `phoenix` table, create an overlaid line plot of the **average maximum temperature** and **average minimum temperature** for each year between 1900 and 2020 (both ends inclusive). 

*Hint:* To draw a line plot with more than one line, call `plot` on the column label of the x-axis values and all other columns will be treated as y-axis values.

**Student scaffold:**

```python
...
```

**Solution:**

```python
phoenix.select('Year', 'tmax', 'tmin').group("Year", np.mean).where('Year', are.between_or_equal_to(1900, 2020)).plot("Year") # SOLUTION
```

![Plot output from cell 46 — see preceding code](project2_assets/cell046_out0.png)

---

**Question 1.2.4:** Although still hotly debated (pun intended), many climate scientists agree that the effects of climate change began to surface in the early 1960s as a result of elevated levels of greenhouse gas emissions. How does the graph you produced in Question 1.2.3 support the claim that modern-day global warming began in the early 1960s?

**SOLUTION:** After about 1963, the minimum temperatures increase rapidly and the maximum temperatures increase slowly. Before then, they stayed within a consistent range.

Averaging temperatures across an entire year can obscure some effects of climate change. For example, if summers get hotter but winters get colder, the annual average may not change much. Let's investigate how average **monthly** maximum temperatures have changed over time in Phoenix.

---

**Question 1.2.5:** Create a copy of the `phoenix` table called `phoenix_periods` with a new column called 
`"period"` containing the corresponding **period** for each row. The period refers to whether the year is in the `"Past"`, `"Present"`, or `"Other"` category. You may find the `period` function helpful to see which years correspond to each period.

**Student scaffold:**

```python
def period(year):
    "Output if a year is in the Past, Present, or Other."
    if 1900 <= year <= 1960:
        return "Past"
    elif 2019 <= year <= 2021:
        return "Present"
    else:
        return "Other"
    
...
phoenix_periods = ...
phoenix_periods.show(5)
```

**Solution:**

```python
def period(year):
    "Output if a year is in the Past, Present, or Other."
    if 1900 <= year <= 1960:
        return "Past"
    elif 2019 <= year <= 2021:
        return "Present"
    else:
        return "Other"
    
""" # BEGIN PROMPT
...
phoenix_periods = ...
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
periods = phoenix.apply(period, 'Year')
phoenix_periods = phoenix.with_column('period', periods)
# END SOLUTION
phoenix_periods.show(5)
```

*Output:*

| Date | tmax | tmin | prcp | Year | Month | period |
| --- | --- | --- | --- | --- | --- | --- |
| 1896-01-01 | 66 | 30 | 0 | 1896 | 01 (Jan) | Other |
| 1896-01-02 | 64 | 30 | 0 | 1896 | 01 (Jan) | Other |
| 1896-01-03 | 68 | 30 | 0 | 1896 | 01 (Jan) | Other |
| 1896-01-04 | 69 | 34 | 0 | 1896 | 01 (Jan) | Other |
| 1896-01-05 | 70 | 46 | 0 | 1896 | 01 (Jan) | Other |

**Test — `q1_2_5` (2 points)**

```python
>>> bool(phoenix_periods.labels == ('Date', 'tmax', 'tmin', 'prcp', 'Year', 'Month', 'period'))
True

>>> bool(phoenix_periods.num_rows == 46021)
True

# hidden test
>>> bool(phoenix_periods.row(2000).item('period') == 'Past')
True

# hidden test
>>> def period(year):
...     """Output if a year is in the Past, Present, or Other."""
...     if 1900 <= year <= 1960:
...         return 'Past'
...     elif 2019 <= year <= 2021:
...         return 'Present'
...     else:
...         return 'Other'
>>> periods_test = phoenix.apply(period, 'Year')
>>> phoenix_periods_test = phoenix.with_column('period', periods_test)
>>> bool(np.all(phoenix_periods.column('period') == phoenix_periods_test.column('period')))
True
```

---

**Question 1.2.6:** Use `phoenix_periods` to create a `monthly_increases` table with one row per month and the following four columns in order: 
1. `"Month"`: The month (such as `"02 (Feb)"`)
2. `"Past"`: The average max temperature in that month from 1900-1960 (both ends inclusive)
3. `"Present"`: The average max temperature in that month from 2019-2021 (both ends inclusive)
4. `"Increase"`: The difference between the present and past average max temperatures in that month

Feel free to use as many lines as you need.

*Hint*: What table method can we use to get each **unique value** as its own column? 

*Note*: Please do **not** re-assign the `phoenix` variable!

**Student scaffold:**

```python
...
monthly_increases = ...
monthly_increases.show()
```

**Solution:**

```python
""" # BEGIN PROMPT
...
monthly_increases = ...
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
p = phoenix_periods.pivot('period', 'Month', 'tmax', np.average).drop('Other')
monthly_increases = p.with_column('Increase', p.column(2) - p.column(1))
# END SOLUTION
monthly_increases.show()
```

*Output:*

| Month | Past | Present | Increase |
| --- | --- | --- | --- |
| 01 (Jan) | 65.0164 | 67.8312 | 2.81479 |
| 02 (Feb) | 68.8485 | 69.1859 | 0.337362 |
| 03 (Mar) | 74.6499 | 75.9796 | 1.32965 |
| 04 (Apr) | 82.6421 | 88.4 | 5.75792 |
| 05 (May) | 91.4299 | 94.571 | 3.14104 |
| 06 (Jun) | 101.166 | 105.734 | 4.56832 |
| 07 (Jul) | 103.599 | 107.245 | 3.64654 |
| 08 (Aug) | 101.416 | 107.384 | 5.96769 |
| 09 (Sep) | 97.6874 | 101.238 | 3.55035 |
| 10 (Oct) | 86.798 | 90.1667 | 3.36868 |
| 11 (Nov) | 74.6273 | 80.5178 | 5.89046 |
| 12 (Dec) | 65.9064 | 67.4548 | 1.54844 |

**Test — `q1_2_6` (3.0 points)**

```python
>>> bool(monthly_increases.num_rows == 12)
True

>>> bool(monthly_increases.labels == ('Month', 'Past', 'Present', 'Increase'))
True

>>> bool(monthly_increases.row(2).item('Month') == '03 (Mar)')
True

# hidden test
>>> bool(np.isclose(monthly_increases.row(2).item('Past'), 74.64992067689053))
True

# hidden test
>>> bool(np.isclose(monthly_increases.row(2).item('Present'), 75.97956989247312))
True
```

### February in Phoenix

The `"Past"` column values are averaged over many decades, and so they are reliable estimates of the average high temperatures in those months before the effects of modern climate change. However, the `"Present"` column is based on only three years of observations. February, the shortest month, has the fewest total observations: only 85 days. Run the following cell to see this.

**Code:**

```python
# Just run this cell
feb_present = phoenix.where('Year', are.between_or_equal_to(2019, 2021)).where('Month', '02 (Feb)')
feb_present.num_rows
```

*Output:*

```text
85
```

Look back to your `monthly_increases` table. Compared to the other months, the increase for the month of February is quite small; the February difference is very close to zero. Run the following cell to print out our observed difference.

**Code:**

```python
# Just run this cell
print(f"February Difference: {monthly_increases.row(1).item('Increase')}")
```

*Output (stdout):*

```text
February Difference: 0.3373623297258632
```

Perhaps that small difference is somehow due to chance! To investigate this idea requires a thought experiment.

We can observe all of the February maximum temperatures from 2019 to 2021 (the present period), so we have access to the census; there's no random sampling involved. But, we can imagine that if more years pass with the same present-day climate, there would be different but similar maximum temperatures in future February days. From the data we observe, we can try to estimate the **average maximum February temperature** in this imaginary collection of all future February days that would occur in our modern climate, assuming the climate doesn't change any further and many years pass.

We can also imagine that the maximum temperature each day is like a **random draw from a distribution of max daily temperatures for that month**. Treating actual observations of natural events as if they were each *randomly* sampled from some unknown distribution is a simplifying assumption. These temperatures were not actually sampled at random—instead they occurred due to the complex interactions of the Earth's climate—but treating them as if they were random abstracts away the details of this naturally occurring process and allows us to carry out statistical inference.  Conclusions are only as valid as the assumptions upon which they rest, but in this case thinking of daily temperatures as random samples from some unknown climate distribution seems at least plausible.

If we assume that the **actual temperatures were drawn at random from some large population of possible February days** in our modern climate, then we can not only estimate the population average of this distribution, but also quantify our uncertainty about that estimate using a confidence interval.

**We will now compute the confidence interval of the present February average max daily temperature.** To unpack this statement, we are saying that this confidence interval is looking at present-day February conditions (think about which table is relevant to this), and the confidence interval is for present-day February average max daily temperatures. We will compare this confidence interval to the historical average (ie. the `"Past"` value in our `monthly_increases` table). How will we do the comparison? Well, since we are essentially interested in seeing if the average February max daily temperatures have ***changed*** since the past, we care about whether the historical average lies within the confidence interval we create.

---

**Question 1.2.7.** Based on the information above, define a null and alternative hypothesis for the investigation.

*Note:* Please format your answer as follows:
- Null Hypothesis: ...
- Alternative Hypothesis: ...

**SOLUTION:**

- *Null Hypothesis:* The average maximum February temperature in the present-period is the same as the average maximum February temperature in the past. Any observed difference is simply due to chance.

- *Alternative Hypothesis:* The average maximum February temperature in the present-period is different from the average maximum February temperature in the past. Any observed difference is not just due to chance.

---

**Question 1.2.8.** Complete the implementation of the function `make_ci`, which takes a one-column table `tbl` containing sample observations and a confidence `level` percentage such as 95 or 99. **It returns an array containing the lower and upper bound in that order, of a confidence interval** for the population mean constructed using 5,000 bootstrap resamples.

After defining `make_ci`, we have provided a line of code that calls `make_ci` on the present-day February max temperatures to output the 99% confidence interval for the average of daily max temperatures in February. The result should be around 67 degrees for the lower bound and around 71 degrees for the upper bound of the interval.

**Student scaffold:**

```python
def make_ci(tbl, level):
    """Compute a level% confidence interval of the average of the population for 
    which column 0 of Table tbl contains a sample. This function should return an 
    array of the lower and upper bounds of the confidence interval.
    """
    stats = make_array()
    for k in np.arange(5000):
        stat = ...
        stats = ...
    lower_bound = ...
    upper_bound = ...
    ...

# Call make_ci on the max temperatures in present-day February to find the lower and upper bound of a 99% confidence interval.
feb_present_ci = make_ci(feb_present.select('tmax'), 99)
feb_present_ci
```

**Solution:**

```python
def make_ci(tbl, level):
    """Compute a level% confidence interval of the average of the population for 
    which column 0 of Table tbl contains a sample. This function should return an 
    array of the lower and upper bounds of the confidence interval.
    """
    stats = make_array()
    for k in np.arange(5000):
        stat = np.average(tbl.sample().column(0)) # SOLUTION
        stats = np.append(stats, stat) # SOLUTION
    lower_bound = percentile((100 - level) / 2, stats) # SOLUTION
    upper_bound = percentile(100 - (100 - level) / 2, stats) # SOLUTION
    return make_array(lower_bound, upper_bound) # SOLUTION

# Call make_ci on the max temperatures in present-day February to find the lower and upper bound of a 99% confidence interval.
feb_present_ci = make_ci(feb_present.select('tmax'), 99)
feb_present_ci
```

*Output:*

```text
array([ 66.99647059,  71.25529412])
```

**Test — `q1_2_8` (5.0 points)**

```python
>>> bool(66.6 <= feb_present_ci.item(0) <= 67.3)
True

>>> bool(70.7 <= feb_present_ci.item(1) <= 72)
True
```

---

**Question 1.2.9** The `feb_present_ci` 99% confidence interval contains the observed past February average maximum temperature of 68.8485 (from the `monthly_increases` table). What conclusion can you draw about the effect of climate change on February maximum temperatures in Phoenix from this information? Use a 1% p-value cutoff.

*Note*: If you're stuck on this question, consider your null and alternative hypotheses from Question 1.2.6. What does your conclusion imply about the effect of climate change? Re-reading the paragraphs under the *February* heading (particularly the first few) may be helpful.

**SOLUTION:** The confidence interval for the present average contains the past average, so we cannot reject the null hypothesis that the present average is in fact the past average. Under our assumptions, it's consistent with the data that climate change has not affected the average maximum February temperature at all.

### All Months

---

**Question 1.2.10.** Repeat the process of seeing whether the **past average for each month** is **contained within the 99% confidence interval** of the **present average**. Just as a note for the context, remember that these “averages” are averages of the max daily temperatures within those time periods. Code has already been written to print out the results in the format of a month (e.g., `02 (Feb)`), the observed past average, the confidence interval for the present average, and whether the past average was contained in the interval or not.

Use the provided call to `print` in order to format the result as one line per month.

*Hint*: Your code should follow the same format as our code from above (i.e. the *February* section).

**Student scaffold:**

```python
comparisons = make_array()
months = ...
for month in months:
    past_average = ...
    present_observations = ...
    present_ci = ...
    
    # Do not change the code below this line
    GREEN_BOLD = '\033[1;32m'
    RED_BOLD = '\033[1;31m'
    RESET_STYLE = '\033[0m'
    within = (past_average >= present_ci.item(0)) and (past_average <= present_ci.item(1))
    if within:
        comparison = f'{GREEN_BOLD}contained{RESET_STYLE}'
    else:
        comparison = f'{RED_BOLD}NOT contained{RESET_STYLE}'
    comparisons = np.append(comparisons, comparison)
    
    print(f'For {month} the past avg {round(past_average, 1)} is {comparison} in the interval '
           f'{np.round(present_ci, 1)}, the 99% CI of the present avg.\n')
```

**Solution:**

```python
comparisons = make_array()
months = monthly_increases.column('Month') # SOLUTION
for month in months:
    past_average = monthly_increases.where('Month', month).row(0).item('Past') # SOLUTION
    present_observations = phoenix.where('Year', are.between_or_equal_to(2019, 2021)).where('Month', month) # SOLUTION
    present_ci = make_ci(present_observations.select('tmax'), 99) # SOLUTION
    
    # Do not change the code below this line
    GREEN_BOLD = '\033[1;32m'
    RED_BOLD = '\033[1;31m'
    RESET_STYLE = '\033[0m'
    within = (past_average >= present_ci.item(0)) and (past_average <= present_ci.item(1))
    if within:
        comparison = f'{GREEN_BOLD}contained{RESET_STYLE}'
    else:
        comparison = f'{RED_BOLD}NOT contained{RESET_STYLE}'
    comparisons = np.append(comparisons, comparison)
    
    print(f'For {month} the past avg {round(past_average, 1)} is {comparison} in the interval '
           f'{np.round(present_ci, 1)}, the 99% CI of the present avg.\n')
```

*Output (stdout):*

```text
For 01 (Jan) the past avg 65.0 is NOT contained in the interval [ 66.3  69.2], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 02 (Feb) the past avg 68.8 is contained in the interval [ 67.   71.3], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 03 (Mar) the past avg 74.6 is contained in the interval [ 74.   77.9], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 04 (Apr) the past avg 82.6 is NOT contained in the interval [ 86.5  90.5], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 05 (May) the past avg 91.4 is NOT contained in the interval [ 92.5  96.6], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 06 (Jun) the past avg 101.2 is NOT contained in the interval [ 104.2  107.2], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 07 (Jul) the past avg 103.6 is NOT contained in the interval [ 105.4  108.8], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 08 (Aug) the past avg 101.4 is NOT contained in the interval [ 105.7  108.9], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 09 (Sep) the past avg 97.7 is NOT contained in the interval [  99.2  103.1], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 10 (Oct) the past avg 86.8 is NOT contained in the interval [ 87.9  92.3], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 11 (Nov) the past avg 74.6 is NOT contained in the interval [ 78.1  82.8], the 99% CI of the present avg.
```

*Output (stdout):*

```text
For 12 (Dec) the past avg 65.9 is contained in the interval [ 65.6  69.2], the 99% CI of the present avg.
```

**Test — `q1_2_10` (4 points)**

```python
>>> bool(type(months) == np.ndarray)
True

# hidden test
>>> comparison_results = make_array('\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;32mcontained\x1b[0m', '\x1b[1;32mcontained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;31mNOT contained\x1b[0m', '\x1b[1;32mcontained\x1b[0m')
>>> bool(np.all(comparisons == comparison_results))
True
```

---

**Question 1.2.11.** Summarize your findings. After checking whether the past average (of max temperatures, as defined above 1.2.6)  is contained in the 99% confidence interval for each month, what conclusions can we make about the monthly average maximum temperature in historical (1900-1960) vs. modern (2019-2021) times in the twelve months? In other words, what null hypothesis should you consider, and for which months would you reject or fail to reject the null hypothesis? Use a 1% p-value cutoff.

*Hint*: Do you notice any seasonal patterns?

**SOLUTION:** For most months, the modern average maximum temperature for the month is above the historical average maximum temperature, indicating the climate has changed. But for some winter months—Feb, March, Dec—we fail to reject the null, as we do not have evidence that the average maximum temperature has changed.

> It is important to be wary of making conclusions based on the results of multiple hypothesis tests. Specifically, recall that a 1% p-value cutoff means that if the null is true, we would expect to incorrectly reject the null 1% of the time. Now, if we run multiple of these tests, the chance we observe an error will be greater than if we had just run one test – the error chance compounds.

### Checkpoint (due Friday, 4/10 by 5:00pm PT)

![dog](project2_assets/charlee.jpg)

Congrats on reaching the checkpoint! **Charlee** says good job on finishing the first half of the project.

**Run the following cells and submit to the <u>Project 2 Checkpoint</u>** Pensieve assignment.

--- 

To earn full credit for this checkpoint, you must pass all the public autograder tests above this cell. The cell below will re-run all of the autograder tests for Part 1 to double check your work.

**Code:**

```python
checkpoint_tests = ["q1_1_3", "q1_1_4", "q1_1_5", 
                    "q1_2_1", "q1_2_2", "q1_2_5", "q1_2_6", "q1_2_8", "q1_2_10"]

for test in checkpoint_tests:
    display(grader.check(test))
```

*Output (stdout):*

```text
Unexpected exception formatting exception. Falling back to standard exception
```

*Output (stderr):*

```text
Traceback (most recent call last):
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/interactiveshell.py", line 3577, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/folders/xv/tl5mnl5s0mz_ykhsrhdyb_rm0000gn/T/ipykernel_68017/2873164019.py", line 5, in <module>
    display(grader.check(test))
            ^^^^^^
NameError: name 'grader' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/interactiveshell.py", line 2168, in showtraceback
    stb = self.InteractiveTB.structured_traceback(
        etype, value, tb, tb_offset=tb_offset
    )
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1454, in structured_traceback
    return FormattedTB.structured_traceback(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, etype, evalue, etb, tb_offset, number_of_lines_of_context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1345, in structured_traceback
    return VerboseTB.structured_traceback(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, etype, value, tb, tb_offset, number_of_lines_of_context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1192, in structured_traceback
    formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,
                                                           tb_offset)
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1082, in format_exception_as_a_whole
    self.get_records(etb, number_of_lines_of_context, tb_offset) if etb else []
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1179, in get_records
    res = list(stack_data.FrameInfo.stack_data(etb, options=options))[tb_offset:]
          ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/core.py", line 597, in stack_data
    yield from collapse_repeated(
    ...<4 lines>...
    )
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/utils.py", line 83, in collapse_repeated
    yield from map(mapper, original_group)
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/core.py", line 587, in mapper
    return cls(f, options)
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/core.py", line 551, in __init__
    self.executing = Source.executing(frame_or_tb)
                     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/executing/executing.py", line 283, in executing
    assert_(new_stmts <= stmts)
    ~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/executing/executing.py", line 80, in assert_
    raise AssertionError(str(message))
AssertionError
```

## Submission

Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**

**Reminders**:

- If you worked on Project 2 with a partner, please remember to add your partner to your Pensieve submission. If you resubmit, make sure to re-add your partner, as Pensieve does not save any partner information.
- Make sure to wait until the autograder finishes running to ensure that your submission was processed properly and that you submitted to the correct assignment.

**Code:**

```python
# Run this cell to set up the notebook, but please don't change it.
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
np.set_printoptions(legacy='1.13')
 
import warnings
warnings.simplefilter('ignore')
```

---
# Part 2: Drought

According to the [United States Environmental Protection Agency](https://www.epa.gov/), "Large portions of the Southwest have experienced drought conditions since weekly Drought Monitor records began in 2000. For extended periods from 2002 to 2005 and from 2012 to 2020, nearly the entire region was abnormally dry or even drier." 

Assessing the impact of drought is challenging with just city-level data because so much of the water that people use is transported from elsewhere, but we'll explore the data we have and see what we can learn.

Let's first take a look at the precipitation data in the Southwest region. The `southwest.csv` file contains total annual precipitation for 13 cities in the southwestern United States for each year from 1960 to 2021. This dataset is aggregated from the daily data and includes only the Southwest cities from the original dataset that have consistent precipitation records back to 1960.

**Code:**

```python
southwest = Table.read_table('southwest.csv')
southwest.show(5)
```

*Output:*

| City | Year | Total Precipitation |
| --- | --- | --- |
| Albuquerque | 1960 | 8.12 |
| Albuquerque | 1961 | 8.87 |
| Albuquerque | 1962 | 5.39 |
| Albuquerque | 1963 | 7.47 |
| Albuquerque | 1964 | 7.44 |

---

**Question 2.1.** Create a table `totals` that has one row for each year in chronological order. It should contain the following columns:
1. `"Year"`: The year (a number)
2. `"Precipitation"`: The total precipitation in all 13 southwestern cities that year

**Student scaffold:**

```python
totals = ...
totals
```

**Solution:**

```python
totals = southwest.drop(0).group('Year', sum).relabeled(1, 'Precipitation') # SOLUTION
totals
```

*Output:*

| Year | Precipitation |
| --- | --- |
| 1960 | 149.58 |
| 1961 | 134.82 |
| 1962 | 130.41 |
| 1963 | 132.18 |
| 1964 | 123.41 |
| 1965 | 187.53 |
| 1966 | 120.27 |
| 1967 | 179.02 |
| 1968 | 136.25 |
| 1969 | 191.72 |

**Test — `q2_1` (5 points)**

```python
>>> bool(totals.num_rows == 61)
True

>>> bool(totals.labels == ('Year', 'Precipitation'))
True

# hidden test
>>> bool(list(totals.row(5)) == [1965, 187.53])
True

# hidden test
>>> bool(list(totals.row(59)) == [2019, 172.10000000000002])
True
```

Run the cell below to plot the total precipitation in these cities over time, so that we can try to spot the drought visually. As a reminder, the drought years given by the EPA were  (2002-2005) and (2012-2020).

**Code:**

```python
# Just run this cell
totals.plot("Year", "Precipitation")
```

![Plot output from cell 93 — see preceding code](project2_assets/cell093_out0.png)

This plot isn't very revealing. Each year has a different amount of precipitation, and there is quite a bit of variability across years, as if each year's precipitation is a random draw from a distribution of possible outcomes. 

Could it be that these so-called "drought conditions" from 2002-2005 and 2012-2020 can be explained by chance? In other words, could it be that the annual precipitation amounts in the Southwest for these drought years are like **random draws from the same underlying distribution** as for other years? Perhaps nothing about the Earth's precipitation patterns has really changed, and the Southwest U.S. just happened to experience a few dry years close together. 

To assess this idea, let's conduct an A/B test in which **each year's total precipitation** is an outcome, and the condition is **whether or not the year is in the EPA's drought period**.

This `drought_label` function distinguishes between drought years as described in the U.S. EPA statement above (2002-2005 and 2012-2020) and other years. Note that the label "other" is perhaps misleading, since there were other droughts before 2000, such as the massive [1988 drought](https://en.wikipedia.org/wiki/1988%E2%80%9390_North_American_drought) that affected much of the U.S. However, if we're interested in whether these modern drought periods (2002-2005 and 2012-2020) are *normal* or *abnormal*, it makes sense to distinguish the years in this way.

**Code:**

```python
def drought_label(n):
    """Return the label for an input year n."""
    if 2002 <= n <= 2005 or 2012 <= n <= 2020:
        return 'drought'
    else:
        return 'other'
```

---

**Question 2.2.** Define null and alternative hypotheses for an A/B test that investigates whether drought years are **drier** (have less precipitation) than other years.

*Note:* Please format your answer using the following structure.

- *Null hypothesis:* ...
- *Alternative hypothesis:* ...

**SOLUTION:** 

- *Null hypothesis:* The drought year total precipitation amounts are sampled from the same distribution as other year total precipitation amounts. 

- *Alternative hypothesis:* The drought year total precipitation amounts are sampled from a drier distribution than the other year total precipitation amounts.

---

**Question 2.3.** First, define the table `drought`. It should contain one row per year and the following two columns:
- `"Label"`: Denotes if a year is part of a `"drought"` year or an `"other"` year
- `"Precipitation"`: The sum of the total precipitation in 13 Southwest cities that year

Then, construct an overlaid histogram of two observed distributions: the total precipitation in drought years and the total precipitation in other years. 

*Note*: Use the provided `bins` when creating your histogram, and do not re-assign the `southwest` table. Feel free to use as many lines as you need!

*Hint*: The optional `group` argument in a certain function might be helpful!

**Student scaffold:**

```python
bins = np.arange(85, 215+1, 13)
drought = ...
...
```

**Solution:**

```python
bins = np.arange(85, 215+1, 13)
drought = totals.with_column('Label', totals.apply(drought_label, 'Year')).select('Label', 'Precipitation') # SOLUTION
drought.hist("Precipitation", group="Label", bins=bins, unit='inch') # SOLUTION
```

![Plot output from cell 101 — see preceding code](project2_assets/cell101_out0.png)

Before you continue, inspect the histogram you just created and try to guess the conclusion of the A/B test. Building intuition about the result of hypothesis testing from visualizations is quite useful for data science applications.

---

**Question 2.4.** Our next step is to choose a test statistic based on our alternative hypothesis in Question 2.2. Which of the following options are valid choices for the test statistic? Assign `ab_test_stat` to **an array of integers** corresponding to valid choices. Assume averages and totals are taken over the total precipitation sums for each year.

1. The difference between the **total** precipitation in **drought** years and the **total** precipitation in **other** years.
2. The difference between the **total** precipitation in **others** years and the **total** precipitation in **drought** years.
3. The **absolute** difference between the **total** precipitation in others years and the **total** precipitation in drought years.
1. The difference between the **average** precipitation in **drought** years and the **average** precipitation in **other** years.
2. The difference between the **average** precipitation in **others** years and the **average** precipitation in **drought** years.
3. The **absolute** difference between the **average** precipitation in others years and the **average** precipitation in drought years.

**Student scaffold:**

```python
ab_test_stat = ...
```

**Solution:**

```python
ab_test_stat = make_array(1, 2, 4, 5) # SOLUTION
```

**Test — `q2_4` (5 points)**

```python
>>> bool(type(ab_test_stat) == np.ndarray)
True

>>> bool(all([1 <= option <= 6 for option in ab_test_stat]))
True

>>> bool(all([type(option) in set([np.int64, np.int32, int]) for option in list(ab_test_stat)]))
True

# hidden test
>>> bool(all([option in list(ab_test_stat) for option in make_array(4, 5)]))
True

# hidden test
>>> bool(len(ab_test_stat) == 4 and np.all(np.sort(ab_test_stat) == make_array(1, 2, 4, 5)))
True
```

---

**Question 2.5.** Fellow climate scientists Noah and Sarah point out that there are more **other** years than **drought** years, and so measuring the difference between total precipitation will always favor the **other** years. They conclude that all of the options above involving **total** precipitation are invalid test statistic choices. Do you agree with them? Why or why not?

> *Hint 1:* Think about how permutation tests work with imbalanced classes! Does the number of labels in each group change?

> *Hint 2:* Do our test statistics have to be centered at 0?

**SOLUTION:** No. Permutation tests apply equally well to datasets with imbalanced classes, and an averaging test statistic is not required. A permutation test always ensures that there are the same number of each class during simulation, making the observed and simulated test statistics comparable.

Before going on, check your `drought` table. It should have two columns `"Label"` and `"Precipitation"` with 61 rows, 13 of which are for `"drought"` years.

**Code:**

```python
drought.show(3)
```

*Output:*

| Label | Precipitation |
| --- | --- |
| other | 149.58 |
| other | 134.82 |
| other | 130.41 |

**Code:**

```python
drought.group('Label')
```

*Output:*

| Label | count |
| --- | --- |
| drought | 13 |
| other | 48 |

---

**Question 2.6.** For our A/B test, we'll use the difference between the average precipitation in drought years and the average precipitation in other years as our test statistic:

$$\text{average precipitation in ``drought" years} - \text{average precipitation in ``other" years}$$

First, complete the function `test_statistic`. It should take in a two-column table `t` with one row per year and two columns:
- `"Label"`: the label for that year (either `"drought"` or `"other"`)
- `"Precipitation"`: the total precipitation in the 13 Southwest cities that year. 

Then, use the function you define to assign `observed_statistic` to the observed test statistic.

**Student scaffold:**

```python
def test_statistic(t):
    ...

observed_statistic = ...
observed_statistic
```

**Solution:**

```python
def test_statistic(t):
    means = t.group("Label", np.mean).column(1) # SOLUTION NO PROMPT
    return means.item(0) - means.item(1) # SOLUTION

observed_statistic = test_statistic(drought) # SOLUTION
observed_statistic
```

*Output:*

```text
-15.856714743589748
```

**Test — `q2_6` (4 points)**

```python
>>> bool(observed_statistic < 0)
True

# hidden test
>>> bool(test_statistic(drought.sample()) != test_statistic(drought.sample()))
True

# hidden test
>>> bool(np.isclose(test_statistic(drought), -15.856714743589748))
True

# hidden test
>>> bool(np.isclose(test_statistic(drought), observed_statistic))
True
```

Now that we have defined our hypotheses and test statistic, we are ready to conduct our hypothesis test. We’ll start by defining a function to simulate the test statistic under the null hypothesis, and then call that function 5,000 times to construct an empirical distribution under the null hypothesis.

---

**Question 2.7.** Write a function to simulate the test statistic under the null hypothesis. The `simulate_precipitation_null` function should simulate the null hypothesis once (not 5,000 times) and return the value of the test statistic for that simulated sample.

*Hint*: For example, using `t.with_column(...)` with a column name that already exists in an arbitrary table `t` will replace that column with the newly specified values.

**Student scaffold:**

```python
def simulate_precipitation_null():
    ...

# Run your function a couple times to make sure that it works
simulate_precipitation_null()
```

**Solution:**

```python
def simulate_precipitation_null():
    # BEGIN SOLUTION
    shuffled_frame = drought.sample(with_replacement=False)
    permuted_table = drought.with_column('Label', shuffled_frame.column('Label'))
    return test_statistic(permuted_table)
    # END SOLUTION

# Run your function a couple times to make sure that it works
simulate_precipitation_null()
```

*Output:*

```text
-9.699038461538464
```

**Test — `q2_7` (4 points)**

```python
>>> bool(-50 < simulate_precipitation_null() < 50)
True

# hidden test
>>> ts = [simulate_precipitation_null() for _ in range(1000)]
>>> bool(6 <= np.array(ts).std() <= 10)
True
```

---

**Question 2.8.** Fill in the blanks below to complete the simulation for the hypothesis test. Your simulation should compute 5,000 values of the test statistic under the null hypothesis and store the result in the array `sampled_stats`.

*Hint:* You should use the `simulate_precipitation_null` function you wrote in the previous question!

*Note:* Running this cell may take a few seconds. If it takes more than a minute, try to find a different (faster) way to implement your `simulate_precipitation_null` function.

**Student scaffold:**

```python
sampled_stats = ...

repetitions = ...
for i in np.arange(repetitions):
    ...

# Do not change these lines
Table().with_column('Difference Between Means', sampled_stats).hist()
plt.scatter(observed_statistic, 0, c="r", s=50);
plt.ylim(-0.01);
```

**Solution:**

```python
sampled_stats = make_array() # SOLUTION

repetitions = 5000 # SOLUTION
for i in np.arange(repetitions):
    # BEGIN SOLUTION
    new_difference = simulate_precipitation_null()
    sampled_stats = np.append(sampled_stats, new_difference)
    # END SOLUTION

# Do not change these lines
Table().with_column('Difference Between Means', sampled_stats).hist()
plt.scatter(observed_statistic, 0, c="r", s=50);
plt.ylim(-0.01);
```

![Plot output from cell 120 — see preceding code](project2_assets/cell120_out0.png)

**Test — `q2_8` (4 points)**

```python
>>> bool(len(sampled_stats) == 5000)
True

>>> bool(np.std(sampled_stats) > 0)
True

# hidden test
>>> bool(6 < np.std(sampled_stats) < 10)
True

# hidden test
>>> bool(-11.5 < percentile(10, sampled_stats) < -9)
True
```

---

**Question 2.9.** Compute the p-value for this hypothesis test, and assign it to the variable `precipitation_p_val`.

**Student scaffold:**

```python
precipitation_p_val = ...
precipitation_p_val
```

**Solution:**

```python
precipitation_p_val = np.count_nonzero(sampled_stats <= observed_statistic) / repetitions # SOLUTION
precipitation_p_val
```

*Output:*

```text
0.025
```

**Test — `q2_9` (4 points)**

```python
>>> bool(type(precipitation_p_val) in set([float, np.float32, np.float64]))
True

>>> bool(0 <= precipitation_p_val <= 1)
True

# hidden test
>>> bool(0.015 < precipitation_p_val < 0.035)
True
```

---

**Question 2.10.** State a conclusion from this test using a p-value cutoff of 5%. What have you learned about the EPA's statement on drought?

**SOLUTION:** Because the p-value is less than the 5% p-value cutoff, our results are statistically significant and we reject the null hypothesis. We can conclude that the drought years were drier than the other years in these 13 cities.

---

**Question 2.11.** Does your conclusion from Question 2.10 apply to the entire Southwest region of the U.S.? Why or why not?

> *Note:* Feel free to do some research into geographical features of this region of the U.S.!

**SOLUTION:** We cannot generalize to the whole Southwestern U.S. because our sample only includes 13 cities. The cities we measured may not be representative of the whole region, which includes lots of mountains and deserts that aren't particularly suitable to city construction.

---
# Conclusion

Data science plays a central role in climate change research because massive simulations of the Earth's climate are necessary to assess the implications of climate data recorded from weather stations, satellites, and other sensors. [Berkeley Earth](http://berkeleyearth.org/data/) is a common source of data for these kinds of projects.

In this project, we found ways to apply our statistical inference techniques that rely on random sampling even in situations where the data were not generated randomly, but instead by some complicated natural process that appeared random. We made assumptions about randomness and then came to conclusions based on those assumptions. Great care must be taken to choose assumptions that are realistic, so that the resulting conclusions are not misleading. However, making assumptions about data can be productive when doing so allows inference techniques to apply to novel situations.

***Important Reminders:***

- If you worked on Project 2 with a partner, please remember to add your partner to your Pensive submission. If you resubmit, make sure to re-add your partner, as Pensive does not save any partner information.
- Make sure to wait until the autograder finishes running to ensure that your submission was processed properly and that you submitted to the correct assignment.

![Hamster eating](project2_assets/cookie_hamster.jpg)

##### **Congratulations -- Cookie the Hamster is proud of you for finishing Project 2!**
She might recommend eating a delicious meal to reward yourself :)

---

To double-check your work, the cell below will rerun all of the autograder tests.

## Submission

Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `city_info.csv`

461 rows, 8 columns.

| Column | Type |
| --- | --- |
| `Unnamed: 0` | int |
| `Name` | str |
| `ID` | str |
| `Lat` | float |
| `Lon` | float |
| `Stn.Name` | str |
| `Stn.stDate` | str |
| `Stn.edDate` | str |

### `phoenix.csv`

46,021 rows, 5 columns.

| Column | Type |
| --- | --- |
| `Unnamed: 0` | int |
| `Date` | str |
| `tmax` | float |
| `tmin` | float |
| `prcp` | float |

### `southwest.csv`

793 rows, 3 columns.

| Column | Type |
| --- | --- |
| `City` | str |
| `Year` | int |
| `Total Precipitation` | float |
