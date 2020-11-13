#!/usr/bin/env python

import os

for var_name in [
        'CI', 'CIRCLECI', 'CIRCLE_BRANCH', 'CIRCLE_BUILD_NUM', 'CIRCLE_BUILD_URL', 'CIRCLE_JOB',
        'CIRCLE_NODE_INDEX', 'CIRCLE_NODE_TOTAL']:
    print(var_name, os.environ.get(var_name, None))
