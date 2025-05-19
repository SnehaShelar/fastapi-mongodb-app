from collections import OrderedDict
from fastapi import status, Response
import json
from fastapi.responses import JSONResponse

class ResponseHandler:
    """ Common Http response handler methods """

    @staticmethod
    def success(
            message: str = "",
            data: dict = {},
            headers: dict = {},
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status.HTTP_200_OK,
            status=True,
            data=data
        )
        response_dict.update(kwargs)
        return JSONResponse(
            content=response_dict,
            media_type="application/json",
            headers=headers)

    @staticmethod
    def bad_request(
            message: str = "",
            payload: dict = {},
            headers: dict = {},
            status_code: int = status.HTTP_400_BAD_REQUEST,
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            payload=payload
        )
        response_dict.update(kwargs)
        return Response(response_dict, status=status_code, headers=headers)

    @staticmethod
    def exception_response(
            message="",
            payload: dict = {},
            status_code: int = status.HTTP_400_BAD_REQUEST,
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            payload=payload
        )
        response_dict.update(kwargs)
        return Response(response_dict, status=status_code)

    @staticmethod
    def serializer_error(errors):
        if errors is not None:
            if isinstance(errors, list):
                prepared_response = []
                for error in iter(errors):
                    prepared_response.append(
                        ResponseHandler.change_error_format(error))
            else:
                prepared_response = ResponseHandler.change_error_format(errors)
            return prepared_response
        return errors

    def change_error_format(errors):
        """ Change in Error Formate """
        if hasattr(errors, 'items'):
            for key, value in errors.items():
                if isinstance(value, dict):
                    # nested dict
                    ResponseHandler.change_error_format(value)
                elif isinstance(value, list) \
                        and isinstance(value[0], dict) \
                        or isinstance(value, list) and \
                        len(value) > 1:
                    # list of dict
                    for nest_dict in value:
                        ResponseHandler.change_error_format(nest_dict)
                elif isinstance(value, list):
                    # remove list
                    errors[key] = errors[key][0]
        elif isinstance(errors, list) and len(errors) > 0:  # error in listre
            # remove list
            errors = ResponseHandler.change_error_format(errors[0])
        return errors

    @staticmethod
    def not_found(
            message: str = "",
            payload: dict = {},
            headers: dict = {},
            status_code: int = status.HTTP_404_NOT_FOUND,
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            payload=payload
        )
        response_dict.update(kwargs)
        return Response(response_dict, status=status_code, headers=headers)

    def unauthorized(
            message: str = "",
            payload: dict = {},
            headers: dict = {},
            status_code: int = status.HTTP_401_UNAUTHORIZED,
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            payload=payload
        )
        response_dict.update(kwargs)
        return JSONResponse(
        content=response_dict,
        media_type="application/json",
        headers=headers)
        # return Response(response_dict, status=status_code, headers=headers)

    @staticmethod
    def conflict(
            message: str = "",
            payload: dict = {},
            headers: dict = {},
            status_code: int = status.HTTP_409_CONFLICT,
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            payload=payload
        )
        response_dict.update(kwargs)
        return Response(response_dict, status=status_code, headers=headers)
