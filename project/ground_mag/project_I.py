from hapiclient import hapi
from hapiclient import hapitime2datetime
server     = 'https://imag-data.bgs.ac.uk/GIN_V1/hapi'
dataset    = 'bou/definitive/PT1M/xyzf'
parameters = ''
start      = '1991-01-01T00:00:00Z' # min 1991-01-01T00:00:00Z
stop       = '1991-01-10T00:00:00.000Z' # max 2024-12-31T23:59:00Z

data, meta = hapi(server, dataset, parameters, start, stop)
time = hapitime2datetime(data['Time'])

from matplotlib import pyplot as plt
# You will need to set values of 99999 equal to np.nan to get a decent plot
field = data['Field_Vector']
import numpy as np
field = np.where(field == 99999, np.nan, field)
plt.plot(time, field)
plt.show()

# To get a decent plot, either plot the components on separate plots, or
# subtract off the average as in 
# https://hapi-server.org/servers/#server=INTERMAGNET&dataset=bou/definitive/PT1M/xyzf&parameters=&start=1991-01-01T00:00:00Z&stop=1991-01-10T00:00:00.000Z&return=image&format=hapiplot&style=svg
