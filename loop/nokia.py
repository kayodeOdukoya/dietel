# def display_submenu(submenu):
#     print(f"For {submenu}:")
#     for index, option in enumerate(submenu, start=1):
#         print(f"{index} -> {option}")
#     return int(input())
#
# def process_menu_option(option):
#     if option == 1:
#         print("Phone book")
#         phonebook_submenu = [
#             "Search", "Services Nos.", "Add name", "Erase", "Edit",
#             "Assign tone", "Send b'card", "Options", "Speed dial", "Voice tags"
#         ]
#         typeOfView = display_submenu(phonebook_submenu)
#         if typeOfView == 1:
#             print("Search")
#         elif typeOfView == 2:
#             print("Service Nos")
#         elif typeOfView == 3:
#             print("Add name")
#         elif typeOfView == 4:
#             print("Erase")
#         elif typeOfView == 5:
#             print("Edit")
#         elif typeOfView == 6:
#             print("Assign tone")
#         elif typeOfView == 7:
#             print("Send b'card")
#         elif typeOfView == 8:
#             print("Options")
#         elif typeOfView == 9:
#             print("Speed dials")
#         elif typeOfView == 10:
#             print("Voice tags")
#         # more menu
#
#     elif option == 2:
#         print("Message")
#         message_submenu = [
#             "Write messages", "Inbox", "Outbox", "Picture message", "Template",
#             "Smileys", "Message settings"
#         ]
#         message = display_submenu(message_submenu)
#         if message == 1:
#             print("Write message")
#         elif message == 2:
#             print("Inbox")
#         elif message == 3:
#             print("Outbox")
#         # more menu
#
#     # more menu
#
# menu_items = [
#     "Phone book", "Message", "Chat", "Call register", "Tones",
#     "Settings", "Call divert", "Games", "Calculator", "Reminders",
#     "Clock", "Profiles", "SIM services"
# ]
#
# while True:
#     print("List of menu functions:")
#     for index, item in enumerate(menu_items, start=1):
#         print(f"{index} -> {item}")
#
#     nokia = int(input("Enter your choice (0 to exit): "))
#
#     if nokia == 0:
#         break
#     elif 1 <= nokia <= len(menu_items):
#         process_menu_option(nokia)
#     else:
#         print("Invalid menu selection. Please try again.")
