# Copyright (c) 2021, Libracore AG and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
    ]

def get_data(filters):
    return data
