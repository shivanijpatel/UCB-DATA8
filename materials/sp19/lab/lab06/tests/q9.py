test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 <= proportion_greater_or_equal <= 1
          True
          >>> proportion_greater_or_equal*1000 == np.count_nonzero(simulated_statistics >= observed_statistic)
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
