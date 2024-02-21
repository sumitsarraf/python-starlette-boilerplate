'''
@Author : Sumit Ranjan
'''
#import base64
#import binascii
# Third-party Imports
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
#import os
#print('path---------',os.getcwd())
#from openaigpt3 import get_models, get_completions
from mystarlette_app import get_completions



#for BotDploy

        
class GetCompletions(HTTPEndpoint):
    async def post(self, request):
        if request.user.is_authenticated:
            params = await request.json()
            response = get_completions(params)
            return JSONResponse(response)
        else:
            return JSONResponse("Authentication Failed")         
           