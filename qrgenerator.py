from MyQR import myqr
import os
import sys

if len(sys.argv) > 1:
  urlforqr = sys.argv[1] 
  version, level, qr_name = myqr.run(
      urlforqr,
      version=1,
      level='H',
      picture=None,
      colorized=False,
      contrast=1.0,
      brightness=1.0,
      save_name=None,
      save_dir=os.getcwd()
    )

else:
  print('No url found')