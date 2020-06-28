from src.db.models import Project, Workspace, Workitem
from sqlalchemy import and_


def get_workitems_by_workspace_id(workspace_id):
    return Workitem.query.filter(Workitem.workspace_id == workspace_id).all()


def get_workitem_by_id(workitem_id):
    return Workitem.query.filter(Workitem.id == workitem_id).one_or_none()


def get_workspaces_by_project_id(project_id):
    return Project.query.find(Workspace.project_id == project_id).all()


def get_all_projects_by_user_id(user_id):
    return Project.query.filter(Project.user_id == user_id).all()


def get_project_by_id_and_user(user_id, project_id):
    return Project.query.filter(and_(user_id == Project.user_id, project_id == Project.id)).one_or_none()
