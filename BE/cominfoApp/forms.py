from .models import User
from django import forms

class MyUserForm(forms.ModelForm):
    # 필요한 필드 및 폼 위젯을 커스터마이즈합니다.
    # 회원명 필드를 커스터마이즈하기 위한 예시:
    name = forms.CharField(label='회원이름', max_length=100)

    class Meta:
        model = User
        fields = ('name', 'email', 'auth_state', 'sus_reason')
        widgets = {
            'auth_state': forms.Select(choices=User.AUTH_STATE_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 계정상태 필드를 드롭다운 메뉴로 변경하기 위한 예시:
        self.fields['auth_state'].widget = forms.Select(choices=[('정지', '정지'), ('정상', '정상')])
        # 거래 목록을 표시하기 위한 예시:
        # transactions = self.instance.transactions.all()
        # self.fields['transactions'].widget = forms.TextInput(attrs={'readonly': True, 'value': transactions})

    def clean(self):
        cleaned_data = super().clean()
        # 필요한 유효성 검사 로직을 작성합니다.

        return cleaned_data