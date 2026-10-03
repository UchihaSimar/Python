"""
Master Guide: Python Function Call Mechanics, Packing, and Unpacking
====================================================================
This executable guide covers parameter types, function signatures,
var-positional (*args), var-keyword (**kwargs), and argument unpacking rules.
"""

def master_func(
    p_only,              # 1. Positional-Only (must come before '/')
    /, 
    pos_or_kw,           # 2. Positional or Keyword
    default_pos=10,      # 3. Positional or Keyword with Default
    *args,               # 4. Variable Positional Arguments (packs remaining pos args into a tuple)
    kw_only,             # 5. Keyword-Only Parameter (must come after '*')
    default_kw=20,       # 6. Keyword-Only with Default
    **kwargs             # 7. Variable Keyword Arguments (packs remaining kw args into a dict)
):
    """
    Demonstrates every parameter classification in Python syntax.
    
    Order of Parameters in Definition:
    1. Positional-only parameters (before /)
    2. Positional-or-keyword parameters
    3. *args
    4. Keyword-only parameters (after * or *args)
    5. **kwargs
    """
    print("\n--- Execution Trace ---")
    print(f"  [p_only]      Positional-Only:          {p_only!r}")
    print(f"  [pos_or_kw]   Positional/Keyword:       {pos_or_kw!r}")
    print(f"  [default_pos] Positional w/ Default:    {default_pos!r}")
    print(f"  [*args]       Extra Positional Tuple:   {args!r}")
    print(f"  [kw_only]     Keyword-Only:             {kw_only!r}")
    print(f"  [default_kw]  Keyword-Only w/ Default:  {default_kw!r}")
    print(f"  [**kwargs]    Extra Keyword Dict:       {kwargs!r}")


# ----------------------------------------------------------------------
# 1. Standard Function Call & Unpacking Examples
# ----------------------------------------------------------------------

def run_demonstrations():
    print("=== Master Function Calling Pattern ===")
    
    # Sequence to unpack into positional arguments (*)
    extra_pos = [100, 200, 300]
    
    # Dictionary to unpack into keyword arguments (**)
    extra_kw = {"custom_flag": True, "user_role": "admin"}

    # Full Master Call
    master_func(
        "Positional_1",   # p_only
        "Positional_2",   # pos_or_kw
        99,               # default_pos (overrides default 10)
        *extra_pos,       # Unpacked into args -> (100, 200, 300)
        kw_only="ValueX", # kw_only (required keyword arg)
        **extra_kw        # Unpacked into kwargs -> {'custom_flag': True, 'user_role': 'admin'}
    )


# ----------------------------------------------------------------------
# 2. Key Edge Cases & Common Traps
# ----------------------------------------------------------------------

def mutable_default_trap(item, target=[]):
    """
    TRAP: Mutable Default Arguments.
    `target=[]` is evaluated ONCE when the function is defined, not per call.
    """
    target.append(item)
    return target


def safe_default_pattern(item, target=None):
    """
    SOLUTION: Use None as default for mutable types.
    """
    if target is None:
        target = []
    target.append(item)
    return target


def dictionary_unpacking_behavior():
    """
    Unpacking a dict with * vs **
    """
    data = {"a": 1, "b": 2}
    
    # Unpacking with * extracts KEYS
    keys = [*data]  # ['a', 'b']
    
    # Unpacking with ** merges DICTIONARIES
    merged = {**data, "c": 3, "a": 99}  # {'a': 99, 'b': 2, 'c': 3}
    
    return keys, merged


if __name__ == "__main__":
    run_demonstrations()
    
    print("\n=== Demonstrating Mutable Default Trap ===")
    print("Call 1:", mutable_default_trap(1))  # [1]
    print("Call 2:", mutable_default_trap(2))  # [1, 2] (retained previous call state!)
    
    print("\n=== Safe Mutable Pattern ===")
    print("Call 1:", safe_default_pattern(1))  # [1]
    print("Call 2:", safe_default_pattern(2))  # [2]
    
    print("\n=== Dictionary Unpacking ===")
    keys, merged = dictionary_unpacking_behavior()
    print("Keys extracted using *:", keys)
    print("Merged dict using **:", merged)