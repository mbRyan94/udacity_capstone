"""delete user model

Revision ID: fc96e9e16d52
Revises: eaac0dede227
Create Date: 2020-06-24 22:28:50.994915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc96e9e16d52'
down_revision = 'eaac0dede227'
branch_labels = None
depends_on = None


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('workitem')
    op.drop_table('workspace')
    op.drop_table('project')

    op.create_table('user',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('email', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='user_pkey')
                    )
    op.create_table('project',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        'nextval(\'"project_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('start_date', sa.Date(),
                              autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.Timestamp(),
                              autoincrement=False, nullable=True),
                    sa.Column('user_id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='project_pkey')
                    )
    op.create_table('workspace',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        'nextval(\'"workspace_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('price', sa.Float(),
                              autoincrement=False, nullable=True),
                    sa.Column('start_date', sa.Date(),
                              autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.Timestamp(),
                              autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(
                        ('project_id', ), ['project.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id', name='workspace_pkey')
                    )
    op.create_table('workitem',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        'nextval(\'"workitem_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('duration', sa.Float(),
                              autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.Timestamp(),
                              autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(
                        ('workspace_id', ),  ['workspace.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id', name='workitem_pkey')
                    )

    # ### end Alembic commands ###


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('workitem')
    op.drop_table('workspace')
    op.drop_table('project')

    op.create_table('user',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('email', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='user_pkey')
                    )
    op.create_table('project',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        'nextval(\'"project_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('start_date', sa.Date(),
                              autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.Timestamp(),
                              autoincrement=False, nullable=True),
                    sa.Column('user_id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='project_pkey')
                    )
    op.create_table('workspace',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        'nextval(\'"workspace_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('price', sa.Float(),
                              autoincrement=False, nullable=True),
                    sa.Column('start_date', sa.Date(),
                              autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.Timestamp(),
                              autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(
                        ('project_id', ), ['project.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id', name='workspace_pkey')
                    )
    op.create_table('workitem',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text(
                        'nextval(\'"workitem_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('duration', sa.Float(),
                              autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.Timestamp(),
                              autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(
                        ('workspace_id', ),  ['workspace.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id', name='workitem_pkey')
                    )

    # ### end Alembic commands ###
