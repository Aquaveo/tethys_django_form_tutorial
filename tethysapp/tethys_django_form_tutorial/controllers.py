from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from tethys_sdk.permissions import login_required
from django_param.forms import ParamForm
from django.views.decorators.csrf import ensure_csrf_cookie
import param
import datetime as dt
import pandas as pd
import os


# Specify your param class
class MyParamString(param.Parameterized):
    favorite_quote = param.String(default="hello world!", doc="Your String")


class MyParamXYCoordinates(param.Parameterized):
    home_town = param.XYCoordinates(default=(-111.65, 40.23))


class MyParamDataFrame(param.Parameterized):
    dataset = param.DataFrame(pd.util.testing.makeDataFrame().iloc[:3])


class MyParamColor(param.Parameterized):
    color = param.Color(default='#FFFFFF')


class MyParamList(param.Parameterized):
    # list = param.List(default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    list = param.ListSelector(objects=["red", "yellow", "green", "blue"])


class MyParamSelectString(param.Parameterized):
    choose_color = param.ObjectSelector(default="yellow", objects=["red", "yellow", "green"])


class MyParamDate(param.Parameterized):
    datetime = param.Date(dt.datetime(2020, 1, 1, 0, 0, 0), bounds=(dt.datetime(2017, 1, 1, 0, 0, 0),
                                                                    dt.datetime(2021, 1, 1, 0, 0, 0)))
    date = param.CalendarDate(dt.date(2020, 1, 1))


class MyParamBoolean(param.Parameterized):
    enable_sprocket = param.Boolean(True, doc="A sample Boolean parameter")


class MyParamFileSelector(param.Parameterized):
    which_file = param.MultiFileSelector(path='*', precedence=0.5)


class MyParamMagnitude(param.Parameterized):
    r_squared = param.Magnitude(default=0.9)


class MyParamNumber(param.Parameterized):
    age = param.Number(49, bounds=(0, 100), doc="Any Number between 0 to 100")


@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {}

    return render(request, 'tethys_django_form_tutorial/home.html', context)


@login_required()
def param_boolean(request):
    """
    Controller for the app home page.
    """

    data_boolean = ""

    my_param = MyParamBoolean()

    form = ParamForm(param=my_param)

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
    data_datetime= ""
    my_param = MyParamDate()

    form = ParamForm(param=my_param)

    if request.POST:
        data_datetime = request.POST.get('datetime', '')
        data_date = request.POST.get('date', '')
    context = {
        'form': form,
        'data_date': data_date,
        'data_datetime': data_datetime,
    }

    return render(request, 'tethys_django_form_tutorial/Date.html', context)


@login_required()
def dataframe(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamDataFrame()

    form = ParamForm(param=my_param)
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

    form = ParamForm(param=my_param)

    if request.POST:
        data_color = request.POST.get('color', '')

    context = {
        'form': form,
        'data_color': data_color,
    }

    return render(request, 'tethys_django_form_tutorial/colorpicker.html', context)


@login_required()
def param_list(request):
    """
    Controller for the app home page.
    """

    data_list = ""

    my_param = MyParamList()

    form = ParamForm(param=my_param)

    if request.POST:
        data_list = request.POST.getlist('list', '')

    context = {
        'form': form,
        'data_list': data_list,
    }

    return render(request, 'tethys_django_form_tutorial/list.html', context)


@login_required()
def select_string(request):
    """
    Controller for the app home page.
    """

    data_select_string = ""

    my_param = MyParamSelectString()

    form = ParamForm(param=my_param)

    if request.POST:
        data_select_string = request.POST.get('select_string', '')

    context = {
        'form': form,
        'data_select_string': data_select_string,
    }

    return render(request, 'tethys_django_form_tutorial/select_string.html', context)


@login_required()
def multiple_files(request):
    """
    Controller for the app home page.
    """

    data_multiple_files = []

    my_param = MyParamFileSelector()

    form = ParamForm(param=my_param)

    if request.POST:
        data_multiple_files = request.POST.getlist('multiple_files', '')

    context = {
        'form': form,
        'data_multiple_files': data_multiple_files,
    }

    return render(request, 'tethys_django_form_tutorial/multiple_files.html', context)


@login_required()
def magnitude(request):
    """
    Controller for the app home page.
    """

    data_magnitude = ""

    my_param = MyParamMagnitude()

    form = ParamForm(param=my_param)

    if request.POST:
        data_magnitude = request.POST.get('magnitude', '')

    context = {
        'form': form,
        'data_magnitude': data_magnitude,
    }

    return render(request, 'tethys_django_form_tutorial/magnitude.html', context)


@login_required()
def number(request):
    """
    Controller for the app home page.
    """

    data_number = ""

    my_param = MyParamNumber()

    form = ParamForm(param=my_param)

    if request.POST:
        data_number = request.POST.get('number', '')

    context = {
        'form': form,
        'data_number': data_number,
    }

    return render(request, 'tethys_django_form_tutorial/number.html', context)


@login_required()
def param_string(request):
    """
    Controller for the app home page.
    """

    data_string = ""

    my_param = MyParamString()
    from django import forms
    from django.forms.widgets import Textarea

    widget_map = {
        param.parameterized.String:
            lambda po, p, name: forms.CharField(
                initial=po.inspect_value(name) or p.default,
                widget=Textarea,
            ),
    }

    form = ParamForm(param=my_param, widget_map=widget_map)

    if request.POST:
        data_string = request.POST.get('param_string', '')

    context = {
        'form': form,
        'data_string': data_string,
    }

    return render(request, 'tethys_django_form_tutorial/string.html', context)


@login_required()
def xy_coordinates(request):
    """
    Controller for the app home page.
    """

    data_xy_coordinates = ""

    my_param = MyParamXYCoordinates()

    form = ParamForm(param=my_param)

    if request.POST:
        data_xy_coordinates = request.POST.get('xy_coordinates', '')

    context = {
        'form': form,
        'data_xy_coordinates': data_xy_coordinates,
    }

    return render(request, 'tethys_django_form_tutorial/xy_coordinates.html', context)


@ensure_csrf_cookie
@login_required()
def all_supported(request):
    """
    Nathan's testing controller.
    """
    class MyParameterized(param.Parameterized):
        enable = param.Boolean(True, doc="A sample Boolean parameter")
        what_proportion = param.Magnitude(default=0.9)
        age = param.Number(49, bounds=(0, 100), doc="Any Number between 0 to 100")
        how_many = param.Integer()
        favorite_quote = param.String(default="Hello, world!")

        choose_file_or_folder = param.Path(search_paths='./')
        choose_folder = param.Foldername(search_paths="./")
        choose_file = param.Filename(search_paths="./")
        select_a_file = param.FileSelector(path='./*')
        select_multiple_files = param.MultiFileSelector(path='./*')

        favorite_color = param.ObjectSelector(default="green", objects=["red", "yellow", "green"])
        favorite_fruit = param.Selector(default="Apple", objects=["Orange", "Apple", "Mango"])
        select_multiple = param.ListSelector(default=[3, 5], objects=[1, 2, 3, 4, 5])

        birthday = param.CalendarDate(dt.date(2017, 1, 1), bounds=(dt.date(2017, 1, 1), dt.date(2017, 2, 1)))
        appointment = param.Date(dt.datetime(2017, 1, 1), bounds=(dt.datetime(2017, 1, 1), dt.datetime(2017, 2, 1)))
        least_favorite_color = param.Color(default='#FF0000')
        dataset = param.DataFrame(pd.util.testing.makeDataFrame().iloc[:3])

        this_strange_thing = param.Tuple(default=(1, 2.0, '3', 'Hello', False))
        some_numbers = param.NumericTuple(default=(1, 2, 3.0, 4.0))
        home_city = param.XYCoordinates(default=(-111.65, 40.23))
        bounds = param.Range(default=(-10, 10))

    my_param = MyParameterized()

    if request.method == 'POST':
        form = ParamForm(request.POST, param=my_param)
        if form.is_valid():
            message = 'Form is valid!'
            success = True
            the_param = form.as_param()
        else:
            message = 'Form is not valid!'
            success = False
            the_param = my_param
    else:
        message = 'Please submit the form.'
        success = None
        the_param = my_param
        form = ParamForm(param=my_param)

    context = {
        'form': form,
        'message': message,
        'success': success,
        'param': the_param
    }
    return render(request, 'tethys_django_form_tutorial/testing.html', context)
