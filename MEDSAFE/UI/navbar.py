import reflex as rx
from ..navigation import routes, NavState


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar_searchbar_desktop() -> rx.Component:
    return rx.desktop_only(
            rx.hstack(
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Search...",
                    type="search",
                    size="2",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        bg=rx.color("accent", 3),
        #padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        #width="100%",
        ),
        
def navbar_searchbar_mobile() -> rx.Component:
    return rx.mobile_and_tablet(
            rx.hstack(
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Search...",
                    type="search",
                    size="2",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ), 
        bg=rx.color("accent", 3),
        #padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        #width="100%",
        ),
        



   
def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                        on_click=NavState.to_home,
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold", on_click=NavState.to_home,
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", routes.HOME_ROUTE),
                    navbar_link("About", routes.ABOUT_ROUTE),
                    navbar_link("Pricing", routes.PRICING_ROUTE),
                    navbar_link("Contact", routes.CONTACT_ROUTE),
                    
                    spacing="5",
                ),
                rx.hstack(
                    navbar_searchbar_desktop(),
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3", on_click=NavState.to_login),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                        on_click=NavState.to_home
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold", on_click=NavState.to_home
                    ),
                    navbar_searchbar_mobile(),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=NavState.to_home),
                        rx.menu.item("About", on_click=NavState.to_about),
                        rx.menu.item("Pricing", on_click=NavState.to_pricing),
                        rx.menu.item("Contact", on_click=NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=NavState.to_login),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )


