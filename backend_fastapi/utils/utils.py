def calc_offset(page: int, limit: int):
    return (page - 1) * limit if page else 0
