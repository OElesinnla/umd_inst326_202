import view

def test_main_screen_display():
    view.main_screen()
    input("[Enter to proceed]")
    assert True

def test_mode1_player_name_form():
    view.player_init_1()
    input("[Enter to proceed]")
    assert True

def test_mode2_player_name_form():
    view.player_init_2(1)
    input("[Enter to proceed]")
    assert True
    view.player_init_2(2)
    input("[Enter to proceed]")
    assert True

def test_begin_game_screen():
    view.begin_game_screen("dummy1", "dummy2")
    input("[Enter to proceed]")
    assert True

def test_turn_winner_screens():
    view.middle_won_screen()
    input("[Enter to proceed]")