def GarbageCollection(_global: dict) -> None:
    for variable in list(_global):
        if str(variable).startswith("TEMP_"):
            del _global[variable]
