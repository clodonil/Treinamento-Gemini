# ~api/app/resources/routes.py

from .chat import ChatApi


def initialize_routes(api):
    api.add_resource(ChatApi, '/api/chat')
