from app import handlers

page_routes = [
    ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/home", "home", handlers.pages.home_page, ["GET"]),
    ("/events/add", "add-event", handlers.pages.add_event, ["GET"]),
]

form_routes = [
    ("/events/add/form", "add-event-form", handlers.forms.add_event, ["POST"])
]
