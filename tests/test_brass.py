from __future__ import annotations

from brass import *

def make_profitable_industry(owner: Player, victory_points: int) -> IndustryTile:
    tile = IndustryTile(owner, victory_points)
    tile.profitable = True
    return tile

def test_compute_scores() -> None:
    alice = Player("Alice")
    bob = Player("Bob")

    coalbrookdale = Town("Coalbrookdale")
    wolverhampton = Town("Wolverhampton")
    walsall = Town("Walsall")
    birmingham = Town("Birmingham")
    dudley = Town("Dudley")
    kidderminster = Town("Kidderminster")

    coalbrookdale_wolverhampton = Connection(coalbrookdale, wolverhampton)
    coalbrookdale_kidderminster = Connection(coalbrookdale, kidderminster)
    wolverhampton_walsall = Connection(wolverhampton, walsall)
    wolverhampton_dudley = Connection(wolverhampton, dudley)
    birmingham_walsall = Connection(birmingham, walsall)
    birmingham_dudley = Connection(birmingham, dudley)
    dudley_kidderminster = Connection(dudley, kidderminster)

    game = Game(
        players=[
            alice,
            bob,
        ],
        towns=[
            coalbrookdale,
            wolverhampton,
            walsall,
            birmingham,
            dudley,
            kidderminster,
        ],
        connections=[
            coalbrookdale_wolverhampton,
            coalbrookdale_kidderminster,
            wolverhampton_walsall,
            wolverhampton_dudley,
            birmingham_walsall,
            birmingham_dudley,
            dudley_kidderminster,
        ]
    )

    birmingham.build_industry(IndustryTile(alice, 5))
    birmingham.build_industry(make_profitable_industry(alice, 7))
    birmingham.build_industry(make_profitable_industry(bob, 3))

    dudley.build_industry(IndustryTile(bob, 10))
    dudley.build_industry(make_profitable_industry(bob, 12))
    dudley.build_industry(make_profitable_industry(alice, 5))

    kidderminster.build_industry(IndustryTile(alice, 100))
    kidderminster.build_industry(make_profitable_industry(alice, 2))

    birmingham_dudley.build(alice)
    birmingham_walsall.build(alice)
    dudley_kidderminster.build(bob)

    scores = game.compute_scores()
    assert scores[alice] == (7+5+2) + (2+2) + 2
    assert scores[bob] == (3+12) + (2+1)
