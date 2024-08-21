import reflex as rx
from ..UI.base import base_page

def about_page() -> rx.Component:
    # About Page (Index)
    return base_page(
        
        rx.vstack(
            rx.heading("About Us", size="9"),
            
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
    

