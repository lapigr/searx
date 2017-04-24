'''
searx is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

searx is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with searx. If not, see < http://www.gnu.org/licenses/ >.

(C) 2015 by Adam Tauber, <asciimoo@gmail.com>
'''
from flask_babel import gettext
import re
name = "Pig search criteria handlers"
description = gettext('Try to handle mail tracking numbers properly')
default_on = True


# Self User Agent regex
p = re.compile('[0-9]{20,}')


# attach callback to the post search hook
#  request: flask request object
#  ctx: the whole local context of the pre search hook
def post_search(request, search):
    if search.search_query.pageno > 1:
        return True
    if p.match(search.search_query.query):
        search.result_container.answers.clear()
        search.result_container.answers.add('track')
    return True
