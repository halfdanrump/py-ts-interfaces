# Stubs for astroid.interpreter._import.spec (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc
from collections import namedtuple
from typing import Any, Optional

ModuleType: Any

_ModuleSpec = namedtuple('_ModuleSpec', 'name type location origin submodule_search_locations')

class ModuleSpec(_ModuleSpec):
    def __new__(cls, name: Any, module_type: Any, location: Optional[Any] = ..., origin: Optional[Any] = ..., submodule_search_locations: Optional[Any] = ...): ...

class Finder(metaclass=abc.ABCMeta):
    def __init__(self, path: Optional[Any] = ...) -> None: ...
    @abc.abstractmethod
    def find_module(self, modname: Any, module_parts: Any, processed: Any, submodule_path: Any) -> Any: ...
    def contribute_to_path(self, spec: Any, processed: Any) -> None: ...

class ImpFinder(Finder):
    def find_module(self, modname: Any, module_parts: Any, processed: Any, submodule_path: Any): ...
    def contribute_to_path(self, spec: Any, processed: Any): ...

class ExplicitNamespacePackageFinder(ImpFinder):
    def find_module(self, modname: Any, module_parts: Any, processed: Any, submodule_path: Any): ...
    def contribute_to_path(self, spec: Any, processed: Any): ...

class ZipFinder(Finder):
    def __init__(self, path: Any) -> None: ...
    def find_module(self, modname: Any, module_parts: Any, processed: Any, submodule_path: Any): ...

class PathSpecFinder(Finder):
    def find_module(self, modname: Any, module_parts: Any, processed: Any, submodule_path: Any): ...
    def contribute_to_path(self, spec: Any, processed: Any): ...

def find_spec(modpath: Any, path: Optional[Any] = ...): ...