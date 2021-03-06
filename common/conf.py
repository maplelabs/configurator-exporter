"""
*******************
*Copyright 2017, MapleLabs, All Rights Reserved.
*
********************
"""

COLLECTDBIN = '/opt/collectd/sbin/collectd'
CollectdPluginDestDir = '/opt/collectd/plugins'
CollectdPluginConfDir = '/opt/collectd/conf'
CollectdConfDir = '/opt/collectd/etc'
TEMPLATE_DIR = 'config_handler/templates'
ConfigDataDir = 'config_handler/data'
RESP_NOERROR = 200
EXPORTER_PORT = 8000
LEVEL = 'DEBUG'
EXPORTERLOGPATH = 'log'
LOGFILE = 'configurator_exporter.log'
FORMATTER = '[*(asctime)s-*(filename)s:*(name)s:*(lineno)s-*(funcName)s()] -*(levelname)s: *(message)s'
STATS_DATADIR = "/opt/collectd/var/lib/data"
FluentdPluginConfDir = "/etc/td-agent"
