import platform
import os

print("System Information")
print("------------------")
print("OS:", platform.system())
print("Release:", platform.release())
print("Python Version:", platform.python_version())
print("Current Directory:", os.getcwd())
