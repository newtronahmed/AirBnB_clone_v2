#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['100.26.220.252', '54.209.204.18']
env.user = 'ubuntu'


def do_deploy(archive_path):
        """Deploy web files to server
        """
        try:
                if not (os.path.exists(archive_path)):
                        return False

                timestamp = archive_path[-17:-4]
                if os.getenv("run_local", None) is None:
                        os.environ["run_local"] = "True"
                        local('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                        local('sudo tar -zxf {} -C /data/web_static/releases/web_static_{}'.format(archive_path, timestamp))

                        #local('sudo mv -f /data/web_static/releases/web_static_{}/web_static/* \
#/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))
                        #local('sudo rm -rf /data/web_static/releases/\
#web_static_{}/web_static'
                    #.format(timestamp))

                        local('sudo rm -rfR /data/web_static/current')
                        local('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(timestamp))
                # upload archive
                put(archive_path, '/tmp/')

                # create target dir
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # uncompress archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # move contents into host web_static
                #run('sudo mv -f /data/web_static/releases/web_static_{}/web_static/* \
#/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # remove extraneous web_static dir
                #run('sudo rm -rf /data/web_static/releases/\
#web_static_{}/web_static'
                   # .format(timestamp))

                # delete pre-existing sym link
                run('sudo rm -rf /data/web_static/current')

                # re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # return True on success
        return True
