"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from MEDSAFE.UI.base import base_page
from rxconfig import config
from .pages1.about import about_page
from .pages1.pricing import pricing_page
from .pages1.contact import contact_page
from .navigation import routes







class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"
    def handle_input_change(self, val):
        self.label = val
    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.input(default_value=State.label, on_change=State.handle_input_change),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
            id="vstack_range",
        )
        
    )
    


app = rx.App()
app.add_page(index)
app.add_page(about_page, route=routes.ABOUT_ROUTE)
app.add_page(pricing_page, route =routes.PRICING_ROUTE)
app.add_page(contact_page, route=routes.CONTACT_ROUTE)

