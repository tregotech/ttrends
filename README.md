# ttrends

Python library to extract Google search trends for >5 keywords. Built on top of [Pytrends](https://pypi.org/project/pytrends/).

Check out a GUI / App [here](https://github.com/tregotech/ttrends-streamlit). 

## Usage 
```python
>>> from ttrends import Trends
>>> trend = Trends(geo='GB',years=5)
>>> search_terms = ['apple','adele','batman']
```
#### Getting Related Terms 

```python
>>> related = trend.get_top_related(search_terms)
>>> print(related[:10])

    ['adele 2020',
	 'adele 2021',
	 'adele album',
	 'adele concert',
	 'adele easy on me',
	 'adele hello',
	 'adele hello lyrics',
	 'adele lyrics',
	 'adele net worth',
	 'adele news']

```


#### Getting Trends 

```python
>>> df = trend.get_trends(related[:10])
>>> df.head()

                        adele 2020  adele easy on me  adele album  adele 2021  adele concert  adele net worth  \
date                                                                                                
2017-02-26  0.0         0.0               1.66         0.0         1.36           4.32              
2017-03-05  0.0         0.0               0.83         0.0         1.80           2.59              
2017-03-12  0.0         0.0               2.49         0.0         1.80           1.73              
2017-03-19  0.0         0.0               2.06         0.0         1.80           2.59              
2017-03-26  0.0         0.0               1.23         0.0         0.93           3.46              

            adele lyrics  adele news  adele hello  adele hello lyrics  
date                                                                   
2017-02-26  6.0           1.66         7.97        3.84                
2017-03-05  5.0           3.72         9.56        4.08                
2017-03-12  7.0           2.06        11.16        4.11                
2017-03-19  4.0           1.23         7.17        3.11                
2017-03-26  4.0           1.23        10.36        3.28
```