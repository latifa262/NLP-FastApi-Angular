## Table of contents
* [FastApi](#fastapi)
* [Frontend](#frontend)
* [Running it all together](#Running-it-all-together)


## FastApi
After the creation of the nlp model the next step is to save the model in $\color[rgb]{1,1,1} model.h5$
 and the Tokenizer $\color[rgb]{1,1,1} tokenizer.pickle$, so we can load both files in the $\color[rgb]{1,1,1} main file$ This file puts all other pieces together and builds the REST API with FastAPI.

--Install FastApi and ASGI server :
```
$pip install fastapi
$pip install uvicorn
```
-- to testing the server-side
```
$uvicorn main:app --reload

```

## Frontend
