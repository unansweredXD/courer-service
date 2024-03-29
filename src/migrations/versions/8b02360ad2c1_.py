"""empty message

Revision ID: 8b02360ad2c1
Revises: 
Create Date: 2024-02-16 00:23:12.803098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b02360ad2c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('couriers',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('districts', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('active_order', sa.UUID(), nullable=True),
    sa.Column('avg_day_orders', sa.Integer(), nullable=False),
    sa.Column('avg_order_complete_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['active_order'], ['orders.sid'], use_alter=True),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_index(op.f('ix_couriers_sid'), 'couriers', ['sid'], unique=True)
    op.create_table('orders',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('in_progress', 'complete', name='order_status'), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('courier_sid', sa.UUID(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['courier_sid'], ['couriers.sid'], use_alter=True),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_index(op.f('ix_orders_sid'), 'orders', ['sid'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_sid'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_couriers_sid'), table_name='couriers')
    op.drop_table('couriers')
    # ### end Alembic commands ###
