```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,4),columns=list("ABCD"))
df.iloc[2:4,2:4] = np.nan
df.iloc[1,0:2] = np.nan
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>-0.323262</td>
      <td>-1.281065</td>
      <td>1.199474</td>
      <td>2.121828</td>
    </tr>
    <tr>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.337739</td>
      <td>-0.082217</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.208822</td>
      <td>0.474932</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>3</td>
      <td>-1.467442</td>
      <td>0.155873</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>4</td>
      <td>-1.856260</td>
      <td>1.116175</td>
      <td>-0.037934</td>
      <td>1.028386</td>
    </tr>
    <tr>
      <td>5</td>
      <td>-0.201312</td>
      <td>0.429019</td>
      <td>0.064620</td>
      <td>0.691049</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>3</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.fillna({"A":0.5},inplace = True)
df["A"]
```




    0   -0.323262
    1    0.500000
    2    1.208822
    3   -1.467442
    4   -1.856260
    5   -0.201312
    Name: A, dtype: float64




```python
df["B"].fillna(method = "bfill")
```




    0   -1.281065
    1    0.474932
    2    0.474932
    3    0.155873
    4    1.116175
    5    0.429019
    Name: B, dtype: float64




```python
df["C"].fillna(method = "ffill")
```




    0    1.199474
    1   -0.337739
    2   -0.337739
    3   -0.337739
    4   -0.037934
    5    0.064620
    Name: C, dtype: float64




```python
df["D"][df["D"].isnull()] = df["D"].mean()
df["D"]
```




    0    2.121828
    1   -0.082217
    2    0.939761
    3    0.939761
    4    1.028386
    5    0.691049
    Name: D, dtype: float64


