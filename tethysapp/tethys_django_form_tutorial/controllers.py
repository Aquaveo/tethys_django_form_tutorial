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
    favorite_quote = param.String(default="hello world!", doc="Empty String is not allowed", allow_None=False)


class MyParamXYCoordinates(param.Parameterized):
    home_town = param.XYCoordinates(default=(-111.65, 40.23))
    my_numeric_tuples = param.NumericTuple(default=(1, 2, 3))


class MyParamDataFrame(param.Parameterized):
    dataset = param.DataFrame(pd.util.testing.makeDataFrame().iloc[:3])


class MyParamColor(param.Parameterized):
    color = param.Color(default='#FFFFFF')


class MyParamList(param.Parameterized):
    selector = param.Selector(objects=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    choose_color = param.ObjectSelector(default="yellow", objects=["red", "yellow", "green"])
    choose_multiple_color = param.ListSelector(default=['red', 'yellow'], objects=["red", "yellow", "green", "blue"])


class MyParamDate(param.Parameterized):
    datetime = param.Date(dt.datetime(2020, 1, 1, 0, 0, 0), bounds=(dt.datetime(2017, 1, 1, 0, 0, 0),
                                                                    dt.datetime(2021, 1, 1, 0, 0, 0)))
    date = param.CalendarDate(dt.date(2020, 1, 1))


class MyParamBoolean(param.Parameterized):
    enable_sprocket = param.Boolean(True, doc="A sample Boolean parameter", allow_None=True)


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

    my_param = MyParamBoolean()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/boolean.html', context)


@login_required()
def date_selection(request):
    """
    Controller for the app home page.
    """
    my_param = MyParamDate()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/Date.html', context)


@login_required()
def dataframe(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamDataFrame()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/dataframe.html', context)


@login_required()
def colorpicker(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamColor()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/colorpicker.html', context)


@login_required()
def param_list(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamList()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/list.html', context)


@login_required()
def select_string(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamFileSelector()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/select_string.html', context)


@login_required()
def multiple_files(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamFileSelector()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/multiple_files.html', context)


@login_required()
def magnitude(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamMagnitude()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/magnitude.html', context)


@login_required()
def number(request):
    """
    Controller for the app home page.
    """

    my_param = MyParamNumber()

    context = get_context(request, my_param)
    return render(request, 'tethys_django_form_tutorial/number.html', context)


@login_required()
def param_string(request):
    """
    Controller for the app home page.
    """

    data_string = ""

    from django import forms
    from django.forms.widgets import Textarea

    widget_map = {
        param.parameterized.String:
            lambda po, p, name: forms.CharField(
                initial=po.inspect_value(name) or p.default,
                widget=Textarea,
            ),
    }

    my_param = MyParamString()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/string.html', context)


@login_required()
def xy_coordinates(request):
    """
    Controller for the app home page.
    """
    my_param = MyParamXYCoordinates()

    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/xy_coordinates.html', context)


@ensure_csrf_cookie
@login_required()
def all_supported(request):
    """
    Nathan's testing controller.
    """
    class MyParameterized(param.Parameterized):
        enable = param.Boolean(True, doc="A sample Boolean parameter", allow_None=True)
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

        this_strange_thing = param.Tuple(default=(False,), allow_None=True)
        some_numbers = param.NumericTuple(default=(1, 2, 3.0, 4.0))
        home_city = param.XYCoordinates(default=(-111.65, 40.23))
        bounds = param.Range(default=(-10, 10))

    my_param = MyParameterized()
    context = get_context(request, my_param)

    return render(request, 'tethys_django_form_tutorial/testing.html', context)


def get_context(request, my_param):
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
    return context
