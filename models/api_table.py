# -*- coding: utf-8 -*-
from . import dbModel
from .relation_cls import ModelRelationCLS
from modules import import_module_name
from constants import SITE_CONFIG_CACHE

API_MODULE = import_module_name(SITE_CONFIG_CACHE.project_name, 'ApiModule')


class ApiModel(dbModel):
    """API表"""
    __tablename__ = 'app_account_table'
    uuid = dbModel.UUIDField(btn_show=True)
    name = dbModel.StringField('api名称', nullable=False)
    statu = dbModel.BooleanField('api状态', default=1, true_text='启用', false_text='停用', nullable=False)
    bind_module = dbModel.DictField('处理模块', dict_cls=API_MODULE, nullable=False, placeholder='选择处理模块')
    api_url = dbModel.StringField('API路径')
    _current_date = dbModel.DateTimeField('当前日期')
    note = dbModel.StringField('备注')
    @classmethod
    def field_search(cls):
        return ['statu', 'bind_module', 'name', 'note']
    @classmethod
    def field_sort(cls):
        return ['name', 'statu', 'bind_module', 'api_url', 'note']
    @classmethod
    def add_field_sort(cls):
        return ['name', 'api_url', 'bind_module', 'note']
    @classmethod
    def edit_field_sort(cls):
        return cls.add_field_sort()


class ApiCallLogModel(dbModel):
    """API调用日志"""
    __tablename__ = 'api_call_log_table'
    uuid = dbModel.UUIDField()
    ip = ModelRelationCLS.ip
    api_uuid = ModelRelationCLS.api_uuid('API名称', nullable=False)
    statu = dbModel.BooleanField('调用状态', default=1, true_text='成功', false_text='失败')
    note = dbModel.StringField('备注')
    req_data = dbModel.StringField('请求数据')
    _create_time = dbModel.DateTimeField('调用时间', nullable=False, show_total=True)
    @classmethod
    def field_sort(cls):
        return ['_create_time', 'ip', 'api_uuid', 'statu', 'note']
    @classmethod
    def field_search(cls):
        return ['api_uuid', 'statu', 'ip', '_create_time']


