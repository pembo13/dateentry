import datetime
from django import forms
from django.conf import settings
from django.shortcuts import render



class TimeEntryForm(forms.Form):

	at = forms.TimeField(label='Happened At', required=True)

	pass


def entry(request):
	is_valid = False

	time_format = settings.TIME_INPUT_FORMATS[-1]  # last format
	example_dt = datetime.datetime.now()
	example_dt_formatted = example_dt.strftime(time_format)

	if request.method == 'POST':
		form = TimeEntryForm(request.POST)

		if form.is_valid():
			is_valid = True
			pass
		pass
	else:
		form = TimeEntryForm(initial={
			'at': example_dt_formatted,
		})

	return render(request, 'entry.html', {
		'form': form,

		'is_valid': is_valid,

		'example_dt': example_dt,
		'example_dt_formatted': example_dt_formatted,
		'time_format': time_format,
	})

