import sys
import collections
import itertools
print(f"you are currently using python {sys.winver}")

print("BUILTIN MODULES")
for module in sys.builtin_module_names:
    print(module)
print(f"You are currently using Windows {sys.getwindowsversion()[0]}")
print(sys.getallocatedblocks())

print(collections.__all__)
for i in zip(li, li2):
    print(i)