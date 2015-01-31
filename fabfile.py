from fabric.api import *
import os

SITE_BUILD_DIR = os.path.abspath(os.path.join(os.getcwd(), "build"))
BASE_URL = "http://tomo.inkandfeet.com/"
SCP_TARGET = os.environ["SCP_TARGET"]


def build():
    local("./fgallery photos build")


def deploy_site():
    local("rsync -avz -e ssh --progress %s/ %s" % (SITE_BUILD_DIR, SCP_TARGET,))


def deploy():
    build()
    deploy_site()
