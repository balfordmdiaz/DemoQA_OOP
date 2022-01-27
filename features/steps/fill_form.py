from behave import *

@given(u'go to the url')
def step_impl(context):
    context.driver.get(context.webQA)


@given(u'insert the firstname "{fname}", lastname "{lname}", email "{email}"')
def step_impl(context, fname, lname, email):
    context.demoQA.fill_first_name(fname)
    context.demoQA.fill_last_name(lname)
    context.demoQA.fill_email(email)


@given(u'select gender')
def step_impl(context):
    context.demoQA.select_gender()


@given(u'insert mobile "{phone}", date, subjects')
def step_impl(context, phone):
    context.demoQA.fill_number(phone)
    context.demoQA.select_date_birth()
    context.demoQA.select_subjects()


@given(u'insert hobbies, upload the Profile picute and the address "{address}"')
def step_impl(context, address):
    context.demoQA.select_hobbies()
    context.demoQA.upload_picture()
    context.demoQA.insert_address(address)


@given(u'select state "{state}" and city "{city}"')
def step_impl(context, state, city):
    context.demoQA.select_state(state)
    context.demoQA.select_city(city)

@then(u'submit form')
def step_impl(context):
    context.demoQA.submit_form()