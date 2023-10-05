def main_menu():
    menu = ("""
    1 -> Phone book
    2 -> Messages
    3 -> Chats
    4 -> Call register
    5 -> Tones
    6 -> Settings
    7 -> Call divert
    8 -> Games
    9 -> Calculator
    10-> Reminders
    11-> Clock
    12-> Profiles
    13-> SIM services
    """)
    print(menu)
    main = int(input())
    match main:
        case 1:
            phone_book()
        case 2:
            messages()
        case 3:
            chats()
        case 4:
            call_register()
        case 5:
            tones()
        case 6:
            settings()
        case 7:
            call_divert()
        case 8:
            games()
        case 9:
            calculator()
        case 10:
            reminders()
        case 11:
            clock()
        case 12:
            profiles()
        case 13:
            sim_services()


def phone_book():
    print("""
    1-> Search
    2-> Service Nos
    3-> Add name
    4-> Erase
    5-> Edit
    6-> Assign Tone
    7-> Send b'card
    8-> Options
    9-> Speed dials
    10-> Voice tags
    11->main_menu""")
    response = int(input())
    match response:
        case 1:
            print("Search")
        case 2:
            print("Service Nos")
        case 3:
            print("Add name")
        case 4:
            print("Erase")
        case 5:
            print("Edit")
        case 6:
            print("Assign Tone")
        case 7:
            print("Send b'card")
        case 8:
            print("""
            1->Type of view
            2->Memory status
            3->Go back
            4.Main menu
            """)
            option = int(input())
            match option:
                case 1:
                    print("type_of_view")
                case 2:
                    print("memory_status")
                case 3:
                    phone_book()
                case 4:
                    main_menu()
        case 9:
            print("Speed dial")
        case 10:
            print("Voice tags")
        case 11:
            print("main menu")
        case 12:
            main_menu()


def messages():
    print("""
    1-> Write messages
    2-> Inbox
    3-> Outbox
    4-> Picture messages
    5-> Templates
    6-> Smileys
    7-> Message settings
    8-> main_menu""")
    response = int(input())
    match response:
        case 1:
            print("Write messages")
        case 2:
            print("Inbox")
        case 3:
            print("Outbox")
        case 4:
            print("picture_messages")
        case 5:
            print("templates")
        case 6:
            print("smileys")
        case 7:
            print("""
           1. Set
           2.Common
           3.Go back
           4.Main menu""")
            responses = int(input())
            match responses:
                case 1:
                    print(""""
                        1->Message centre number
                        2->Message sent as
                        3->Message Validity
                        4->go_back
                        5->main_menu""")
                    response = int(input())
                    match response:
                        case 1:
                            print("Message centre number")
                        case 2:
                            print("Message sent as")
                        case 3:
                            print("Message Validity")
                        case 4:
                            messages()
                        case 5:
                            main_menu()
                case 2:
                    print("""
                        1->delivery
                        2->reply_via_same_centre
                        3->character_support
                        4->go_back
                        5->main_menu""")
                    response = int(input())
                    match response:
                        case 1:
                            print("delivery")
                        case 2:
                            print("reply_via_same_centre")
                        case 3:
                            print("character_support")
                        case 4:
                            messages()
                        case 5:
                            main_menu()
        case 8:
            print("info_service")
        case 9:
            print("voice_mailbox_number")
        case 10:
            print("service_command_editor")
        case 11:
            main_menu()


def chats():
    print("""
    1->chat
    2->main menu""")
    response = int(input())
    match response:
        case 1:
            print("chat")
        case 2:
            chats()
        case 3:
            main_menu()


def call_register():
    print("""
    call_register
    1->missed_calls
    2->received_calls
    3->dialled_numbers
    4->erase_recent_call_list
    5->show_call_duration
    6->show_call_cost
    7->call_cost_settings
    8->prepaid_credit
    9->main_menu""")
    response = int(input())
    match response:
        case 1:
            print("missed_calls")
        case 2:
            print("received_calls")
        case 3:
            print("dialled_calls")
        case 4:
            print("erase_recent_call_list")
        case 5:
            print("""
                    1->last_call_duration
                    2->all_calls_duration
                    3->received_calls_duration
                    4->dialled_calls_duration
                    5->clear_timers
                    6->go_back
                    7->main_menu""")

            response = int(input())
            match response:
                case 1:
                    print("last_call_duration")
                case 2:
                    print("all_calls_duration")
                case 3:
                    print("received_calls_duration")
                case 4:
                    print("dialled_calls_duration")
                case 5:
                    print("clear_timers")
                case 6:
                    call_register()
                case 7:
                    main_menu()
        case 6:
            print("""
            1->last_call_cost
            2->all_call_cost
            3->clear_counters
            4->go_back
            5->main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("last_call_cost")
                case 2:
                    print("all_call_cost")
                case 3:
                    print("clear_counters")
                case 4:
                    call_register()
                case 5:
                    main_menu()
        case 7:
            print("""
            1->call_cost_limit
            2->show_cost_in
            3->go_back
            4->main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("call_cost_limit")
                case 2:
                    print("show_cost_in")
                case 3:
                    call_register()
                case 4:
                    main_menu()
        case 8:
            print("""
            1->prepaid_credit
            2->go_back
            3->main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("prepaid_credit")
                case 2:
                    call_register()
                case 3:
                    main_menu()


def tones():
    print("""
    1->ringing_tone
    2->ringing_volume
    3->incoming_call_alert
    4->composer
    5->message_alert_tone
    6->keypad_tones
    7->warning_and_games_tones
    8->vibrating_alert
    9->screen_saver
    10->main_menu""")
    response = int(input())
    match response:
        case 1:
            print("ringing_tone")
        case 2:
            print("ringing_volume")
        case 3:
            print("incoming_call_alert")
        case 4:
            print("composer")
        case 5:
            print("message_alert_tone")
        case 6:
            print("keypad_tones")
        case 7:
            print("warning_and_games_tones")
        case 8:
            print("vibrating_alert")
        case 9:
            print("""
            1-> screen_saver
            2-> go_back
            3-> main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("screen_saver")
                case 2:
                    tones()
                case 3:
                    main_menu()


def settings():
    print("""
    1->call_settings
    2->phone_settings
    3->security_settings
    4->restore_factory_settings
    5->go_back
    6->main_menu""")
    response = int(input())
    match response:
        case 1:
            print("""
            1->automatic_redial
            2->speed_dialling
            3->call_waiting_options
            4->own_number_sending
            5->phone_line_in_use
            6->automatic_answer
            7->go_back
            8->main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("automatic_redial")
                case 2:
                    print("speed_dialling")
                case 3:
                    print("call_waiting_options")
                case 4:
                    print("own_number_sending")
                case 5:
                    print("phone_line_in_use")
                case 6:
                    print("automatic_answer")
                case 7:
                    print("""
                    1-> automatic_answer
                    2-> go_back
                    3-> main_menu""")
                    response = int(input())
                    match response:
                        case 1:
                            print("automatic_answer")
                        case 2:
                            settings()
                        case 3:
                            main_menu()

        case 2:
            print("""
            1-> language
            2-> cell_info_display
            3-> welcome_note
            4-> network_selection
            5-> lights
            6-> confirm_sim_service_action
            7-> go_back
            8-> main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("language")
                case 2:
                    print("cell_info_display")
                case 3:
                    print("welcome_note")
                case 4:
                    print("network_selection")
                case 5:
                    print("lights")
                case 6:
                    print("confirm_sim_service_action")
                case 7:
                    settings()
                case 8:
                    print("""
                    1-> confirm_sim_service_action
                    2-> go_back
                    3-> main_menu""")
                    response = int(input())
                    match response:
                        case 1:
                            print("confirm_sim_service_action")
                        case 2:
                            settings()
                        case 3:
                            main_menu()

        case 3:
            print("""
            1-> pin_code_request
            2-> call_barring_service
            3-> fixed_dialling
            4-> closed_user_group
            5-> phone_security
            6-> change_access_codes
            7-> go_back
            8-> main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("pin_code_request")
                case 2:
                    print("call_barring_service")
                case 3:
                    print("fixed_dialling")
                case 4:
                    print("closed_user_group")
                case 5:
                    print("phone_security")
                case 6:
                    print("change_access_codes")
                case 7:
                    settings()
                case 8:
                    main_menu()
                    print("""
                    1-> change_access_codes
                    2-> go_back
                    3-> main_menu""")
                    response = int(input())
                    match response:
                        case 1:
                            print("change_access_codes")
                        case 2:
                            settings()
                        case 3:
                            main_menu()

        case 4:
            print("""
            1-> restore_factory_settings
            2-> go_back
            3-> main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("restore_factory_settings")
                case 2:
                    settings()
                case 3:
                    main_menu()


def call_divert():
    print("""
    1.call_divert
    2.main_menu""")
    response = int(input())
    match response:
        case 1:
            print("call_divert")
        case 2:
            call_divert()
        case 3:
            main_menu()


def games():
    print("""
    1.games
    2.main_menu""")
    response = int(input())
    match response:
        case 1:
            print("games")
        case 2:
            games()
        case 3:
            main_menu()


def calculator():
    print("""
    1.calculator
    2.main_menu""")
    response = int(input())
    match response:
        case 1:
            print("calculator")
        case 2:
            calculator()
        case 3:
            main_menu()


def reminders():
    print("""
    1.reminders
    2.main_menu""")
    response = int(input())
    match response:
        case 1:
            print("reminders")
        case 2:
            reminders()
        case 3:
            main_menu()


def clock():
    print("""
    1->alarm_clock
    2->clock_settings
    3->date_settings
    4->stopwatch
    5->countdown_timer
    6->auto_update_of_time_and_date
    7->go_back
    8->main_menu""")
    response = int(input())
    match response:
        case 1:
            print("alarm_clock")
        case 2:
            print("clock_settings")
        case 3:
            print("date_settings")
        case 4:
            print("stopwatch")
        case 5:
            print("countdown_timer")
        case 6:
            print("""
            1-> auto_update_of_time_and_date
            2-> go_back
            3-> main_menu""")
            response = int(input())
            match response:
                case 1:
                    print("auto_update_of_time_and_date")
                case 2:
                    clock()
                case 3:
                    main_menu()



def profiles():
    print("""
    1->profiles
    2->main_menu""")
    response = int(input())
    match response:
        case 1:
            print("profiles")
        case 2:
            profiles()
        case 3:
            main_menu()


def sim_services():
    print("""
    1->sim_services
    2->main menu""")
    response = int(input())
    match response:
        case 1:
            print("sim_services")
        case 2:
            sim_services()
        case 3:
            main_menu()
