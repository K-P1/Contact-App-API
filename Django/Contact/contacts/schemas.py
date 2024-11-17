from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

create_contact_schema = extend_schema(
        responses={
            201: OpenApiResponse(
                description="Success message when contact is created.",
                examples={"message": "Contact created"},
            ),
            400: OpenApiResponse(
                description="Error message when contact is not created.",
                examples={"error": "Contact not created"},
            ),
        },
    )

get_contact_schema = extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                description='Identifier used to find a contact. Can be a phone number, name, or email.',
                required=False,
                type=str,
                location=OpenApiParameter.PATH,
            )
        ],
        responses={
            200: OpenApiResponse(
                description="Success message when contact is found.",
                examples={"message": "Contact found"},
            ),
            404: OpenApiResponse(
                description="Error message when contact is not found.",
                examples={"error": "Contact not found"},
            ),
        },
    )

update_contact_schema = extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                description='Identifier used to find a contact. Can be a phone number, name, or email.',
                required=True,
                type=str,
                location=OpenApiParameter.PATH,
            )
        ],
        responses={
            200: OpenApiResponse(
                description="Success message when contact is updated.",
                examples={"message": "Contact updated"},
            ),
            400: OpenApiResponse(
                description="Error message when contact is not updated.",
                examples={"error": "Contact not updated"},
            ),
            404: OpenApiResponse(
                description="Error message when contact is not found.",
                examples={"error": "Contact not found"},
            ),
        },
    )

delete_contact_schema = extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                description='Identifier used to find a contact. Can be a phone number, name, or email.',
                required=False,
                type=str,
                location=OpenApiParameter.PATH,
            )
        ],
        responses={
            200: OpenApiResponse(
                description="Success message when contact is deleted.",
                examples={"message": "Contact deleted"},
            ),
            404: OpenApiResponse(
                description="Error message when contact is not found.",
                examples={"error": "Contact not found"},
            ),
        },
    )