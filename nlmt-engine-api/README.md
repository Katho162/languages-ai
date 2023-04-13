# NLMT Engine

NLMT (Next-Gen Language Management Tool) is a Machine Learning model that can suggest a next-to-learn language based on your previously learned languages. This is a FastAPI app that manages and serve the model in as a RESTful service.

## Get Started

First you need to install [Python](https://www.python.org/). After that, being sure there's a correct image of the model in `app/model/nlmt.pkl`. You need to enter venv mode using `python -m venv venv` and using `venv\Scripts\activate` on Windows or `source venv/bin/activate` on MacOS/Linux. After that, you need to install the dependencies from `requirements.txt` using `pip install -r requirements.txt`. 

Everything done? You can start the app by using:

```
$ uvicorn src.app.main:app --reload
```

## Jupyter Nootbook

In construction

## DS Tools

There's structured `io` and `fs` modules inside `tools/` to handle all the DS models and jobs. Keep that structure in order to pickle all the DS Models images organized and in place.

## Copyright

© Felipe Gomes 2022. All rights reserved.