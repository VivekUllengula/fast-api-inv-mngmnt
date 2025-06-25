from fastapi import HTTPException, status

class ItemNotFoundException(Exception):
    pass

class ItemAlreadyExistsException(Exception):
    pass

def item_not_found_exception():
    return HTTPException (
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Item not found."
    )

def item_already_exists_exception():
    return HTTPException(
        status_code= status.HTTP_400_BAD_REQUEST,
        detail = " Item ID already exists"
    )
