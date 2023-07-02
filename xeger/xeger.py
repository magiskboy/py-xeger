"""Library to generate random strings from regular expressions.
Code borrowed and cleaned up from the python module rstr:
https://bitbucket.org/leapfrogdevelopment/rstr/

In turn inspired by the Java library Xeger:
http://code.google.com/p/xeger/
"""
from typing import Dict, Any, Callable, Union, List, Optional
import re
import sys
import string
import itertools
from random import Random

py_version = sys.version_info

if py_version.minor < 11:
    import sre_parse           # type: ignore

elif py_version == 11 and py_version.releaselevel != 'final':
    sre_parse = re.sre_parse   # type: ignore

else:
    sre_parse = re._parser     # type: ignore


class Xeger:
    def __init__(self, limit: Optional[int] = 10, seed: Optional[Any] = None):
        self._limit = limit or 10
        self._cache: Dict[str, str] = dict()

        self._random = Random()
        self.random_choice = self._random.choice
        self.random_int = self._random.randint
        if seed:
            self.seed(seed)

        self._alphabets: Dict[str, str] = {
            'printable': string.printable,
            'letters': string.ascii_letters,
            'uppercase': string.ascii_uppercase,
            'lowercase': string.ascii_lowercase,
            'digits': string.digits,
            'punctuation': string.punctuation,
            'nondigits': string.ascii_letters + string.punctuation,
            'nonletters': string.digits + string.punctuation,
            'whitespace': string.whitespace,
            'nonwhitespace': string.printable.strip(),
            'normal': string.ascii_letters + string.digits + ' ',
            'word': string.ascii_letters + string.digits + '_',
            'nonword': ''.join(set(string.printable)
                            .difference(string.ascii_letters +
                                        string.digits + '_')),
            'postalsafe': string.ascii_letters + string.digits + ' .-#/',
            'urlsafe': string.ascii_letters + string.digits + '-._~',
            'domainsafe': string.ascii_letters + string.digits + '-'
        }

        self._categories: Dict[str, Callable] = {
            "category_digit": lambda: self._alphabets['digits'],
            "category_not_digit": lambda: self._alphabets['nondigits'],
            "category_space": lambda: self._alphabets['whitespace'],
            "category_not_space": lambda: self._alphabets['nonwhitespace'],
            "category_word": lambda: self._alphabets['word'],
            "category_not_word": lambda: self._alphabets['nonword'],
        }

        self._cases: Dict[str, Callable] = {
            "literal": lambda x: chr(x),
            "not_literal":
                lambda x: self.random_choice(string.printable.replace(chr(x), '')),
            "at": lambda x: '',
            "in": lambda x: self._handle_in(x),
            "any": lambda x: self.random_choice(string.printable.replace('\n', '')),
            "range": lambda x: [chr(i) for i in range(x[0], x[1] + 1)],
            "category": lambda x: self._categories[str(x).lower()](),
            'branch':
                lambda x: ''.join(self._handle_state(i) for i in self.random_choice(x[1])),
            "subpattern": lambda x: self._handle_group(x),
            "assert": lambda x: ''.join(self._handle_state(i) for i in x[1]),
            "assert_not": lambda x: '',
            "groupref": lambda x: self._cache[x],
            'min_repeat': lambda x: self._handle_repeat(*x),
            'max_repeat': lambda x: self._handle_repeat(*x),
            'negate': lambda x: [False],
        }

    def xeger(self, regex: Union[str, re.Pattern]) -> str:
        if isinstance(regex, str):
            pattern = regex
        elif isinstance(regex, re.Pattern):
            pattern = regex.pattern
        else:
            raise TypeError("regex must be string or re.Pattern")

        parsed = sre_parse.parse(pattern)
        result = self._build_string(parsed)
        self._cache.clear()
        return result

    @property
    def random(self):
        return self._random

    @random.setter
    def random(self, random_instance: Random):
        self._random = random_instance
        self.random_choice = self._random.choice
        self.random_int = self._random.randint

    def seed(self, seed: Any):
        self._random.seed(seed)

    def _build_string(self, parsed) -> str:
        newstr: List[str] = []
        for state in parsed:
            newstr.append(self._handle_state(state))
        return ''.join(newstr)

    def _handle_state(self, state) -> str:
        opcode, value = state
        return self._cases[str(opcode).lower()](value)

    def _handle_group(self, value: List[str]) -> str:
        result = ''.join(self._handle_state(i) for i in value[3])
        if value[0]:
            self._cache[value[0]] = result
        return result

    def _handle_in(self, value) -> str:
        candidates = list(itertools.chain(*(self._handle_state(i) for i in value)))
        if candidates[0] is False:
            candidates = set(string.printable).difference(candidates[1:])
            return self.random_choice(list(candidates))
        else:
            return self.random_choice(candidates)

    def _handle_repeat(self, start_range: int, end_range: int, value) -> str:
        result = []
        end_range = min(end_range, self._limit)
        times = self.random_int(start_range, max(start_range, end_range))
        for i in range(times):
            result.append(''.join(self._handle_state(i) for i in value))
        return ''.join(result)
