from fastapi import HTTPException, status

class ItemNotFoundException(Exception):
    pass

def item_not_found_exception():
    return HTTPException (
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Account not found."
    )
