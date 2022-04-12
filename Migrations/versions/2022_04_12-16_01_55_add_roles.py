"""Add roles

Revision ID: cd8a43134e04
Revises: 0a5b20c60074
Create Date: 2022-04-12 16:01:55.757602

"""
from alembic import op
import sqlalchemy as sa
from Tables import Role


# revision identifiers, used by Alembic.
revision = 'cd8a43134e04'
down_revision = '0a5b20c60074'
branch_labels = None
depends_on = None

roles_table = Role.__table__

def upgrade():
    op.execute(
        roles_table.insert().values([
            {
                'role': 'root'
            },
            {
                'role': 'admin'
            }
        ])
    )


def downgrade():
    pass
