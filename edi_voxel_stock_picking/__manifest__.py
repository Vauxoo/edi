# Copyright 2019 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Voxel stock picking",
    "summary": "Sends stock picking report to Voxel.",
    "version": "12.0.1.0.0",
    "category": "Warehouse Management",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/oca/edi/",
    "license": "AGPL-3",
    "depends": [
        "edi_voxel",
        "sale_stock",
        "product_supplierinfo_for_customer",
    ],
    "data": [
        "views/report_voxel_picking.xml",
        "views/stock_picking_views.xml",
        "views/res_company_view.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
}
