# Outputs a list of all models of the project
from django.core.management.base import AppCommand
from optparse import make_option


class Command(AppCommand):

    option_list = AppCommand.option_list + (
        make_option('--count', action = 'store_true', dest = 'count',
            default = False,
            help ='Add object count information'),
    )
    help = 'Prints model names for projects \
         applications and optional object count.'

    requires_model_validation = True

    def handle(self, *app, **options):
        from django.db.models import get_models, get_apps
        lines = []
        app_list = get_apps()
        for ap in app_list:
            lines.append("--------------------")
            lines.append("%s" % str(ap))
            lines.append("-----------------------------\
                          -----------------------------")
            for model in get_models(ap):
                lines.append("[%s]" % model.__name__ + (options["count"] and\
                    " - %s objects" % model._default_manager.count() or ""))
        return "\n".join(lines)
