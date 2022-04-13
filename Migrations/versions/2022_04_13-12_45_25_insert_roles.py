"""Insert roles

Revision ID: 1d138caf57f8
Revises: f29afd626450
Create Date: 2022-04-13 12:45:25.359399

"""
from alembic import op
import sqlalchemy as sa
from Tables import Role


# revision identifiers, used by Alembic.
revision = '1d138caf57f8'
down_revision = 'f29afd626450'
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
    op.execute(
        roles_table.delete()
    )
