from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from django_param.forms import ParamForm
import param
import datetime as dt
import pandas as pd


class MyParamDataFrame(param.Parameterized):
    dataframe = param.DataFrame(pd.util.testing.makeDataFrame().iloc[:3])


class MyParamColor(param.Parameterized):
    color = param.Color(default='#FFFFFF')


class MyParamSelectString(param.Parameterized):
    select_string = param.ObjectSelector(default="yellow", objects=["red", "yellow", "green"])


class MyParamDate(param.Parameterized):
    date = param.Date(dt.datetime(2017, 1, 1), bounds=(dt.datetime(2017, 1, 1), dt.datetime(2017, 2, 1)))


class MyParamBoolean(param.Parameterized):
    boolean = param.Boolean(True, doc="A sample Boolean parameter")
    # int_list = param.ListSelector(default=[3, 5], objects=[1, 3, 5, 7, 9], precedence=0.5)


class MyParamFileSelector(param.Parameterized):
    multiple_files = param.MultiFileSelector(path='*', precedence=0.5)


@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    data_int_list = ""
    data_boolean = ""

    my_param = MyParamBoolean()

    form = ParamForm(param_class=my_param)

    if request.POST:
        data_int_list = request.POST.get('int_list', '')
        data_boolean = request.POST.get('boolean', '')

    context = {
        'form': form,
        'data_int_list': data_int_list,
        'data_boolean': data_boolean,
    }

    return render(request, 'tethys_django_form_tutorial/home.html', context)


@login_required()
def param_boolean(request):
    """
    Controller for the app home page.
    """

    data_int_list = ""
    data_boolean = ""

    my_param = MyParamBoolean()

    form = ParamForm(param_class=my_param)

    if request.POST:
        data_boolean = request.POST.get('boolean', '')

    context = {
        'form': form,
        'data_boolean': data_boolean,
    }

    return render(request, 'tethys_django_form_tutorial/boolean.html', context)

@login_required()
def date_selection(request):
    """
    Controller for the app home page.
    """

    data_date = ""

    my_param = MyParamDate()

    form = ParamForm(param_class=my_param)

    if request.POST:
        data_date = request.POST.get('date', '')

    context = {
        'form': form,
        'data_date': data_date,
    }

    return render(request, 'tethys_django_form_tutorial/Date.html', context)


@login_required()
def dataframe(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamDataFrame()

    form = ParamForm(param_class=my_param)
    data_a, data_b, data_c, data_d = "", "", "", ""
    if request.POST:
        data_a = request.POST.getlist('A', '')
        data_b = request.POST.getlist('B', '')
        data_c = request.POST.getlist('C', '')
        data_d = request.POST.getlist('D', '')

    context = {
        'form': form,
        'data_a': data_a,
        'data_b': data_b,
        'data_c': data_c,
        'data_d': data_d,
    }

    return render(request, 'tethys_django_form_tutorial/dataframe.html', context)


@login_required()
def colorpicker(request):
    """
    Controller for the app home page.
    """

    data_color = ""

    my_param = MyParamColor()

    form = ParamForm(param_class=my_param)

    if request.POST:
        data_color = request.POST.get('color', '')

    context = {
        'form': form,
        'data_color': data_color,
    }

    return render(request, 'tethys_django_form_tutorial/colorpicker.html', context)


@login_required()
def select_string(request):
    """
    Controller for the app home page.
    """

    data_select_string = ""

    my_param = MyParamSelectString()

    form = ParamForm(param_class=my_param)

    if request.POST:
        data_select_string = request.POST.get('select_string', '')

    context = {
        'form': form,
        'data_select_string': data_select_string,
    }

    return render(request, 'tethys_django_form_tutorial/select_string.html', context)


@login_required()
def file_selector(request):
    """
    Controller for the app home page.
    """

    data_multiple_files = []

    my_param = MyParamFileSelector()

    form = ParamForm(param_class=my_param)

    if request.POST:
        data_multiple_files = request.POST.getlist('multiple_files', '')

    context = {
        'form': form,
        'data_multiple_files': data_multiple_files,
    }

    return render(request, 'tethys_django_form_tutorial/file_selector.html', context)
