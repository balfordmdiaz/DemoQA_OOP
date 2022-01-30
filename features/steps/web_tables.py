from behave import *

@given(u'select elements')
def step_impl(context):
    context.wtbl.select_element_option()


@given(u'select web tables')
def step_impl(context):
    context.wtbl.select_webtables()


@given(u'edit one register of the list')
def step_impl(context):
    context.wtbl.select_element_to_edit()


@given(u'insert firstname "{firstname}" and lastname "{lastname}"')
def step_impl(context, firstname, lastname):
    context.wtbl.edit_first_name(firstname)
    context.wtbl.edit_last_name(lastname)


@given(u'insert email "{mail}" and age')
def step_impl(context, mail):
    context.wtbl.edit_email(mail)
    context.wtbl.edit_age()


@given(u'insert salary and department "{depart}"')
def step_impl(context, depart):
    context.wtbl.edit_salary()
    context.wtbl.edit_department(depart)


@given(u'submit the modified register')
def step_impl(context):
    context.wtbl.save_modification()


@then(u'validate the register')
def step_impl(context):
    context.wtbl.select_element_to_edit()