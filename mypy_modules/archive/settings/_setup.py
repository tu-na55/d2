from setuptools import setup

setup()

# => setup.cfg
# setup(
#     name="パッケージの名前",
#     version="1.0.0",
#     install_requires=["packageA", "packageB"],
#     extras_require={
#         "develop": ["dev-packageA", "dev-packageB"]
#     },
#     entry_points={
#         "console_scripts": [
#             "foo = package_name.module_name:func_name",
#             "foo_dev = package_name.module_name:func_name [develop]"
#         ],
#         "gui_scripts": [
#             "bar = gui_package_name.gui_module_name:gui_func_name"
#         ]
#     }
# )
