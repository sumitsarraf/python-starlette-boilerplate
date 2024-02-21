# Python Built-in Imports
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Third-Party Imports
import uvicorn
from starlette.applications import Starlette
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from urls import routes
from settings import BasicAuthBackend

middleware = [
  Middleware(
  CORSMiddleware, 
  allow_origins=['*',"http://localhost","http://localhost:8080"],
  allow_methods=['POST', 'GET'],
  allow_headers=['access-control-allow-origin', 'authorization', 'content-type'],
  )]


def startup():
    print('Starlette glpt3 Framework is Ready!!!')


app = Starlette(debug=True, routes=routes,middleware=middleware, on_startup=[startup])
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=9001)
