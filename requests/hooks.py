# -*- coding: utf-8 -*-

"""
requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``args``:
    A dictionary of the arguments being sent to Request().

``pre_request``:
    The Request object, directly before being sent.

``post_request``:
    The Request object, directly after being sent.

``response``:
    The response generated from a Request.

"""

import warnings
import collections


def dispatch_hook(key, hooks, hook_data):
    """Dipatches a hook dictionary on a given peice of data."""

    hooks = (hooks or {}).get(key, [])
    hooks = hooks if isinstance(hooks, collections.Iterable) else [hooks]

    for hook in hooks:
        try:
            hook_data = hook(hook_data) or hook_data
        except Exception, why:
            warnings.warn(str(why))

    return hook_data
