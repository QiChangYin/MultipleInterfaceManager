from django.db import models

from HttpApiManager.managers import UserTypeManager, UserInfoManager, ProjectInfoManager, ModuleInfoManager, \
    TestCaseInfoManager, EnvInfoManager


# Create your models here.


class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'


class UserType(BaseTable):
    class Meta:
        verbose_name = '用户类型'
        db_table = 'UserType'

    type_name = models.CharField(max_length=20)
    type_desc = models.CharField(max_length=50)
    objects = UserTypeManager()


class UserInfo(BaseTable):
    class Meta:
        verbose_name = '用户信息'
        db_table = 'UserInfo'

    username = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=20)
    email = models.EmailField('邮箱')
    status = models.IntegerField('有效/无效', default=1)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    objects = UserInfoManager()


class ProjectInfo(BaseTable):
    # meta是指定数据库的名字
    class Meta:
        verbose_name = '项目信息'
        db_table = 'ProjectInfo'

    project_name = models.CharField('项目名称', max_length=50)
    responsible_name = models.CharField('负责人', max_length=20)
    test_user = models.CharField('测试人员', max_length=100)
    dev_user = models.CharField('开发人员', max_length=100)
    publish_app = models.CharField('发布应用', max_length=60)
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)
    objects = ProjectInfoManager()


class ModuleInfo(BaseTable):
    class Meta:
        verbose_name = '模块信息'
        db_table = 'ModuleInfo'

    module_name = models.CharField('模块名称', max_length=50)
    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    test_user = models.CharField('测试负责人', max_length=50)
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)
    objects = ModuleInfoManager()

  # def __str__(self):
  #   """返回模型的字符串表示"""
  #   return self.text

class TestCaseInfo(BaseTable):
    class Meta:
        verbose_name = '用例信息'
        db_table = 'TestCaseInfo'

    type = models.IntegerField('test/config', default=1)
    name = models.CharField('用例/配置名称', max_length=50)
    belong_project = models.CharField('所属项目', max_length=50)
    # # 表示外键关联到作者表,当作者表删除了该条数据,图书表中不删除,仅仅是把外键置空
    # CASCADE: 这就是默认的选项，级联删除，你无需显性指定它。
    # PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
    # SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank = True, null = True, 定义该字段的时候，允许为空。
    # SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
    # SET(): 自定义一个值，该值当然只能是对应的实体了
    belong_module = models.ForeignKey(ModuleInfo, on_delete=models.CASCADE)
    include = models.CharField('包含config/test', max_length=500, null=True)
    author = models.CharField('编写人员', max_length=20)
    request = models.TextField('请求信息')
    objects = TestCaseInfoManager()


class TestReports(BaseTable):
    class Meta:
        verbose_name = "测试报告"
        db_table = 'TestReports'

    report_name = models.CharField(max_length=40)
    start_at = models.CharField(max_length=40, null=True)
    status = models.BooleanField()
    testsRun = models.IntegerField()
    successes = models.IntegerField()
    reports = models.TextField()


class EnvInfo(BaseTable):
    class Meta:
        verbose_name = '环境管理'
        db_table = 'EnvInfo'

    env_name = models.CharField(max_length=40)
    base_url = models.CharField(max_length=40)
    simple_desc = models.CharField(max_length=50)
    objects = EnvInfoManager()


class DebugTalk(BaseTable):
    class Meta:
        verbose_name = '驱动py文件'
        db_table = 'DebugTalk'
    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    debugtalk = models.TextField()


class TestSuite(BaseTable):
    class Meta:
        verbose_name = '用例集合'
        db_table = 'TestSuite'

    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    suite_name = models.CharField(max_length=100)
    include = models.TextField()
