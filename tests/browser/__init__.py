# Copyright Action Without Borders, Inc., the Alfajor authors and contributors.
# All rights reserved.  See AUTHORS.
#
# This file is part of 'alfajor' and is distributed under the BSD license.
# See LICENSE for more details.

from alfajor import WebBrowser


browser = WebBrowser()
browser.configure_in_scope('self-tests')
