'''
lapig pig@lapig.xyz
'''
from flask_babel import gettext
import re
name = "Pig search criteria handlers"
description = gettext('Try to handle mail tracking numbers properly')
default_on = True


# Match long numbers
p = re.compile('[0-9]{20,}')


# attach callback to the post search hook
#  request: flask request object
#  ctx: the whole local context of the pre search hook
def post_search(request, search):
    if search.search_query.pageno > 1:
        return True
    if p.match(search.search_query.query):
        search.result_container.answers.clear()
        search.result_container.answers.add('uspstrack')
    return True
