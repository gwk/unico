
from bisect import bisect
from itertools import chain

from . import abbreviated_planes, intersect_coalesced_ranges
from .categories import unicode_categories, unicode_category_aliases
from .data_09_00 import blocks, category_ranges


def is_code_in_charset(code, charset):
  p = (code, code)
  i = bisect(charset, p)
  if i < len(charset):
    s, e = charset[i]
    if s <= code < e: return True
  p0, p1 = charset[i - 1] if i > 0 else (0, 0)
  return i > 0 and code < charset[i - 1][1]


def _gen_charsets():
  charsets = {}

  # categories.
  for cat in unicode_categories:
    if cat.subs:
      charsets[cat.key] = tuple(sorted(chain(*(category_ranges[k] for k in cat.subs))))
    else:
      charsets[cat.key] = category_ranges[cat.key]
  # add aliases in a second pass to reuse range values by reference.
  for name, cat in unicode_category_aliases.items():
    if name in charsets: continue
    charsets[name] = charsets[cat.key]

  # blocks.
  for k, r in blocks.items():
    charsets[k] = (r,)

  # planes.
  for k, plane in abbreviated_planes.items():
    charsets[k] = plane

  # Control characters. Note that 'Cc' also includes 0x7F (DEL).
  charsets['C0'] = ((0x0000, 0x0020),)
  charsets['C1'] = ((0x0080, 0x00A0),)

  # Ascii.
  charsets['Ascii'] = ((0x00, 0x80),)
  charsets['A'] = charsets['Ascii']

  return charsets

unicode_charsets = _gen_charsets()

