OK_FORMAT = True
test = {
  'name': 'Question 4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(sum(celsius_temperature_ranges))
          768487
          >>> len(celsius_temperature_ranges)
          65000
          >>> celsius_temperature_ranges[1]
          10.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
