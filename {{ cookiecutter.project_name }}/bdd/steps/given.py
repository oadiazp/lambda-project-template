from json import loads
from behave import use_step_matcher, given


use_step_matcher("parse")


@given("mock the method {method} with the response")
def step_impl(context, method):
    context.enable_mocking = True
    context.mocking_class_path = method
    context.mocking_response = loads(context.text)
