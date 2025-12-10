"""empty message

Revision ID: cf72c680d3a6
Revises: 4b689ddbfa55
Create Date: 2025-12-09 14:15:25.938534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'cf72c680d3a6'
down_revision: Union[str, Sequence[str], None] = '4b689ddbfa55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create the enum type first
    op.execute("CREATE TYPE status AS ENUM ('UPLOADED', 'PROCESSING', 'READY', 'FAILED')")
    
    # Now add the columns
    op.add_column('documents', sa.Column('status', postgresql.ENUM('UPLOADED', 'PROCESSING', 'READY', 'FAILED', name='status', create_type=False), nullable=False))
    op.add_column('documents', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    # Drop columns first
    op.drop_column('documents', 'updated_at')
    op.drop_column('documents', 'status')
    
    # Then drop the enum type
    op.execute("DROP TYPE IF EXISTS status")
