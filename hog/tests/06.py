test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=2, say=echo)
          46384f1b91067efe2db7061edf72cafa
          3270ccc2d8e87b5fea4628d2c594dae7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play.
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=7, say=echo)
          46384f1b91067efe2db7061edf72cafa
          16e2cf37e8254529473d9e0a36b75fcb
          b2e4d14a8333b08801b894f7f3f9f3d8
          872dbe4a4fe5d8451aa842c21194c866
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=1, say=both(echo_0, echo_1))
          ef8fa39d05cae48a27c2f160ddf666f0
          4a64fe964dc771a219ed773c3a146c75
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(0), always_roll(0), goal=10, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 2
          Player 1 takes the lead by 1
          Player 0 now has 2 and Player 1 now has 4
          Player 0 now has 2 and Player 1 now has 7
          Player 0 now has 10 and Player 1 now has 7
          Player 0 takes the lead by 3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
