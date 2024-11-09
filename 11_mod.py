import inspect
def introspection_info(obj):
    info = {}
    info['Type'] = type(obj).__name__

    info['Attributes'] = [attribute for attribute in dir(obj) if callable(getattr(obj, attribute))]

    info['Methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    module = inspect.getmodule(obj)
    if module:
        info['Module'] = module.__name__

    if isinstance(obj, (int, float)):
        info['Value'] = obj


    return info



number_info = introspection_info(42)

print(number_info)

