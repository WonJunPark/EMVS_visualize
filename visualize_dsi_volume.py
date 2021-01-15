import numpy as np
import argparse
import visvis as vv
app = vv.use()

def flip(m, axis):
    if not hasattr(m, 'ndim'):
        m = asarray(m)
    indexer = [slice(None)] * m.ndim
    try:
        indexer[axis] = slice(None, None, -1)
    except IndexError:
        raise ValueError("axis=%i is invalid for the %i-dimensional input array"
                         % (axis, m.ndim))
    return m[tuple(indexer)]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Plot the disparity space image (DSI) using 3D slices')
    parser.add_argument('-i', '--input', default='dsi.npy', type=str,
                        help='path to the NPY file containing the DSI (default: dsi.npy)')
    args = parser.parse_args()

    a = vv.gca()
    a.daspect = 1, -1, 1
    a.daspectAuto = True
    vol = np.load(args.input)
    
    # Reorder axis so that the Z axis points forward instead of up
    vol = np.swapaxes(vol, 0, 1)
    vol = flip(vol, axis=0)
    
    t = vv.volshow(vol, renderStyle = 'mip')
    t.colormap = vv.CM_HOT
    
    app.Run()
