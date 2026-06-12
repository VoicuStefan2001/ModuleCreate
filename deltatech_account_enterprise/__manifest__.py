# ©  2008-2022 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Deltatech Account Enterprise",
    "version": "15.0.0.0.0",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "summary": "AccountEnterprise",
    "category": "Generic Modules",
    "depends": ["account", "web_dashboard", "account_accountant"],
    "license": "OPL-1",
    "price": 15.00,
    "currency": "EUR",
    "data": ["report/account_statement_report_view.xml", "security/ir.model.access.csv"],
    "images": ["static/description/main_screenshot.png"],
    "development_status": "Mature",
    "maintainers": ["dhongu"],
    "auto_install": ["account", "web_dashboard"],
    "assets": {
        "web.assets_qweb": [
            "deltatech_account_enterprise/static/src/xml/**/*",
        ],
    },
    "qweb": ["static/src/xml/template.xml"],
}
