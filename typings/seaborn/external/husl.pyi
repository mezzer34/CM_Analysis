"""
This type stub file was generated by pyright.
"""

__version__ = ...
m = ...
m_inv = ...
refX = ...
refY = ...
refZ = ...
refU = ...
refV = ...
lab_e = ...
lab_k = ...
def husl_to_rgb(h, s, l): # -> list[Unknown | float]:
    ...

def husl_to_hex(h, s, l): # -> str:
    ...

def rgb_to_husl(r, g, b): # -> list[float | Unknown | Any]:
    ...

def hex_to_husl(hex): # -> list[float | Unknown | Any]:
    ...

def huslp_to_rgb(h, s, l): # -> list[Unknown | float]:
    ...

def huslp_to_hex(h, s, l): # -> str:
    ...

def rgb_to_huslp(r, g, b): # -> list[float | Unknown | Any]:
    ...

def hex_to_huslp(hex): # -> list[float | Unknown | Any]:
    ...

def lch_to_rgb(l, c, h): # -> list[Unknown | float]:
    ...

def rgb_to_lch(r, g, b): # -> list[float | Unknown | Any]:
    ...

def max_chroma(L, H): # -> float:
    ...

def max_chroma_pastel(L): # -> float:
    ...

def dot_product(a, b): # -> Any | int:
    ...

def f(t): # -> float:
    ...

def f_inv(t): # -> float:
    ...

def from_linear(c): # -> float:
    ...

def to_linear(c): # -> float:
    ...

def rgb_prepare(triple): # -> list[Unknown]:
    ...

def hex_to_rgb(hex): # -> list[float]:
    ...

def rgb_to_hex(triple): # -> str:
    ...

def xyz_to_rgb(triple): # -> list[Unknown | float]:
    ...

def rgb_to_xyz(triple): # -> list[Any | int]:
    ...

def xyz_to_luv(triple): # -> list[float] | list[float | Unknown]:
    ...

def luv_to_xyz(triple): # -> list[float] | list[Unknown | float]:
    ...

def luv_to_lch(triple): # -> list[Unknown | float]:
    ...

def lch_to_luv(triple): # -> list[Unknown]:
    ...

def husl_to_lch(triple): # -> list[int | float | Unknown] | list[float | Unknown] | list[Unknown]:
    ...

def lch_to_husl(triple): # -> list[Unknown | float] | list[Unknown]:
    ...

def huslp_to_lch(triple): # -> list[int | float | Unknown] | list[float | Unknown] | list[Unknown]:
    ...

def lch_to_huslp(triple): # -> list[Unknown | float] | list[Unknown]:
    ...

