# Datasheet
## Motivation
* This data was collected in support of research on understanding the media landscape during highly controversial topics
* This data was collected by researchers affiliated with the Army Cyber Institute at West Point
  and supported in part by the Office of Naval Research (ONR) under Support Agreement No. USMA 20057. 
## Composition
* This data is composed of the raw news articles with unique identifiers, their associated urls, article text, the domain, 
and the corresponding domain data labels from
[Clustering Analysis of Website Usage on Twitter during the COVID-19 Pandemic](https://figshare.com/articles/conference_contribution/Clustering_Analysis_of_Website_Usage_on_Twitter_during_the_COVID-19_Pandemic/13079657?file=25030256)
* The raw data has instances of missing labels and duplicative articles (addressed in ppreprocessing functions).

## Collection process
* This data was automatically scraped using the methodology discussed in [DocNet](https://arxiv.org/abs/2406.10965)

## Preprocessing
* Our data cleaning functions are made available in `process_data.py` and `newsnet_utils.py` addresses most of these concerns.

## Uses
* This data is used for media bias research as in [DocNet](https://arxiv.org/abs/2406.10965)
and [Analysis of Media Writing Style Bias](https://arxiv.org/abs/2305.13098)
* Further research could also explore media credibility, factuality, and event framing from this dataset.

### Disclaimers:
* This work does not reflect the official policy or
position of the United States Military Academy, the United States Army,
the Department of Defense, or the United States Government.
* This data was collected and is made available under the
provisions of Section 107 of the U.S. Copyright Act and the fair use category.
