
from src.api.projects.projects import Projects


def initialize_routes(api):
    api.add_resource(Projects, '/api/projects')
