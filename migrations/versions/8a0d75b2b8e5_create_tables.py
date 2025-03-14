"""Create tables

Revision ID: 8a0d75b2b8e5
Revises: 
Create Date: 2025-03-06 09:04:18.364596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a0d75b2b8e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('password', name=op.f('uq_user_password')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_question_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_question'))
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_answer_question_id_question')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_answer_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_answer'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    op.drop_table('question')
    op.drop_table('user')
    # ### end Alembic commands ###
