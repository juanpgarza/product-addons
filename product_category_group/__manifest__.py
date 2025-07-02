# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Category Group",
    "summary": "",
    "version": "17.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/juanpgarza/product-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
                "product",
                "stock",
            ],
    "data": [
        'views/product_category_group_views.xml',
        'views/product_category_views.xml',        
        'security/ir.model.access.csv',        
        ],
    "installable": False,
}
