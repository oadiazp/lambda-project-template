from chalice.test import Client
from behave import register_type, use_fixture

from app import app


def parse_int(string):
    return int(string)


register_type(int=parse_int)


def cast(string):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            return string


register_type(cast=cast)


def get_client(context, *args, **kwargs):
    if not hasattr(context, 'client'):
        context.client = Client(app)

    yield context.client


def before_feature(context, feature):
    use_fixture(get_client, context)


def use_fixture_by_tag(tag, context, fixture_registry):
    _, fixture_name = tag.split('.')
    fixture_data = fixture_registry.get(fixture_name, None)
    if fixture_data is None:
        raise LookupError("Unknown fixture-tag: %s" % tag)

    fixture_func = fixture_data
    return use_fixture(fixture_func, context)
