from json import loads

from behave import use_step_matcher, step, then
from jsonpath_ng import parse
from pytest import fail

use_step_matcher("parse")


@then("the REST response is successful")
def step_impl(context):
    status_code = context.response.status_code
    assert 200 <= status_code < 299, f'Received status: {status_code}'


@step("{value:cast} is in the path {path}")
def step_impl(context, value, path):
    expresion = parse(path)

    if not hasattr(context, 'body'):
        context.body = {
            'data': context.response.data
        }

    result = expresion.find(context.body)

    if not isinstance(result, list) or len(result) == 0:
        fail(f"""
Expected value: {value}
Actual value: {result}
Response: {context.body}
        """)

    result = result[0].value
    assert result == value, f"""
Expected value: {value}
Actual value: {result}
Response: {context.body}
    """


@step("{path} is not empty")
def step_impl(context, path):
    expresion = parse(path)

    body = loads(context.response.render().content)

    result = expresion.find(body)[0].value

    assert result is not None, f'Path: {result}'


@then("the response is a bad requested")
def step_impl(context):
    status_code = context.response.status_code

    assert 400 <= status_code < 499, f'Status code: {status_code}'


@step("there is {amount:cast} items in the path {path}")
def step_impl(context, amount, path):
    expresion = parse(path)
    result = expresion.find(context.body)

    assert len(result) == amount, f"""
Actual amount: {len(result)}
Expected amount: {amount},
    """
