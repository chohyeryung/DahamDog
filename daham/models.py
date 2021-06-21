from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    #일반 user
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('올바른 이메일을 입력해주세요')
        if not nickname:
            raise ValueError('닉네임을 입력해주세요')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(default='', max_length=200, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)

    # 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # 사용자의 username field는 nickname으로
    USERNAME_FIELD = 'email'
    #필수 작성 field
    REQUIRED_FIELDS = ['email', 'nickname']

    def __str__(self):
        return self.nickname

# class User(models.Model): 유저 모델
#     name = models.CharField(max_length=200, verbose_name='이름')
#     email = models.EmailField(max_length=128, verbose_name='이메일')
#     password = models.CharField(max_length=64, verbose_name='비밀번호')


class Board(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()
    # deadline = models.DateTimeField(input_formats=['%Y/%m/%d %H:%M:%S'])
    end_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Application(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    created_date = models.DateTimeField(auto_now_add=True)