# -*- coding: utf-8 -*-
#
# This file is part of Invenio-Previewer-ISPY
# Copyright (C) 2014 CERN
#
# Invenio-Previewer-ISPY is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio-Previewer-ISPY is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio-Previewer-ISPY; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from flask import render_template, request

def can_preview(f):
    """Return ``True`` if filetype can be previewed."""
    return f.superformat == '.ig'


def preview(f):
    """Return appropiate template and passes the file and an embed flag."""
    return render_template("previewer/ispy.html", f=f,
                           embed=request.args.get('embed', type=bool))
