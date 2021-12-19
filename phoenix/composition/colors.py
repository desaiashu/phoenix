def merge_colors(color_1, color2, method='average'):
  if method == 'average':
      return (
        (color_1[0] + color2[0]) / 2,
        (color_1[1] + color2[1]) / 2,
        (color_1[2] + color2[2]) / 2
      )

color_patterns = {
  'psychedelic': [
    (255, 235, 0),
    (252, 0, 25),
    (1, 255, 79),
    (255, 1, 215),
    (86, 0, 204),
    (0, 237, 245)
  ]
}