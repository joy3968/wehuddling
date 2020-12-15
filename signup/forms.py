from django import forms
from admin.models import customer_tbl
from django.contrib.auth.models import User

# # 유저 폼
# class UserForm(forms.ModelForm):
#     re_password = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(attrs={'class': 'form-control'}),max_length=100)
#     class Meta:
#         model = User
#         fields = ('username', 'password','re_password')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'username':'아이디',
#             'password':'비밀번호'
#         }
#
#     # 유효성 검사
#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         re_password = cleaned_data.get('re_password')
#
#         # 비밀번호 중복
#         if password != re_password:
#             self.add_error('re_password','비밀번호가 다릅니다.')
#
#         # 비밀번호 8자 미만
#         if len(password) < 8:
#             self.add_error('re_password','비밀번호는 8자 이상입니다.')
#
#         # 아이디 중복
#         try:
#             User.objects.get(username=email)
#             self.add_error('username','이미 가입된 이메일입니다.')
#         except:
#             pass

# 아이디
class UserForm(forms.ModelForm):
    re_password = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                  max_length=100)
    class Meta:
        model = customer_tbl
        fields = ('username', 'password','re_password','c_name','c_phone')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'c_name': forms.TextInput(attrs={'class':'form-control'}),
            'c_phone': forms.TextInput(attrs={'class':'form-control'}),

        }

        labels = {
            'username' : '아이디',
            'password' : '비밀번호',
            'c_name' : '이름',
            'c_phone' : '휴대폰 번호',

        }