from behave import when, use_step_matcher

use_step_matcher('parse')


@when("a GET request to {url} is made")
def step_impl(context, url):
    context.response = context.client.http.get(url)
