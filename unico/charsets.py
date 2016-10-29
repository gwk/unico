
from bisect import bisect
from itertools import chain

from . import abbreviated_planes, intersect_sorted_ranges
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

  def add(name, abbr, *ranges):
    charsets[name] = tuple(ranges)
    if abbr: charsets[abbr] = charsets[name]

  # Ascii.
  add('Ascii', 'A', (0x00, 0x80))
  Ascii = charsets['Ascii']

  for cat in unicode_categories:
    ranges = tuple(intersect_sorted_ranges(Ascii, charsets[cat.name]))
    if not ranges: continue
    add('Ascii_' + cat.name, 'A' + cat.key, *ranges)

  # Control characters. Note that 'Cc' also includes 0x7F (DEL).
  add('Control_0', 'C0', (0x0000, 0x0020))
  add('Control_1', 'C1', (0x0080, 0x00A0))

  # Common numeric sets for programming languages.
  add('Binary',   None, (0x30, 0x32))
  add('Octal',    None, (0x30, 0x38))
  add('Decimal',  None, (0x30, 0x3A)) # remove as redundant with Ascii_Number?
  add('Hexadecimal', 'Hex', (0x30, 0x3A), (0x41, 0x47), (0x61, 0x67))

  return charsets

unicode_charsets = _gen_charsets()

