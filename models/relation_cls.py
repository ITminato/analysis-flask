# -*- coding: utf-8 -*-
from . import dbModel
from constants import OnClick


class ModelRelationCLS(object):

    ip = dbModel.IPField('ip', href='https://www.baidu.com/baidu?wd=%s&ie=utf-8', onclick=OnClick.JUMP_HREF, is_index=True)

    @classmethod
    def admin_uuid(cls, field_name='管理员uuid', **kwargs):
        return dbModel.RelationField(
            field_name,
            relation_collection='cms_user_table',
            relation_show_field='telephone',
            is_index=True,
            dbref='cms_user_table.uuid',
            **kwargs
        )

    @classmethod
    def api_uuid(cls, field_name='API UUID', **kwargs):
        return dbModel.RelationField(
            field_name,
            relation_collection='app_account_table',
            relation_show_field='name',
            is_index=True,
            **kwargs
        )

    @classmethod
    def category_uuid(cls, field_name='栏目名称', **kwargs):
        return dbModel.RelationField(
            field_name,
            relation_collection='category_table',
            relation_show_field='category_name',
            is_index=True,
            **kwargs
        )

    @classmethod
    def article_uuid(cls, field_name='文章名称', **kwargs):
        return dbModel.RelationField(
            field_name,
            relation_collection='article_table',
            relation_show_field='title',
            is_index=True,
            **kwargs
        )

    @classmethod
    def tags(cls, field_name='标签'):
        return dbModel.RelationField(
            field_name,
            relation_collection='tags_table',
            relation_show_field='text',
            target_relation_collection='article_tag_relation',
            localField='tag_uuid',
            foreignField='uuid',
        )

    @classmethod
    def keyword_category_uuid(cls, field_name='关键词分类', **kwargs):
        return dbModel.RelationField(
            field_name,
            relation_collection='keyword_category_table',
            relation_show_field='name',
            is_index=True,
            **kwargs
        )
