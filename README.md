A tiny python module containing helpful wrappers around the built-in `re` module.

## Example:

```python
>>> import regget
>>> regget.first_group_or_none("CO-(\d+)", "CO-43")
"43"
>>> regget.all_groups_or_none("(A)(\d+)(B)", "A43B")
("A", "43", "B")
>>> regget.all_groups_or_none("(A)(\d+)(B)", "???")
None
>>>
>>> from functools import partial
>>> PATTERN = "CO-(\d+)"
>>> grab_number = partial(regget.first_group_or_none, PATTERN)
>>> document_names = ["CO-3", "CO-9", "CO-12"]
>>> valid_numbers = [grab_number(s) for s in document_names]
>>> print(valid_numbers)
"3", "9", "12"
```
