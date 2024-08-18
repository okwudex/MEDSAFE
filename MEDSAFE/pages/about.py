import reflex as rx
from ..UI.base import base_page

def index() -> rx.Component:
    # About Page (About Us)
    return base_page(
        
        rx.vstack(
            rx.heading('ABOUT US', size="9"),
            
            rx.text(
                "We are a new web development company just trying things out.",
                
            ),
            
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
            id="vstack_range",
        )
        
    )
    
