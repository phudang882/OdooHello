{
    'name': 'Construntion Manager',  # This is the name of your module
    'version': '1.0',
    'summary': ' Construction company manager',
    'sequence': -101,
    'description': """
        This module allows users to manage documents with proper access control
        and synchronization mechanisms.
    """,
    'category': 'Productivity',
    'author': 'Phu Dang Kim',
    'license': 'LGPL-3',
    'website': '',
    'depends': ['base','hr'],  # Other modules this depends on
    'data': [
        'security/group_rule.xml',
        'security/ir.model.access.csv',
        'views/document.xml',
        # 'views/employee.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}