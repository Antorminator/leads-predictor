# Preparación de los datos


```python
# Importación de las librerías necesarias
import pandas as pd
import numpy as np
```

### Carga del dataset y análisis
Primero cargamos el dataset utilizado en la práctica y visualizamos las columnas que lo componen, con su tipología y algunos ejemplos de valores.


```python
# Carga y análisis previo del dataset en un DataFrame de Pandas

df = pd.read_csv('../datasets/Leads.csv')

print(len(df)) # Visualización del número total de registros

df.head().T # Visualización de las columnas con algunas filas de ejemplo
```

    9240





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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Prospect ID</th>
      <td>7927b2df-8bba-4d29-b9a2-b6e0beafe620</td>
      <td>2a272436-5132-4136-86fa-dcc88c88f482</td>
      <td>8cc8c611-a219-4f35-ad23-fdfd2656bd8a</td>
      <td>0cc2df48-7cf4-4e39-9de9-19797f9b38cc</td>
      <td>3256f628-e534-4826-9d63-4a8b88782852</td>
    </tr>
    <tr>
      <th>Lead Number</th>
      <td>660737</td>
      <td>660728</td>
      <td>660727</td>
      <td>660719</td>
      <td>660681</td>
    </tr>
    <tr>
      <th>Lead Origin</th>
      <td>API</td>
      <td>API</td>
      <td>Landing Page Submission</td>
      <td>Landing Page Submission</td>
      <td>Landing Page Submission</td>
    </tr>
    <tr>
      <th>Lead Source</th>
      <td>Olark Chat</td>
      <td>Organic Search</td>
      <td>Direct Traffic</td>
      <td>Direct Traffic</td>
      <td>Google</td>
    </tr>
    <tr>
      <th>Do Not Email</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Do Not Call</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Converted</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>TotalVisits</th>
      <td>0.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Total Time Spent on Website</th>
      <td>0</td>
      <td>674</td>
      <td>1532</td>
      <td>305</td>
      <td>1428</td>
    </tr>
    <tr>
      <th>Page Views Per Visit</th>
      <td>0.0</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Last Activity</th>
      <td>Page Visited on Website</td>
      <td>Email Opened</td>
      <td>Email Opened</td>
      <td>Unreachable</td>
      <td>Converted to Lead</td>
    </tr>
    <tr>
      <th>Country</th>
      <td>NaN</td>
      <td>India</td>
      <td>India</td>
      <td>India</td>
      <td>India</td>
    </tr>
    <tr>
      <th>Specialization</th>
      <td>Select</td>
      <td>Select</td>
      <td>Business Administration</td>
      <td>Media and Advertising</td>
      <td>Select</td>
    </tr>
    <tr>
      <th>How did you hear about X Education</th>
      <td>Select</td>
      <td>Select</td>
      <td>Select</td>
      <td>Word Of Mouth</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>What is your current occupation</th>
      <td>Unemployed</td>
      <td>Unemployed</td>
      <td>Student</td>
      <td>Unemployed</td>
      <td>Unemployed</td>
    </tr>
    <tr>
      <th>What matters most to you in choosing a course</th>
      <td>Better Career Prospects</td>
      <td>Better Career Prospects</td>
      <td>Better Career Prospects</td>
      <td>Better Career Prospects</td>
      <td>Better Career Prospects</td>
    </tr>
    <tr>
      <th>Search</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Magazine</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Newspaper Article</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>X Education Forums</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Newspaper</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Digital Advertisement</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Through Recommendations</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Receive More Updates About Our Courses</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Tags</th>
      <td>Interested in other courses</td>
      <td>Ringing</td>
      <td>Will revert after reading the email</td>
      <td>Ringing</td>
      <td>Will revert after reading the email</td>
    </tr>
    <tr>
      <th>Lead Quality</th>
      <td>Low in Relevance</td>
      <td>NaN</td>
      <td>Might be</td>
      <td>Not Sure</td>
      <td>Might be</td>
    </tr>
    <tr>
      <th>Update me on Supply Chain Content</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Get updates on DM Content</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Lead Profile</th>
      <td>Select</td>
      <td>Select</td>
      <td>Potential Lead</td>
      <td>Select</td>
      <td>Select</td>
    </tr>
    <tr>
      <th>City</th>
      <td>Select</td>
      <td>Select</td>
      <td>Mumbai</td>
      <td>Mumbai</td>
      <td>Mumbai</td>
    </tr>
    <tr>
      <th>Asymmetrique Activity Index</th>
      <td>02.Medium</td>
      <td>02.Medium</td>
      <td>02.Medium</td>
      <td>02.Medium</td>
      <td>02.Medium</td>
    </tr>
    <tr>
      <th>Asymmetrique Profile Index</th>
      <td>02.Medium</td>
      <td>02.Medium</td>
      <td>01.High</td>
      <td>01.High</td>
      <td>01.High</td>
    </tr>
    <tr>
      <th>Asymmetrique Activity Score</th>
      <td>15.0</td>
      <td>15.0</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>Asymmetrique Profile Score</th>
      <td>15.0</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>17.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>I agree to pay the amount through cheque</th>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>A free copy of Mastering The Interview</th>
      <td>No</td>
      <td>No</td>
      <td>Yes</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Last Notable Activity</th>
      <td>Modified</td>
      <td>Email Opened</td>
      <td>Email Opened</td>
      <td>Modified</td>
      <td>Modified</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Estadísticas genéricas del dataset, por columnas
df.describe()
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
      <th>Lead Number</th>
      <th>Converted</th>
      <th>TotalVisits</th>
      <th>Total Time Spent on Website</th>
      <th>Page Views Per Visit</th>
      <th>Asymmetrique Activity Score</th>
      <th>Asymmetrique Profile Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>9240.000000</td>
      <td>9240.000000</td>
      <td>9103.000000</td>
      <td>9240.000000</td>
      <td>9103.000000</td>
      <td>5022.000000</td>
      <td>5022.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>617188.435606</td>
      <td>0.385390</td>
      <td>3.445238</td>
      <td>487.698268</td>
      <td>2.362820</td>
      <td>14.306252</td>
      <td>16.344883</td>
    </tr>
    <tr>
      <th>std</th>
      <td>23405.995698</td>
      <td>0.486714</td>
      <td>4.854853</td>
      <td>548.021466</td>
      <td>2.161418</td>
      <td>1.386694</td>
      <td>1.811395</td>
    </tr>
    <tr>
      <th>min</th>
      <td>579533.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>596484.500000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>12.000000</td>
      <td>1.000000</td>
      <td>14.000000</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>615479.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>248.000000</td>
      <td>2.000000</td>
      <td>14.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>637387.250000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>936.000000</td>
      <td>3.000000</td>
      <td>15.000000</td>
      <td>18.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>660737.000000</td>
      <td>1.000000</td>
      <td>251.000000</td>
      <td>2272.000000</td>
      <td>55.000000</td>
      <td>18.000000</td>
      <td>20.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Visualización de los tipos de datos que componen el dataset
df.dtypes
```




    Prospect ID                                       object
    Lead Number                                        int64
    Lead Origin                                       object
    Lead Source                                       object
    Do Not Email                                      object
    Do Not Call                                       object
    Converted                                          int64
    TotalVisits                                      float64
    Total Time Spent on Website                        int64
    Page Views Per Visit                             float64
    Last Activity                                     object
    Country                                           object
    Specialization                                    object
    How did you hear about X Education                object
    What is your current occupation                   object
    What matters most to you in choosing a course     object
    Search                                            object
    Magazine                                          object
    Newspaper Article                                 object
    X Education Forums                                object
    Newspaper                                         object
    Digital Advertisement                             object
    Through Recommendations                           object
    Receive More Updates About Our Courses            object
    Tags                                              object
    Lead Quality                                      object
    Update me on Supply Chain Content                 object
    Get updates on DM Content                         object
    Lead Profile                                      object
    City                                              object
    Asymmetrique Activity Index                       object
    Asymmetrique Profile Index                        object
    Asymmetrique Activity Score                      float64
    Asymmetrique Profile Score                       float64
    I agree to pay the amount through cheque          object
    A free copy of Mastering The Interview            object
    Last Notable Activity                             object
    dtype: object



De un vistazo rápido podemos ver que las siguientes filas pueden ser candidatas a un tratamiento previo al entrenamiento de nuestro modelo:

* Do Not Email: de object a int
* Do Not Call: de object a int
* Search: de object a int
* Magazine: de object a int
* Newspaper Article: de object a int
* X Education Forums: de object a int
* Newspaper: de object a int
* Digital Advertisement: de object a int
* Through Recommendations: de object a int
* Receive More Updates About Our Courses: de object a int
* Update me on Supply Chain Content: de object a int
* Get updates on DM Content: de object a int
* I agree to pay the amount through cheque: de object a int
* A free copy of Mastering The Interview: de object a int
* Lead Quality: de object a int
* Lead Profile: de object a int
* Asymmetrique Activity Index: de object a float
* Asymmetrique Profile Index: de object a float


El primer tratamiento que vamos a hacer es homogeneizar los nombres de columna, pasándolas a minúscula y sustituyendo sus espacios en blanco por guión bajo. Ello nos ayudará a tratar mejor el conjunto de datos:


```python
# Función de reemplazo
replacer = lambda str: str.lower().str.replace(' ','_')

# Aplicación del reemplazo a los nombres de las columnas
df.columns = replacer(df.columns.str)

# Aplicación del reemplazo a los valores de las columnas de tipo cadena
for col in list(df.dtypes[df.dtypes == 'object'].index):
    df[col] = replacer(df[col].str)
df.head().T
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>prospect_id</th>
      <td>7927b2df-8bba-4d29-b9a2-b6e0beafe620</td>
      <td>2a272436-5132-4136-86fa-dcc88c88f482</td>
      <td>8cc8c611-a219-4f35-ad23-fdfd2656bd8a</td>
      <td>0cc2df48-7cf4-4e39-9de9-19797f9b38cc</td>
      <td>3256f628-e534-4826-9d63-4a8b88782852</td>
    </tr>
    <tr>
      <th>lead_number</th>
      <td>660737</td>
      <td>660728</td>
      <td>660727</td>
      <td>660719</td>
      <td>660681</td>
    </tr>
    <tr>
      <th>lead_origin</th>
      <td>api</td>
      <td>api</td>
      <td>landing_page_submission</td>
      <td>landing_page_submission</td>
      <td>landing_page_submission</td>
    </tr>
    <tr>
      <th>lead_source</th>
      <td>olark_chat</td>
      <td>organic_search</td>
      <td>direct_traffic</td>
      <td>direct_traffic</td>
      <td>google</td>
    </tr>
    <tr>
      <th>do_not_email</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>do_not_call</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>converted</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>totalvisits</th>
      <td>0.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>total_time_spent_on_website</th>
      <td>0</td>
      <td>674</td>
      <td>1532</td>
      <td>305</td>
      <td>1428</td>
    </tr>
    <tr>
      <th>page_views_per_visit</th>
      <td>0.0</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>last_activity</th>
      <td>page_visited_on_website</td>
      <td>email_opened</td>
      <td>email_opened</td>
      <td>unreachable</td>
      <td>converted_to_lead</td>
    </tr>
    <tr>
      <th>country</th>
      <td>NaN</td>
      <td>india</td>
      <td>india</td>
      <td>india</td>
      <td>india</td>
    </tr>
    <tr>
      <th>specialization</th>
      <td>select</td>
      <td>select</td>
      <td>business_administration</td>
      <td>media_and_advertising</td>
      <td>select</td>
    </tr>
    <tr>
      <th>how_did_you_hear_about_x_education</th>
      <td>select</td>
      <td>select</td>
      <td>select</td>
      <td>word_of_mouth</td>
      <td>other</td>
    </tr>
    <tr>
      <th>what_is_your_current_occupation</th>
      <td>unemployed</td>
      <td>unemployed</td>
      <td>student</td>
      <td>unemployed</td>
      <td>unemployed</td>
    </tr>
    <tr>
      <th>what_matters_most_to_you_in_choosing_a_course</th>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
    </tr>
    <tr>
      <th>search</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>magazine</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>newspaper_article</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>x_education_forums</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>newspaper</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>digital_advertisement</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>through_recommendations</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>receive_more_updates_about_our_courses</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>tags</th>
      <td>interested_in_other_courses</td>
      <td>ringing</td>
      <td>will_revert_after_reading_the_email</td>
      <td>ringing</td>
      <td>will_revert_after_reading_the_email</td>
    </tr>
    <tr>
      <th>lead_quality</th>
      <td>low_in_relevance</td>
      <td>NaN</td>
      <td>might_be</td>
      <td>not_sure</td>
      <td>might_be</td>
    </tr>
    <tr>
      <th>update_me_on_supply_chain_content</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>get_updates_on_dm_content</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>lead_profile</th>
      <td>select</td>
      <td>select</td>
      <td>potential_lead</td>
      <td>select</td>
      <td>select</td>
    </tr>
    <tr>
      <th>city</th>
      <td>select</td>
      <td>select</td>
      <td>mumbai</td>
      <td>mumbai</td>
      <td>mumbai</td>
    </tr>
    <tr>
      <th>asymmetrique_activity_index</th>
      <td>02.medium</td>
      <td>02.medium</td>
      <td>02.medium</td>
      <td>02.medium</td>
      <td>02.medium</td>
    </tr>
    <tr>
      <th>asymmetrique_profile_index</th>
      <td>02.medium</td>
      <td>02.medium</td>
      <td>01.high</td>
      <td>01.high</td>
      <td>01.high</td>
    </tr>
    <tr>
      <th>asymmetrique_activity_score</th>
      <td>15.0</td>
      <td>15.0</td>
      <td>14.0</td>
      <td>13.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>asymmetrique_profile_score</th>
      <td>15.0</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>17.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>i_agree_to_pay_the_amount_through_cheque</th>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>a_free_copy_of_mastering_the_interview</th>
      <td>no</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <th>last_notable_activity</th>
      <td>modified</td>
      <td>email_opened</td>
      <td>email_opened</td>
      <td>modified</td>
      <td>modified</td>
    </tr>
  </tbody>
</table>
</div>



Tras esta conversión, analizamos el número de valores  **únicos** que tiene cada columna:


```python
df.nunique() # Número de valores únicos por columna
```




    prospect_id                                      9240
    lead_number                                      9240
    lead_origin                                         5
    lead_source                                        20
    do_not_email                                        2
    do_not_call                                         2
    converted                                           2
    totalvisits                                        41
    total_time_spent_on_website                      1731
    page_views_per_visit                              114
    last_activity                                      17
    country                                            38
    specialization                                     19
    how_did_you_hear_about_x_education                 10
    what_is_your_current_occupation                     6
    what_matters_most_to_you_in_choosing_a_course       3
    search                                              2
    magazine                                            1
    newspaper_article                                   2
    x_education_forums                                  2
    newspaper                                           2
    digital_advertisement                               2
    through_recommendations                             2
    receive_more_updates_about_our_courses              1
    tags                                               26
    lead_quality                                        5
    update_me_on_supply_chain_content                   1
    get_updates_on_dm_content                           1
    lead_profile                                        6
    city                                                7
    asymmetrique_activity_index                         3
    asymmetrique_profile_index                          3
    asymmetrique_activity_score                        12
    asymmetrique_profile_score                         10
    i_agree_to_pay_the_amount_through_cheque            1
    a_free_copy_of_mastering_the_interview              2
    last_notable_activity                              16
    dtype: int64



Se puede apreciar que el DataFrame contiene varias columnas con 1 único valor, como ya se intuía con las estadísticas generadas con .describe(). De ellas no podremos *inferir* nada, por lo que las suprimimos para simplificar nuestro conjunto de datos:


```python
colums_to_drop = { 'magazine', 'receive_more_updates_about_our_courses',
            'update_me_on_supply_chain_content', 'get_updates_on_dm_content',
            'i_agree_to_pay_the_amount_through_cheque'}

for column in colums_to_drop:
    df.drop(column, axis = 1, inplace=True)
```

También podemos comprobar si hay errores en algunas columnas. Por ejemplo, se asume que la columna *prospect_id* debe contener valores únicos, lo cual podemos comprobar con el siguiente código:

A continuación convertimos las columnas con valores yes/no a tipo entero 1/0, para que nuestro modelo predictivo funcione mejor. 

Antes que nada, para cada una de estas columnas, se comprueba que no tengan valores distintos más allá de los yes/no.


```python
yes_no_columns = {'do_not_email', 'do_not_call', 'search', 
    'newspaper_article', 'x_education_forums', 'newspaper', 
    'digital_advertisement', 'through_recommendations', 
    'a_free_copy_of_mastering_the_interview'}

for column in yes_no_columns:
    print(column,' = ',df[column].unique())
```

    through_recommendations  =  ['no' 'yes']
    digital_advertisement  =  ['no' 'yes']
    newspaper_article  =  ['no' 'yes']
    x_education_forums  =  ['no' 'yes']
    do_not_call  =  ['no' 'yes']
    search  =  ['no' 'yes']
    do_not_email  =  ['no' 'yes']
    a_free_copy_of_mastering_the_interview  =  ['no' 'yes']
    newspaper  =  ['no' 'yes']


Comprobados que los valores de las columnas están dentro de lo esperado, procedemos a la conversión a 1/0 anteriormente comentada:


```python
yes_no_columns = {'do_not_email', 'do_not_call', 'search', 
    'newspaper_article', 'x_education_forums', 'newspaper', 
    'digital_advertisement', 'through_recommendations', 
    'a_free_copy_of_mastering_the_interview'}

for column in yes_no_columns:
    df[column] = (df[column] == 'yes').astype(int)
    print(column,' = ',df[column].unique())
```

    through_recommendations  =  [0 1]
    digital_advertisement  =  [0 1]
    newspaper_article  =  [0 1]
    x_education_forums  =  [0 1]
    do_not_call  =  [0 1]
    search  =  [0 1]
    do_not_email  =  [0 1]
    a_free_copy_of_mastering_the_interview  =  [0 1]
    newspaper  =  [0 1]


Antes de aplicar la transformación a int de las columnas asymmetrique_activity_index y asymmetrique_profile_index, comprobamos sus valores:


```python
asymetric_index_columns = { 'asymmetrique_activity_index', 'asymmetrique_profile_index' }

for column in asymetric_index_columns:
    print(column,' = ',df[column].unique())
```

    asymmetrique_profile_index  =  ['02.medium' '01.high' '03.low' nan]
    asymmetrique_activity_index  =  ['02.medium' '01.high' '03.low' nan]


Vemos que ambas columnas tienen valores similares, por lo que podrían ser redundantes. Sin embargo, vemos que tienen valores NA, por lo que antes de iniciar un tratamiento vamos a computar el número de celdas sin datos. Como parece haber una correlación entre estas columnas y las de asymmetrique_activity_score y asymmetrique_profile_score, comprobamos las 4:


```python
asymetric_columns = { 'asymmetrique_activity_index', 'asymmetrique_profile_index', 'asymmetrique_activity_score', 'asymmetrique_profile_score' }

for column in asymetric_columns:
    num_data = df[column].count() # En este conteo se omiten los na
    num_na = df[column].isna().sum()
    print(column,'=> Data rows = ',num_data,', NA rows = ',num_na)
```

    asymmetrique_profile_index => Data rows =  5022 , NA rows =  4218
    asymmetrique_profile_score => Data rows =  5022 , NA rows =  4218
    asymmetrique_activity_score => Data rows =  5022 , NA rows =  4218
    asymmetrique_activity_index => Data rows =  5022 , NA rows =  4218


Como el número de valores NA de cada columna es elevado (rondando el 50% de cada columna), se suprimen por simplificación:


```python
for column in asymetric_columns:
    df.drop(column, axis = 1, inplace = True)
```

Vemos finalmente como ha quedado nuestro dataset:


```python
df.head().T
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>prospect_id</th>
      <td>7927b2df-8bba-4d29-b9a2-b6e0beafe620</td>
      <td>2a272436-5132-4136-86fa-dcc88c88f482</td>
      <td>8cc8c611-a219-4f35-ad23-fdfd2656bd8a</td>
      <td>0cc2df48-7cf4-4e39-9de9-19797f9b38cc</td>
      <td>3256f628-e534-4826-9d63-4a8b88782852</td>
    </tr>
    <tr>
      <th>lead_number</th>
      <td>660737</td>
      <td>660728</td>
      <td>660727</td>
      <td>660719</td>
      <td>660681</td>
    </tr>
    <tr>
      <th>lead_origin</th>
      <td>api</td>
      <td>api</td>
      <td>landing_page_submission</td>
      <td>landing_page_submission</td>
      <td>landing_page_submission</td>
    </tr>
    <tr>
      <th>lead_source</th>
      <td>olark_chat</td>
      <td>organic_search</td>
      <td>direct_traffic</td>
      <td>direct_traffic</td>
      <td>google</td>
    </tr>
    <tr>
      <th>do_not_email</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>do_not_call</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>converted</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>totalvisits</th>
      <td>0.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>total_time_spent_on_website</th>
      <td>0</td>
      <td>674</td>
      <td>1532</td>
      <td>305</td>
      <td>1428</td>
    </tr>
    <tr>
      <th>page_views_per_visit</th>
      <td>0.0</td>
      <td>2.5</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>last_activity</th>
      <td>page_visited_on_website</td>
      <td>email_opened</td>
      <td>email_opened</td>
      <td>unreachable</td>
      <td>converted_to_lead</td>
    </tr>
    <tr>
      <th>country</th>
      <td>NaN</td>
      <td>india</td>
      <td>india</td>
      <td>india</td>
      <td>india</td>
    </tr>
    <tr>
      <th>specialization</th>
      <td>select</td>
      <td>select</td>
      <td>business_administration</td>
      <td>media_and_advertising</td>
      <td>select</td>
    </tr>
    <tr>
      <th>how_did_you_hear_about_x_education</th>
      <td>select</td>
      <td>select</td>
      <td>select</td>
      <td>word_of_mouth</td>
      <td>other</td>
    </tr>
    <tr>
      <th>what_is_your_current_occupation</th>
      <td>unemployed</td>
      <td>unemployed</td>
      <td>student</td>
      <td>unemployed</td>
      <td>unemployed</td>
    </tr>
    <tr>
      <th>what_matters_most_to_you_in_choosing_a_course</th>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
      <td>better_career_prospects</td>
    </tr>
    <tr>
      <th>search</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>newspaper_article</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>x_education_forums</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>newspaper</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>digital_advertisement</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>through_recommendations</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>tags</th>
      <td>interested_in_other_courses</td>
      <td>ringing</td>
      <td>will_revert_after_reading_the_email</td>
      <td>ringing</td>
      <td>will_revert_after_reading_the_email</td>
    </tr>
    <tr>
      <th>lead_quality</th>
      <td>low_in_relevance</td>
      <td>NaN</td>
      <td>might_be</td>
      <td>not_sure</td>
      <td>might_be</td>
    </tr>
    <tr>
      <th>lead_profile</th>
      <td>select</td>
      <td>select</td>
      <td>potential_lead</td>
      <td>select</td>
      <td>select</td>
    </tr>
    <tr>
      <th>city</th>
      <td>select</td>
      <td>select</td>
      <td>mumbai</td>
      <td>mumbai</td>
      <td>mumbai</td>
    </tr>
    <tr>
      <th>a_free_copy_of_mastering_the_interview</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>last_notable_activity</th>
      <td>modified</td>
      <td>email_opened</td>
      <td>email_opened</td>
      <td>modified</td>
      <td>modified</td>
    </tr>
  </tbody>
</table>
</div>



# Creación del modelo

Lo primero que haremos será la extracción de nuestra variable objetivo, que en nuestro caso es *converted*:


```python
target_name = "converted" # Variable objetivo
target = df[target_name]

data = df.drop(columns=[target_name])
```

Tras ello, procedemos a realizar la división de los datos para quedarnos con una parte para entrenamiento del modelo y otra para test:


```python
from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    data, target, test_size = 0.2, random_state=42) # División: 80% entrenamiento, 20% test
```

A continuación, instanciamos 2 preprocesadores distintos para las columnas numéricas y para las categóricas, y lo vinculamos a un transformador por columnas:


```python
from sklearn.compose import make_column_selector as selector
#from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

numerical_columns_selector = selector(dtype_exclude=object)  # Selector para extraer columnas numéricas
categorical_columns_selector = selector(dtype_include=object)  # Selector para extraer columnas categóricas

numerical_columns = numerical_columns_selector(data)
categorical_columns = categorical_columns_selector(data)

numerical_preprocessor = StandardScaler() # Escalador para columnas numéricas
#categorical_preprocessor = OneHotEncoder(handle_unknown="ignore") # Transformador para columnas categóricas
categorical_preprocessor = OrdinalEncoder(handle_unknown="use_encoded_value",
                                          unknown_value=-1)

preprocessor = ColumnTransformer([
    ('categorical', categorical_preprocessor, categorical_columns),
    ('numerical', numerical_preprocessor, numerical_columns)])
```

Ahora instanciaremos un modelo y lo vincularemos mediante una *pipeline* a nuestro transformador por columnas. Para el problema expuesto, se elige un modelo de clasificación ***HistGradientBoostingClassifier***:


```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingClassifier

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", HistGradientBoostingClassifier(random_state=42, max_leaf_nodes=4) )
])
```


```python
from sklearn.model_selection import cross_validate

cv_result = cross_validate(model, data_train, target_train, cv=5)

np.median(cv_result['test_score'])
```




    0.935723951285521




```python
from sklearn.model_selection import cross_validate

cv_result = cross_validate(model, data_test, target_test, cv=5)

np.median(cv_result['test_score'])
```




    0.9243243243243243



Para buscar la mejor configuración del modelo usaremos ***RandomizedSearchCV***, que se encarga de buscar de forma aleatoria y ofrecer una elección de hiperparámetros, utilizando además validación cruzada para puntuar el rendimiento del ajuste seleccionado: TODO

# Serialización del modelo

Para exportar nuestro modelo, lo serializamos utilizando *pickle*:


```python
import pickle

model.fit(data_train, target_train)

with open('../models/converted-model.pck', 'wb') as f:
    pickle.dump(model, f)
```

Y lo probamos con *cURL*:


```python
!curl --request POST 'http://127.0.0.1:8000/predict' \
--header 'Content-Type: application/json'\
--data-raw '{\
   "prospect_id": "7927b2df-8bba-4d29-b9a2-b6e0beafe620",\
   "lead_number": 660737,\
   "lead_origin": "api",\
   "lead_source": "olark_chat",\
   "do_not_email": 0,\
   "do_not_call": 0,\
   "converted": 0,\
   "totalvisits": 0.0,\
   "total_time_spent_on_website": 0,\
   "page_views_per_visit": 0.0,\
   "last_activity": "page_visited_on_website",\
   "country": "NaN",\
   "specialization": "select",\
   "how_did_you_hear_about_x_education": "select",\
   "what_is_your_current_occupation": "unemployed",\
   "what_matters_most_to_you_in_choosing_a_course": "better_career_prospects",\
   "search": 0,\
   "newspaper_article": 0,\
   "x_education_forums": 0,\
   "newspaper": 0,\
   "digital_advertisement": 0,\
   "through_recommendations": 0,\
   "tags": "interested_in_other_courses",\
   "lead_quality": "low_in_relevance",\
   "lead_profile": "select",\
   "city": "select",\
   "a_free_copy_of_mastering_the_interview": 0,\
   "last_notable_activity": "modified"\
}'
```

    {
      "convert_probability": 0
    }

