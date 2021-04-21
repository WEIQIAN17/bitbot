"""empty message

Revision ID: b2bcecd93c74
Revises: 759d435602c8
Create Date: 2021-04-20 23:04:47.269860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2bcecd93c74'
down_revision = '759d435602c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bit_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('horah', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('order', sa.String(length=16), nullable=True),
    sa.Column('subcription_type', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Product_subcription_type'), 'Product', ['subcription_type'], unique=False)
    op.create_index(op.f('ix_Product_username'), 'Product', ['username'], unique=False)
    op.create_table('Transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('action', sa.String(length=16), nullable=True),
    sa.Column('order', sa.String(length=16), nullable=True),
    sa.Column('status', sa.String(length=16), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Transaction_username'), 'Transaction', ['username'], unique=False)
    op.create_table('Strategy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('strategy_name', sa.String(length=64), nullable=True),
    sa.Column('product_strategy_algorithm', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['Product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Strategy_product_strategy_algorithm'), 'Strategy', ['product_strategy_algorithm'], unique=False)
    op.create_index(op.f('ix_Strategy_strategy_name'), 'Strategy', ['strategy_name'], unique=False)
    op.drop_index('ix_Strategies_product_strategy_algorithm', table_name='Strategies')
    op.drop_index('ix_Strategies_strategy_name', table_name='Strategies')
    op.drop_table('Strategies')
    op.drop_index('ix_transaction_username', table_name='transaction')
    op.drop_table('transaction')
    op.drop_index('ix_Products_subcription_type', table_name='Products')
    op.drop_table('Products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Products',
    sa.Column('product_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('subcription_type', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_index('ix_Products_subcription_type', 'Products', ['subcription_type'], unique=False)
    op.create_table('transaction',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('action', sa.VARCHAR(length=16), nullable=True),
    sa.Column('amount', sa.FLOAT(), nullable=True),
    sa.Column('order', sa.VARCHAR(length=16), nullable=True),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('status', sa.VARCHAR(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_transaction_username', 'transaction', ['username'], unique=False)
    op.create_table('Strategies',
    sa.Column('product_id', sa.INTEGER(), nullable=False),
    sa.Column('strategy_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('product_strategy_algorithm', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_index('ix_Strategies_strategy_name', 'Strategies', ['strategy_name'], unique=False)
    op.create_index('ix_Strategies_product_strategy_algorithm', 'Strategies', ['product_strategy_algorithm'], unique=False)
    op.drop_index(op.f('ix_Strategy_strategy_name'), table_name='Strategy')
    op.drop_index(op.f('ix_Strategy_product_strategy_algorithm'), table_name='Strategy')
    op.drop_table('Strategy')
    op.drop_index(op.f('ix_Transaction_username'), table_name='Transaction')
    op.drop_table('Transaction')
    op.drop_index(op.f('ix_Product_username'), table_name='Product')
    op.drop_index(op.f('ix_Product_subcription_type'), table_name='Product')
    op.drop_table('Product')
    op.drop_table('bit_price')
    # ### end Alembic commands ###