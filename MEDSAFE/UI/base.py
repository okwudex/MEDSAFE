
import reflex as rx

from .navbar import navbar, navbar_link

def base_page(child: rx.Component) -> rx.Component:
    return ( 
        rx.fragment(
            navbar(),
            child,
            rx.color_mode.button(position="bottom-left", id="lights-colours-id"),
            rx.logo(),
        )
     )

