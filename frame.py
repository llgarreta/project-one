

import threading
import datetime

class ThreadClass(threading.Thread):

  def run(self):
    now = datetime.datetime.now()
    print("%s dice hola en el tiempo: %s" %
    (self.getName(), now))

for i in range(4):
  t = ThreadClass()
  t.start()
