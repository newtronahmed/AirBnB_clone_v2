#!/usr/bin/python3
"""A fabric configuration module to manage static web deployment

This module contain a function do_pack that bundles and compresses
all content of the web_static to  version folder
"""
import os
import fabric.api as api
from datetime import datetime
from pathlib import Path


def do_pack():
    """Bundles convert the contents of web_static directory to tgz
    """
    version_dir = Path('./versions')
    if not version_dir.exists():
        os.mkdir(version_dir)
    now = datetime.now()

    # absolute path to the compressed file
    file_name = version_dir / "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second)
    try:
        api.local("tar -zcvf {} -C web_static .".format(file_name.absolute()))
        return str(file_name.absolute())
    except Exception:
        return None
