from behave import given, when, then
import requests
from universal_var.read_var1 import *

@given('we have detail of book')
def fetch_api(context):
 context.a=read_var12()
 context.url=context.a['API']['url']

@when('we submit book detail in addBook api')
def bookinfo_add_(context):
  context.headerss={"Content-Type":"application/json"}
  context.book_detail_payload={
  "id": 3,
  "title": "string",
  "description": "string",
  "pageCount": 0,
  "excerpt": "string",
  "publishDate": "2024-10-22T09:50:56.428Z"}
  context.req1=requests.post(context.url,json=context.book_detail_payload,headers=context.headerss)
  context.json_result=context.req1.json()
  context.resultID=context.json_result['id']
  print(f" id------>= {context.resultID}")
  print(f" url------>= {context.req1}")
  context.status=context.req1.status_code
  print(f" status------>= {context.status}")
    
@then('sucess in adding book')
def status_(context):
 
 print("----->",context.json_result)

  
 assert context.status==200,"error occure "
