from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

# 此用户选项是官方默认通过UserAdmin这个类注册到后台的，那么我们也引入进来，后面继承这个类
from django.contrib.auth.admin import UserAdmin

# 引入我们定义的模型
from .models import UserProfile

# 先取消关联注册User
admin.site.unregister(User)

# 定义关联对象的样式，stackedInline为纵向排列每一行，TabularInline为并排排列每一行
class UserProfileInline(admin.StackedInline):
    model = UserProfile  # 关联的模型
    
# 开始继承UserAdmin,关联UserProfile
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline] 

# 注册User模型
admin.site.register(User,UserProfileAdmin)