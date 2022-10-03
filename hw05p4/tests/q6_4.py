OK_FORMAT = True
test = {
  'name': 'Question 6_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sales.sort_values("box ID")
                  fruit name  count sold  price per fruit ($)
          box ID                                             
          25274        apple           0                 0.80
          26187   strawberry          25                 0.15
          43566        peach          17                 0.80
          48800       orange          35                 0.60
          52357   strawberry         102                 0.25
          53686         kiwi           3                 0.50
          57181   strawberry         101                 0.20
          57930        grape         355                 0.06
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
