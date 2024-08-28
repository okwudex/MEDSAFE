import reflex as rx
from ..UI.base import base_page
from ..navigation import routes

class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        #Handle form Submit
        print(form_data)
        self.form_data = form_data

@rx.page(route=routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    my_form = rx.form(
            rx.vstack(
                rx.input(
                    name="first_name",
                    placeholder="First Name",
                    required=True,
                    
                ),
                rx.input(
                    name="last_name",
                    placeholder="Last Name",
                    
                ),
                rx.input(
                    name="email",
                    placeholder="Your email",
                    type="email",
                    required=True,
                    
                ),
                rx.text_area(
                    name="Message",
                    placeholder="Send us your message",
                    required=True,
                    
                ),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),
    # About Page (Index)
    mychild = rx.vstack(
            rx.heading("Contact Us", size="9"), 
            rx.desktop_only(my_form),
            rx.mobile_and_tablet(my_form),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
            id="vstack_range",
        )
    return base_page(mychild)
    

