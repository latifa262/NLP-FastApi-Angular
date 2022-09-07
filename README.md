## Table of contents
* [FastApi](#fastapi)
* [Frontend](#frontend)
* [Running it all together](#Running-it-all-together)


## FastApi
After the creation of the nlp model the next step is to save the model in $\color[rgb]{1,1,1} model.h5$
 and the Tokenizer $\color[rgb]{1,1,1} tokenizer.pickle$, so we can load both files in the $\color[rgb]{1,1,1} main file$ This file puts all other pieces together and builds the REST API with FastAPI.

-- Install FastApi and ASGI server :
```
$pip install fastapi
$pip install uvicorn
```
-- To test the server-side
```
$uvicorn main:app --reload
```
FastAPI provides an Automatic Interactive API documentation page. To access it navigate to http://127.0.0.1:8000/docs in your browser and then you will see the documentation page created automatically by FastAPI.

## Frontend
For the web application, we use Angular. For that, you need to install Node.js and npm.
to install Angular:

```
$npm install -g angular-cli
```
