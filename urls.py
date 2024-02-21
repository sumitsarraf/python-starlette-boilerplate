# Starlette Imports
from starlette.routing import Route

# RHEA related Views

#for query
#from views import GetModels, GetCompletions
from views import GetCompletions


routes = [
    #Route("/models", endpoint=GetModels),
    Route("/completions/query", endpoint=GetCompletions)
]
