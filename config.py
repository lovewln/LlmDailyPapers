# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')

# The repository to add this issue to
REPO_OWNER = 'lovewln'
REPO_NAME = 'LlmDailyPapers'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["large language model", "llm"]


OPENAI_API_KEYS = [os.getenv('OPENAI_API_KEY')]
LANGUAGE = "zh"  # zh | en
