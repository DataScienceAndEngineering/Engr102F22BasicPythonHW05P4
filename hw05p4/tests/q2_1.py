OK_FORMAT = True
test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(weird_numbers)
          <class 'numpy.ndarray'>
          >>> np.allclose(weird_numbers, np.array([-2.,  0.93203909,  3.,  1.79174913]), rtol=1e-03, atol=1e-03)
          True
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
