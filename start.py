#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'Entry file, all the start.'
__version__ = 'sdp1.1'

try:
  import sys,os,re
  from Core.public import genpasswd,read_conf
  from subprocess import call
except ImportError as Errmsg:
  print __file__,"import module failed, because %s" % Errmsg

CONF_NAME = 'sdp.conf'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_CONF = os.path.join(BASE_DIR, str(CONF_NAME))
APPS = ("mongodb", "mysql", "redis", "memcache", "tair")
WEBS = ("nginx", "tengine", "httpd", "lighttpd", "tomcat", "resin")

#get variables from sdp.conf, format is dict.
GLOBAL_CONF = read_conf(BASE_CONF, 'globals')
REDIS_CONF = read_conf(BASE_CONF, 'redis')
MYSQL_CONF = read_conf(BASE_CONF, 'mysql')
DOCKER_CONF = read_conf(BASE_CONF, 'docker')

#set global variables
LANG = GLOBAL_CONF['LANG']
SDP_HOME = GLOBAL_CONF['SDP_HOME']
SDP_DATA_HOME = GLOBAL_CONF['SDP_DATA_HOME']
SDP_USER_DATA_HOME = os.path.join(SDP_DATA_HOME, str(GLOBAL_CONF['SDP_USER_DATA_HOME']))
SDP_LOGS_DATA_HOME = os.path.join(SDP_DATA_HOME, str(GLOBAL_CONF['SDP_LOGS_DATA_HOME']))
SDP_UC = os.path.join(SDP_DATA_HOME, str(GLOBAL_CONF['SDP_UC']))

#set redis variables
REDIS_HOST = REDIS_CONF['host']
REDIS_PORT = REDIS_CONF['port']
REDIS_DB = REDIS_CONF['db']
REDIS_PASSWORD = REDIS_CONF['password']

#set mysql variables
MYSQL_HOST = MYSQL_CONF['host']
MYSQL_PORT = MYSQL_CONF['port']
MYSQL_DB = MYSQL_CONF['db']
MYSQL_USER = MYSQL_CONF['user']
MYSQL_PASSWORD = MYSQL_CONF['password']

#set docker variables
DOCKER_PUSH = DOCKER_CONF['Push']
DOCKER_IMG_PRE = DOCKER_CONF['Img_prefix']
DOCKER_TAG = DOCKER_CONF['TagRegistry']
DOCKER_REGISTRY = DOCKER_CONF['DockerRegistry']

def main(user):
  reload(sys)
  sys.setdefaultencoding(LANG)
  if not isinstance(user, (dict)):
    raise('Bae Parameter, ask dict.')

  if user_service in WEBS:
    call(['python ' + os.path.join(BASE_DIR, 'Web.py')], shell=True)
  elif user_service in APPS:
    call(['python ' + os.path.join(BASE_DIR, 'App.py')], shell=True)
  else:
    print "Unsupported service type."
    sys.exit(2)

if __name__ == "__main__":
  try:
    user_name = sys.argv[1]
    user_passwd = genpasswd()
    user_time = int(sys.argv[2])
    user_service = sys.argv[3]
    user_email = sys.argv[4]

    if not isinstance(user_name, (str)):
      raise TypeError('Bad Type, user_name ask string.')
      sys.exit(127)
 
    if not isinstance(user_service, (str)):
      raise TypeError('Bad Type, user_service ask string.')
      sys.exit(127)

    if not isinstance(user_time, (int)) or user_time <= 0:
      raise ValueError('Bad Value, demand is greater than 0 of the number.')
      sys.exit(127)

    if not isinstance(user_email, (str)):
      raise TypeError('Bad Type, user_email ask string.')
      sys.exit(127)

    if re.match(r'[a-zA-Z\_][0-9a-zA-Z\_]{0,19}', user_name) == None:
      print 'user_name illegal:A letter is required to begin with a letter or number, and the maximum number is 19.'
      sys.exit(1)

    if re.match(r'([0-9a-zA-Z\_*\.*\-*]+)@([a-zA-Z0-9\-*\_*\.*]+)\.([a-zA-Z]+$)', user_email) == None:
      print "Mail format error."
      sys.exit(129)

  except:
    print "\033[0;31;40mUsage:user time service email\033[0m"
    exit(1)
'''
  if user_name and user_passwd and user_time and user_service and user_email:
    user = {
      'NAME':user_name,
      'PASSWD':user_passwd,
      'SERVICE':user_service,
      'EMAIL':user_email
    }
  else:
    #print "\033[0;31;40mUsage:user time service email\033[0m"
    exit(1)

  #main()
'''
