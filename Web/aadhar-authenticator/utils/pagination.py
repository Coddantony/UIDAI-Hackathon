DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100


def normalize_page(page: int = 1, limit: int = DEFAULT_PAGE_SIZE):
    page = max(1, int(page))
    limit = min(MAX_PAGE_SIZE, max(1, int(limit)))
    return page, limit
