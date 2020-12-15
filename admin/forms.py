from django import forms
from admin.models import *

class GoodsForm(forms.ModelForm):
    class Meta:
        model = goods_tbl

        fields = ['cp_no', 'gd_category', 'gd_name', 'gd_price', 'gd_stock', 'gd_desc']

        widgets = {
            # 거래처 일련번호
            'cp_no': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            # 카테고리
            'gd_category': forms.Select(attrs={'class': 'form-control', 'placeholder' : '(명)','rows': 5}),
            # 상품 명
            'gd_name': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            # 상품 가격
            'gd_price': forms.TextInput(attrs={'class': 'form-control' ,'rows': 5, 'placeholder' : '(단위 : 원)'}),
            # 재고
            'gd_stock': forms.TextInput(attrs={'class': 'form-control', 'id' : 'date-text', 'rows': 5}),
            # 상품 설명
            'gd_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

        }

        labels = {
            # 거래처 일련번호지만 거래처 명을 표시(DB엔 거래처 일련번호를 저장)
            'cp_no': '거래처 명',
            # 카테고리
            'gd_category': '카테 고리',
            # 상품 명
            'gd_name': '상품 명',
            # 상품 가격
            'gd_price': '상품 가격(단위 : 원)',
            # 재고
            'gd_stock': '상품 재고',
            # 상품 설명
            'gd_desc': '상품 설명',
        }


class ShipperForm(forms.ModelForm):
    class Meta:
        model = shipper_tbl

        fields = ['sp_name', 'sp_phone', 'sp_city', 'sp_borough']

        widgets = {
            # 배송인 이름
            'sp_name': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            # 배송인 휴대폰번호
            'sp_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : '휴대폰 번호를 입력 해 주세요','rows': 5}),
            # 담당 지역
            'sp_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'ex)서울, 경기','rows': 5}),
            # 담당 시
            'sp_borough': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'ex)성남시 / 서울일 경우 구를 입력 ex)강남구', 'rows': 5}),

        }

        labels = {
            'sp_name': '배송인 이름',
            # 휴대전화 번호
            'sp_phone': '휴대폰 번호',
            # 담당 구역(지역)
            'sp_city': '담당 구역(지역)',
            # 담당 구역(시)
            'sp_borough': '담당 구역(시)',
        }