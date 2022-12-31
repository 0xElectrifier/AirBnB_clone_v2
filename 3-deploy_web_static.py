#!/usr/bin/python3
"""Fabric script that defines a function 'deploy'"""
from os.path import exists
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """Creates and distributes an archive to your my server"""
    archive_path = do_pack()
    if not exists(archive_path):
        return False

    ret = do_deploy(archive_path)
    return (ret)
