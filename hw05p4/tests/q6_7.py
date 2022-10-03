OK_FORMAT = True
test = {
  'name': 'Question 6_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your table doesn't have all 3 columns that are
          >>> # in the inventory table.
          >>> len(remaining_inventory.columns)
          2
          >>> # It looks like you forgot to subtract off the sales.
          >>> remaining_inventory.iloc[2,-1] < 40
          True
          >>> remaining_inventory[remaining_inventory['fruit name']=='grape']
                 fruit name  count
          box ID                  
          57930       grape    162
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
