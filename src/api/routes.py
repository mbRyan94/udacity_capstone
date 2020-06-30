
from src.api.projects.projects import Projects
from src.api.projects.project import Project
from src.api.profile.profile import Profile
from src.api.workitems.workitems import Workitems
from src.api.workitems.workitem import Workitem
from src.api.workspaces.workspaces import Workspaces
from src.api.workspaces.workspace import Workspace


def initialize_routes(api):
    api.add_resource(Projects, '/api/projects')
    api.add_resource(Project, '/api/projects/<int:project_id>')
    api.add_resource(Profile, '/api/profile')
    api.add_resource(Workspaces, '/api/projects/<int:project_id>/workspaces')
    api.add_resource(
        Workspace, '/api/projects/<int:project_id>/workspaces/<int:workspace_id>')
    api.add_resource(
        Workitems, '/api/projects/<int:project_id>/workspaces/<int:workspace_id>/workitems')
    api.add_resource(
        Workitem, '/api/projects/<int:project_id>/workspaces/<int:workspace_id>/workitems/<int:workitem_id>')
