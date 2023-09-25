# -*- coding: UTF-8 -*-
from . import dbModel
from constants import FRONT_CATEGORY_CACHE, UrlReTypes, OnClick, SITE_CONFIG_CACHE, CategoryTypes
from models.relation_cls import ModelRelationCLS
from modules import import_module_name

CategoryModule = import_module_name(SITE_CONFIG_CACHE.project_name, 'CategoryModule')


class CategoryModel(dbModel):
    """前端栏目"""
    __tablename__ = 'category_table'
    uuid = dbModel.UUIDField()
    id = dbModel.IDField()
    index = dbModel.IDField()
    category_name = dbModel.StringField('名称')
    statu = dbModel.StringField('栏目状态')
    show_statu = dbModel.BooleanField('显示', default=1, true_text='是', false_text='否')
    url_path = dbModel.StringField('路径', nullable=False)
    title = dbModel.StringField('标题', nullable=False)
    upper_uuid = dbModel.StringField('上级栏目')
    keywords = dbModel.StringField('关键词', nullable=False)
    keyword1 = dbModel.StringField('关键词1')
    keyword2 = dbModel.StringField('关键词2')
    keyword3 = dbModel.StringField('关键词3')
    keyword4 = dbModel.StringField('关键词4')
    keyword5 = dbModel.StringField('关键词5')
    description = dbModel.StringField('描述', nullable=False)
    click_count = dbModel.IntegerField('访问量', default=0)
    template = dbModel.StringField('模版文件', nullable=False)
    bind_module = dbModel.DictField('处理模块', dict_cls=CategoryModule, is_index=True)
    category_code = dbModel.StringField('栏目代码', nullable=False)
    _create_time = dbModel.DateTimeField('创建时间', nullable=False)
    category_re = dbModel.StringField('栏目匹配正则', nullable=False)
    page_re = dbModel.StringField('栏目分页匹配正则', nullable=False)
    article_re = dbModel.StringField('文章匹配正则', nullable=False)
    placed_top = dbModel.BooleanField('置顶', nullable=False)
    intro = dbModel.TextField('栏目介绍')
    category_img = dbModel.ImagesField('栏目图片')
    category_type = dbModel.DictField('栏目类型', dict_cls=CategoryTypes, nullable=False)
    @classmethod
    def update_menus(cls):
        if FRONT_CATEGORY_CACHE:
            for _c_k in list(FRONT_CATEGORY_CACHE.keys()):
                FRONT_CATEGORY_CACHE.pop(_c_k)
        menu_groups = CategoryModel.find_many({'upper_uuid': ''}, sort=[['index', 1]])
        for group in menu_groups:
            group['downers'] = cls.find_many({'upper_uuid': group.get('uuid')}, sort=[['index', 1]])
            FRONT_CATEGORY_CACHE[group.get('uuid')] = group
    @classmethod
    def edit_field_sort(cls):
        return ['category_name', 'url_path', 'title', 'description', 'click_count', 'keywords', 'keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5', 'template', 'category_re', 'page_re', 'article_re', 'bind_module', 'intro', 'category_img', 'category_type']


class UrlPathReModel(dbModel):
    """前端路径正则"""
    __tablename__ = 'url_path_re_table'
    uuid = dbModel.UUIDField(onclick=OnClick.SHOW_CONTENT, show_total=True)
    url_path_re = dbModel.StringField('正则匹配规则', text_align='text-left')
    name = dbModel.StringField('名称')
    re_type = dbModel.DictField('匹配类型', dict_cls=UrlReTypes, nullable=False)
    bind_uuid = ModelRelationCLS.category_uuid('栏目名称')
    @classmethod
    def field_sort(cls):
        return ['uuid', 'name', 'url_path_re', 're_type', 'bind_uuid']
    @classmethod
    def field_search(cls):
        return ['bind_uuid', 're_type', 'name']


class FrontCacheModel(dbModel):
    __tablename__ = 'front_cache_table'
    uuid = dbModel.UUIDField()
    cache_key = dbModel.StringField('缓存KEY')

