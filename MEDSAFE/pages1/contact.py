import reflex as rx
from ..UI.base import base_page
import navigation

@rx.pages1(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    # About Page (Index)
    return base_page(
        
        rx.vstack(
            rx.heading("Contact Us", size="9"),
            
            rx.text(
                "Just trying out this new web coding called reflex!"
            ),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
            id="vstack_range",
        )
        
    )
    

