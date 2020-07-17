from tethys_sdk.base import TethysAppBase, url_map_maker


class TethysDjangoFormTutorial(TethysAppBase):
    """
    Tethys app class for Tethys Django Form with Param Tutorial.
    """

    name = 'Tethys Django Form with Param Tutorial'
    index = 'tethys_django_form_tutorial:home'
    icon = 'tethys_django_form_tutorial/images/icon.gif'
    package = 'tethys_django_form_tutorial'
    root_url = 'tethys-django-form-tutorial'
    color = '#d35400'
    description = 'Demonstrate how to use django form with param'
    tags = 'tutorial'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='tethys-django-form-tutorial',
                controller='tethys_django_form_tutorial.controllers.home'
            ),
            UrlMap(
                name='date',
                url='date',
                controller='tethys_django_form_tutorial.controllers.date_selection'
            ),
            UrlMap(
                name='dataframe',
                url='dataframe',
                controller='tethys_django_form_tutorial.controllers.dataframe'
            ),
            UrlMap(
                name='colorpicker',
                url='colorpicker',
                controller='tethys_django_form_tutorial.controllers.colorpicker'
            ),
            UrlMap(
                name='select_string',
                url='select_string',
                controller='tethys_django_form_tutorial.controllers.select_string'
            ),
            UrlMap(
                name='file_selector',
                url='file_selector',
                controller='tethys_django_form_tutorial.controllers.file_selector'
            ),
        )

        return url_maps