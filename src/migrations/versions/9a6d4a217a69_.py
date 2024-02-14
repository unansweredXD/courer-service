"""empty message

Revision ID: 9a6d4a217a69
Revises: 
Create Date: 2024-02-14 21:32:28.277893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a6d4a217a69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('couriers',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('districts', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('order_id', sa.UUID(), nullable=True),
    sa.Column('avg_orders', sa.Integer(), nullable=False),
    sa.Column('avg_order_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_couriers_id'), 'couriers', ['id'], unique=True)
    op.create_table('orders',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('in_progress', 'complete', name='order_status'), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('courier_id', sa.UUID(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_couriers_id'), table_name='couriers')
    op.drop_table('couriers')
    # ### end Alembic commands ###