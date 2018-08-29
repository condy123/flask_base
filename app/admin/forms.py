from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Regexp

from app.models import User


class LoginForm(FlaskForm):
    username = StringField(
        label="账号",
        validators=[
            DataRequired('请输入用户名'),
            Regexp('1[3458]\\d{9}', message='必须是手机号码')
        ],
        description="账号",

        # # 附加选项,会自动在前端判别
        # render_kw={
        #     "class": "form-control",
        #     "placeholder": "请输入账号!",
        #     "required": 'required'  # 表示输入框不能为空，并有提示信息
        # }

    )

    password = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码'),
            Length(6, 21, '密码长度是6到21')
        ],
        description="密码",

        # # 附加选项(主要是前端样式),会自动在前端判别
        # render_kw={
        #     "class": "form-control",
        #     "placeholder": "请输入密码!",
        #     "required": 'required' # 表示输入框不能为空
        # }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )



class RegForm(FlaskForm):

    username = StringField(
        label="账号",
        validators=[
            DataRequired('请输入用户名'),
            Regexp('1[3458]\\d{9}', message='必须是手机号码')
        ],
        description="账号",

        # # 附加选项,会自动在前端判别
        # render_kw={
        #     "class": "form-control",
        #     "placeholder": "请输入账号!",
        #     "required": 'required'  # 表示输入框不能为空，并有提示信息
        # }

    )

    password = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码'),
            Length(6, 21, '密码长度是6到21')
        ],
        description="密码",

        # # 附加选项(主要是前端样式),会自动在前端判别
        # render_kw={
        #     "class": "form-control",
        #     "placeholder": "请输入密码!",
        #     "required": 'required' # 表示输入框不能为空
        # }
    )

    password_re = PasswordField(
        # 标签
        label="确认密码",
        # 验证器
        validators=[
            DataRequired('请输入确认密码'),
            EqualTo('password', message="两次密码输入不一致")# 判断两次输入的密码是否一致
        ],
        description="确认密码",

        # # 附加选项(主要是前端样式),会自动在前端判别
        # render_kw={
        #     "class": "form-control",
        #     "placeholder": "请输入密码!",
        #     "required": 'required' # 表示输入框不能为空
        # }
    )

    submit = SubmitField(
        label="注册",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    logo = FileField(
        label='头像',
        validators=[
            DataRequired('请上传头像')
        ],
        description='头像',
    )

    def validate_username(self,field):
        """
        验证用户名是否存在  在forms里面 validate_xxxx (xxx标识要验证的字段，方法里面写对应的判断)
        判断有误则直接抛出异常，在html页面能直接显示错误信息
        :param field:
        """
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError('用户名已经存在')