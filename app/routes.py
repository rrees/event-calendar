from app import handlers

page_routes = [
    ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/home", "home", handlers.pages.home_page, ["GET"]),
]
