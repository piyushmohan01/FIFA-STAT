import cv2

def player_pos_map(st):
  import os
  dir = 'assets/images/pitch-temp'
  for f in os.listdir(dir):
      os.remove(os.path.join(dir, f))
  img = cv2.imread('assets/images/pitch-original/pitch-pos-cropped.png', 1)
  # x = 46; y=46;
  # mx = 1; my = 1;
  # x_cell = 0; y_cell = 1;
  markers = {
      'LW': [(15, 15), (76, 150+1)],
      'LM': [(15, 150+2), (76, 300-3)],
      'LWB': [(15, 225), (75, 375-4)],
      'CM': [(75+2, 150+38), (225+5, 300-38-2)],
      'CAM': [(75+2, 75+38), (225+5, 225-38)],
      'CDM': [(75+2, 225+38-2), (225+5, 375-38-2)],
      'CB': [(75+2, 300), (225+6, 375-3)],
      'LB': [(15, 300), (75+38+6, 375-3)],
      'RB': [(225+3-38, 300), (300-6, 375-3)],
      'RWB': [(225+7, 225), (300-6, 375-3)],
      'RM': [(225+7, 150+2), (300-6, 305-3)],
      'RW': [(225+7, 15), (300-6, 150+1)],
      'GK': [(150-38+8, 375+25-4), (225-38+3, 450-10-4)],
      'ST': [(75+2, 15+38+3), (225+7, 150-38-2)],
      'CF': [(75+2, 15+25-5), (225+7, 77)]
  }
  sample_string = st
  pos_list = sample_string.split(', ')
  for position in pos_list:
    overlay = img.copy()
    cv2.rectangle(
      img, markers[position][0], markers[position][1],
      color=(255, 255, 19),
      thickness=-1,
    )
    alpha=0.4
    img = cv2.addWeighted(overlay, alpha, img, 1-alpha, 0)
  file_ = str('assets/images/pitch-temp/{}.png'.format(sample_string))
  cv2.imwrite(file_, img)
  return file_
