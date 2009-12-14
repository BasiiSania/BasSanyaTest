'''DATABASE_NAME = 'C:\Documents and Settings\Ingusik\BasSanyaTest\mysite\mydb.db'             # Or path to database file if using sqlite3.
TEMPLATE_DIRS = ('C:/Documents and Settings/Ingusik/BasSanyaTest/mysite/Templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)'''
'''
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)
DEBUG_TOOLBAR_PANELS = (
	'debug_toolbar.panels.timer.TimerDebugPanel',
	'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
	'debug_toolbar.panels.headers.HeaderDebugPanel',
	'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
	'debug_toolbar.panels.template.TemplateDebugPanel',
	'debug_toolbar.panels.sql.SQLDebugPanel',
	'debug_toolbar.panels.cache.CacheDebugPanel',
	'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
}'''