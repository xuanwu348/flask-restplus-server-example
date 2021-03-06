"""empty message

Revision ID: bfd746605962
Revises: 82184d7d1e88
Create Date: 2020-06-15 18:51:12.902899

"""

# revision identifiers, used by Alembic.
revision = 'bfd746605962'
down_revision = '82184d7d1e88'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AI_Constant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('const_name', sa.String(length=64), nullable=False),
    sa.Column('const_value_male', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_value_female', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_child_16', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('sigma', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_AI_Constant'))
    )
    op.create_table('AI_Constant_APP',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('const_id', sa.Integer(), nullable=False),
    sa.Column('const_name', sa.String(length=64), nullable=False),
    sa.Column('const_value_male', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_value_female', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_child_16', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_min', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_max', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('range_min', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('range_max', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_sigma', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('const_description', sa.String(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_AI_Constant_APP'))
    )
    op.create_table('AI_UPID',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upid_int', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=128), nullable=False),
    sa.Column('pag', sa.Integer(), nullable=False),
    sa.Column('des_basic', sa.String(length=1024), nullable=False),
    sa.Column('des_positive', sa.String(length=1024), nullable=False),
    sa.Column('des_negative', sa.String(length=1024), nullable=False),
    sa.Column('des_suggest', sa.String(length=1024), nullable=False),
    sa.Column('des_child_16', sa.String(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_AI_UPID'))
    )
    op.create_table('AI_USER_APPKEY',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('log_id', sa.String(length=128), nullable=False),
    sa.Column('cuid', sa.Integer(), nullable=False),
    sa.Column('page_type', sa.Integer(), nullable=False),
    sa.Column('tree_height', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_width', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_area', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_on_left', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_on_right', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_on_top', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_on_bottom', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_on_page', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_height', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_width', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area_1', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area_2', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area_3', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area_4', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area_5', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_crown_area_6', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_trunk_height', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_trunk_width', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_trunk_area', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_root_height', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_root_width', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('tree_root_area', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('xinzhi_value', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('siwei_value', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('qingxu_value', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('juese_value', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('nengli_value', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('qianyishi_value', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('log_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_AI_USER_APPKEY'))
    )
    op.create_table('AI_USER_INFO',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cuid', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=64), nullable=False),
    sa.Column('region', sa.String(length=128), nullable=False),
    sa.Column('orignal_cuid', sa.String(length=128), nullable=True),
    sa.Column('client_id', sa.String(length=128), nullable=False),
    sa.Column('reg_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_AI_USER_INFO'))
    )
    op.create_table('AI_USER_REP',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('log_id', sa.String(length=128), nullable=False),
    sa.Column('cuid', sa.Integer(), nullable=False),
    sa.Column('analysis_rep', sa.Text(), nullable=False),
    sa.Column('log_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_AI_USER_REP'))
    )
    
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('open_id', sa.String(length=256), nullable=True),
    sa.Column('identifier', sa.String(length=128), nullable=False),
    sa.Column('req_source', sa.String(length=256), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_index(op.f('ix_users_identifier'), 'users', ['identifier'], unique=True)
    op.drop_table('team_member')
    op.drop_table('team')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('AI_USER_REP')
    op.drop_table('AI_USER_INFO')
    op.drop_table('AI_USER_APPKEY')
    op.drop_table('AI_UPID')
    op.drop_table('AI_Constant_APP')
    op.drop_table('AI_Constant')
    # ### end Alembic commands ###
