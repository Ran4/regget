#!/usr/bin/env python3
from typing import Optional, Any, Tuple
import re

def first_group_or_none(pattern, value) -> Optional[Any]:
    match = re.match(pattern, value)
    if not match:
        return None
    try:
        return match.group(1)
    except IndexError:
        return None
    
def all_groups_or_none(pattern, value) -> Optional[Tuple]:
    match = re.match(pattern, value)
    if not match:
        return None

    try:
        return match.groups() or None
    except IndexError:
        return None
