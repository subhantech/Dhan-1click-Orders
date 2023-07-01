from typing import List, Union, Literal
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dhanhq import dhanhq
from fastapi.responses import HTMLResponse
import math
from getOptionStrikes import getOptionStrikes
from pydantic import BaseModel
import time

    
templates = Jinja2Templates(directory="templates")
templates.env.autoescape = False
client_id = 1100915906
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNjkwMzEyODM4LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMDkxNTkwNiJ9.0k0tb0qPq7WhJ5cZgB7VuRWfisg85n-IQoj7KzRMO5h9P2RCa62766vA-hBwLuLcX9J2jfaIHAcHVtrL2w0UaA"
dhan = dhanhq("client_id",access_token)

########################## Functions section
getOptionStrikes = getOptionStrikes()
app = FastAPI()

class Indices(BaseModel):
    indice_name: str 


app.mount("/static", StaticFiles(directory="static"), name="static")

################## below block is working perfectly
@app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("base.html", {"request": request})
#########################
async def indexltp(request: Request):
    niftyIdx = getOptionStrikes.indiceLTP("nifty")
    bankniftyIdx = getOptionStrikes.indiceLTP("banknifty")
    finniftyIdx = getOptionStrikes.indiceLTP("finnifty")
   
    return templates.TemplateResponse("indiceltp.html", {"request": request, "nifty" : niftyIdx, "banknifty" : bankniftyIdx, "finnifty" : finniftyIdx  })
################################### above section works


# @app.get("/static/", response_class=HTMLResponse)

############# Functions to get option dATA

###############################################################3
## Using these for testing purposes
#############################################################


# @app.get("/form")
# def form_post(request: Request):
#     result = "Type a number"
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


# @app.post("/form")
# def form_post(request: Request, num: int = Form(...)):
#     result = num
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})
