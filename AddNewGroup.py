# -*- coding: utf-8 -*-

from training.application import Application
from group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username='admin', password="secret")
    app.create_group(Group(name="Test_1", header="Test group_1", footer="test footer_1"))
    app.logout()


def test_add_empty_group(app):
    app.login( username='admin', password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


