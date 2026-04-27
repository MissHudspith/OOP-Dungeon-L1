# test_game.py  —  GitHub Classroom autograder
# Tests for Lesson 1: Classes & Objects
import pytest
from game import Room, Player, Item
 
 
# ── Room tests ───────────────────────────────────────────────────────
 
class TestRoom:
    def test_room_has_name(self):
        r = Room("Hall", "A big hall.")
        assert r.name == "Hall"
 
    def test_room_has_description(self):
        r = Room("Hall", "A big hall.")
        assert r.description == "A big hall."
 
    def test_room_items_starts_empty(self):
        r = Room("Hall", "A big hall.")
        assert r.items == []
 
    def test_room_exits_starts_empty(self):
        r = Room("Hall", "A big hall.")
        assert r.exits == {}
 
    def test_add_exit(self):
        r1 = Room("Hall", "A big hall.")
        r2 = Room("Cellar", "Dark and damp.")
        r1.add_exit('south', r2)
        assert r1.exits['south'] is r2
 
 
# ── Player tests ─────────────────────────────────────────────────────
 
class TestPlayer:
    def test_player_has_name(self):
        p = Player("Asha")
        assert p.name == "Asha"
 
    def test_player_starts_with_100_health(self):
        p = Player("Asha")
        assert p.health == 100
 
    def test_player_inventory_starts_empty(self):
        p = Player("Asha")
        assert p.inventory == []
 
    def test_is_alive_when_healthy(self):
        p = Player("Asha")
        assert p.is_alive() is True
 
    def test_is_alive_false_at_zero_health(self):
        p = Player("Asha")
        p.health = 0
        assert p.is_alive() is False
 
 
# ── Item tests  (Make phase) ──────────────────────────────────────────
 
class TestItem:
    def test_item_has_name(self):
        item = Item("Rusty Key", "An old key.")
        assert item.name == "Rusty Key"
 
    def test_item_has_description(self):
        item = Item("Rusty Key", "An old key.")
        assert item.description == "An old key."
 
    def test_item_can_take_defaults_true(self):
        item = Item("Rusty Key", "An old key.")
        assert item.can_take is True
 
    def test_item_describe_runs_without_error(self, capsys):
        item = Item("Torch", "A burning torch.")
        item.describe()
        captured = capsys.readouterr()
        assert "Torch" in captured.out
 
    def test_two_items_are_independent(self):
        key  = Item("Key",   "A key.")
        book = Item("Book",  "A book.")
        assert key.name  == "Key"
        assert book.name == "Book"

