from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render
from django import forms

class CodeForm(forms.Form):
	code=forms.CharField(label='code',max_length=100)

def home(request):
	if request.method=='POST':
		form=CodeForm(request.POST)
		if form.is_valid():
			code=form.cleaned_data['code']
			exec code
			return render(request,'template.html',{'code':code,'result':result})
	form=CodeForm()
	return render(request,'template.html',{'form':form})
