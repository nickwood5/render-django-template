from ninja import NinjaAPI
from mynewproject.views.debug.router import debug_router

api = NinjaAPI(urls_namespace="mynewproject")

api.add_router("/debug", debug_router)
