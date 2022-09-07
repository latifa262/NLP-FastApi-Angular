## Table of contents
   This is an app that helps to analyze travelers feelings on Twitter about the Airlines, is it positive or negative. 
   This work can be useful for the airline company to understand what are the problems to work on.
   
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
For the web application, we use Angular. For that, you need to :

1. Install NodeJs from NodeJs Official Page.
2. Open Terminal
3. Go to your file project
4. Run in terminal: ``` npm install -g @angular/cli ```
5. Then: ``` npm install ```
6. And: ``` ng serve ```
7. Navigate to http://localhost:4200/

## Running it all together

To run the server side you need to go to the fastapi foler :
```
uvicorn main:app --reload
```
In another terminal you need to go to the frontend folder :
```
npm install
ng serve
```
Once you have done so, you can go to localhost:4200 and test the application.




