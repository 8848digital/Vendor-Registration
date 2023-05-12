from . import __version__ as app_version

app_name = "vendor_registration"
app_title = "Vendor Registration"
app_publisher = "Deepak Kumar"
app_description = "Vendor can register based on that supplier/customer will be created. We will have workflow based field value update of Supplier/Customer."
app_email = "deepakkumar@8848digital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vendor_registration/css/vendor_registration.css"
# app_include_js = "/assets/vendor_registration/js/vendor_registration.js"

# include js, css files in header of web template
# web_include_css = "/assets/vendor_registration/css/vendor_registration.css"
# web_include_js = "/assets/vendor_registration/js/vendor_registration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "vendor_registration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Supplier": "public/js/supplier_custom.js",
    "Customer": "public/js/customer_custom.js",
    "Item": "public/js/item_custom.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
fixtures = [
    {
        "doctype": "Workflow",
        "filters": {
            "name": ["in", 
            [
                "Supplier Registration Workflow", "Supplier Update Approval Workflow",
                "Customer Registration Workflow", "Customer Update Approval Workflow",
                "Item Registration Workflow", "Item Update Approval Workflow",
            ]
            ]
        },
    },
]
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "vendor_registration.utils.jinja_methods",
#	"filters": "vendor_registration.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "vendor_registration.install.before_install"
# after_install = "vendor_registration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "vendor_registration.uninstall.before_uninstall"
# after_uninstall = "vendor_registration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vendor_registration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
    "Supplier": {
        "after_insert": "vendor_registration.utils.link_update_supplier"
    },
    "Customer": {
        "after_insert": "vendor_registration.utils.link_update_customer"
    },
    "Item": {
        "after_insert": "vendor_registration.utils.link_update_item"
    }
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"vendor_registration.tasks.all"
#	],
#	"daily": [
#		"vendor_registration.tasks.daily"
#	],
#	"hourly": [
#		"vendor_registration.tasks.hourly"
#	],
#	"weekly": [
#		"vendor_registration.tasks.weekly"
#	],
#	"monthly": [
#		"vendor_registration.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "vendor_registration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "vendor_registration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "vendor_registration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["vendor_registration.utils.before_request"]
# after_request = ["vendor_registration.utils.after_request"]

# Job Events
# ----------
# before_job = ["vendor_registration.utils.before_job"]
# after_job = ["vendor_registration.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"vendor_registration.auth.validate"
# ]