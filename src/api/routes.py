
from src.api.projects.projects import Projects
from src.api.projects.project import Project
from src.api.profile.profile import Profile


def initialize_routes(api):
    api.add_resource(Projects, '/api/projects')
    api.add_resource(Project, '/api/projects/<int:project_id>')
    api.add_resource(Profile, '/api/profile')
